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
            uart_atmega.LED_SETTING(0)
            uart_atmega.Download_Process_led_color_RED()
            uart_atmega.Download_Process_led_bar(10)
            time.sleep(10)
            uart_atmega.LED_SETTING(0)
            key0=0
            
    else :
        if key0==1:
            print("flash Download Mode")
            uart_atmega.LED_SETTING(0)
            uart_atmega.Download_Process_led_color_GREEN()
            uart_atmega.Download_Process_led_bar(10)
            time.sleep(10)
            uart_atmega.LED_SETTING(0)
        key0=0
        uart_atmega.LED_SETTING(0)



