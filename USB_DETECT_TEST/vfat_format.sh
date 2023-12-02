#!/bin/bash

USB_MEMORY_DIR=$PROJECT_DIR/USB_DETECT_TEST/usb_memory

echo device name : $1
sudo mkfs.vfat /dev/$1