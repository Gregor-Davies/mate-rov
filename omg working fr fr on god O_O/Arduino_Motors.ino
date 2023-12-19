int M1A = 10;
int M1B = 12;
int motorValue = 0;

void setup() {
  Serial.begin(9600);
  pinMode(M1A, OUTPUT);
  pinMode(M1B, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) { // Check if data is available to read
    String serialData = Serial.readStringUntil('\n'); // Read the incoming byte
    motorValue = serialData.toInt(); // Convert the received string to an integer

    if (motorValue == 100) {
      digitalWrite(M1A, HIGH);
      digitalWrite(M1B, LOW);
    } else if (motorValue == -100) {
      digitalWrite(M1A, LOW);
      digitalWrite(M1B, HIGH);
    } else if (motorValue == 0) {
      digitalWrite(M1A, LOW);
      digitalWrite(M1B, LOW);
    }
  }
}
