import subprocess
import download
import uart_atmega
import time
import flash_download_mode  as FD
import usb_update_copy      as UC

delete_log=0
key0=0
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
        key0=key0+1
        if key0>=1:
            uart_atmega.LED_SETTING(key0)     
    else :
        if key0==1:
            subprocess.run(["sudo rm -rf /var/log/*"],shell=True)
            FD.Flash_download()
        if key0==3:
            subprocess.run(["sudo rm -rf /var/log/*"],shell=True)
            UC.USB_Update_copy()
        if key0==4:
            print("LOG DELETE")
            subprocess.run(["sudo rm -rf /var/log/*"],shell=True)
        if key0==5:
            subprocess.run(["sudo rm -rf /var/log/*"],shell=True)
            UC.USB_Script_copy()
        if key0==7:
            subprocess.run(["sudo rm -rf /var/log/*"],shell=True)
            UC.USB_Log_copy()
        if key0==12:
            print("USB VFAT FOMAT")
            UC.USB_vfat_format()
            
        key0=0
        uart_atmega.LED_SETTING(0)



