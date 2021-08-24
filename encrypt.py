import subprocess
import os
import time

for entry in os.scandir('raw'):
    file = entry.name
    subprocess.Popen(['gpg', '--recipient', 'backup', '--output', f'encrypted/{file}', '--encrypt', f'raw/{file}'])

time.sleep(1)

for entry in os.scandir('raw'):
    os.remove(entry.path)