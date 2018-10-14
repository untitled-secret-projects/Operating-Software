#!/usr/bin/env python
import serial
import gpiozero
from signal import pause
from Command import Command
#from time import sleep

#Port 17 is Enter
#Port 27 is Back
#Port 22 is Left
#Port 10 is Right

port = "/dev/ttyACM0"
rate = 9600

button1 = gpiozero.Button(17, pull_up=False)
button2 = gpiozero.Button(27, pull_up=False)
button3 = gpiozero.Button(22, pull_up=False)
button4 = gpiozero.Button(10, pull_up=False)

s1 = serial.Serial(port, rate)
s1.flushInput()

def pressed1():
    print(Command.enter.value)
    s1.write(Command.enter.value.encode())
def pressed2():
    print(Command.back.value)
    s1.write(Command.back.value.encode())
def pressed3():
    print(Command.left.value)
    s1.write(Command.left.value.encode())
def pressed4():
    print(Command.right.value)
    s1.write(Command.right.value.encode())

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
