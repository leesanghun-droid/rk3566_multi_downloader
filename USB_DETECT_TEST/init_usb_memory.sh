#!/bin/bash

usb_msg="USB Mass Storage device detected"
dmesg_usb_result=$(dmesg | grep "USB Mass Storage device detected")
USB_DETECT=FALSE
if [[ "$dmesg_usb_result" == *"$usb_msg"* ]]; then USB_DETECT=TRUE; else USB_DETECT=FALSE; fi;
#echo FIND_USB : $USB_DETECT

device_msg="sda: sd"
DEVICE_DETECT=FALSE
dmesg_device_result=$(dmesg | grep "sda: sd")
if [[ "$dmesg_device_result" == *"$device_msg"* ]]; then DEVICE_DETECT=TRUE; else DEVICE_DETECT=FALSE; fi;
#echo FIND_DEVICE : $DEVICE_DETECT

if [[ "$DEVICE_DETECT" == "TRUE" ]] && [[ "$USB_DETECT" == "TRUE" ]]
then
device="${dmesg_device_result:(-4)}"
echo $device
sudo dmesg -c
. $PROJECT_DIR/USB_DETECT_TEST/mount.sh $device
fi