import subprocess
import download
import uart_atmega
import time
import flash_download_mode  as FD
import usb_update_copy      as UC

delete_log=0
cmd=0
num=0

while True:
    uart_atmega.EX_POWER_OFF()
    uart_atmega.BUTTON_LED_OFF()
    num=num+1
    delete_log=delete_log+1
    result=uart_atmega.read_serial()
    print(str(num)+" : "+result)
    
    if delete_log>=100:
        print("DELETE LOG")
        subprocess.run(["sudo rm -rf /var/log/*"],shell=True)
        delete_log=0
    if result=="Press":
        cmd=cmd+1
        if cmd>=1:
            uart_atmega.LED_SETTING(cmd)     
    else :
        if cmd==1:
            FD.Flash_download()
        if cmd==3:
            UC.USB_Update_copy()
        if cmd==5:
            UC.USB_Script_copy()
        if cmd==12:
            print("USB VFAT FOMAT")
            UC.USB_vfat_format()
        cmd=0
        uart_atmega.LED_SETTING(0)



