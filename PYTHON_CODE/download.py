import subprocess
import Run_after_script
import Run_before_script

def Download_start():
    print("Download_start")
    before_result=Run_before_script.run_before_script()
    if before_result==0:
        subprocess.run(["/home/linaro/rk3566_multi_downloader/DOWNLOAD_TOOL/download.sh"],shell=True)
    else:
        print("Run_before_script_Faild~")
        
    after_result=Run_after_script.run_after_script()
    if before_result==1:
        print("Run_after_script_Faild~")
        
def scan_disk_and_mount():
    subprocess.run(["/home/linaro/rk3566_multi_downloader/USB_DETECT_TEST/init_usb_memory.sh mount"],shell=True)
    
def updata_img_unpack():
    subprocess.run(["/home/linaro/rk3566_multi_downloader/USB_DETECT_TEST/init_usb_memory.sh unpack"],shell=True)
    
def disk_all_unmount():
    subprocess.run(["/home/linaro/rk3566_multi_downloader/USB_DETECT_TEST/init_usb_memory.sh unmount"],shell=True)
    
    
    #/home/linaro/rk3566_multi_downloader/USB_DETECT_TEST/init_usb_memory.sh unmount