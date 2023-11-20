#파이썬 개발버전  v3.9
import datetime        # 현재시간 관련 함수
import time            # sleep 함수
import pandas as pd    # read_csv 함수
import tkinter as tk   # gui 함수
import serial          # serial 통신 함수

gear1=1
gear2=1
motor1_dir=1
motor2_dir=1

print('Start - program')
ser = serial.Serial('COM9',115200)

read_point = 0
df = pd.read_csv('data.csv')
df['time'] = pd.to_datetime(df['time'],format="%Y-%m-%d %H:%M:%S")
line_len=df.shape[0]

end = 0
angle1=0
angle2=0;
target_angle1=df['angle1'][0]
target_angle2=df['angle2'][0]

root = tk.Tk()
lbl = tk.Label()
lbl2 = tk.Label()

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

def update():

        global read_point
        global line_len
        global end
        global angle1
        global angle2
        global target_angle1
        global target_angle2

        p = read_point
        read_time = df['time'][p]

        now_time = datetime.datetime.now()
        diff_time = read_time-now_time;
        zero_time = datetime.timedelta(0)
    
        #print(read_time)
        #print(now_time)
        #print(diff_time)
        
        if end == 0:
            #print("")
            if diff_time > zero_time:
                a=5
                #print("wait")
            else:
                #print("move")
                #print(p)
                #print(df['angle1'][p])
                #print(df['angle2'][p])
                angle1=df['angle1'][p]
                angle2=df['angle2'][p]
                set_angle(angle1*100,angle2*100)
                read_serial();
                tp=p+1
                #if tp<df.shape[0]:
                    #target_angle1=df['angle1'][p+1]
                    #target_angle2=df['angle2'][p+1]
                if p<(df.shape[0]-1):
                    p=p+1
                else:
                    end=1
                read_point=p

        
        now_str = time.strftime("%Y-%m-%d   %H:%M:%S")
        
        str1='방위->' +str(angle1) + ' 고도->' + str(angle2) + ' 시간->'+ now_str
        lbl.configure(text=str1)

        read_str = df['time'][p].strftime("%Y-%m-%d   %H:%M:%S")
        target_angle1=df['angle1'][p]
        target_angle2=df['angle2'][p]

        str2='방위->' +str(target_angle1) + ' 고도->' + str(target_angle2) + ' 시간->'+ read_str
        lbl2.configure(text=str2)


        root.after(100, update)

def window_setting():
        global root
        global lbl
        global lbl2
        
        root.title("test_program")
        root.geometry("600x130")

        now_lb = tk.Label(text="now", font=('Helvetica', 12), fg='red')
        now_lb.pack()

        lbl = tk.Label(text="", font=('Helvetica', 16), fg='black')
        lbl.pack()

        next_lb = tk.Label(text="next", font=('Helvetica', 12), fg='blue')
        next_lb.pack()

        lbl2 = tk.Label(text="", font=('Helvetica', 16), fg='black')
        lbl2.pack()
def init():
        for i in range(0,3):
                set_init(gear1,gear2,motor1_dir,motor2_dir)
                read_serial();
                time.sleep(0.5)

window_setting()
update()
init()
root.mainloop()
ser.close()
