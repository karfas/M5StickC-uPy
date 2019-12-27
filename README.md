# M5StickC-uPy

Micropython utilities for the M5StickC.

Currently contains:

## Library for dealing with M5StickC hardware.


#### Usage:

```python
import sys

try:
    from m5stickc import lcd_backlight_power, power_button, axp

    lcd_backlight_power(False)
    print("Battery Voltage: {}".format(axp.battery_voltage()))
    print("Battery Current: {}".format(axp.battery_current()))
    print("Bus Voltage: {}".format(axp.bus_voltage()))
    print("Bus Current: {}".format(axp.bus_current()))
    print("Input Voltage: {}".format(axp.input_voltage()))
    print("Input Current: {}".format(axp.input_current()))

#    while True:
#        print("power button: {}".format(power_button()))
#        time.sleep_ms(100)
except Exception as e:
    sys.print_exception(e)
```

## Driver for AXP192 power management device

The AXP192 driver was (partly) ported from the Arduino libraries.
On my M5StickC, the readings look plausible (except for input_voltage())

#### Usage:

Copy of code in m5stickc.py:

```python
from machine import I2C, Pin
from axp192 import AXP192

hw_i2c_0 = I2C(0, sda=Pin(21), scl=Pin(22))
axp = AXP192(hw_i2c_0)
axp.setup()

def lcd_backlight_power(status=True):
    """On M5StickC, LCD backlight is connected to LD02"""
    axp.set_LD02(status)


def power_button():
    if axp.get_button():
        return True
    return False

```
