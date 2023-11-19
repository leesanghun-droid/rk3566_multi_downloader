#!/bin/bash

usb_msg="USB Mass Storage device detected"
dmesg_usb_result=$(dmesg | grep "USB Mass Storage device detected")
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

echo -e "\e[47;1;32m mount start~ \e[0m"
. $PROJECT_DIR/USB_DETECT_TEST/mount.sh $device
echo -e "\e[47;1;32m unpack start~ \e[0m"
. $PROJECT_DIR/UNPACK_TOOL/aarch64/unpack_aarch64.sh update.img
echo -e "\e[47;1;32m unmount start~ \e[0m"
. $PROJECT_DIR/USB_DETECT_TEST/unmount.sh
echo -e "\e[47;1;32m unmount done~ \e[0m"
fi