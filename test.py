# coding: utf-8
# import matplotlib
# matplotlib.use('Agg')
import cv2
import mediapipe as mp
import numpy as np
from keras.models import load_model
from LSTM.predict import pred
from LSTM.DataProcess import *
import serial

# 两个初始化
mpPose = mp.solutions.pose
pose = mpPose.Pose(static_image_mode=True)
# 初始化画图工具
mpDraw = mp.solutions.drawing_utils
# 调用摄像头
cap = cv2.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

#port = 'COM5'
#baudrate = 9600
# 打开串口
#ser = serial.Serial(port, baudrate)
input_pose_points=[]

model = load_model("./checkpoints/LSTM.h5")
res=''
while (cap.isOpened()):
    # 读取图像
    success, img = cap.read()
    # 转换为RGB格式，因为Pose类智能处理RGB格式，读取的图像格式是BGR格式
    try:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    except:
        break
    # 检测关键点
    results = pose.process(img)
    # print(results.pose_landmarks)
    # 检测到人体的话：
    if results.pose_landmarks:
        tmp_poselist=[]
        # 使用mpDraw来刻画人体关键点并连接起来
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        # 如果我们想对33个关键点中的某一个进行特殊操作，需要先遍历33个关键点
        for id, lm in enumerate(results.pose_landmarks.landmark):
            # 打印出来的关键点坐标都是百分比的形式，我们需要获取一下视频的宽和高
            h, w, c = img.shape
            tmp_poselist.append(lm.x)
            tmp_poselist.append(lm.y)
            tmp_poselist.append(lm.z)
            # 将x乘视频的宽，y乘视频的高转换成坐标形式
            cx, cy = int(lm.x * w), int(lm.y * h)
            # 使用cv2的circle函数将关键点特殊处理
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

        if len(input_pose_points) == 10:
            input_pose_points.pop(0)
            input_pose_points.append(tmp_poselist)
        else:
            input_pose_points.append(tmp_poselist)

    if len(input_pose_points) == 10:
        res = pred(np.array(input_pose_points),model)

    cv2.putText(img, res, (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    cv2.namedWindow('Image')
    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break