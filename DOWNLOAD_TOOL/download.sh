#!/bin/bash

IMAGE_DIR="/home/linaro/rk3566_multi_downloader/IMAGE/Image"
TOOL_DIR="/home/linaro/rk3566_multi_downloader/DOWNLOAD_TOOL"
RKDEVELOPTOOL=$TOOL_DIR/rkdeveloptool
ADB=$TOOL_DIR/rk3566_adb

num=0
while [ ${num} -le 20 ]
do
        maskrom=$(lsusb | grep "2207:350a" | wc -l)
        num=$((${num}+1))

if [ ${maskrom} == "1" ]
then
  echo -e "\e[34mFIND [2207:350a]\e[0m"
  num2=0
  break
else
  echo -e "\e[31mFalse into MASKROM MODE~~! goto loader mode!! try ${num}/20 times\e[0m"
  sudo $ADB -d reboot loader
  sleep 2
fi
done

if [ ${maskrom} == "1" ]
then
  echo -e "\e[34mFind MASKROM MODE OK\e[0m"
  work=$(sudo $RKDEVELOPTOOL td);echo ""
  if [[ "${work}" == *failed!* ]]
    then
    echo "Test Device faild~!!"
    echo "CMD ==>> sudo ./rkdeveloptool db ./MiniLoaderAll.bin"
    sudo $RKDEVELOPTOOL db ${TOOL_DIR}/MiniLoaderAll.bin
    sleep 5
  fi
  work=$(sudo $RKDEVELOPTOOL td);echo ""
  if [[ "${work}" == *OK.* ]]
    then
    echo "Test Device ok."
    echo start_flash~~
    . $TOOL_DIR/flash.sh
  fi
else
  echo -e "\e[31mMASKROM MODE Find Faild \e[0m"
fi