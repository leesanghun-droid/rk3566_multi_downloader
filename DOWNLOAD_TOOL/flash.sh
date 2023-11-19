#!/bin/bash

IMAGE_DIR="/home/linaro/rk3566_multi_downloader/IMAGE/Image"
TOOL_DIR="/home/linaro/rk3566_multi_downloader/DOWNLOAD_TOOL"
RKDEVELOPTOOL=$TOOL_DIR/rkdeveloptool

echo $IMAGE_DIR

sudo $RKDEVELOPTOOL ef
sleep 1
sudo $RKDEVELOPTOOL rd 
sleep 5
sudo $RKDEVELOPTOOL db $IMAGE_DIR/MiniLoaderAll.bin
sleep 5
sudo $RKDEVELOPTOOL gpt $IMAGE_DIR/parameter.txt                    ;sleep 1;
sudo $RKDEVELOPTOOL prm $IMAGE_DIR/parameter.txt                    ;sleep 1;
sudo $RKDEVELOPTOOL ppt                                             ;sleep 1;
echo "u-boot upload..."
sudo $RKDEVELOPTOOL wlx uboot $IMAGE_DIR/uboot.img                  ;sleep 1;
echo "misc upload..."
sudo $RKDEVELOPTOOL wlx misc $IMAGE_DIR/misc.img                    ;sleep 1;
echo "dtbo upload..."
sudo $RKDEVELOPTOOL wlx dtbo $IMAGE_DIR/dtbo.img                    ;sleep 1;
echo "vbmeta upload..."
sudo $RKDEVELOPTOOL wlx vbmeta $IMAGE_DIR/vbmeta.img                ;sleep 1;
echo "boot upload..."
sudo $RKDEVELOPTOOL wlx boot $IMAGE_DIR/boot.img                    ;sleep 1;
echo "recovery upload..."
sudo $RKDEVELOPTOOL wlx recovery $IMAGE_DIR/recovery.img            ;sleep 1;
echo "baseparameter upload..."
sudo $RKDEVELOPTOOL wlx baseparameter $IMAGE_DIR/baseparameter.img  ;sleep 1;
echo "super upload..."
sudo $RKDEVELOPTOOL wlx super $IMAGE_DIR/super.img                  ;sleep 1;
echo "loader upload..."
sudo $RKDEVELOPTOOL ul $IMAGE_DIR/MiniLoaderAll.bin                 ;sleep 1;
sudo $RKDEVELOPTOOL rd                                              ;sleep 1;
