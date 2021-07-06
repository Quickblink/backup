import subprocess
import time


ab = []

#subprocess.Popen(['openssl', 'genrsa', '-out', '/tmp/pwgen/private.pem'])
#time.sleep(0.1)
#subprocess.Popen(['openssl', 'rsa', '-in', '/tmp/pwgen/private.pem', '-outform', 'PEM', '-pubout', '-out', 'public.pem'])
plainfile = "/home/eric/.gnupg/private-keys-v1.d.zip"

for i in range(4):
    with open(f'/tmp/pwgen/file.txt', 'w') as f:
        subprocess.Popen(['openssl', 'rand', '-hex', '16'], stdout=f)
    time.sleep(0.1)
    with open(f'/tmp/pwgen/file.txt', 'r') as f:
        ab.append(f.read())


for i in range(4):
    for k in range(4):
        if i < k:
            with open(f'/tmp/pwgen/file.txt', 'w') as f:
                f.write((ab[i]+ab[k]).replace('\n', ''))
            subprocess.Popen(['openssl', 'enc', '-nosalt', '-aes-256-ecb', '-pbkdf2', '-in', plainfile, '-out', f'c{i}{k}', '-kfile', '/tmp/pwgen/file.txt'])
            #time.sleep(0.1)
            #subprocess.Popen(['openssl', 'enc', '-nosalt', '-aes-256-ecb', '-pbkdf2', '-out', f'/tmp/pwgen/or{i}{k}.txt', '-in', f'c{i}{k}.txt', '-kfile', '/tmp/pwgen/file.txt', '-d'])
            time.sleep(0.1)

last = ""
for i, sec in enumerate(ab):
    last += f'Secret {i}:\n'+sec[:16]+'\n'+sec[16:]

with open(f'/tmp/pwgen/file.txt', 'w') as f:
    f.write(last)


