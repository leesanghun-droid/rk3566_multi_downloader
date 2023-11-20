import serial
import time

def Flash_Download_Process_led_bar(num):
    num=num/10
    if num>=0x50:
        num=0x50
    ser.write([0xAA])
    ser.write([0x55])
    ser.write([0x20+int(num)])


def LED_SETTING(num):
    ser.write([0xAA])
    ser.write([0x55])
    ser.write([0x10+num])


def read_serial():
    if ser.readable():
        res = ser.readline()
        return res.decode()[:len(res)-2]

ser = serial.Serial('/dev/ttyACM1',9600)
ser.timeout = 1
# time.sleep(4) # bootled delay
# ser.write([0xAA])
# ser.write([0x55])
# ser.write([0x01])
time.sleep(4) # bootled delay

