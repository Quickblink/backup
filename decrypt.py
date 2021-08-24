import subprocess
import time
import os
from shutil import copyfile


secret_file = '/home/eric/Desktop/secrets.txt'
sec1 = 0
sec2 = 1
plainfile = "/home/eric/.gnupg/secretkeys.zip"
plainfolder = "/home/eric/.gnupg/secretkeys"


subprocess.Popen(['openssl', 'enc', '-nosalt', '-aes-256-ecb', '-pbkdf2', '-out', plainfile, '-in', f'privatekey/c{sec1}{sec2}', '-kfile', secret_file, '-d'])

time.sleep(0.5)
os.remove(secret_file)
subprocess.Popen(['unzip', plainfile, '-d', plainfolder])

time.sleep(0.5)
os.remove(plainfile)
secretkeys = []

for entry in os.scandir(f'{plainfolder}/private-keys-v1.d'):
    secretkeys.append(entry.name)
    copyfile(f'{plainfolder}/private-keys-v1.d/{entry.name}', f'/home/eric/.gnupg/private-keys-v1.d/{entry.name}')

time.sleep(0.5)

subprocess.Popen(['rm', '-r', plainfolder])
for entry in os.scandir('encrypted'):
    file = entry.name
    subprocess.Popen(['gpg', '--output', f'raw/{file}', '--decrypt', f'encrypted/{file}'])

time.sleep(0.5)

for key in secretkeys:
    os.remove(f'/home/eric/.gnupg/private-keys-v1.d/{key}')
