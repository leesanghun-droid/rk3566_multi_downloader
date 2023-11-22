import download
import uart_atmega
import time
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
            #print("LED" + str(key0))#LED(GREEN,key0)
            uart_atmega.LED_SETTING(key0)
        if key0==5:
            print("usb Copy Mode")
            uart_atmega.LED_SETTING(0)
            uart_atmega.Download_Process_led_color_YELLOW()
            uart_atmega.Download_Process_led_bar(640)
            download.scan_disk_and_mount()
            download.updata_img_unpack()
            download.disk_all_unmount()
            uart_atmega.LED_SETTING(0)
            uart_atmega.Download_Process_led_bar(0)
            key0=0
            
    else :
        if key0==1:
            print("flash Download Mode")
            uart_atmega.BUTTON_LED_ON()
            uart_atmega.EX_POWER_ON()
            time.sleep(20)
            uart_atmega.LED_SETTING(0)
            uart_atmega.Download_Process_led_color_GREEN()
            uart_atmega.Download_Process_led_bar(200) # set 10 => 10 second
            download.Download_start()
            uart_atmega.EX_POWER_OFF()
            uart_atmega.BUTTON_LED_OFF()
            uart_atmega.LED_SETTING(0)
            uart_atmega.Download_Process_led_bar(0)
        key0=0
        uart_atmega.LED_SETTING(0)



