
// 3- Pins, Vcc - 5V, GND - GND, Data - Pin 2

// Collect data from Sensor

#include "DHT.h"

DHT dht(2,DHT11);


void setup() {
  Serial.begin(115200);
  dht.begin();
}

void loop() {
  float h=dht.readHumidity();
  float t=dht.readTemperature();

  if (isnan(h) || isnan(t))
    return;

  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.print(",Temp: ");
  Serial.println(t);
  delay(4000); // 4-seconds
}
