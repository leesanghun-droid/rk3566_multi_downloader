#!/bin/bash
TOOL_DIR="/home/linaro/rk3566_multi_downloader/DOWNLOAD_TOOL"
ATCOM_DIR=$TOOL_DIR/atcom
ADB=$TOOL_DIR/rk3566_adb

echo LTE_SETUP_error

echo "ADB root"
$ADB -d root
echo "COPY atcom"
$ADB -d push $ATCOM_DIR /data