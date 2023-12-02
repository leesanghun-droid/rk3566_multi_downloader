#!/bin/bash

USB_MEMORY_DIR=$PROJECT_DIR/USB_DETECT_TEST/usb_memory

echo device name : $1
mkdir -p $USB_MEMORY_DIR
chmod 777 $USB_MEMORY_DIR
sudo mount -t ntfs /dev/$1 $USB_MEMORY_DIR
#sudo eject /dev/sda1