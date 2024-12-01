from machine import Pin, PWM, ADC
import time

# Pinbelegung für den Joystick
VRX_PIN = 25  # GPIO39 (ADC3) für VRX
VRY_PIN = 26  # GPIO36 (ADC0) für VRY
SW_PIN = 17   # GPIO17 für den Button (falls benötigt)

# Motorsteuerungs-Pins (angepasst an dein Setup)
MOTOR1_FORWARD = 25  # GPIO25 für Motor 1 vorwärts
MOTOR1_BACKWARD = 26 # GPIO26 für Motor 1 rückwärts
MOTOR2_FORWARD = 27  # GPIO27 für Motor 2 vorwärts
MOTOR2_BACKWARD = 14 # GPIO14 für Motor 2 rückwärts

# Initialisierung der Joystick-Pins
vrx = ADC(Pin(VRX_PIN))
vry = ADC(Pin(VRY_PIN))
vrx.atten(ADC.ATTN_11DB)
vry.atten(ADC.ATTN_11DB)

# Initialisierung der Motorsteuerung
motor1_forward = PWM(Pin(MOTOR1_FORWARD), freq=1000)
motor1_backward = PWM(Pin(MOTOR1_BACKWARD), freq=1000)
motor2_forward = PWM(Pin(MOTOR2_FORWARD), freq=1000)
motor2_backward = PWM(Pin(MOTOR2_BACKWARD), freq=1000)

# Funktion zum Stoppen aller Motoren
def stop_motors():
    motor1_forward.duty(0)
    motor1_backward.duty(0)
    motor2_forward.duty(0)
    motor2_backward.duty(0)

# Funktion zum Vorwärtsfahren
def move_forward(speed):
    motor1_forward.duty(speed)
    motor1_backward.duty(0)
    motor2_forward.duty(speed)
    motor2_backward.duty(0)

# Schwellenwert für Joystick
JOYSTICK_THRESHOLD = 2750

# Hauptloop
while True:
    # Joystick-Werte lesen
    x_value = vrx.read()
    y_value = vry.read()

    # Debug-Ausgabe (optional)
    print(f"Joystick X: {x_value}, Y: {y_value}")

    # Bedingung: Joystick-Werte über dem Schwellenwert
    if x_value >= JOYSTICK_THRESHOLD or x_value <= JOYSTICK_THRESHOLD:
        # Bedingung: Joystick ganz nach vorne gedrückt
        if x_value > 2850:  # Schwellenwert für "nach vorne" (anpassen, falls nötig)
            print("Joystick nach vorne gedrückt! Auto bewegt sich vorwärts.")
            move_forward(512)  # Geschwindigkeit einstellen (0-1023)
        elif x_value < 2650:
            print("Auto fährt rückwärts")
        else:
            print("Joystick nicht nach vorne oder hinten. Auto stoppt.")
            stop_motors()
    
    
    else:
        print("Joystick innerhalb des Totbereichs. Auto stoppt.")
        stop_motors()

    time.sleep(0.1)  # Kleines Delay für Stabilität
