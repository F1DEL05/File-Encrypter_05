from cryptography.fernet import Fernet
import os
files=[]
for i in os.listdir():
    if i!="encrypter.py" and i!="decrypter.py" and i!="key.key" and os.path.isfile(i):
        files.append(i)
with open("key.key","br") as key:
    gen_key=key.read()
    key.close()
for j in files:
    with open(j,"br") as file1:
        enc_text=file1.read()
        dec_text=Fernet(gen_key).decrypt(enc_text)
        file1.close()
    with open(j,"bw") as file2:
        file2.write(dec_text)
        file2.close()