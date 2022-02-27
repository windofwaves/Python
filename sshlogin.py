#!/usr/bin/python3

import paramico 
import pyfiglet #to make a fancy banner

banner = pyfiglet.finglet_format("SSH LOGIN")

host = input("Enter the IP Address: ")
port = 22
username = "raziel"
password = "4efi44aA"
command = "ls -l"


ssh = paramico.SSHClient()
ssh.set_missing_host_key_policy(paramico.AutoAddPolicy())
ssh.connect(host,port,username,password)
stdin,stdout,stderr = ssh.exec_command((command))
lines = stdout.readlines()
print(lines)


