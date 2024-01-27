
import subprocess

def run_before_script():
    
    result=subprocess.run(["/home/linaro/rk3566_multi_downloader/USER_SCRIPT/download_before.sh"], stdout=subprocess.PIPE)
    result_as_string = result.stdout.decode('iso8859-1')
    search_string="SCRIPT_ERROR"
    RETURN_FAILD=0
    if search_string in result_as_string:
        RETURN_FAILD=1
    return RETURN_FAILD
    
    
    