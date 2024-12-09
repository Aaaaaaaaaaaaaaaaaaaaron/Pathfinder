import network
import esp
import espnow
import machine
import time
from machine import Pin, PWM

# Motor 1 (left) setup
class DCMotor:
    def __init__(self, pin1, pin2, enable_pin, min_duty=750, max_duty=1023):
        self.pin1 = pin1
        self.pin2 = pin2
        self.enable_pin = enable_pin
        self.min_duty = min_duty
        self.max_duty = max_duty

    def forward(self, speed):
        self.enable_pin.duty(self.duty_cycle(speed))
        self.pin1.value(1)
        self.pin2.value(0)

    def backward(self, speed):
        self.enable_pin.duty(self.duty_cycle(speed))
        self.pin1.value(0)
        self.pin2.value(1)

    def stop(self):
        self.enable_pin.duty(0)
        self.pin1.value(0)
        self.pin2.value(0)

    def duty_cycle(self, speed):
        if speed <= 0 or speed > 100:
            return 0
        return int(self.min_duty + (self.max_duty - self.min_duty) * (speed / 100))

# Initialize motors
frequency = 15000

# Motor 1 (left)
pin1_left = Pin(12, Pin.OUT)
pin2_left = Pin(14, Pin.OUT)
enable_left = PWM(Pin(13), frequency)
motor_left = DCMotor(pin1_left, pin2_left, enable_left)

# Motor 2 (right)
pin1_right = Pin(25, Pin.OUT)
pin2_right = Pin(26, Pin.OUT)
enable_right = PWM(Pin(33), frequency)
motor_right = DCMotor(pin1_right, pin2_right, enable_right)

# Initialize Wi-Fi in station mode
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.disconnect()

# Initialize ESP-NOW
e = espnow.ESPNow()
e.active(True)

# Add peer controller: 1c:69:20:cd:57:e4
peer = b'\x1c\x69\x20\xcd\x57\xe4'
e.add_peer(peer)

# Threshold values for joystick neutral position (adjustable)
NEUTRAL_LOW = 1700
NEUTRAL_HIGH = 1900

# Define the callback for receiving data
def on_receive_callback(e):
    sender_mac, msg = e.irecv()
    if msg:  # Check if message is not None
        try:
            # Decode and parse the received message
            x1, x2 = map(int, msg.decode('utf-8').split(','))
            print(f"Received x1: {x1}, x2: {x2}")

            # Control motor 1 (left) based on x1
            if x1 < NEUTRAL_LOW:
                speed = int((NEUTRAL_LOW - x1) / (NEUTRAL_LOW) * 100)
                motor_left.backward(speed)
                print(f"Motor 1 backward with speed {speed}")
            elif x1 > NEUTRAL_HIGH:
                speed = int((x1 - NEUTRAL_HIGH) / (4095 - NEUTRAL_HIGH) * 100)
                motor_left.forward(speed)
                print(f"Motor 1 forward with speed {speed}")
            else:
                motor_left.stop()
                print("Motor 1 stop")

            # Control motor 2 (right) based on x2
            if x2 < NEUTRAL_LOW:
                speed = int((NEUTRAL_LOW - x2) / (NEUTRAL_LOW) * 100)
                motor_right.backward(speed)
                print(f"Motor 2 backward with speed {speed}")
            elif x2 > NEUTRAL_HIGH:
                speed = int((x2 - NEUTRAL_HIGH) / (4095 - NEUTRAL_HIGH) * 100)
                motor_right.forward(speed)
                print(f"Motor 2 forward with speed {speed}")
            else:
                motor_right.stop()
                print("Motor 2 stop")
        except ValueError:
            print("Invalid data received")

# Main loop
def main():
    while True:
        on_receive_callback(e)  # Check for received messages
        time.sleep(0.1)
        motor_left.stop()
        motor_right.stop()

if __name__ == "__main__":
    main()
