# Collecting Request from Thingspeak IoT Cloud

import urllib.request as url
import time
import serial as node

data=node.Serial('COM9',115200,timeout=0.5)


cloudAPI='https://api.thingspeak.com/channels/1673824/feeds.json?api_key=WLM7I25TB0631SUA&results=1'

while True:
  response=url.urlopen(cloudAPI).read().decode('utf-8')
  response=int(response.split(':')[-1][1:-4])
  #print(response)
  if(response==0):
      print('Device: OFF')
      data.write('off'.encode('utf-8'))
  elif(response==10):
      print('Device: ON')
      data.write('on'.encode('utf-8'))
  time.sleep(4)
