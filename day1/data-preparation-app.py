import serial
import pandas as pd

ser=serial.Serial('COM9',115200,timeout=0.5)
data=[]
count=0

while True:
    if(ser.inWaiting()>0):
        k=ser.readline().decode('utf-8')
        k=k.split(',')
        hum=k[0].split(':')[1][1:]
        temp=k[1].split(':')[1][1:-2]
        #print(hum,temp)
        dummy=[]
        dummy.append(hum)
        dummy.append(temp)
        data.append(dummy)
        print(data)
        count+=1
        if(count==300):
            pd.DataFrame(data)
            data.to_csv('iot.csv')
            break
