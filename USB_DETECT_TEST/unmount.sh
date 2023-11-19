#!/bin/bash
USB_MEMORY_DIR=/home/lsh/rk3566_multi_downloader/USB_DETECT_TEST/usb_memory

sudo eject /dev/sda1
sudo rm -r $USB_MEMORY_DIR