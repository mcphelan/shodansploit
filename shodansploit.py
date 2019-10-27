#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import os
import signal

# shodansploit v1.0.0

searchploit_txt = """
      _               _                       _       _ _
  ___| |__   ___   __| | __ _ _ __  ___ _ __ | | ___ (_) |_
 / __| '_ \ / _ \ / _` |/ _` | '_ \/ __| '_ \| |/ _ \| | __|
 \__ \ | | | (_) | (_| | (_| | | | \__ \ |_) | | (_) | | |_
 |___/_| |_|\___/ \__,_|\__,_|_| |_|___/ .__/|_|\___/|_|\__|
                                       |_|            v1.2.0
	Author : Ismail Tasdelen
	GitHub : github.com/ismailtasdelen
      Linkedin : linkedin.com/in/ismailtasdelen
       Twitter : twitter.com/ismailtsdln
"""

shodansploit_menu_txt = """
[1] GET > /shodan/host/{ip}
[2] GET > /shodan/host/count
[3] GET > /shodan/host/search
[4] GET > /shodan/host/search/tokens
[5] GET > /shodan/ports

[6] GET > /shodan/exploit/author
[7] GET > /shodan/exploit/cve
[8] GET > /shodan/exploit/msb
[9] GET > /shodan/exploit/bugtraq-id
[10] GET > /shodan/exploit/osvdb
[11] GET > /shodan/exploit/title
[12] GET > /shodan/exploit/description
[13] GET > /shodan/exploit/date
[14] GET > /shodan/exploit/code
[15] GET > /shodan/exploit/platform
[16] GET > /shodan/exploit/port

[17] GET > /dns/resolve
[18] GET > /dns/reverse
[19] GET > /labs/honeyscore/{ip}

[20] GET > /account/profile
[21] GET > /tools/myip
[22] GET > /tools/httpheaders
[23] GET > /api-info

[24] Exit
"""

if os.path.exists("./api.txt") and os.path.getsize("./api.txt") > 0:
    with open('api.txt', 'r') as file:
        shodan_api=file.readline().rstrip('\n')
else:
    file = open('api.txt', 'w')
    shodan_api = input('[*] Please enter a valid Shodan.io API Key: ')
    file.write(shodan_api)
    print('[~] File written: ./api.txt')
    file.close()

def signal_handler(signal, frame):
    print("\nExiting...\n")
    exit()

def shodan_host_ip():
	host_ip = input("Shodan Host Search : ")
	url = "https://api.shodan.io/shodan/host/"+ host_ip +"?key=" + shodan_api
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))

def shodan_count_search():
	host_search = input("Shodan Host Search : ")
	url = "https://api.shodan.io/shodan/host/count?key="+ shodan_api +"&query=" + host_search
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))

def host_search():
	host_search = input("Shodan Host Search : ")
	url = "https://api.shodan.io/shodan/host/search?key="+ shodan_api +"&query=" + host_search
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))

def shodan_token_search():
	token_search = input("Shodan Token Search : ")
	url = "https://api.shodan.io/shodan/host/search/tokens?key="+ shodan_api +"&query=" + token_search
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))

def shodan_ports():
	url = "https://api.shodan.io/shodan/ports?key=" + shodan_api
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))

def shodan_dns_lookup():
	hostnames = input("DNS Lookup : ")
	url = "https://api.shodan.io/dns/resolve?hostnames="+ hostnames +"&key=" + shodan_api
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))

def shodan_dns_reverse():
	ips = input("DNS Reverse : ")
	url = "https://api.shodan.io/dns/reverse?ips="+ ips +"&key=" + shodan_api
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))

def shodan_honeyscore():
	honeypot = input("Honeypot IP : ")
	url = "https://api.shodan.io/labs/honeyscore/"+ honeypot +"&key=" + shodan_api
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))

def shodan_profile():
	url = "https://api.shodan.io/account/profile?key=" + shodan_api
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))

def shodan_myip():
	url = "https://api.shodan.io/tools/myip?key=" + shodan_api
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))

def shodan_httpheaders():
	url = "https://api.shodan.io/tools/httpheaders?key=" + shodan_api
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))

def shodan_api_info():
	url = "https://api.shodan.io/api-info?key=" + shodan_api
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))

def shodan_exploit_author():
	exploit_author = input("Exploit Author : ")
	url = "https://exploits.shodan.io/api/search?query="+ "author:" + exploit_author +"&key=" + shodan_api
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))

def shodan_exploit_cve():
	exploit_cve = input("Exploit CVE : ")
	url = "https://exploits.shodan.io/api/search?query="+ "cve:" + exploit_cve +"&key=" + shodan_api
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))

def shodan_exploit_msb():
	exploit_msb = input("Exploit Microsoft Security Bulletin ID : ")
	url = "https://exploits.shodan.io/api/search?query="+ "msb:" + exploit_msb +"&key=" + shodan_api
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))

def shodan_exploit_bid():
	exploit_bid = input("Exploit Bugtraq ID : ")
	url = "https://exploits.shodan.io/api/search?query="+ "bid:" + exploit_bid +"&key=" + shodan_api
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))

def shodan_exploit_osvdb():
	exploit_osvdb = input("Exploit Open Source Vulnerability Database ID : ")
	url = "https://exploits.shodan.io/api/search?query="+ "osvdb:" + exploit_osvdb +"&key=" + shodan_api
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))

def shodan_exploit_title():
	exploit_title = input("Exploit Title : ")
	url = "https://exploits.shodan.io/api/search?query="+ "title:" + exploit_title +"&key=" + shodan_api
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))

def shodan_exploit_description():
	exploit_description = input("Exploit Description : ")
	url = "https://exploits.shodan.io/api/search?query="+ "description:" + exploit_description +"&key=" + shodan_api
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))

def shodan_exploit_date():
	exploit_date = input("Exploit Date : ")
	url = "https://exploits.shodan.io/api/search?query="+ "description:" + exploit_date +"&key=" + shodan_api
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))

def shodan_exploit_code():
	exploit_code = input("Exploit Code : ")
	url = "https://exploits.shodan.io/api/search?query="+ "code:" + exploit_code +"&key=" + shodan_api
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))

def shodan_exploit_platform():
	exploit_platform = input("Exploit Platform : ")
	url = "https://exploits.shodan.io/api/search?query="+ "platform:" + exploit_platform +"&key=" + shodan_api
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))

def shodan_exploit_port():
	exploit_platform = input("Exploit Port : ")
	url = "https://exploits.shodan.io/api/search?query="+ "port:" + exploit_platform +"&key=" + shodan_api
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))

def shodansploit_exit():
	exit()

def pause():
    input("\nPress the <ENTER> key to continue...")

# Author : Ismail Tasdelen
# GitHub : https://github.com/ismailtasdelen/
# Linkedin : https://www.linkedin.com/in/ismailtasdelen/
# Twitter : https://twitter.com/ismailtsdln/

# multi function use
def run():

	choice = int(input("Which option number : "))

	if choice == 1:
		shodan_host_ip()

	elif choice == 2:
		shodan_count_search()

	elif choice == 3:
		host_search()

	elif choice == 4:
		shodan_token_search()

	elif choice == 5:
		shodan_ports()

	elif choice == 6:
		shodan_exploit_author()

	elif choice == 7:
		shodan_exploit_cve()

	elif choice == 8:
		shodan_exploit_msb()

	elif choice == 9:
		shodan_exploit_bid()

	elif choice == 10:
		shodan_exploit_osvdb()

	elif choice == 11:
		shodan_exploit_title()

	elif choice == 12:
		shodan_exploit_description()

	elif choice == 13:
		shodan_exploit_date()

	elif choice == 14:
		shodan_exploit_code()

	elif choice == 15:
		shodan_exploit_platform()

	elif choice == 16:
		shodan_exploit_port()

	elif choice == 17:
		shodan_dns_lookup()

	elif choice == 18:
		shodan_dns_reverse()

	elif choice == 19:
		shodan_honeyscore()

	elif choice == 20:
		shodan_profile()

	elif choice == 21:
		shodan_myip()

	elif choice == 22:
		shodan_httpheaders()

	elif choice == 23:
		shodan_api_info()

	elif choice == 24:
		shodansploit_exit()

signal.signal(signal.SIGINT, signal_handler)
while 1:
    print (searchploit_txt)
    print (shodansploit_menu_txt)
    try:        
        run()

        pause()

    except ValueError as e:
        print('\n[✘] Error: %s' % e)
        option = input('[*] Would you like to change API Key? <Y/n>: ').lower()
        if option.startswith('y'):
            file = open('api.txt', 'w')
            shodan_api = input('[*] Please enter valid Shodan.io API Key: ')
            file.write(shodan_api)
            print('[~] File written: ./api.txt')
            file.close()
            print('[~] Restarting...')
            print('')
        else:
            print('')
            print('[•] Exiting...')
            exit()
