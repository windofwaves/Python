import hashlib
from termcolor import colored


string = input("[+] Enter a string to Convert into hash: ")

hash1 = hashlib.md5()
hash1.update(string.encode())
print(colored("MD5: " + hash1.hexdigest() + "\n",'red'))


hash2 = hashlib.sha1()
hash2.update(string.encode())

print(colored("SHA1: " + hash2.hexdigest() + "\n",'blue'))

hash3 = hashlib.sha224()
hash3.update(string.encode())
print(colored("SHA224: " + hash3.hexdigest() + "\n",'cyan'))


hash4 = hashlib.sha256()
hash4.update(string.encode())
print(colored("SHA256: " + hash4.hexdigest() + "\n",'green'))

hash5 = hashlib.sha512()
hash5.update(string.encode())
print(colored("SHA512: " + hash5.hexdigest() + "\n",'yellow'))




