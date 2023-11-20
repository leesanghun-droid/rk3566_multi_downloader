import subprocess

PROJECT_DIR="/home/linaro/rk3566_multi_downloader"
TOOL_DIR=PROJECT_DIR+"/DOWNLOAD_TOOL"
DOWNLOAD=TOOL_DIR+ "/download.sh"

print(DOWNLOAD)
subprocess.run([DOWNLOAD], shell=True)