# Robotics Projects (Arduino)

Six Arduino-based projects. Use the free Arduino IDE: https://www.arduino.cc/en/software

## Setup

1. Install the Arduino IDE and connect your Arduino board via USB.
2. In the IDE: Tools → Board → select your board (usually "Arduino Uno").
3. Tools → Port → select the port your Arduino is connected to.
4. Write or paste your code into the editor, then click Upload (→ arrow icon) to send it to the board.

---

## 1. Doorbell using Melody Generator (Class 8)

**Watch and follow along:**
📺 [DIY Arduino Doorbell | Easy Beginner Project with Buzzer](https://www.youtube.com/watch?v=prnDVqp9ZUg)

**Components:** Arduino, push button, piezo buzzer, resistor

**Build order:**
1. Wire a push button circuit and confirm it registers a press (test with an LED first if unsure)
2. Replace the LED with a buzzer
3. Look up a note-frequency table (e.g. for "Twinkle Twinkle" or any simple tune)
4. Use the `tone()` function to sequence notes into a melody
5. Add a short debounce delay so one press plays the tune once, not repeatedly

---

## 2. Buzz Wire Game (Class 8)

**Watch and follow along:**
📺 [Make a Buzz Wire Game with an Arduino](https://www.youtube.com/watch?v=ZfoFRF2ro80)

**Components:** bent wire "maze," wand (metal ring), buzzer, LED, Arduino

**Build order:**
1. Build the physical wire shape first — this is the craft/design challenge
2. Wire the wand and wire maze as a simple switch into a digital input pin
3. When they touch (circuit completes) → trigger the buzzer and LED
4. Add code to count contacts or track survival time, turning it into a scoreboard

---

## 3. Walking Robot (Class 8)

**Watch and follow along:**
📺 [How to make simple Arduino Walking Robot using Servo Motor](https://www.youtube.com/watch?v=KCTVP1tMOPA)

**Components:** 2–4 servo motors, cardboard/chassis, Arduino, battery pack

**Build order:**
1. Get ONE leg moving correctly with a single servo before building the rest
2. Mirror and sequence the remaining legs once one works reliably
3. Write movements as named functions (`stepForward()`, `turnLeft()`) instead of one long block of code

⚠️ This is the most mechanically demanding project — budget extra time, and consider a simplified 2-servo "wobble walk" as a backup if the full gait proves too time-consuming.

---

## 4. Automatic Irrigation System (Class 9)

**Watch and follow along:**
📺 [How to Make Automatic Irrigation System Using Soil Moisture Sensor and Arduino](https://www.youtube.com/watch?v=efTr8ZPPTZM)

**Components:** soil moisture sensor, relay module, small water pump, Arduino, tubing

**Build order:**
1. Test the moisture sensor first — record readings for dry soil vs. wet soil
2. Pick a threshold value based on your real readings (not a guessed number)
3. Wire the relay and pump so the pump activates when moisture drops below the threshold
4. Add a status LED (e.g. red = dry, green = watered)

---

## 5. Automatic Water Dispenser (Class 9)

**Watch and follow along:**
📺 [Arduino - Automatic Water Dispenser using Ultrasonic Sensor (HC-SR04)](https://www.youtube.com/watch?v=0-oUEYXvCQs)

**Components:** ultrasonic sensor, small pump or servo-actuated valve, Arduino

**Build order:**
1. Get distance sensor readings working reliably first
2. Set a detection range that isn't overly sensitive (test with a real hand/cup)
3. Trigger the pump for a fixed, timed burst when an object is detected
4. Add a short cooldown so it doesn't re-trigger immediately after dispensing

---

## 6. Smart Dustbin (Class 9)

**Watch and follow along:**
📺 [Smart Dustbin using Arduino Uno R3, Servo and Ultrasonic Sensor HC-SR04](https://www.youtube.com/watch?v=S3U_8gX3p_Q)

**Components:** ultrasonic sensor, servo motor (lid), Arduino

**Build order:**
1. Mount the sensor at the right height/angle and test placement
2. Tune the detection distance so it doesn't open randomly from background movement
3. Use `myservo.write()` with short delays to open the lid, pause, then close it

---

## Rules for every team

- **Test your sensor readings before wiring the full circuit.** Most bugs in these projects come from acting on an untested threshold or reading.
- **Build in stages** — get the simplest version working (one servo, one reading, one trigger) before adding the rest.
- Keep spare jumper wires and a charged battery on hand — something always comes loose right before a demo.
- Once your base project works, personalize it: a different tune for the doorbell, a decorated enclosure, a display showing live sensor readings. This is what makes a project stand out to judges.