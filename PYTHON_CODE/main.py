import serial

ser = serial.Serial('/dev/ttyACM0',9600)
ser.write([0xAA])
ser.write([0x55])
ser.close()