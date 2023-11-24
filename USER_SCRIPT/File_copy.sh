#!/bin/bash

PROJECT_DIR=/home/linaro/rk3566_multi_downloader
USB_MEMORY_DIR=$PROJECT_DIR/USB_DETECT_TEST/usb_memory

BEFORE_SCRIPT_FILE=$USB_MEMORY_DIR/USER_SCRIPT/download_before.sh
AFTER_SCRIPT_FILE=$USB_MEMORY_DIR/USER_SCRIPT/download_after.sh

if [ -e $BEFORE_SCRIPT_FILE ]
then
    echo "BEFORE_SCRIPT_FILE exist~"
else
    echo "BEFORE_SCRIPT_FILE not exist~"
fi

if [ -e $AFTER_SCRIPT_FILE ]
then
    echo "AFTER_SCRIPT_FILE exist~"
else
    echo "AFTER_SCRIPT_FILE not exist~"
fi