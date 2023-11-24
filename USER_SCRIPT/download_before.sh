#!/bin/bash

echo "download before script start~~"

USER_SCRIPT_DIR=/home/linaro/rk3566_multi_downloader/USER_SCRIPT
TOOL_DIR="/home/linaro/rk3566_multi_downloader/DOWNLOAD_TOOL"
LOG_DIR=$USER_SCRIPT_DIR/log
ATCOM_DIR=$TOOL_DIR/atcom
ADB=$TOOL_DIR/rk3566_adb

echo "wait 15 sec"

echo "ADB root"
$ADB -d root
echo "install atcom"
$ADB -d push $ATCOM_DIR /data
echo "atcom add Permission"
$ADB -d shell chmod 777 /data/atcom

echo "wait 10 sec"
sleep 10

echo "START LTE INIT..."
echo "0. AT"
echo "#RESULT############################"
$ADB -d shell /data/atcom "AT"
echo "###################################"
echo ""
sleep 1

echo "###################################"
echo "                                   "
echo "          LTE SETUP                "
echo "                                   "
echo "###################################"

# echo "1. AT+QMBNCFG=\"autosel\",0"
# echo "#RESULT############################"
# $ADB -d shell /data/atcom "AT+QMBNCFG=\'autosel\',0"
# echo "###################################"
# echo ""
# sleep 5

# echo "2. AT+QMBNCFG="Select","Commercial-SKT""
# echo "#RESULT############################"
# $ADB -d shell /data/atcom "AT+QMBNCFG=\'Select\',\'Commercial-SKT\'"
# echo "###################################"
# echo ""
# sleep 5

# echo "3. AT+CFUN=1,1"
# echo "#RESULT############################"
# $ADB -d shell /data/atcom "AT+CFUN=1,1"
# echo "###################################"
# echo ""
# echo "wait 40 sec..."
# sleep 40

# echo "4. AT+CGDCONT=2"
# echo "#RESULT############################"
# $ADB -d shell /data/atcom "AT+CGDCONT=2"
# echo "###################################"
# echo ""
# sleep 1

# echo "5. AT+CGDCONT=3"
# echo "#RESULT############################"
# $ADB -d shell /data/atcom "AT+CGDCONT=3"
# echo "###################################"
# echo ""
# sleep 1


# echo "6. AT+CGDCONT=4"
# echo "#RESULT############################"
# $ADB -d shell /data/atcom "AT+CGDCONT=4"
# echo "###################################"
# echo ""
# sleep 1


# echo "7. AT+QIMSCFG=\"IMS\",2"
# echo "#RESULT############################"
# $ADB -d shell /data/atcom "AT+QIMSCFG=\'IMS\',2"
# echo "###################################"
# echo ""
# sleep 1

# echo "8. AT+QCFG=\"NWSCANMODE\",3"
# echo "#RESULT############################"
# $ADB -d shell /data/atcom "AT+QCFG=\'NWSCANMODE\',3"
# echo "###################################"
# echo ""
# sleep 1

# echo "9. AT+QCFG=\"band\",0,14,0,0"
# echo "#RESULT############################"
# $ADB -d shell /data/atcom "AT+QCFG=\'band\',0,14,0,0"
# echo "###################################"
# echo ""
# sleep 1

# echo "10. AT+QCFG=\"lte/bandprior\",5,3"
# echo "#RESULT############################"
# $ADB -d shell /data/atcom "AT+QCFG=\'lte/bandprior\',5,3"
# echo "###################################"
# echo ""
# sleep 1

# echo "10. AT+CGDCONT=1,\"IPV4V6\",\"lte-internet.sktelecom.com\""
# echo "#RESULT############################"
# $ADB -d shell /data/atcom "AT+CGDCONT=1,\'IPV4V6\',\'lte-internet.sktelecom.com\'"
# echo "###################################"
# echo ""
# sleep 1

# echo "11. AT+QPRTPARA=2"
# echo "#RESULT############################"
# $ADB -d shell /data/atcom "AT+QPRTPARA=2"
# echo "###################################"
# echo ""
# sleep 1

# echo "12. AT+CFUN=1,1"
# echo "#RESULT############################"
# $ADB -d shell /data/atcom "AT+CFUN=1,1"
# echo "###################################"
# echo ""
# echo "wait 30 sec..."
# sleep 30

# echo "13. AT+CGDCONT?"
# echo "#RESULT############################"
# $ADB -d shell /data/atcom "AT+CGDCONT?"
# echo "###################################"
# echo ""
# sleep 1



# echo "###################################"
# echo "                                   "
# echo "            OUTPUT                 "
# echo "                                   "
# echo "###################################"

# echo "1. AT+CGDCONT?"
# echo "#RESULT############################"
# $ADB -d shell /data/atcom "AT+CGDCONT?"
# echo "###################################"
# echo ""
# sleep 1

# echo "2. AT+QIMSCFG=\"IMS\""
# echo "#RESULT############################"
# $ADB -d shell /data/atcom "AT+QIMSCFG=\'IMS\'"
# echo "###################################"
# echo ""
# sleep 1

# echo "3. AT+QCFG=\"NWSCANMODE\""
# echo "#RESULT############################"
# $ADB -d shell /data/atcom "AT+QCFG=\'NWSCANMODE\'"
# echo "###################################"
# echo ""
# sleep 1
