#!/usr/bin/python3
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = input ("Enter IP Address: ")
port = int (input ("Enter the port Number: ")) 


def portScan(port):
    result = sock.connect_ex((host,port))
    if result == 0:
         print("Port is open")
    else:
         print("port is closed")
portScan (port) 


