#include <Stepper.h>

const int stepsPerRevolution = 200;  // Change this to fit the number of steps per revolution of your motor
const int motorSpeed = 20;           // Set the speed of the motor

const int stepPin = 2;
const int dirPin = 3;

Stepper myStepper(stepsPerRevolution, stepPin, 4);  // Initialize the stepper library

void setup() {
  // Initialize Serial communication
  Serial.begin(9600);

  // Set the speed of the motor
  myStepper.setSpeed(motorSpeed);

  // Set direction pin as output
  pinMode(dirPin, OUTPUT);
}

void loop() {
  // Move 200 steps clockwise
  digitalWrite(dirPin, HIGH);
  myStepper.step(200);
  delay(1000);  // Wait for a second

  // Move 200 steps counterclockwise
  digitalWrite(dirPin, LOW);
  myStepper.step(-200);
  delay(1000);  // Wait for a second

  digitalWrite(dirPin, HIGH);
  myStepper.step(-200);
  delay(1000);  // Wait for a second
}
