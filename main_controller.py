from machine import Pin, PWM, ADC
import network
import espnow
import time
from machine import Pin
import sys
import select
# Konfiguration der Wi-Fi-Verbindung im station mode
wlan = network.WLAN(network.STA_IF)
wlan.active(True)  # Wi-Fi aktivieren
wlan.disconnect()  # Trennen, da wir ESP-NOW verwenden werden

# Initialisierung von ESP-NOW
e = espnow.ESPNow()
e.active(True)  # ESP-NOW aktivieren

# MAC-Adresse des Empfängers (Auto)
peer = b'\x1c\x69\x20\xcd\x31\xbc'  # car mac: 1c:69:20:cd:31:bc
e.add_peer(peer)
# Pinbelegung für den Joystick
VRX_PIN = 33  # GPIO39 (ADC3) für VRX
VRY_PIN = 32  # GPIO36 (ADC0) für VRY
SW_PIN = 35   # GPIO17 für den Button

VRX2_PIN = 34  # 
VRY2_PIN = 39  # 
SW2_PIN = 36   # nicht aktiviert

# Initialisierung der Joystick-Pins
vrx = ADC(Pin(VRX_PIN))
vry = ADC(Pin(VRY_PIN))
vrx.atten(ADC.ATTN_11DB)
vry.atten(ADC.ATTN_11DB)
 
# Initialisierung der Joystick-Pins
vrx2 = ADC(Pin(VRX2_PIN))
vry2 = ADC(Pin(VRY2_PIN))
vrx2.atten(ADC.ATTN_11DB)
vry2.atten(ADC.ATTN_11DB)
 
# Schwellenwert für Joystick
JOYSTICK_THRESHOLD = 1750
JOYSTICK_THRESHOLD2 = 1750



# Variable zur Steuerung der Befehlssendung
command_sent = None
 
# Hauptloop
while True:
    # Joystick-Werte lesen
    x_value = vrx.read()
    y_value = vry.read()
    x_value2 = vrx2.read()
    y_value2 = vry2.read()
 
    # Debug-Ausgabe (optional)
    print(f"Joystick 1: {x_value}, Y: {y_value}")
    print(f"Joystick 2: {x_value2}, Y: {y_value2}")
    
    # Bedingung: Joystick-Werte über dem Schwellenwert
    if x_value >= JOYSTICK_THRESHOLD or x_value <= JOYSTICK_THRESHOLD:
        # Bedingung: Joystick ganz nach vorne gedrückt
        if x_value > 2050 and x_value2 > 1050 and x_value2 < 2050:  # Schwellenwert für "nach vorne" (anpassen, falls nötig)
            print("motor1 vorwärts.") #right
            e.send(peer, b'm1v')
            print("Command 'm1v' sent")
            command_sent = 'm1v'
            
        if x_value < 1050 and x_value2 > 1050 and x_value2 < 2050:
            print("motor1 rückwärts") #left
            e.send(peer, b'm1r')
            print("Command 'm1r' sent")
            command_sent = 'm1r'
        
        if x_value2 > 2050 and x_value > 1050 and x_value < 2050:  # Schwellenwert für "nach vorne" (anpassen, falls nötig)
            print("motor2 vorwärts.") #left
            e.send(peer, b'm2v')
            print("Command 'm2v' sent")
            command_sent = 'm2v'
            
        if x_value2 < 1050 and x_value > 1050 and x_value < 2050:
            print("motor2 rückwärts") #right
            e.send(peer, b'm2r')
            print("Command 'm2r' sent")
            command_sent = 'm2r'
            
        if x_value2 < 1050 and x_value < 1050:
            print("backward")
            e.send(peer, b'backward')
            print("Command 'backward' sent")
            command_sent = 'backward'
            
        if x_value2 > 2050 and x_value > 2050:
            print("forward")
            e.send(peer, b'forward')
            print("Command 'forward' sent")
            command_sent = 'forward'
        
        if x_value > 1050 and x_value < 2050 and x_value2 > 1050 and x_value2 < 2050: 
            print("Auto steht.") #stop
        
            e.send(peer, b'stop')
            print("Command 'stop' sent")
            command_sent = 'stop'
            

    else:
        print("Joystick innerhalb des Totbereichs.")
       
 
    time.sleep(0.1)  # Kleines Delay für Stabilität
