#!/bin/bash
USB_MEMORY_DIR=/home/lsh/rk3566_multi_downloader/USB_DETECT_TEST/usb_memory

sudo eject /dev/sda1
sudo eject /dev/sdb1
sudo eject /dev/sdc1
sudo eject /dev/sdd1
sudo eject /dev/sde1
sudo eject /dev/sdf1
sudo eject /dev/sdg1
sudo eject /dev/sdh1

sudo rm -r $USB_MEMORY_DIR