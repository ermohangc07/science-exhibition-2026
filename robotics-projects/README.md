# Robotics Projects (Arduino)

Projects: Doorbell Melody, Buzz Wire Game, Walking Robot, Automatic Irrigation System, Automatic Water Dispenser, Smart Dustbin

Use the Arduino IDE (free): https://www.arduino.cc/en/software

**Note:** Arduino sketch (`.ino`) starter files will be added here once built.

## 1. Doorbell using Melody Generator
Components: Arduino, push button, piezo buzzer, resistor
Build order: button + LED test circuit → replace LED with buzzer → look up note-frequency table → sequence notes into a tune → add debounce so one press = one ring.

## 2. Buzz Wire Game
Components: bent wire maze, wand (metal ring), buzzer, LED, battery/Arduino
Build order: build the physical wire shape first → wire it as a switch to a digital input → code a contact/time counter for a scoreboard.

## 3. Walking Robot
Components: 2-4 servo motors, chassis, Arduino, battery pack
Build order: get ONE leg moving correctly → mirror/sequence for remaining legs → write movement as functions (`stepForward()`, `turnLeft()`).
*Highest-risk project for a 1-week timeline — have a simplified 2-servo wobble-walk as backup.*

## 4. Automatic Irrigation System
Components: soil moisture sensor, relay module, small water pump, Arduino, tubing
Build order: test moisture sensor readings (dry vs wet) → pick a threshold from real data → wire relay + pump → add status LED.

## 5. Automatic Water Dispenser
Components: ultrasonic/IR sensor, small pump or servo valve, Arduino
Build order: get distance readings reliable first → set detection range → trigger pump for a timed burst → add cooldown to prevent re-triggering.

## 6. Smart Dustbin
Components: ultrasonic sensor, servo motor (lid), Arduino
Build order: mount sensor and test placement → tune detection distance → use `myservo.write()` with delays to open/close the lid.
