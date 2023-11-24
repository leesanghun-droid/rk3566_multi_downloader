import script_copy
import download
import uart_atmega
import time

def USB_Update_copy():    
    print("usb Copy Mode")
    uart_atmega.BUTTON_LED_ON()
    uart_atmega.LED_SETTING(12)
    uart_atmega.Download_Process_led_color_YELLOW()
    uart_atmega.Download_Process_led_bar(240)
    download.scan_disk_and_mount()
    download.updata_img_unpack()
    download.disk_all_unmount()
    uart_atmega.LED_SETTING(0)
    uart_atmega.Download_Process_led_bar(0)
    time.sleep(12)
    uart_atmega.BUTTON_LED_OFF()
    
def USB_Script_copy():    
    print("User_script copy mode")
    uart_atmega.BUTTON_LED_ON()
    uart_atmega.LED_SETTING(12)
    uart_atmega.Download_Process_led_color_RED()
    uart_atmega.Download_Process_led_bar(20)
    download.scan_disk_and_mount()
    script_copy.Script_copy()
    time.sleep(20)
    download.disk_all_unmount()
    uart_atmega.LED_SETTING(0)
    uart_atmega.Download_Process_led_bar(0)
    #time.sleep(12)
    uart_atmega.BUTTON_LED_OFF()