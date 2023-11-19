#!/bin/bash

export PROJECT_DIR=/home/lsh/rk3566_multi_downloader

while [ TRUE ]
do
. $PROJECT_DIR/USB_DETECT_TEST/init_usb_memory.sh
sleep 1
done


#/home/lsh/rk3566_multi_downloader/USB_DETECT_TEST/unmount.sh