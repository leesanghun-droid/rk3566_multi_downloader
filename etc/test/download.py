import subprocess

result=subprocess.run(["/home/linaro/rk3566_multi_downloader/etc/test/download_before.sh"], stdout=subprocess.PIPE)
result_as_string = result.stdout.decode('utf-8')
print(result.stdout)