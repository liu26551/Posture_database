# coding: utf-8
import serial.tools.list_ports


def list_serial_ports():
    return serial.tools.list_ports.comports()


# 打印出所有可用的串口号
ports = list_serial_ports()
if ports:
    print(f"Found {len(ports)} serial ports:")
    for index, port in enumerate(ports):
        print(f"{index + 1}: {port}")
else:
    print("No serial ports found.")