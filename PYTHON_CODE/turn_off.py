import serial

def EX_POWER_OFF():
    ser.write([0xAA])
    ser.write([0x55])
    ser.write([0x75])

ser = serial.Serial('/dev/ttyS4',9600)

EX_POWER_OFF()

ser.close()

