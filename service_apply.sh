#!/bin/bash
cd /home/linaro/rk3566_multi_downloader/BOOT_SERVICE
sudo systemctl stop boot.service
sudo systemctl daemon-reload
sudo systemctl enable boot.service
sudo systemctl start boot.service
sudo systemctl status boot.service