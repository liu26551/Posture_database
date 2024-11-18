# coding: utf-8
import serial
import time

# 设置串口参数
# 请根据你的ESP32串口设置相应的端口号（例如 COM5）和波特率
port = 'COM5'
baudrate = 9600

# 打开串口
ser = serial.Serial(port, baudrate)
with open('data3.txt','w') as file:
    while True:
        received_data = ser.readline()
        print("Received data: ", received_data)
        file.write(str(received_data))
        file.write('\n')

# 关闭串口
ser.close()


