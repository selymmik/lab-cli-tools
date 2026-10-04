from zipfile import ZipFile, BadZipFile
import zlib      

passwords = []
with open("Ashley-Madison.txt") as f:
    for i in f:
        passwords.append(i.strip())

with ZipFile("whitehouse_secrets.zip") as zf:
    for i, password in enumerate(passwords):
        try:
            zf.extractall(pwd=password.encode())
            print("Found it:", password)
            break
        except (RuntimeError, BadZipFile, zlib.error):
            continue 