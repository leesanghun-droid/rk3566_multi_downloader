#!/bin/bash

IMAGE_DIR=$PROJECT_DIR/USB_DETECT_TEST/usb_memory

image=$1

TOOL=$PROJECT_DIR/UNPACK_TOOL/aarch64
TEMP_OUT=$TOOL/output
OUT=$IMAGE_DIR/output
RKIMAGEMAKER=${TOOL}/rkImageMaker
AFPTOOL=${TOOL}/afptool
IMAGE=$IMAGE_DIR/$1
UNZIP_IMAGE_DIR=$PROJECT_DIR/IMAGE
QEMU_AARCH64=$TOOL/qemu-x86_64-static

sudo rm -r ${OUT}
sudo mkdir -p ${OUT}
sudo mkdir -p ${UNZIP_IMAGE_DIR}

start_time=$(date +%s)
sudo $QEMU_AARCH64 ${RKIMAGEMAKER} -unpack ${IMAGE} ${OUT} || pause
end_time=$(date +%s)
rkImage_time=$(( end_time - start_time ))
echo -e "\e[47;1;32m rkImage_time: $rkImage_time sec \e[0m"

start_time2=$(date +%s)
sudo $QEMU_AARCH64 ${AFPTOOL}  -unpack ${OUT}/firmware.img ${UNZIP_IMAGE_DIR} || pause
end_time2=$(date +%s)

afptool_time=$(( end_time2 - start_time2 ))
total_time=$(( end_time2 - start_time ))

echo -e "\e[47;1;32m afptool_time: $afptool_time sec \e[0m"
echo -e "\e[47;1;32m total_time: $total_time sec \e[0m"