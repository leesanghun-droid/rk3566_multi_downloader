#!/bin/bash

PROJECT_DIR=/home/linaro/rk3566_multi_downloader
USB_MEMORY_DIR=$PROJECT_DIR/USB_DETECT_TEST/usb_memory
USER_SCRIPT_DIR=/home/linaro/rk3566_multi_downloader/USER_SCRIPT

DEVICE_SCRIPT_LOG_DIR=$USER_SCRIPT_DIR/log
work=`cat /home/linaro/device_Identity`
MEMORY_SCRIPT_LOG_DIR=$USB_MEMORY_DIR/USER_SCRIPT/log/$work

echo log_copy~

sudo mkdir -p $MEMORY_SCRIPT_LOG_DIR

sudo cp -r $DEVICE_SCRIPT_LOG_DIR/*  $MEMORY_SCRIPT_LOG_DIR