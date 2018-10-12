#!/usr/bin/env python
import serial
import gpiozero
from signal import pause
#from time import sleep

port = "/dev/ttyACM0"
rate = 9600

button1 = gpiozero.Button(17, pull_up=False)
button2 = gpiozero.Button(27, pull_up=False)
button3 = gpiozero.Button(22, pull_up=False)
button4 = gpiozero.Button(10, pull_up=False)

s1 = serial.Serial(port, rate)
s1.flushInput()

def pressed1():
    print("button 17")
    s1.write("button 17".encode())
def pressed2():
    print("button 27")
    s1.write("button 27".encode())
def pressed3():
    print("button 22")
    s1.write("button 22".encode())
def pressed4():
    print("button 10")
    s1.write("button 10".encode())

button1.when_pressed = pressed1
button2.when_pressed = pressed2
button3.when_pressed = pressed3
button4.when_pressed = pressed4

pause()
#while True:
#    if button.is_pressed:
#        s1.write(str(n).encode())
#    n += 1
#    sleep(1)
    #inline = input("Enter a string: ")
    #s1.write(inline.encode())
