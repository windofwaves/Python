#!/usr/bin/python3
from socket import*
import pyfiglet
import sys

banner = pyfiglet.figlet_format("PORT SCANNER") 
print(banner)
if len(sys.argv) == 2:
    targetIP = gethostbyname(sys.argv[1]) #python3 nameofscript1  and then the ip address2 -> two arguments 1 is the script 2 is the ip address
    print (targetIP)
else:
    print("Invalid argument")
try:
    for i in range(20,1025):
        s = socket(AF_INET,SOCK_STREAM)
        result = s.connect_ex((targetIP,i))
        if (result == 0):
            print('Port {}: Open'.format(i))
            s.close()
except KeyboardInterrupt:
    print ("\n Exitting Program")
    sys.exit()
except socket.gaierror:
    print("\n Hostname could not be resolved")
    sys.exit()
except socket.error:
    print("\n Server not Responding")
    sys.exit()

