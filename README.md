# M5StickC-uPy

Micropython utilities for the M5StickC.

## Contents:

- main.py: For development. 
  - Initializes WIFI (using a wifi_manager) 
  - Starts the WEBREPL server.
  - Starts the ftp server.
- app.py: Testbed for the other modules.
- m5stickc.py: first steps for a high-level interface to the M5StickC hardware.
  Provides:
  - `power_button()` 
  - `lcd_backlight_power()`
- axp192.py: Driver for AXP192 as used in the M5StickC (port from Arduino)
  **Not** ported were:
  - the Coulombcounter functions
  - the `LightSleep()` and `DeepSleep()` functions. 
    In my opinion, these shouldn't be part of the AXP192 interface, anyway.
    The (provided) `set_sleep()` turns off most outputs, but doesn't put the ESP32 into sleep.

## Usage:

Please see app.py and m5stickc.py for example usage.

### For a fast try:
- install micropython on your M5StickC
- copy app.py, m5stickc.py and axp192.py to your device.
- open a terminal session and enter

```
import app.py
app.run()
```

## Credits:

tayfununlu's WifiManager: https://github.com/tayfunulu/WiFiManager
robert-hh's ftp server: https://github.com/robert-hh/FTP-Server-for-ESP8266-ESP32-and-PYBD.git

