import subprocess

def Script_copy():
    print("script copy start")
    subprocess.run(["/home/linaro/rk3566_multi_downloader/USER_SCRIPT/File_copy.sh"],shell=True)
    
def Script_LOG_copy():
    print("script log copy start")
    subprocess.run(["/home/linaro/rk3566_multi_downloader/USER_SCRIPT/log_copy.sh"],shell=True)