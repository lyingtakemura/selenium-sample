#!/bin/bash

python3 -m venv venv
source venv/bin/activate

pip install flake8 selenium

sudo apt install chromium-driver -y

echo '-'
echo 'init.sh exec'
echo '-'
