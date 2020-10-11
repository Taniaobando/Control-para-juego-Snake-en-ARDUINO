#include <Keyboard.h>
char serialData;
int pin = 10;
int pin1 = 9;
int pin2 = 11;
int motor = 6;
int i;
void setup() {
    Keyboard.begin();
    pinMode(2, INPUT_PULLUP); //Joystick izq
    pinMode(3, INPUT_PULLUP); //Joystick der
    pinMode(4, INPUT_PULLUP); //Joystick arriba
    pinMode(5, INPUT_PULLUP); //Joystick abajo
    pinMode(12, INPUT_PULLUP); //Boton menu
    pinMode(7, INPUT_PULLUP); //Boton pausa/play
    pinMode(8, INPUT_PULLUP); //Boton seleccionar
    Keyboard.end();
    pinMode(pin, OUTPUT);
    pinMode (motor, OUTPUT);
    pinMode(pin1, OUTPUT);
    pinMode(pin2, OUTPUT);
    Serial.begin(9600);
    analogWrite(motor,0);

    
}

void loop() {
int b2= digitalRead(2);
int b3= digitalRead(3);
int b4= digitalRead(4);
int b5= digitalRead(5);
int b12= digitalRead(12);
int b7= digitalRead(7);
int b8= digitalRead(8);
if (Serial.available () > 0){
  serialData = Serial.read();
  Serial.print(serialData);
  if (serialData == '2'){
    for (i=0; i <=255; i+=85){
      analogWrite (motor, i);
      Serial.println(i);
      delay (3000);
   }
    for (i=255; i >=0; i-=85){
      analogWrite (motor, i);
      Serial.println(i);
      delay (3000);
    }
    serialData = '5';  
  }
   if (serialData == '1'){
        
        digitalWrite(pin, HIGH);
        digitalWrite(pin1,HIGH);
        digitalWrite(pin2, HIGH);}
        
   else if (serialData == '0'){
        
        digitalWrite(pin, LOW);
        digitalWrite(pin1,LOW);
        digitalWrite(pin2,LOW);}
}


if (b2 == LOW){
  Keyboard.press(216);
  delay (280);
}
else{
  Keyboard.release(216);
}

if (b3 == LOW){
  Keyboard.press(215);
  delay (280);
}
else{
  Keyboard.release(215);
}
if (b4 == LOW) {
  Keyboard.press(218);
  delay (280);
}
else {
  Keyboard.release(218);
}
if (b5 == LOW){
  Keyboard.press(217);
  delay (280);
}
else{
  Keyboard.release (217);
}


if (b12 == LOW){
  Keyboard.press(177);
  delay (280);
}
else{
  Keyboard.release (177);
}

if (b7 == LOW){
  Keyboard.write(112);
  delay (280);
}
else{
  Keyboard.release (112);
}

if (b8 == LOW){
  Keyboard.press(32);
  delay (280);
}
else{
  Keyboard.release (32);
}
}





