#!/bin/bash

wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz
tar -xf geckodriver-v0.30.0-linux64.tar.gz
rm geckodriver-v0.30.0-linux64.tar.gz
mv geckodriver $HOME/.local/bin

pip3 install requirements.txt

ln -s $HOME/.local/bin/gsyncpy $PWD/main.py 

echo "GSYNCPY installation completed!"
