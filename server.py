#!/usr/bin/python3
import socket   #thats a library

s = socket.socket()   #variable
print ("Socket successfully Created")

port = 1234

s.bind(('',port))   # this makes the server listening for requests comming from other pc from a network

print("socket binded to %s"  %(port))   


s.listen(5)
print("socket is listening")

while True :
    c,addr = s.accept()
    print ("Got connection from", addr)
    c.send(b"Thank you for Connecting")
    c.close()
    
