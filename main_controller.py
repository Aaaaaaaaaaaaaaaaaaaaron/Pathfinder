from machine import Pin, PWM, ADC
import time
 
# Pinbelegung für den Joystick
VRX_PIN = 12  # GPIO39 (ADC3) für VRX
VRY_PIN = 14  # GPIO36 (ADC0) für VRY
SW_PIN = 27   # GPIO17 für den Button

VRX2_PIN = 26  # 
VRY2_PIN = 25  # 
SW2_PIN = 33   # nicht aktiviert

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
        if x_value > 1850:  # Schwellenwert für "nach vorne" (anpassen, falls nötig)
            print("motor1 vorwärts.")
            
        elif x_value < 1650:
            print("motor1 rückwärts")
        
        if x_value2 > 1850:  # Schwellenwert für "nach vorne" (anpassen, falls nötig)
            print("motor2 vorwärts.")
            
        elif x_value2 < 1650:
            print("motor2 rückwärts")
        else:
            print("Auto steht.")
            

    else:
        print("Joystick innerhalb des Totbereichs.")
       
 
    time.sleep(0.1)  # Kleines Delay für Stabilität

