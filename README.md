# M5StickC-uPy

Micropython utilities for the M5StickC.

## Contents:

- main.py: For development. Initializes WIFI (using a wifi_manager) and starts the WEBREPL server.
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
    These don't belong to the AXP192 interface, anyway.

## Usage:

Please see app.py and m5stickc.py for example usage.
