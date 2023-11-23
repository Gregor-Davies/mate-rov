const int ledPin = LED_BUILTIN; // LED pin on most Arduino boards
int M1A = 10;
int M1B = 12;
int PWM_PERIOD = 36000;
int motor_duty_cycle[1] = {0};

void setup() {
  Serial.begin(9600); // Initialize serial communication
  pinMode(ledPin, OUTPUT); // Set the LED pin as an output
}

void loop() {
  if (Serial.available() > 0) { // Check if data is available to read
    String serialData = Serial.readStringUntil('\n'); // Read the incoming byte
    sscanf(serialData.c_str(), "%d\n", &motor_duty_cycle[0]);
/*
    if (receivedChar == "001") {
      digitalWrite(ledPin, HIGH);
      digitalWrite(10, HIGH); // Turn on the LED
    } else if (receivedChar == "000") {
      digitalWrite(10, LOW);
      digitalWrite(ledPin, LOW); // Turn off the LED
    }
*/
    int eTime = 0;
    for(int x = 0; x < 6; x++) {
      // Check if this motor is being driver
      if(motor_duty_cycle[0] == 0) continue;
      
      // Get the pin
      int pin_idx = (x << 1) | (motor_duty_cycle[0] < 0);
  
      // Calculate mark and space times
      int mark_time = motor_duty_cycle[0] * PWM_PERIOD / 1000;
      eTime += mark_time;
  
      digitalWrite(M1A, HIGH);
      delayMicroseconds(mark_time);
      digitalWrite(M1A, LOW);
    }
  
    // Pad time to period if required
    if(eTime < PWM_PERIOD) {
      delayMicroseconds(PWM_PERIOD - eTime);
    }
  }
}