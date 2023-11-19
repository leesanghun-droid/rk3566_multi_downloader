#!/bin/bash

echo start_mount~
echo device name : $1
mkdir -p ./usb_memory
chmod 777 ./usb_memory
sudo mount -t vfat /dev/$1 ./usb_memory
#sudo eject /dev/sda1