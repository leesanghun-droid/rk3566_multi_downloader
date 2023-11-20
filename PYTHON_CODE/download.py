import subprocess

def Download_start():
    print("Download_start")
    subprocess.run(["/home/linaro/rk3566_multi_downloader/DOWNLOAD_TOOL/download.sh"],shell=True)
    
def scan_disk_and_mount():
    subprocess.run(["/home/linaro/rk3566_multi_downloader/USB_DETECT_TEST/init_usb_memory.sh mount"],shell=True)
    
def updata_img_unpack():
    subprocess.run(["/home/linaro/rk3566_multi_downloader/USB_DETECT_TEST/init_usb_memory.sh unpack"],shell=True)
    
def disk_all_unmount():
    subprocess.run(["/home/linaro/rk3566_multi_downloader/USB_DETECT_TEST/init_usb_memory.sh unmount"],shell=True)
    
    
    #/home/linaro/rk3566_multi_downloader/USB_DETECT_TEST/init_usb_memory.sh unmount