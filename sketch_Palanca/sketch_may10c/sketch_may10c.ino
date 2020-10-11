int motor=3;
int i; 
void setup(){
  pinMode(motor, OUTPUT);
  Serial.begin(9600);
  analogWrite(motor,0);
}

void loop(){
  for (i=0; i <=100; i++){
    analogWrite(motor,i);
    Serial.println(i);
    delay(500);  
   }
   
  for (i=100; i >=0; i--){
    analogWrite(motor,i);
    Serial.println(i);
    delay(500);  
   }
}

