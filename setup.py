#!/usr/bin/python3

import os
import sys
import pathlib


print("--------------------Installing dependencies------")

if sys.platform == "linux" or sys.platform == "linux2":

        if os.getuid == 0:
            os.system("sudo apt-get install python3 python3-pip python3-argcomplete xclip xsel git -y")
            os.system("sudo pip3 install requirements.txt")
            os.system("sudo pip3 install ifaddr netifaces linecache pathlib")
            os.system("cd ~")
            os.system("git clone https://github.com/Bashfuscator/Bashfuscator;cd Bashfuscator;python3 setup.py install --user;cd /bashfuscator/bin")
            print("completed")
            print("setting up PATH variable")
            path = pathlib.Path().parent.absolute()
            os.system("export PATH:$PATH:{} >> /etc/profile").format(path)

        elif os.getuid != 0:
            print("please run the setup as sudo user")
            exit()

