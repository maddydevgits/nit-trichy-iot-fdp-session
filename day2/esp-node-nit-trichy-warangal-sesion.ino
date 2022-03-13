// to push data to thingspeak iot cloud
#include <WiFi.h>
#include <ThingSpeak.h>

#define sensor 23
#define bright 0
#define dark 1

#define ssid "The WiFi"
#define password "madhus2022"

#define writeKey "4FZUGB58FGZKL8B3"
#define channelId 1673824

WiFiClient client;

void setup() {
 pinMode(sensor,INPUT);
 Serial.begin(115200);
 connect_wifi_router();
 ThingSpeak.begin(client);
}

void loop() {
  int m=digitalRead(sensor);
  Serial.print("Sensor Value: ");
  Serial.println(m);
  if(m==bright) {
    ThingSpeak.setField(1,0); // light - off
    ThingSpeak.writeFields(channelId,writeKey);
    Serial.println("No light Needed");
  } else if(m==dark) {
    ThingSpeak.setField(1,10); 
    ThingSpeak.writeFields(channelId,writeKey);
    Serial.println("Light Needed");
  }
  delay(20000);
}

void connect_wifi_router() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid,password);
  while(WiFi.status()!=WL_CONNECTED) {
    Serial.print(".");
    delay(50);
  }
  Serial.println("Node connected to Network");
}
