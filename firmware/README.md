# REQUIRE CIRCUITPYTHON 9 (NOT 10)

# Dependencies
- KMK
- [Adafruit CPY SSD1306 lib](https://github.com/adafruit/Adafruit_CircuitPython_DisplayIO_SSD1306/releases) (Download `adafruit-circuitpython-displayio-ssd1306-9.x-mpy-x.x.x.zip`

Unzip and move `/lib/adafruit_displayio_ssd1306.mpy` to `/lib` of your microcontroller

- [Adafruit CPY DIsplay Text lib](https://github.com/adafruit/Adafruit_CircuitPython_Display_Text/releases) (Download `adafruit-circuitpython-display-text-9.x-mpy-x.x.x.zip`

Unzip and move `/lib/adafruit_display_text` to `/lib` of your microcontroller

- [Adafruit CPY NeoPixel lib](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/blob/main/neopixel.py)

Download and move to the root of the microcontroller storage

# File structure

```
CIRCUITPY/
├─ kmk/
│  ├─ ...
├─ lib/
│  ├─ adafruit_display_text/
│  │  ├─ ...
│  ├─ adafruit_displayio_ssd1306.mpy
├─ main.py
├─ neopixel.py
```
