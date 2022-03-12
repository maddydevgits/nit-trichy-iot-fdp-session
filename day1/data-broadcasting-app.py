from turtle import pu
import serial
import paho.mqtt.client as mqtt

pub_client= mqtt.Client()
pub_client.connect('broker.hivemq.com',1883)

ser=serial.Serial('COM9',115200,timeout=0.5)

while True:
    if(ser.inWaiting()>0):
        k=ser.readline().decode('utf-8')
        print(k)
        pub_client.publish('iot/nit',k)
        print('Data Broadcasted')
