import subprocess
import download
import uart_atmega
import time
import flash_download_mode  as FD
import usb_update_copy      as UC

import threading

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


def led():
    for i in range(11):
        currProgress.set(i*10)
        p1.update()
        time.sleep(1)

thread2 = threading.Thread(target = led)

def LED_PROGRESS(mode,time):
    global thread2
    if(thread2!=None and thread2.is_alive()):
        print("thread2_busy")
    else:
        thread2 = threading.Thread(target = led)
        thread2.start()


def downloader():
    LED_PROGRESS(1,13)
    #time.sleep(13)

cnt=0

thread1 = threading.Thread(target = downloader)

def timer_1s():
    global thread1
    if(thread1!=None and thread1.is_alive()):
        print("thread1_busy")
    else:
        thread1 = threading.Thread(target = downloader)
        thread1.start()
    global cnt
    cnt=cnt+1
    print('boot ' + str(cnt) + ' sec: ')
    root.after(1000,timer_1s)


root = ttk.Window(themename="darkly")
root.title("HYODOL 다운로더")
root.geometry("1024x600+0+0")

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

sep2 = ttk.Separator(root,bootstyle="light")
sep2.place(x=0, y=510, relwidth=1)


currProgress = ttk.DoubleVar()
p1 = ttk.Progressbar(root,maximum=100,length=450,variable=currProgress,bootstyle="success")
p1.place(x=300, y=50)

b1 = ttk.Button(root, text='1.전원켜기',
                style='light.Link.TButton',
                width=10)
b1.place(x=10, y=23)

b2 = ttk.Button(root, text='2.장치연결',
                style='light.Link.TButton',
                width=10)
b2.place(x=10, y=123)

b3 = ttk.Button(root, text='3.다운로드',
                style='light.Link.TButton',
                width=10)
b3.place(x=10, y=223)

b4 = ttk.Button(root, text='4.통신셋팅',
                style='light.Link.TButton',
                width=10)
b4.place(x=10, y=323)

b5 = ttk.Button(root, text='5.통신점검',
                style='light.Link.TButton',
                width=10)
b5.place(x=10, y=423)


timer_1s()

root.mainloop()
