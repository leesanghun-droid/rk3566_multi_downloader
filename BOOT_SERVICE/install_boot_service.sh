#!/bin/bash

sudo chmod 755 boot.service
sudo cp boot.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable boot.service
sudo systemctl start boot.service
sudo systemctl status boot.service