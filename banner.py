#!/usr/bin/python3

import socket

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return


def main ():
    ip = input("enter target IP: ")
    for port in range (20,1000):
        banner = retBanner(ip,port)
        if banner:
            print("[+]" + ip + "/" + str(port) + ":" + str(banner))
main()

