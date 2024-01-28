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

def AT_QIMSCFG():
    print("AT_QIMSCFG start")
    result=subprocess.run(["/home/linaro/rk3566_multi_downloader/COM_TOOL/AT_QIMSCFG.sh"], stdout=subprocess.PIPE)
    result_as_string = result.stdout.decode('iso8859-1')

    str1 = result_as_string.replace('\n', '')
    str2 = str1.replace('OK', '')
    print(str2)
    return str2
    print("AT_QIMSCFG end")

def AT_CGDCONT():
    print("AT_CGDCONT start")
    result=subprocess.run(["/home/linaro/rk3566_multi_downloader/COM_TOOL/AT_CGDCONT.sh"], stdout=subprocess.PIPE)
    result_as_string = result.stdout.decode('iso8859-1')

    str1 = result_as_string.replace('\n', '')
    str2 = str1.replace('OK', '')
    print(str2)
    return str2
    print("AT_CGDCONT end")

def AT_QCFG_lte_bandprior():
    print("AT_QCFG_lte_bandprior start")
    result=subprocess.run(["/home/linaro/rk3566_multi_downloader/COM_TOOL/AT_QCFG_lte_bandprior.sh"], stdout=subprocess.PIPE)
    result_as_string = result.stdout.decode('iso8859-1')

    str1 = result_as_string.replace('\n', '')
    str2 = str1.replace('OK', '')
    print(str2)
    return str2
    print("AT_QCFG_lte_bandprior end")

def AT_QCFG_NWSCANMODE():
    print("AT_QCFG_NWSCANMODE start")
    result=subprocess.run(["/home/linaro/rk3566_multi_downloader/COM_TOOL/AT_QCFG_NWSCANMODE.sh"], stdout=subprocess.PIPE)
    result_as_string = result.stdout.decode('iso8859-1')

    str1 = result_as_string.replace('\n', '')
    str2 = str1.replace('OK', '')
    print(str2)
    return str2
    print("AT_QCFG_NWSCANMODE end")