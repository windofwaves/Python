#!/usr/bin/python3
from socket import *
import argparse
from threading import *


def connScan(host, port):
    global sock
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((host, port))
        print("[+]{} /tcp Open".format(port))
    except:
        print("[-] {} /tcp Closed".format(port))
    finally:
        sock.close()


def portScan(host, ports):
    global tgtIP
    try:
        tgtIP = gethostbyname(host)  # gethostbyname function will fetch the ip address from particular ip address
    except:
        print("Unknown host %s " % host)
        try:
            tgtName = gethostbyaddr(tgtIP)
            print("[+] Scan Result For: " + tgtName[0])
        except:
            print("[+] Scan Result For: " + tgtIP)
            setdefaulttimeout(1)
            for port in ports:
                t = Thread(target=connScan, args=(host, int(port)))
                t.start()


def main():
    parser = argparse.ArgumentParser(prog='advancedportscanner.py', usage='%(prog)s -d sam.com -p 21,22',
                                     description='Scan a port given Hostname or IP')
    parser.add_argument('-d', '--host', help='Specify Target Domain')
    parser.add_argument('-p', '--port', help='Specify Target ports separated by comma')

    args = parser.parse_args()

    host = args.host
    ports = str(args.port).split(',')
    if (host == None) | (ports[0] == None):
        print(parser.usage)
        exit(0)
        portScan(host, ports)
        print(portScan)


main()
