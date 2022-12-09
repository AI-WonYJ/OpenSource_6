#  -*- coding: utf-8 -*-
import serial
import time

py_serial = serial.Serial(
    
    # Window
    port='COM7',
    
    # 보드 레이트 (통신 속도)
    baudrate=9600,
)

while True:
  with open("info.txt", "r") as file:
    for line in file.readlines():
      print(line)
  py_serial.write(line.encode())
  print(line)
  time.sleep(1)