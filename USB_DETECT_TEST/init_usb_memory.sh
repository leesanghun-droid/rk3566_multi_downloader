#!/bin/bash

PROJECT_DIR=/home/linaro/rk3566_multi_downloader

########################### mount start ######################################
if [[ "$*" == *mount* ]]
then
usb_msg="New USB device found"
dmesg_usb_result=$(dmesg | grep "New USB device found")
USB_DETECT=FALSE
if [[ "$dmesg_usb_result" == *"$usb_msg"* ]]; then USB_DETECT=TRUE; else USB_DETECT=FALSE; fi;
#echo FIND_USB : $USB_DETECT

DEVICE_DETECT=FALSE

if [[ "$DEVICE_DETECT" == "FALSE" ]]
then
device_msg="sda: sd";dmesg_device_result=$(dmesg | grep "sda: sd")
if [[ "$dmesg_device_result" == *"$device_msg"* ]]; then DEVICE_DETECT=TRUE; else DEVICE_DETECT=FALSE; fi;
fi

if [[ "$DEVICE_DETECT" == "FALSE" ]]
then
device_msg="sdb: sd";dmesg_device_result=$(dmesg | grep "sdb: sd")
if [[ "$dmesg_device_result" == *"$device_msg"* ]]; then DEVICE_DETECT=TRUE; else DEVICE_DETECT=FALSE; fi;
fi

if [[ "$DEVICE_DETECT" == "FALSE" ]]
then
device_msg="sdc: sd";dmesg_device_result=$(dmesg | grep "sdc: sd")
if [[ "$dmesg_device_result" == *"$device_msg"* ]]; then DEVICE_DETECT=TRUE; else DEVICE_DETECT=FALSE; fi;
fi

if [[ "$DEVICE_DETECT" == "FALSE" ]]
then
device_msg="sdd: sd";dmesg_device_result=$(dmesg | grep "sdd: sd")
if [[ "$dmesg_device_result" == *"$device_msg"* ]]; then DEVICE_DETECT=TRUE; else DEVICE_DETECT=FALSE; fi;
fi

if [[ "$DEVICE_DETECT" == "FALSE" ]]
then
device_msg="sde: sd";dmesg_device_result=$(dmesg | grep "sde: sd")
if [[ "$dmesg_device_result" == *"$device_msg"* ]]; then DEVICE_DETECT=TRUE; else DEVICE_DETECT=FALSE; fi;
fi

if [[ "$DEVICE_DETECT" == "FALSE" ]]
then
device_msg="sdf: sd";dmesg_device_result=$(dmesg | grep "sdf: sd")
if [[ "$dmesg_device_result" == *"$device_msg"* ]]; then DEVICE_DETECT=TRUE; else DEVICE_DETECT=FALSE; fi;
fi

if [[ "$DEVICE_DETECT" == "FALSE" ]]
then
device_msg="sdg: sd";dmesg_device_result=$(dmesg | grep "sdg: sd")
if [[ "$dmesg_device_result" == *"$device_msg"* ]]; then DEVICE_DETECT=TRUE; else DEVICE_DETECT=FALSE; fi;
fi

if [[ "$DEVICE_DETECT" == "FALSE" ]]
then
device_msg="sdh: sd";dmesg_device_result=$(dmesg | grep "sdh: sd")
if [[ "$dmesg_device_result" == *"$device_msg"* ]]; then DEVICE_DETECT=TRUE; else DEVICE_DETECT=FALSE; fi;
fi

if [[ "$DEVICE_DETECT" == "TRUE" ]] && [[ "$USB_DETECT" == "TRUE" ]]
then
device="${dmesg_device_result:(-4)}"
echo $device
sudo dmesg -c


if [[ "$*" == *vfat_format* ]]
then
echo -e "\e[47;1;32m vfat format start~ \e[0m"
. $PROJECT_DIR/USB_DETECT_TEST/vfat_format.sh $device
echo -e "\e[47;1;32m vfat format end~ \e[0m"
else
echo -e "\e[47;1;32m mount start~ \e[0m"
. $PROJECT_DIR/USB_DETECT_TEST/mount.sh $device
fi



fi
fi
########################### mount end ######################################

########################### vat format start ######################################

########################### vat format end ######################################

########################### unpack start ######################################
if [[ "$*" == *unpack* ]]
then
echo -e "\e[47;1;32m unpack start~ \e[0m"
. $PROJECT_DIR/UNPACK_TOOL/aarch64/unpack_aarch64.sh update.img
fi
########################### unpack end ######################################

########################### unmount start ######################################
if [[ "$*" == *unmount* ]]
then
echo -e "\e[47;1;32m unmount start~ \e[0m"
. $PROJECT_DIR/USB_DETECT_TEST/unmount.sh
echo -e "\e[47;1;32m unmount done~ \e[0m"
fi
########################### unmount end ######################################