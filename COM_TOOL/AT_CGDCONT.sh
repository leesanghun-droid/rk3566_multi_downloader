#!/bin/bash
TOOL_DIR="/home/linaro/rk3566_multi_downloader/DOWNLOAD_TOOL"
ATCOM_DIR=$TOOL_DIR/atcom
ADB=$TOOL_DIR/rk3566_adb

$ADB -d shell /data/atcom "AT+CGDCONT?"