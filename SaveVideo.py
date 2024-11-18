# coding: utf-8
import cv2

# 初始化摄像头
cap = cv2.VideoCapture(1)  # 0 通常是默认摄像头的标识nn
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
# 定义编解码器并创建VideoWriter对象
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('.\HARdataset\output3.mp4', fourcc, 20.0, (frame_width, frame_height))

while (cap.isOpened()):
    ret, frame = cap.read()  # 读取一帧
    if ret:
        # 写入帧
        out.write(frame)

        # 显示帧
        cv2.imshow('frame', frame)

        # 按'q'退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()