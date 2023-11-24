import download
import uart_atmega
import time

def Flash_download():    
    print("flash Download Mode")
    uart_atmega.BUTTON_LED_ON()
    uart_atmega.EX_POWER_ON()
    time.sleep(10)
    uart_atmega.LED_SETTING(0)
    uart_atmega.Download_Process_led_color_GREEN()
    uart_atmega.Download_Process_led_bar(160) # set 10 => 10 second
    download.Download_start()
    uart_atmega.EX_POWER_OFF()
    uart_atmega.BUTTON_LED_OFF()
    uart_atmega.LED_SETTING(0)
    uart_atmega.Download_Process_led_bar(0)