import network
import esp
import espnow
import machine
import time
from machine import Pin, PWM
#	 from espnow import init

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

# Define the callback for receiving data
def on_receive_callback(e):
    sender_mac, msg = e.irecv()
    if msg:  # Check if message is not None
        command = msg.decode('utf-8')
        if command == 'forward':
            motor_left.forward(100)
            motor_right.forward(100)
        elif command == 'backward':
            motor_left.backward(100)
            motor_right.backward(100)
        elif command == 'stop':
            motor_left.stop()
            motor_right.stop()
        elif command == "left":
            motor_left.backward(100)
            motor_right.forward(100)
        elif command == "right":
            motor_left.forward(100)
            motor_right.backward(100)

# Main loop
def main():
    while True:
        on_receive_callback(e)  # Check for received messages
        time.sleep(0.2)

if __name__ == "__main__":
    main()


