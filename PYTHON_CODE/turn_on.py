import serial

def EX_POWER_ON():
    ser.write([0xAA])
    ser.write([0x55])
    ser.write([0x74])

ser = serial.Serial('/dev/ttyS4',9600)

EX_POWER_ON()

ser.close()

