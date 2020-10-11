/*
Sketch para prender un LED
*/

#include <Keyboard.h>
char serialData;
int pin = 10;

void setup() {
    pinMode(pin, OUTPUT);
    Serial.begin(9600);
}

//ciclo infinito
void loop() {
    if (Serial.available() > 0){
      
      serialData = Serial.read();
      Serial.print(serialData);
      
      if (serialData == '1'){
        
        digitalWrite(pin, HIGH);}
        
      else if (serialData == '0'){
        
        digitalWrite(pin, LOW);}
    }
}

