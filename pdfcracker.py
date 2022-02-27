import pikepdf
from colorama import Fore, Style
from tqdm import tqdm


passwords = [ line.strip() for line in open("wordlist.txt")]
for password in tqdm(passwords, "Decripting PDF"):
    try:
        with pikepdf.open("output.pdf", password=password) as pdf:
            print(Fore.RED + "[+]) Password Successfully FOund:", password)
            break
    except pikepdf._qpdf.PasswordError as e:
         continue

