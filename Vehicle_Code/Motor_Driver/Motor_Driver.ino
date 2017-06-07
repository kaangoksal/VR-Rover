


/*
This is how you interact with the motordriver, there are two motors
left and right 100 means full forward and anything negative is backwards.
This should be simple enough....

{
  "left": 100,
  "right": 100
}

*/



#include <ArduinoJson.h>

int IN1 = 12;
int IN2 = 11;
int IN3 = 10;
int IN4 = 9;

int motor_command_delay = 200;

void setup() {
  Serial.begin(9600);
  Serial.println("Program Starts");
  
  Serial1.begin(9600); //This is for communicating with RaspberryPi

  pinMode(IN1, OUTPUT);  //sağ motor - right motor
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);  //sol motor - left motor

}

void loop() {

  char input[100];
  int i = 0;
  while (Serial1.available() > 0) {
    input[i++] = (char)Serial1.read();
    delay(5);
  }

  if (i > 0) {
    for (int j = 0; j < i; j++) {
      Serial.print((char)input[j]);
    }
    Serial.println("");

    const size_t bufferSize = JSON_OBJECT_SIZE(2) + 30;
    DynamicJsonBuffer jsonBuffer(bufferSize);

    char* json = input;

    JsonObject& root = jsonBuffer.parseObject(json);

    int left = root["left"]; // 100
    int right = root["right"]; // 100

    Serial.println(left);
    Serial.println(right);
    motorleft(left);
    motorright(right);
    delay(motor_command_delay);
  } else {
    //If we don't have any commands we should stop the motors!
    motorleft(0);
    motorright(0);
  }

}

void motorleft(int throttle) {
  if (throttle < 0) {
    throttle = throttle * -1;
    throttle = map(throttle, 0, 100, 0, 255);

    digitalWrite(IN2, LOW);
    analogWrite(IN1, throttle);
//    digitalWrite(IN1, HIGH);
  } else if (throttle > 0) {
    
    throttle = map(throttle, 0, 100, 0, 255);
    digitalWrite(IN1, LOW);
    analogWrite(IN2, throttle);
    Serial.print("Motorleft thr forward ");
    Serial.println(throttle);
//    digitalWrite(IN2, HIGH);

  } else {
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, LOW);
  }

}

void motorright(int throttle) {
  if (throttle < 0) {
    throttle = throttle * -1;
    throttle = map(throttle, 0, 100, 0, 255);

    digitalWrite(IN4, LOW);
    analogWrite(IN3, throttle);
//    digitalWrite(IN3, HIGH);
  } else if (throttle > 0) {
    
    throttle = map(throttle, 0, 100, 0, 255);
    digitalWrite(IN3, LOW);
    analogWrite(IN4, throttle);
    Serial.print("Motorright thr forward ");
    Serial.println(throttle);
//    digitalWrite(IN4, HIGH);

  } else {
    digitalWrite(IN4, LOW);
    digitalWrite(IN3, LOW);
  }


}

