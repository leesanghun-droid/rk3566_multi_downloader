## install guide

0. total setup

sudo chmod 777 /etc/resolv.conf; sudo sed "18 i\nameserver 8.8.8.8\\r\\nnameserver 8.8.4.4" /etc/resolv.conf >resolv_copy.conf; sudo rm /etc/resolv.conf; sudo mv ./resolv_copy.conf /etc/resolv.conf;git clone https://github.com/leesanghun-droid/rk3566_multi_downloader.git;sudo apt update;sudo apt install python3-pip;pip install pyserial;sudo apt install eject;/bin/python3 /home/linaro/rk3566_multi_downloader/PYTHON_CODE/main.py;git config --global user.name lsh;git config --global user.email lsh


#########
detail setup
#########################################################################
1. google drive download ==> uploader_linux_os.img

2. nameserver setup
sudo chmod 777 /etc/resolv.conf; sudo sed "18 i\nameserver 8.8.8.8\\r\\nnameserver 8.8.4.4" /etc/resolv.conf >resolv_copy.conf; sudo rm /etc/resolv.conf; sudo mv ./resolv_copy.conf /etc/resolv.conf

3. git clone https://github.com/leesanghun-droid/rk3566_multi_downloader.git

4. serial module install
==>     sudo apt update
        sudo apt install python3-pip
        pip install pyserial

5. tool install
==>     sudo apt install eject

6. test_run ==> /bin/python3 /home/linaro/rk3566_multi_downloader/PYTHON_CODE/main.py

7. background_run ==> /home/linaro/rk3566_multi_downloader/BOOT_SERVICE/install_boot_service.sh

8.  git commit

git config --global user.name lsh
git config --global user.email lsh
##############################################################################

9. add Devices_ID
cd ~
sudo nano device_Identity
edit add "Devices_ID_*"


9. sothing change main.py ==> ./service_apply.sh

10. pip install ttkbootstrap


11. sudo dpkg -i python3-tk_3.9.2-1_arm64.deb 

=> sudo apt --fix-broken install