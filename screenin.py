#!/usr/bin/env python
import serial

port = "/dev/ttyACM0"
rate = 9600

s1 = serial.Serial(port, rate)
s1.flushInput()

while True:
    inline = input("Enter a string: ")
    s1.write(inline.encode())
