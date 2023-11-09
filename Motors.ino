/* Motor Definitions */
// need to rename the variables from cumtime
#define MTR_1A  8
#define MTR_1B  9
#define MTR_2A  6
#define MTR_2B  7
#define MTR_3A  4
#define MTR_3B  5
#define MTR_4A  3
#define MTR_4B  2
#define MTR_5A  10
#define MTR_5B  11
#define MTR_6A  13
#define MTR_6B  12

#define PWM_PERIOD 1000
int motor_duty_cycle[6] = {0};

const int motor_pins[] = {
  MTR_1A, MTR_1B,
  MTR_2A, MTR_2B,
  MTR_3A, MTR_3B,
  MTR_4A, MTR_4B,
  MTR_5A, MTR_5B,
  MTR_6A, MTR_6B
};

void setup() {
  // Set motor pins to output
  for(int x = 0; x < sizeof(motor_pins) / sizeof(int); x++) {
    pinMode(motor_pins[x], OUTPUT);
  }

  // Setup serial
  Serial.begin(9600);
}

void loop() {
  // Check if we have new motor speeds
  if (Serial.available() > 0) {
    String serialData = Serial.readStringUntil('\n');
    sscanf(serialData.c_str(), "%d %d %d %d %d %d\n",
      &motor_duty_cycle[0], &motor_duty_cycle[1],
      &motor_duty_cycle[2], &motor_duty_cycle[3],
      &motor_duty_cycle[4], &motor_duty_cycle[5]);
  }

  // Drive the motors
  int cumTime = 0;
  for(int x = 0; x < 6; x++) {
    // Check if this motor is being driver
    if(motor_duty_cycle[x] == 0) continue;
    
    // Get the pin
    int pin_idx = (x << 1) | (motor_duty_cycle[x] < 0);

    // Calculate mark and space times
    int mark_time = motor_duty_cycle[x] * PWM_PERIOD / 100;
    cumTime += mark_time;

    digitalWrite(motor_pins[pin_idx], HIGH);
    delayMicroseconds(mark_time);
    digitalWrite(motor_pins[pin_idx], LOW);
  }

  // Pad time to period if required
  if(cumTime < PWM_PERIOD) {
    delayMicroseconds(PWM_PERIOD - cumTime);
  }
}