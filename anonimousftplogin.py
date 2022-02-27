#!/usr/bin/python3
import ftplib
from colorama import Fore,Style
import pyfiglet
import sys

banner = pyfiglet.figlet_format("Anonymous FTP Login")
print (banner)

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymoys', 'anonymous')
        print(Fore.RED + "[+] hostname + "FTP anonymous Succeeded")
        ftp.quit()
        return True
    except:
        print("[!]" + hostname + "FTP anonymous Login Failed")
if len(sys.argv) < 2:
    print("Not enough atguments \n Usage: anonftp.py hostname\n")
    exit ()
else:
     host = sys.argv[1]
     anonLogin(host)
     

