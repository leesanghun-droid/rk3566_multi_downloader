#!/bin/bash

PROJECT_DIR=/home/linaro/rk3566_multi_downloader
USB_MEMORY_DIR=$PROJECT_DIR/USB_DETECT_TEST/usb_memory

BEFORE_SCRIPT_FILE=$USB_MEMORY_DIR/USER_SCRIPT/download_before.sh
AFTER_SCRIPT_FILE=$USB_MEMORY_DIR/USER_SCRIPT/download_after.sh

USER_SCRIPT_DIR=/home/linaro/rk3566_multi_downloader/USER_SCRIPT

if [ -e $BEFORE_SCRIPT_FILE ]
then
    echo "BEFORE_SCRIPT_FILE exist~"
    sudo cp $BEFORE_SCRIPT_FILE $USER_SCRIPT_DIR
    sed -i 's/\r//' $USER_SCRIPT_DIR/download_before.sh 
else
    echo "BEFORE_SCRIPT_FILE not exist~"
fi

if [ -e $AFTER_SCRIPT_FILE ]
then
    echo "AFTER_SCRIPT_FILE exist~"
    sudo cp $AFTER_SCRIPT_FILE $USER_SCRIPT_DIR
    sed -i 's/\r//' $USER_SCRIPT_DIR/download_before.sh 
else
    echo "AFTER_SCRIPT_FILE not exist~"
fi

sudo chmod 777 $USER_SCRIPT_DIR/*