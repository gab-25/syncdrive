#!/bin/bash

pip3 install requirements.txt

wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz
tar -xf geckodriver-v0.30.0-linux64.tar.gz
rm geckodriver-v0.30.0-linux64.tar.gz
mv geckodriver $HOME/.local/bin

ln -s $HOME/.local/bin/gsyncpy $PWD/main.py 
