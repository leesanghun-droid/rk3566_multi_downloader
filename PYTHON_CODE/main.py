import uart_atmega
import time
key0=0
num=0
while True:
    num=num+1
    result=uart_atmega.read_serial()
    print(str(num)+" : "+result)

    if result=="Press":
        key0=key0+1
        if key0>=1:
            #print("LED" + str(key0))#LED(GREEN,key0)
            uart_atmega.LED_SETTING(key0)
        if key0==5:
            print("usb Copy Mode")
            time.sleep(10)
            key0=0
            uart_atmega.LED_SETTING(0)
    else :
        if key0==1:
            print("flash Download Mode")
            uart_atmega.LED_SETTING(0)
            uart_atmega.Flash_Download_Process_led_bar(300)
            time.sleep(300)
            uart_atmega.LED_SETTING(0)
        key0=0
        uart_atmega.LED_SETTING(0)



