import subprocess
import download
import uart_atmega
import time
import flash_download_mode  as FD
import usb_update_copy      as UC

key0=0
num=0

while True:
    uart_atmega.EX_POWER_OFF()
    uart_atmega.BUTTON_LED_OFF()
    num=num+1
    result=uart_atmega.read_serial()
    print(str(num)+" : "+result)

    if result=="Press":
        key0=key0+1
        if key0>=1:
            uart_atmega.LED_SETTING(key0)     
    else :
        if key0==1:
            FD.Flash_download()
        if key0==3:
            UC.USB_Update_copy()
        if key0==5:
            UC.USB_Script_copy()
            
            
        key0=0
        uart_atmega.LED_SETTING(0)



