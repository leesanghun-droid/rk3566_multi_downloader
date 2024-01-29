# import subprocess
import os
import download
import com
import uart_atmega
import time
import script_copy
#import pygame
# import usb_update_copy      as UC

import threading

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

uart_atmega.EX_POWER_OFF()
uart_atmega.BUTTON_LED_OFF()
os.environ['DISPLAY']=':0.0'


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
    # if mode ==5 :
    #     step = 105/t
    #     for i in range(t*10):
    #         progress=int((i/10)*step)
    #         Progress5_value.set(progress)
    #         p5.update()
    #         time.sleep(0.1)

thread2 = threading.Thread(target = led, args = (1,10))

def busy_check():
    while True:
        if(thread2!=None and thread2.is_alive()):
            pass
        else:
            break

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
    # if mode ==5 :
    #     Progress5_value.set(0)
    #     p5.update()



def LED_PROGRESS(mode,t):
    global thread2
    if(thread2!=None and thread2.is_alive()):
        print("thread2_busy")
    else:
        thread2 = threading.Thread(target = led, args = (mode,t))
        thread2.start()

AUTO_MODE=0
cmd=0
EX_POWER=0
def downloader():
    global AUTO_MODE
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
######################################### 0. 초기화 ############################################
        if cmd==0:
            #### 초기화 ####
            Progress2_value.set(0)
            p2.update()
            Progress3_value.set(0)
            p3.update()
            Progress4_value.set(0)
            p4.update()
            label1.config(text='')
            label2.config(text='')
            label3.config(text='')
            label4.config(text='')

            label1_check.config(text='',style='light.Link.TButton')
            label2_check.config(text='',style='light.Link.TButton')
            label3_check.config(text='',style='light.Link.TButton')
            label4_check.config(text='',style='light.Link.TButton')

            pass
            ###############
##################################################################################################
######################################### 1. 자동설치 ############################################
        if cmd==1:
            AUTO_MODE=1
            cmd=2
##################################################################################################
######################################### 2. 전원켜기 ############################################
        if cmd==2:
            if EX_POWER==0:
                uart_atmega.EX_POWER_ON()
                uart_atmega.BUTTON_LED_ON()
                LED_PROGRESS(2,30)
                time.sleep(30)
                EX_POWER=1
                b2.config(text="2.전원끄기")
            else:
                uart_atmega.EX_POWER_OFF()
                uart_atmega.BUTTON_LED_OFF()
                LED_PROGRESS_CLEAR(2)
                EX_POWER=0
                b2.config(text="2.전원켜기")
            busy_check()
            if AUTO_MODE==1:
                cmd=3
##################################################################################################
######################################### 3. 다운로드 ############################################
        if cmd==3:
            if EX_POWER==0:
                uart_atmega.EX_POWER_ON()
                uart_atmega.BUTTON_LED_ON()
                LED_PROGRESS(2,30)
                time.sleep(30)
                EX_POWER=1
                b2.config(text="2.전원끄기")
                busy_check()

            LED_PROGRESS(3,230)
            download.Download_start()
            
            busy_check()
            if AUTO_MODE==1:
                cmd=4
##################################################################################################
######################################### 4. 통신셋팅 ############################################
        if cmd==4:
            print(EX_POWER)
            if EX_POWER==0:
                uart_atmega.EX_POWER_ON()
                uart_atmega.BUTTON_LED_ON()
                LED_PROGRESS(2,30)
                time.sleep(30)
                EX_POWER=1
                b2.config(text="2.전원끄기")
                busy_check()

            LED_PROGRESS(4,70)
            com.com_setup()

            busy_check()
            if AUTO_MODE==1:
                cmd=5
##################################################################################################
######################################### 5. 통신상태 ############################################
        if cmd==5:
            if EX_POWER==0:
                uart_atmega.EX_POWER_ON()
                uart_atmega.BUTTON_LED_ON()
                LED_PROGRESS(2,30)
                time.sleep(30)
                EX_POWER=1
                b2.config(text="2.전원끄기")
                busy_check()

            com.atcom_setup()
            AT_CGDCONT_result=com.AT_CGDCONT()
            AT_QIMSCFG_result=com.AT_QIMSCFG()
            AT_QCFG_NWSCANMODE_result=com.AT_QCFG_NWSCANMODE()
            AT_QCFG_lte_bandprior_result=com.AT_QCFG_lte_bandprior()

            label1.config(text=AT_CGDCONT_result)
            label2.config(text=AT_QIMSCFG_result)
            label3.config(text=AT_QCFG_NWSCANMODE_result)
            label4.config(text=AT_QCFG_lte_bandprior_result)


############################ AT_CGDCONT_result check ##########################
            main_string = AT_CGDCONT_result
            search_string = "1,\"IPV4V6\""

            if search_string in main_string:
                label1_check.config(style='success.TButton')
                label1_check.config(text='OK')
            else:
                label1_check.config(style='danger.TButton')
                label1_check.config(text='ERROR')
################################################################################
############################ AT_QIMSCFG_result check ##########################
            main_string = AT_QIMSCFG_result
            search_string = "\"ims\",2"

            if search_string in main_string:
                label2_check.config(style='success.TButton')
                label2_check.config(text='OK')
            else:
                label2_check.config(style='danger.TButton')
                label2_check.config(text='ERROR')
################################################################################
############################ AT_QCFG_NWSCANMODE_result check ##########################
            main_string = AT_QCFG_NWSCANMODE_result
            search_string = "\"nwscanmode\",3"

            if search_string in main_string:
                label3_check.config(style='success.TButton')
                label3_check.config(text='OK')
            else:
                label3_check.config(style='danger.TButton')
                label3_check.config(text='ERROR')
################################################################################
############################ AT_QCFG_lte_bandprior_result check ##########################
            main_string = AT_QCFG_lte_bandprior_result
            search_string = "\"lte/bandprior\",05,03"

            if search_string in main_string:
                label4_check.config(style='success.TButton')
                label4_check.config(text='OK')
            else:
                label4_check.config(style='danger.TButton')
                label4_check.config(text='ERROR')
################################################################################


            time.sleep(10)
            busy_check()
##################################################################################################
######################################### 6. 펌웨어 교체 ############################################
        if cmd==6:
            print("changw firm start")
            LED_PROGRESS(3,300)
            download.scan_disk_and_mount()
            download.updata_img_unpack()
            download.disk_all_unmount()
            print("changw firm end")
            busy_check()
##################################################################################################
######################################### 7. 스크립트 교체 ############################################
        if cmd==7:
            print("script change start")
            LED_PROGRESS(3,10)
            download.scan_disk_and_mount()
            script_copy.Script_copy()
            time.sleep(5)
            download.disk_all_unmount()
            print("script change end")
            busy_check()
##################################################################################################
######################################### 8. usb 포멧 ############################################
        if cmd==8:
            print("usb format start")
            LED_PROGRESS(3,10)
            download.disk_vfat_fomat()
            time.sleep(5)
            print("usb format end")
            busy_check()
##################################################################################################
        AUTO_MODE=0
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
my_style.configure("light.Outline.TButton",font=("Helvetica",30))

my_style2 = ttk.Style()
my_style2.configure("primary.Link.TButton",font=("Helvetica",20))

my_style3 = ttk.Style()
my_style3.configure("info.Outline.TButton",font=("Helvetica",20))

my_style4 = ttk.Style()
my_style4.configure("success.TButton",font=("Helvetica",20))

my_style5 = ttk.Style()
my_style5.configure("danger.TButton",font=("Helvetica",20))

my_style6 = ttk.Style()
my_style6.configure("light.Link.TButton",font=("Helvetica",20))

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



############################################### COM LABEL 1 ##############################################

label1=ttk.Label(root,  text="",
                        style='primary.Link.TButton',
                        width=40,
                        anchor="w")
label1.place(x=410, y=420)
label1_check=ttk.Label(root,  text="",
                        style='light.Link.TButton',
                        width=6,
                        anchor="center")
label1_check.place(x=280, y=420,height=40)
############################################### COM LABEL 2 ##############################################

label2=ttk.Label(root,  text="",
                        style='primary.Link.TButton',
                        width=40,
                        anchor="w")
label2.place(x=410, y=455)
label2_check=ttk.Label(root,  text="",
                        style='light.Link.TButton',
                        width=6,
                        anchor="center")
label2_check.place(x=280, y=455,height=40)
############################################### COM LABEL 3 ##############################################

label3=ttk.Label(root,  text="",
                        style='primary.Link.TButton',
                        width=40,
                        anchor="w")
label3.place(x=410, y=490)
label3_check=ttk.Label(root,  text="",
                        style='light.Link.TButton',
                        width=6,
                        anchor="center")
label3_check.place(x=280, y=490,height=40)
############################################### COM LABEL 4 ##############################################

label4=ttk.Label(root,  text="",
                        style='primary.Link.TButton',
                        width=40,
                        anchor="w")
label4.place(x=410, y=525)
label4_check=ttk.Label(root,  text="",
                        style='light.Link.TButton',
                        width=6,
                        anchor="center")
label4_check.place(x=280, y=525,height=40)
############################################################################################################

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
# ############################################### 프로그레스바 5 ##############################################
# Progress5_value = ttk.DoubleVar()
# p5 = ttk.Progressbar(root,maximum=100,length=100,variable=Progress5_value,bootstyle="success")
# p5.place(x=300, y=442, height=35)
# ############################################################################################################


############################################### 버튼 1 #####################################################
b1 = ttk.Button(root, text='1.자동설치',
                style='light.Outline.TButton',
                width=9)
def b1_bt_pressed():
    global cmd
    print("b1_bt_pressed")
    cmd=1
b1["command"] = b1_bt_pressed
b1.place(x=10, y=23)
############################################### 버튼 2 #####################################################
b2 = ttk.Button(root, text='2.전원켜기',
                style='light.Outline.TButton',
                width=9)
def b2_bt_pressed():
    global cmd
    print("b2_bt_pressed")
    cmd=2

b2["command"] = b2_bt_pressed
b2.place(x=10, y=125)
############################################### 버튼 3 #####################################################
b3 = ttk.Button(root, text='3.다운로드',
                style='light.Outline.TButton',
                width=9)
def b3_bt_pressed():
    global cmd
    print("b3_bt_pressed")
    cmd=3

b3["command"] = b3_bt_pressed
b3.place(x=10, y=225)
############################################### 버튼 4 #####################################################
b4 = ttk.Button(root, text='4.통신셋팅',
                style='light.Outline.TButton',
                width=9)
def b4_bt_pressed():
    global cmd
    print("b4_bt_pressed")
    cmd=4

b4["command"] = b4_bt_pressed
b4.place(x=10, y=325)
############################################### 버튼 5 #####################################################
b5 = ttk.Button(root, text='5.통신상태',
                style='light.Outline.TButton',
                width=9)
def b5_bt_pressed():
    global cmd
    print("b5_bt_pressed")
    cmd=5

b5["command"] = b5_bt_pressed
b5.place(x=10, y=425)
############################################################################################################
############################################### 버튼 6 #####################################################
b6 = ttk.Button(root, text='펌웨어 교체',
                style='info.Outline.TButton',
                width=10)
def b6_bt_pressed():
    global cmd
    print("b6_bt_pressed")
    cmd=6

b6["command"] = b6_bt_pressed
b6.place(x=800, y=18, height =80)
############################################################################################################
############################################### 버튼 7 #####################################################
b7 = ttk.Button(root, text='스크립트 교체',
                style='info.Outline.TButton',
                width=10)
def b7_bt_pressed():
    global cmd
    print("b7_bt_pressed")
    cmd=7

b7["command"] = b7_bt_pressed
b7.place(x=600, y=18, height =80)
############################################################################################################
############################################### 버튼 8 #####################################################
b8 = ttk.Button(root, text='USB 포멧',
                style='info.Outline.TButton',
                width=10)
def b8_bt_pressed():
    global cmd
    print("b8_bt_pressed")
    cmd=8

b8["command"] = b8_bt_pressed
b8.place(x=400, y=18, height =80)
############################################################################################################

timer_1s()

root.mainloop()
