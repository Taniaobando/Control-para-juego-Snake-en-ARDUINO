#include <Keyboard.h>
char serialData;
int pin = 10;
int pin1 = 9;
int pin2 = 13;
void setup() {
    pinMode(pin, OUTPUT);
    pinMode(pin1, OUTPUT);
    pinMode(pin2, OUTPUT);
    Serial.begin(9600);
}

//ciclo infinito
void loop() {
    if (Serial.available() > 0){
      
      serialData = Serial.read();
      Serial.print(serialData);
      
      if (serialData == '1'){
        
        digitalWrite(pin, HIGH);
        digitalWrite(pin1,HIGH);
        digitalWrite(pin2, HIGH);}
        
      else if (serialData == '0'){
        
        digitalWrite(pin, LOW);
        digitalWrite(pin1,LOW);
        digitalWrite(pin2,LOW);}
    }
}

