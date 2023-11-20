import serial
import time

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

