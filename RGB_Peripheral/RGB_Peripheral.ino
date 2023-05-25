#include <ArduinoBLE.h>

#define RED_PIN   22  
#define GREEN_PIN 23
#define BLUE_PIN  24
#define SHOCK_PIN 12

// Service and characteristic UUIDs
#define SERVICE_UUID        "13012F00-F8C3-4F4A-A8F4-15CD926DA146"
#define RED_UUID            "13012F01-F8C3-4F4A-A8F4-15CD926DA146"
#define GREEN_UUID          "13012F02-F8C3-4F4A-A8F4-15CD926DA146"
#define BLUE_UUID           "13012F03-F8C3-4F4A-A8F4-15CD926DA146"

BLEService nanoService(SERVICE_UUID);
BLEByteCharacteristic redLEDCharacteristic(RED_UUID, BLERead | BLEWriteWithoutResponse);
BLEByteCharacteristic greenLEDCharacteristic(GREEN_UUID, BLERead | BLEWriteWithoutResponse);
BLEByteCharacteristic blueLEDCharacteristic(BLUE_UUID, BLERead | BLEWriteWithoutResponse);

void setup() {
  Serial.begin(9600);

  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);

  digitalWrite(RED_PIN, HIGH);
  digitalWrite(GREEN_PIN, HIGH);
  digitalWrite(BLUE_PIN, HIGH);

  if (!BLE.begin()) {
    Serial.println("Failed to start BLE, Restart in one second.");
    while(1);
  }

  BLE.setLocalName("Arduino Nano 33 BLE Sense");
  BLE.setAdvertisedService(nanoService);

  nanoService.addCharacteristic(redLEDCharacteristic);
  nanoService.addCharacteristic(greenLEDCharacteristic);
  nanoService.addCharacteristic(blueLEDCharacteristic);

  BLE.addService(nanoService);

  redLEDCharacteristic.writeValue(0);
  greenLEDCharacteristic.writeValue(0);
  blueLEDCharacteristic.writeValue(0);

  BLE.advertise();
  Serial.println("Arduino Nano 33 BLE Sense LED Peripheral Service Started");
}

void loop() {
  BLEDevice central = BLE.central();

  if (central) {
    Serial.print("Connected to central: ");
    Serial.println(central.address());

    while (central.connected()) {
      if (redLEDCharacteristic.written()) {
        const bool value = redLEDCharacteristic.value();
        Serial.println(value ? "RED LED on" : "RED LED off");
        digitalWrite(RED_PIN, !value);
      } else if (greenLEDCharacteristic.written()) {
        const bool value = greenLEDCharacteristic.value();
        Serial.println(value ? "GREEN LED on" : "GREEN LED off");
        digitalWrite(GREEN_PIN, !value);
      } else if (blueLEDCharacteristic.written()) {
        const bool value = blueLEDCharacteristic.value();
        Serial.println(value ? "BLUE LED on" : "BLUE LED off");
        digitalWrite(BLUE_PIN, !value);
      }
    }

    Serial.println("Disconnected from central: ");
    Serial.println(central.address());

    digitalWrite(RED_PIN, HIGH);
    digitalWrite(GREEN_PIN, HIGH);
    digitalWrite(BLUE_PIN, HIGH);
  }
}
