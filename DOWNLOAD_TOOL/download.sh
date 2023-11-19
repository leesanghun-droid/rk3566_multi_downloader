#!/bin/bash

echo test

# IMAGE_DIR=$PROJECT_DIR/IMAGE/Image
# RKTOOL=./rkdeveloptool

# echo $IMAGE_DIR

# sudo $RKTOOL rd 
# sleep 1
# sudo $RKTOOL db $IMAGE_DIR/MiniLoaderAll.bin 
# sudo $RKTOOL ef
# sudo $RKTOOL gpt $IMAGE_DIR/parameter.txt 
# sudo $RKTOOL prm $IMAGE_DIR/parameter.txt 
# sudo $RKTOOL ppt
# echo "u-boot upload..."
# sudo $RKTOOL wlx uboot $IMAGE_DIR/uboot.img 
# echo "misc upload..."
# sudo $RKTOOL wlx misc $IMAGE_DIR/misc.img 
# echo "dtbo upload..."
# sudo $RKTOOL wlx dtbo $IMAGE_DIR/dtbo.img 
# echo "vbmeta upload..."
# sudo $RKTOOL wlx vbmeta $IMAGE_DIR/vbmeta.img 
# echo "boot upload..."
# sudo $RKTOOL wlx boot $IMAGE_DIR/boot.img 
# echo "recovery upload..."
# sudo $RKTOOL wlx recovery $IMAGE_DIR/recovery.img 
# echo "super upload..."
# sudo $RKTOOL wlx super $IMAGE_DIR/super.img 
# echo "loader upload..."
# sudo $RKTOOL ul $IMAGE_DIR/MiniLoaderAll.bin 
# sleep 1
# sudo $RKTOOL rd 
# sleep 1







#export ADB=./rk3566_adb
#export RKTOOL=./rkdeveloptool

#${ADB} -d devices
#${ADB} -d shell uname -a

#sudo -S ./rk3566_adb -d reboot loader