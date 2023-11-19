#!/bin/bash

IMAGE_DIR="/home/linaro/rk3566_multi_downloader/IMAGE/Image"
TOOL_DIR="/home/linaro/rk3566_multi_downloader/DOWNLOAD_TOOL"
RKDEVELOPTOOL=$TOOL_DIR/rkdeveloptool

echo $IMAGE_DIR

sudo $RKDEVELOPTOOL ef
sudo $RKDEVELOPTOOL gpt $IMAGE_DIR/parameter.txt 
sudo $RKDEVELOPTOOL prm $IMAGE_DIR/parameter.txt 
sudo $RKDEVELOPTOOL ppt
echo "u-boot upload..."
sudo $RKDEVELOPTOOL wlx uboot $IMAGE_DIR/uboot.img 
echo "misc upload..."
sudo $RKDEVELOPTOOL wlx misc $IMAGE_DIR/misc.img 
echo "dtbo upload..."
sudo $RKDEVELOPTOOL wlx dtbo $IMAGE_DIR/dtbo.img 
echo "vbmeta upload..."
sudo $RKDEVELOPTOOL wlx vbmeta $IMAGE_DIR/vbmeta.img 
echo "boot upload..."
sudo $RKDEVELOPTOOL wlx boot $IMAGE_DIR/boot.img 
echo "recovery upload..."
sudo $RKDEVELOPTOOL wlx recovery $IMAGE_DIR/recovery.img 
echo "super upload..."
sudo $RKDEVELOPTOOL wlx super $IMAGE_DIR/super.img 
echo "loader upload..."
sudo $RKDEVELOPTOOL ul $IMAGE_DIR/MiniLoaderAll.bin 
sleep 1
sudo $RKDEVELOPTOOL rd 
sleep 1
