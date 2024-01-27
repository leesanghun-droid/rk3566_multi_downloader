# import subprocess

import download
import com
import uart_atmega
import time
#import pygame
# import usb_update_copy      as UC

import threading

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

uart_atmega.EX_POWER_OFF()
uart_atmega.BUTTON_LED_OFF()


def led(mode,t):
    if mode ==2 :
        step = 105/t
        for i in range(t*10):
            progress=int((i/10)*step)
            Progress2_value.set(progress)
            p2.update()
            time.sleep(0.1)
    if mode ==3 :
        step = 105/t
        for i in range(t*10):
            progress=int((i/10)*step)
            Progress3_value.set(progress)
            p3.update()
            time.sleep(0.1)
    if mode ==4 :
        step = 105/t
        for i in range(t*10):
            progress=int((i/10)*step)
            Progress4_value.set(progress)
            p4.update()
            time.sleep(0.1)
    if mode ==5 :
        step = 105/t
        for i in range(t*10):
            progress=int((i/10)*step)
            Progress5_value.set(progress)
            p5.update()
            time.sleep(0.1)

thread2 = threading.Thread(target = led, args = (1,10))

def LED_PROGRESS_CLEAR(mode):
    if mode ==2 :
        Progress2_value.set(0)
        p2.update()
    if mode ==3 :
        Progress3_value.set(0)
        p3.update()
    if mode ==4 :
        Progress4_value.set(0)
        p4.update()
    if mode ==5 :
        Progress5_value.set(0)
        p5.update()

def LED_PROGRESS(mode,t):
    global thread2
    if(thread2!=None and thread2.is_alive()):
        print("thread2_busy")
    else:
        thread2 = threading.Thread(target = led, args = (mode,t))
        thread2.start()

cmd=0
EX_POWER=0
def downloader():
    global cmd
    global EX_POWER
    result=uart_atmega.read_serial()
#    print("cmd:"+str(cmd))
    if result=="Press":
        result=''
        cmd=cmd+1
        print(result)
        if cmd>=1:
            uart_atmega.LED_SETTING(cmd)   
        # LED_PROGRESS(1,13)
        # time.sleep(13)
    else:
######################################### 2. 전원켜기 ############################################
        if cmd==2:
            if EX_POWER==0:
                uart_atmega.EX_POWER_ON()
                uart_atmega.BUTTON_LED_ON()
                LED_PROGRESS(2,30)
                time.sleep(30)
                EX_POWER=1
            else:
                uart_atmega.EX_POWER_OFF()
                uart_atmega.BUTTON_LED_OFF()
                LED_PROGRESS_CLEAR(2)
                EX_POWER=0
##################################################################################################
######################################### 3. 다운로드 ############################################
        if cmd==3:
            LED_PROGRESS(3,200)
            download.Download_start()
##################################################################################################
######################################### 4. 통신셋팅 ############################################
        if cmd==4:
            LED_PROGRESS(4,70)
            com.com_setup()
##################################################################################################
######################################### 5. 통신상태 ############################################
        if cmd==5:
            LED_PROGRESS(5,5)
            com.atcom_setup()
            pass
##################################################################################################
        cmd=0
        uart_atmega.LED_SETTING(cmd)

thread1 = threading.Thread(target = downloader)

cnt=0

def timer_1s():
    global thread1
    if(thread1!=None and thread1.is_alive()):
        pass
        #print("thread1_busy")
    else:
        thread1 = threading.Thread(target = downloader)
        thread1.start()
    global cnt
    cnt=cnt+1
    #print('boot ' + str(cnt) + ' sec: ')
    root.after(1000,timer_1s)


root = ttk.Window(themename="darkly")
root.title("HYODOL 다운로더")
root.geometry("1024x600+0+0")
root.config(cursor="none")

my_style = ttk.Style()
my_style.configure("light.Link.TButton",font=("Helvetica",30))

# sep1 = ttk.Separator(root,bootstyle="light")
# sep1.place(x=0, y=10, relwidth=1)

sep2 = ttk.Separator(root,bootstyle="light")
sep2.place(x=0, y=110, relwidth=1)

sep2 = ttk.Separator(root,bootstyle="light")
sep2.place(x=0, y=210, relwidth=1)

sep2 = ttk.Separator(root,bootstyle="light")
sep2.place(x=0, y=310, relwidth=1)

sep2 = ttk.Separator(root,bootstyle="light")
sep2.place(x=0, y=410, relwidth=1)

# sep2 = ttk.Separator(root,bootstyle="light")
# sep2.place(x=0, y=510, relwidth=1)


############################################### 프로그레스바 2 ##############################################
Progress2_value = ttk.DoubleVar()
p2 = ttk.Progressbar(root,maximum=100,length=450,variable=Progress2_value,bootstyle="success")
p2.place(x=300, y=142, height=35)
############################################### 프로그레스바 3 ##############################################
Progress3_value = ttk.DoubleVar()
p3 = ttk.Progressbar(root,maximum=100,length=450,variable=Progress3_value,bootstyle="success")
p3.place(x=300, y=242, height=35)
############################################################################################################
############################################### 프로그레스바 4 ##############################################
Progress4_value = ttk.DoubleVar()
p4 = ttk.Progressbar(root,maximum=100,length=450,variable=Progress4_value,bootstyle="success")
p4.place(x=300, y=342, height=35)
############################################################################################################
############################################### 프로그레스바 4 ##############################################
Progress5_value = ttk.DoubleVar()
p5 = ttk.Progressbar(root,maximum=100,length=100,variable=Progress5_value,bootstyle="success")
p5.place(x=300, y=442, height=35)
############################################################################################################


############################################### 버튼 1 #####################################################
b1 = ttk.Button(root, text='1.자동설치',
                style='light.Link.TButton',
                width=10)
b1.place(x=10, y=23)
############################################### 버튼 2 #####################################################
b2 = ttk.Button(root, text='2.전원켜기',
                style='light.Link.TButton',
                width=10)
def b2_bt_pressed():
    global cmd
    print("b2_bt_pressed")
    cmd=2

b2["command"] = b2_bt_pressed
b2.place(x=10, y=125)
############################################### 버튼 3 #####################################################
b3 = ttk.Button(root, text='3.다운로드',
                style='light.Link.TButton',
                width=10)
def b3_bt_pressed():
    global cmd
    print("b3_bt_pressed")
    cmd=3

b3["command"] = b3_bt_pressed
b3.place(x=10, y=225)
############################################### 버튼 4 #####################################################
b4 = ttk.Button(root, text='4.통신셋팅',
                style='light.Link.TButton',
                width=10)
def b4_bt_pressed():
    global cmd
    print("b4_bt_pressed")
    cmd=4

b4["command"] = b4_bt_pressed
b4.place(x=10, y=325)
############################################### 버튼 5 #####################################################
b5 = ttk.Button(root, text='5.통신상태',
                style='light.Link.TButton',
                width=10)
def b5_bt_pressed():
    global cmd
    print("b5_bt_pressed")
    cmd=5

b5["command"] = b5_bt_pressed
b5.place(x=10, y=425)
############################################################################################################

timer_1s()

root.mainloop()
