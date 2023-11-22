#!/bin/bash

while [ TRUE ]
do
#lsusb
#maskrom=$(lsusb | grep "2207:350a" | wc -l)
lsusb | grep "rk3566"
done