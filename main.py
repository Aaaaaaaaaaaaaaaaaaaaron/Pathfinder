# Created by https://RandomNerdTutorials.com/micropython-esp32-esp8266-dc-motor-l298n/
# This file includes classes to control two DC motors
import machine
import time
from machine import Pin, PWM  # Import Pin and PWM classes

class DCMotor_left:
    # the min_duty and max_duty are defined for 15000Hz frequency
    # you can pass as arguments
    def __init__(self, pin1, pin2, enable_pin, min_duty=750, max_duty=1023):
        self.pin1 = pin1
        self.pin2 = pin2
        self.enable_pin = enable_pin
        self.min_duty = min_duty
        self.max_duty = max_duty
  
    # speed value can be between 0 and 100
    def forward(self, speed):
        self.speed = speed
        self.enable_pin.duty(self.duty_cycle(self.speed))
        self.pin1.value(1)
        self.pin2.value(0)

    def backwards(self, speed):
        self.speed = speed
        self.enable_pin.duty(self.duty_cycle(self.speed))
        self.pin1.value(0)
        self.pin2.value(1)

    def stop(self):
        self.enable_pin.duty(0)
        self.pin1.value(0)
        self.pin2.value(0)
        
    def duty_cycle(self, speed):
        if self.speed <= 0 or self.speed > 100:
            duty_cycle = 0
        else:
            duty_cycle = int(self.min_duty + (self.max_duty - self.min_duty) * ((self.speed - 1) / (100 - 1)))
        return duty_cycle

class DCMotor_right:
    # the min_duty and max_duty are defined for 15000Hz frequency
    # you can pass as arguments
    def __init__(self, pin1, pin2, enable_pin, min_duty=750, max_duty=1023):
        self.pin1 = pin1
        self.pin2 = pin2
        self.enable_pin = enable_pin
        self.min_duty = min_duty
        self.max_duty = max_duty
  
    # speed value can be between 0 and 100
    def forward(self, speed):
        self.speed = speed
        self.enable_pin.duty(self.duty_cycle(self.speed))
        self.pin1.value(1)
        self.pin2.value(0)

    def backwards(self, speed):
        self.speed = speed
        self.enable_pin.duty(self.duty_cycle(self.speed))
        self.pin1.value(0)
        self.pin2.value(1)

    def stop(self):
        self.enable_pin.duty(0)
        self.pin1.value(0)
        self.pin2.value(0)
        
    def duty_cycle(self, speed):
        if self.speed <= 0 or self.speed > 100:
            duty_cycle = 0
        else:
            duty_cycle = int(self.min_duty + (self.max_duty - self.min_duty) * ((self.speed - 1) / (100 - 1)))
        return duty_cycle

frequency = 15000

# Motor 1 (left)
pin1_left = Pin(12, Pin.OUT)
pin2_left = Pin(14, Pin.OUT)
enable_left = PWM(Pin(13), frequency)
dc_motor_left = DCMotor_left(pin1_left, pin2_left, enable_left)

# Motor 2 (right)
pin1_right = Pin(25, Pin.OUT)
pin2_right = Pin(26, Pin.OUT)
enable_right = PWM(Pin(33), frequency)
dc_motor_right = DCMotor_right(pin1_right, pin2_right, enable_right)

button = Pin(27, Pin.IN, Pin.PULL_UP)  # Taster an Pin 27, mit Pull-up-Widerstand

count = 0
while count < 50:
    if button.value() == 0:  # Prüfen, ob der Taster gedrückt ist
        # Beide Motoren steuern
        dc_motor_left.forward(50)
        dc_motor_right.forward(50)
        time.sleep(2)
        
        dc_motor_left.stop()
        dc_motor_right.stop()
        time.sleep(3)
        
        dc_motor_left.backwards(100)
        dc_motor_right.backwards(100)
        time.sleep(2)
        
        dc_motor_left.forward(5)
        dc_motor_right.forward(5)
        time.sleep(5)
        
        dc_motor_left.stop()
        dc_motor_right.stop()
        time.sleep(3)

        count += 1
    else:
        dc_motor_left.stop()  # Motor 1 stoppen, wenn der Taster nicht gedrückt ist
        dc_motor_right.stop()  # Motor 2 stoppen, wenn der Taster nicht gedrückt ist

dc_motor_left.stop()
dc_motor_right.stop()
