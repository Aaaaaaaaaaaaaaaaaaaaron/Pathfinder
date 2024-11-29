import network
import espnow
import time
from machine import Pin
import sys
import select

# Funktion, um Tastaturbefehle zu lesen
def read_input():
    if select.select([sys.stdin], [], [], 0)[0]:
        return sys.stdin.read(1)
    return None


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

# Initialisierung des Tasters an Pin 27
button = Pin(27, Pin.IN, Pin.PULL_UP)

# Variable zur Steuerung der Befehlssendung
command_sent = None

# Hauptschleife
while True:
    key = read_input()
    if key:
        if key == 'w':
            e.send(peer, b'forward')
            print("Command 'forward' sent")
            command_sent = 'forward'
        elif key == 's':
            e.send(peer, b'backward')
            print("Command 'backward' sent")
            command_sent = 'backward'
        elif key == 'a':
            e.send(peer, b'left')
            print("Command 'left' sent")
            command_sent = 'left'
        elif key == 'd':
            e.send(peer, b'right')
            print("Command 'right' sent")
            command_sent = 'right'
        
        if command_sent:
            time.sleep(0.2)  # Warte 0,5 Sekunden
            e.send(peer, b'stop')  # Sende Stopp-Befehl
            print("Command 'stop' sent")
            command_sent = None

    time.sleep(0.1)  # Kurze Verzögerung zur Entlastung der CPU
