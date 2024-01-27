import os
import subprocess
import datetime
import uart_atmega
import time

def run_before_script():
    
    subprocess.run(["sudo find /home/linaro/rk3566_multi_downloader/USER_SCRIPT/log -mtime +1 -delete"],shell=True)

    now = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')

    f = open('/home/linaro/device_Identity','r')
    DEVICES_ID=f.readline()
    f.close()

    DEVICES_ID=DEVICES_ID[0:13]

    USER_SCRIPT_DIR='/home/linaro/rk3566_multi_downloader/USER_SCRIPT/log'
    LOG_DIR=USER_SCRIPT_DIR +'/' + now + '_before_Script_LOG_'+ DEVICES_ID

    def createFolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print ('Error: Creating directory. ' + directory)
    createFolder(USER_SCRIPT_DIR)


    result=subprocess.run(["/home/linaro/rk3566_multi_downloader/USER_SCRIPT/download_before.sh"], stdout=subprocess.PIPE)
    result_as_string = result.stdout.decode('iso8859-1')
    print(result_as_string)

    f = open(LOG_DIR,'w')
    f.write(result_as_string)
    f.close()
    
    search_string="SCRIPT_ERROR"
    
    RETURN_FAILD=0
    
    if search_string in result_as_string:
        uart_atmega.Download_Process_led_color_RED()
        uart_atmega.Download_Process_led_bar(0)
        time.sleep(60)
        uart_atmega.LED_SETTING(0)
        RETURN_FAILD=1
        
    return RETURN_FAILD
    
    
    