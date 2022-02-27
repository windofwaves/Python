import urllib
from urllib.requst import urlopen

import hashlib

from termcolor import colored

sha1hash = input("[+] Enter sha1 hash value")

passlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8')

for password in passlist.split('\n'):
    hashguess = hashlist.sha1(bytes(password, 'utf-8')).hexdigest()
    if hashguess == sha1hash:
        print("[+] The password is :" + str(password))
        quit()
    else:
        print(colored("[-] password guess" + str(password) + "does not match try different wordlist..",'red'))
print("password not in passwordlist")


