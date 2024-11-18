# coding: utf-8
import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import MinMaxScaler

label_dict = {0:"step",1:"back fall",2:"right fall",3:"left fall"}
communicate_dict = {0:"step",1:"back fall",2:"right fall",3:"left fall"}
def loadData(path_of_dataset):
    if os.path.exists(path_of_dataset):
        fileType = path_of_dataset.split(".")[-1]
        if fileType == 'xlsx' or fileType == 'xls':
            data = pd.read_excel(path_of_dataset)
            return data.iloc[:,1:],data.iloc[:,0]
        elif fileType == "csv":
            data = pd.read_csv(path_of_dataset)
            return data.iloc[:,1:],data.iloc[:,0]
        else:
            print("无法读取该格式的文件！！")
    else:
        print("文件不存在！！")


def Norm(data):
    scaler = MinMaxScaler(feature_range=(0, 1))
    norm_data = scaler.fit_transform(data)
    return norm_data


def CreateTimeSeq(data,label,timestep):
    x,y=[],[]
    for i in range(len(data) - timestep):
        # 从当前索引i开始，取sequence_length个连续的价格数据点，并将其作为特征添加到列表 X 中。
        x.append(data[i: i + timestep])
        # 将紧接着这sequence_length个时间点的下一个数据点作为目标添加到列表y中。
        y.append(label[i + timestep])
    x = np.array(x)
    y = np.array(y)
    return x,y


def num2label(num):
    return label_dict[num]
