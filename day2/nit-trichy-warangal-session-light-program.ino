// Node - Program

#define light 5
#define on 0
#define off 1

void setup() {
  pinMode(light,OUTPUT);
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available()>0) {
    String s=Serial.readString();
    if(s=="on") {
      lightOn();
    } else if(s=="off") {
      lightOff();
    }
  }
}

void lightOn() {
  Serial.println("Device: ON");
  digitalWrite(light,on);  
}

void lightOff() {
  Serial.println("Device: OFF");
  digitalWrite(light,off);
}
