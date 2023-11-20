import serial
import time

print('Start - program')

angle1 = 0;
angle2 = 0;

ser = serial.Serial('COM9',115200)

def set_angle(angle1,angle2):
    angle1_high=int(angle1/256)%256
    angle1_low=angle1%256
    angle2_high=int(angle2/256)%256
    angle2_low=angle2%256
    ser.write([0xAA])
    ser.write([0x55])
    ser.write([0x00])
    ser.write([angle1_high])
    ser.write([angle1_low])
    ser.write([angle2_high])
    ser.write([angle2_low])

def set_init(gear1,gear2,motor1_dir,motor2_dir):
    set1 = gear1%256
    set2 = gear2%256
    set3 = motor1_dir%256
    set4 = motor2_dir%256
    
    ser.write([0xAA])
    ser.write([0x55])
    ser.write([0x01])
    ser.write([set1])
    ser.write([set2])
    ser.write([set3])
    ser.write([set4])
def read_serial():
    if ser.readable():
        res = ser.readline()
        print(res.decode()[:len(res)-2])

set_init(1,1,1,1)
read_serial();
time.sleep(0.5)
set_init(1,1,1,1)
read_serial();
time.sleep(0.5)
set_init(1,1,1,1)
read_serial();
time.sleep(0.5)


while True:

    
    print(" set 90,45 ... ")
    set_angle(9000,4500)
    read_serial();
    time.sleep(1)
    
    print(" set 180,90 ... ")
    set_angle(18000,9000)
    read_serial();
    time.sleep(1)
    
    print(" set 270,135 ... ")
    set_angle(27000,13500)
    read_serial();
    time.sleep(1)
    
    print(" set 360,180 ... ")
    set_angle(36000,18000)
    read_serial();
    time.sleep(1)
    
ser.close() 
