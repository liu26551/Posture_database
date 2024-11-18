# coding: utf-8
import serial
import time

# 设置串口参数
# 请根据你的ESP32串口设置相应的端口号（例如 COM5）和波特率
port = 'COM5'
baudrate = 9600

# 打开串口
ser = serial.Serial(port, baudrate)
while True:
# 发送数据到ESP32
#     data_to_send = b'D'
#     ser.write(data_to_send)
# 读取数据
    received_data = ser.readline()
    print("Received data: ", received_data)

# 关闭串口
ser.close()
