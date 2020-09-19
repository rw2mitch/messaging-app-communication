from urllib.request import Request, urlopen
import os
import time

username = 'null'
prevMessage = ''

while not os.path.isfile('Files/stop.txt'):
   time.sleep(5)
   try:
      req = Request('http://boolinbase.com/Files/serverdata.txt')
      data = urlopen(req).read().decode('utf-8')
      if data is not prevMessage and not data.startswith(username):
         prevMessage = data
         localfile = open('Files/importdata.txt', "w+")
         localfile.write(data)
         localfile.close()
   except:
      continue