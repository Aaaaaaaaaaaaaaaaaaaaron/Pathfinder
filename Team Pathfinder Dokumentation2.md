# Dokumentation Team Landrover

**Mitglieder:**

- Jacob Fraas
- Aaron Lange
- Timo Locker

---

## Woche 1 (04.11.2024 - 10.11.2024)

### Aktivitäten:

- **Planung** des groben Aufbaus und Ablaufs (*alle Mitglieder*).
- **Auswahl** und Bestellung der benötigten Komponenten (*Timo Locker*).
- Erste **Code-Recherche** zum Aufbau des Autos und mögliche Code-Ansätze (*Aaron Lange*).
- **Recherche** von bestehenden Projekten für Inspiration und technische Hinweise (*Jacob Fraas*).

### Probleme und Lösungen:

- **Problem:** Initiale Nutzung von ChatGPT brachte keine hilfreichen Ergebnisse.
  - **Lösung:** Erstellung präziser und klarer Prompts, um spezifischere Antworten zu erhalten.

### Quellen:

- [ESP Anschlussbelegung - xplore DNA](https://www.xplore-dna.net/mod/page/view.php?id=4338)

---

## Woche 2 (11.11.2024 - 17.11.2024)

### Aktivitäten:

- Identifikation und **Bestellung fehlender Komponenten**.
- **Einrichtung** eines GitHub-Repositories zur Versionskontrolle.
- Lösung technischer Probleme im Zusammenhang mit dem ESP32.
- **Zusammenbau** und erste Funktionstests des Autos und der Motoren.

### Probleme und Lösungen:

- **Problem:** Die bestellten ESP32 konnten keine Verbindung zu Thonny herstellen.
  - **Ursache:** Defekte USB-Kabel.
  - **Lösung:** Austausch der Kabel.
- **Problem:** ESP32 enthielten keine Firmware.
  - **Lösung:** Firmware wurde heruntergeladen und auf die ESP32 aufgespielt.

### Quellen:

- [Installation von MicroPython auf dem ESP32](https://docs.sunfounder.com/projects/esp32-starter-kit/de/latest/micropython/python_start/install_micropython.html)

---

## Woche 3 (18.11.2024 - 24.11.2024)

### Aktivitäten:

- Erstellung eines Programms zum **Auslesen der beiden MAC-Adressen** der ESP32.
- **Aufbau** der Steckverbindung zwischen H-Brücken und ESP32.
- Schreiben eines Codes zum WLAN-Test (mit Unterstützung von ChatGPT).
- Nachbestellung von fehlenden **Steckverbindungen** und Kabeln.
- Erste **Testfahrt** des Autos.
- Einrichtung von **ESP-NOW** und Verbindungstests.

### Probleme und Lösungen:

- **Problem:** Nicht ausreichende Spannung zur Versorgung der beiden H-Brücken und des ESP32.
  - **Lösung:** Nachbestellung zusätzlicher Batterien und Batteriehalterungen.
- **Problem:** Der von ChatGPT generierte Code für die WLAN-Verbindung der ESP32 war unbrauchbar.
  - **Lösung:** Neue Recherche und eigenständige Entwicklung des Codes.

### Quellen:

- [ESP32 DC Motor Steuerung - Random Nerd Tutorials](https://randomnerdtutorials.com/micropython-esp32-esp8266-dc-motor-l298n/)

### ChatGPT-Prompt:

- "Schreibe mir einen MicroPython-Code für zwei ESPs, um diese mit WLAN zu verbinden."

---

## Woche 4 (25.11.2024 - 01.12.2024)

### Aktivitäten:

- **Erster Code-Push** auf GitHub und Hochladen des Codes auf die ESP32.
- Entwicklung eines ersten **Prototyps der Lenkung**.
- Erstellung der **Basisstruktur** des Codes.
- Einrichtung der Lenkung mit **Joysticks**.
- **Debugging** der Joystick-Funktion.

### Code:

- Siehe Git-History

### Quellen:

- [ESP32 DC Motor Steuerung - Random Nerd Tutorials](https://randomnerdtutorials.com/micropython-esp32-esp8266-dc-motor-l298n/)
- [Joystick Modul Datenblatt](https://cdn.shopify.com/s/files/1/1509/1638/files/Joystick_Modul_Datenblatt.pdf)

### Probleme und Lösungen:

- **Problem:** Joystick wurde auf den falschen Pin (5V) angeschlossen, wodurch keine Funktion gegeben war.
  - **Lösung:** Korrekte Verkabelung des Joysticks.

---

## Woche 5 (02.12.2024 - 08.12.2024)

### Aktivitäten:

- Überprüfung der Funktionen zur Optimierung des **Fahrverhaltens**.
- Analyse und Reduktion des **Delays** bei Joystick-Eingaben.
- Erste richtige Testfahrt mit dem Auto.

### Code:

- Siehe Git-History

### Probleme und Lösungen:

- **Problem:** Verzögerung bei der Übertragung der Joystick-Daten.
  - **Lösung:** Reduktion auf die Übertragung der X-Werte, wodurch die Verzögerung signifikant verringert wurde.

---

## Woche 6 (09.12.2024 - 15.12.2024)

### Aktivitäten:

- Optimierung der Anschlüsse und Vorbereitung zum **Löten** auf eine Lochplatine.
- Erstellung eines Rasters für die **Platinendesign**.
- Prototyp-Entwicklung eines **Controllers** zur Steuerung des Autos.

### Code:

- Siehe Git-History

### Probleme und Lösungen:

- **Problem:** Unterschiedliche Meinungen innerhalb des Teams über den Zusammenbau.
  - **Lösung:** Diskussion und Abstimmung innerhalb der Gruppe.

---

## Woche 7 (16.12.2024 - 22.12.2024)

### Aktivitäten:

- **Löten** der beiden Platinen.
- **3D-Druck** des Controller-Gehäuses.
- Zusammenbau und abschließende Funktionstests von Auto und Controller.

### Code:

- Siehe Git-History

### Probleme und Lösungen:

- **Problem:** Fehlerhaftes Löten durch Parallaxenfehler beim Ablesen des Plans.
  - **Lösung:** Neuverlöten der betroffenen Elemente.
- **Problem:** Steuerung des Autos war zunächst nicht möglich.
  - **Lösung:** Anpassung der Joystick-Range zur Verbesserung der Steuerbarkeit.

### Quellen:

- [ESP Anschlussbelegung - xplore DNA](https://www.xplore-dna.net/mod/page/view.php?id=4338)
- Eigene Pinbelegung

---

## Woche 8/9 (23.12.2024 - 05.01.2025)

### Aktivitäten:

- Finaler **Funktionstest** von Auto und Controller.
- Erstellung eines **Promo-Videos** inklusive Aufnahmen, Schnitt und Komprimierung.

### Probleme und Lösungen:

- **Problem:** Aufgenommenes Video war zu groß und konnte nicht direkt bearbeitet werden.
  - **Lösung:** Nutzung eines Video-Komprimierers.

### Quellen:

- [Clideo Video Komprimierer](https://clideo.com/de/compress-video)





