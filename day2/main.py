from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time

client=AWSIoTMQTTClient('trichy-client')
client.configureEndpoint('a366shaagepcsd-ats.iot.eu-west-1.amazonaws.com',8883)
client.configureCredentials("AmazonRootCA1.pem","device-private.pem.key","device-certificate.pem.crt")

client.configureOfflinePublishQueueing(-1) # Infinite Publishing
client.configureDrainingFrequency(2) # frequency of data transfer
client.configureConnectDisconnectTimeout(10)
client.configureMQTTOperationTimeout(5)

def notification(client,userdata,message):
    print(message.payload)
    print(message.topic)

client.connect()
print("Connected with AWS")

time.sleep(2)
client.subscribe("iot/madhu",1,notification)

while True:
    pass


