from machine import Pin, PWM, ADC
import network
import espnow
import time

# Configure Wi-Fi in station mode
wlan = network.WLAN(network.STA_IF)  # Create a WLAN object in station mode
wlan.active(True)  # Activate the WLAN interface
wlan.disconnect()  # Disconnect from any existing Wi-Fi connection since we will use ESP-NOW

# Initialize ESP-NOW
e = espnow.ESPNow()  # Create an ESPNow object
e.active(True)  # Activate ESP-NOW

# MAC address of the receiver (Car)
peer = b'\x1c\x69\x20\xcd\x31\xbc'  # MAC address of the car (receiver)
e.add_peer(peer)  # Add the car as a peer to send messages to

# Joystick pin configuration
VRX_PIN = 33  # GPIO33 (ADC1_CH5) for VRX
VRY_PIN = 32  # GPIO32 (ADC1_CH4) for VRY
SW_PIN = 35   # GPIO35 for the button (not used)

VRX2_PIN = 34  # GPIO34 (ADC1_CH6) for VRX2
VRY2_PIN = 39  # GPIO39 (ADC1_CH0) for VRY2
SW2_PIN = 36   # GPIO36 for the second button (not used)

# Initialize the joystick pins
vrx = ADC(Pin(VRX_PIN))  # Create an ADC object for VRX pin
vry = ADC(Pin(VRY_PIN))  # Create an ADC object for VRY pin
vrx.atten(ADC.ATTN_11DB)  # Set attenuation for VRX to 11dB for full range (0-3.3V)
vry.atten(ADC.ATTN_11DB)  # Set attenuation for VRY to 11dB for full range (0-3.3V)

vrx2 = ADC(Pin(VRX2_PIN))  # Create an ADC object for VRX2 pin
vry2 = ADC(Pin(VRY2_PIN))  # Create an ADC object for VRY2 pin
vrx2.atten(ADC.ATTN_11DB)  # Set attenuation for VRX2 to 11dB for full range (0-3.3V)
vry2.atten(ADC.ATTN_11DB)  # Set attenuation for VRY2 to 11dB for full range (0-3.3V)

# Threshold values for the joystick
JOYSTICK_THRESHOLD = 1750  # Threshold for the first joystick
JOYSTICK_THRESHOLD2 = 1750  # Threshold for the second joystick

# Main loop
while True:
    # Read joystick values
    x_value = vrx.read()  # Read the X value of the first joystick
    y_value = vry.read()  # Read the Y value of the first joystick
    x_value2 = vrx2.read()  # Read the X value of the second joystick
    y_value2 = vry2.read()  # Read the Y value of the second joystick

    # Debug output (optional)
    print(f"Joystick 1: {x_value}, Y: {y_value}")  # Print the values of the first joystick
    print(f"Joystick 2: {x_value2}, Y: {y_value2}")  # Print the values of the second joystick

    # Encode coordinates as bytes
    msg = f"{x_value},{x_value2}".encode('utf-8')  # Create a message with joystick X values and encode it as bytes

    # Send message
    e.send(peer, msg)  # Send the message to the car
    print(f"Command '{msg}' sent")  

    time.sleep(0.1)  # delay for stability
