#!/bin/bash

str=$(dmesg | grep "sda: sd")
device="${str:(-4)}"
echo $device


#work=$(dmesg)
#echo $work

# for mail in $work
# do
# 	echo $mail
# done


# test=dmesg | grep "USB Mass Storage device detected"

# work=$(cat /proc/uptime | cut -f 1 -d' ')
# echo $work

#dmesg | grep "sda: sd"

#dmesg_text=$(dmesg | cut -f 1 -d']')

#mails=$(echo $work | tr " " "\n")


# for mail in $mails
# do
# 	echo $mail
# done

#echo "This is my message!" | sudo tee /dev/kmsg