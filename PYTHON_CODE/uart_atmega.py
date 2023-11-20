import serial
import time

def Download_Process_led_bar(num):
    num=num/10
    if num>=0x50:
        num=0x50
    ser.write([0xAA])
    ser.write([0x55])
    ser.write([0x20+int(num)])

def Download_Process_led_color_GREEN():
    ser.write([0xAA])
    ser.write([0x55])
    ser.write([0x71])

def Download_Process_led_color_RED():
    ser.write([0xAA])
    ser.write([0x55])
    ser.write([0x72])

def Download_Process_led_color_YELLOW():
    ser.write([0xAA])
    ser.write([0x55])
    ser.write([0x73])


def LED_SETTING(num):
    ser.write([0xAA])
    ser.write([0x55])
    ser.write([0x10+num])


def read_serial():
    if ser.readable():
        res = ser.readline()
        return res.decode()[:len(res)-2]

ser = serial.Serial('/dev/ttyACM0',9600)
ser.timeout = 1
# time.sleep(4) # bootled delay
# ser.write([0xAA])
# ser.write([0x55])
# ser.write([0x01])
time.sleep(4) # bootled delay

