#!/bin/bash
TOOL_DIR="/home/linaro/rk3566_multi_downloader/DOWNLOAD_TOOL"
ATCOM_DIR=$TOOL_DIR/atcom
ADB=$TOOL_DIR/rk3566_adb

echo "ADB root"
$ADB -d root
echo "install atcom"
$ADB -d push $ATCOM_DIR /data
echo "atcom add Permission"
$ADB -d shell chmod 777 /data/atcom

echo "START LTE INIT..."
echo "0. AT"
echo "#RESULT############################"
$ADB -d shell /data/atcom "AT"
echo "###################################"
echo ""