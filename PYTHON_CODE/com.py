import subprocess

def com_setup():
    print("Communication module setup start~")
    result=subprocess.run(["/home/linaro/rk3566_multi_downloader/USER_SCRIPT/download_before.sh"], stdout=subprocess.PIPE)
    result_as_string = result.stdout.decode('iso8859-1')
    print(result_as_string)
    search_string="SCRIPT_ERROR"
    RETURN_FAILD=0
    if search_string in result_as_string:
        RETURN_FAILD=1

    print("Communication module setup end")
    return RETURN_FAILD

def atcom_setup():
    print("atcom_setup start")
    result=subprocess.run(["/home/linaro/rk3566_multi_downloader/COM_TOOL/atcom_setup.sh"], stdout=subprocess.PIPE)
    result_as_string = result.stdout.decode('iso8859-1')
    print(result_as_string)
    search_string="OK"
    if search_string in result_as_string:
        print("ATCOM_SETUP OK~!")
    print("atcom_setup end")