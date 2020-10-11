#include <Keyboard.h>


void setup() {
    Keyboard.begin();
    pinMode(2, INPUT_PULLUP); //Joystick izq
    pinMode(3, INPUT_PULLUP); //Joystick der
    pinMode(4, INPUT_PULLUP); //Joystick arriba
    pinMode(5, INPUT_PULLUP); //Joystick abajo
    pinMode(6, INPUT_PULLUP); //Boton menu
    pinMode(7, INPUT_PULLUP); //Boton pausa/play
    pinMode(8, INPUT_PULLUP); //Boton seleccionar
    Keyboard.end();

    
}

void loop() {
int b2= digitalRead(2);
int b3= digitalRead(3);
int b4= digitalRead(4);
int b5= digitalRead(5);
int b6= digitalRead(6);
int b7= digitalRead(7);
int b8= digitalRead(8);

if (b2 == HIGH){
  Keyboard.press(216);
}
else{
  Keyboard.release(216);
}

if (b3 == HIGH){
  Keyboard.press(215);
}
else{
  Keyboard.release(215);
}
if (b4 == HIGH) {
  Keyboard.press(218);
}
else {
  Keyboard.release(218);
}
if (b5 == HIGH){
  Keyboard.press(217);
}
else{
  Keyboard.release (217);
}
}
