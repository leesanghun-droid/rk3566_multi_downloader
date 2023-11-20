## install guide

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

