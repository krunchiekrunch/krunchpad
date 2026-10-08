# CircuitPython (Tested with 10.3.1)

# Dependencies
- KMK
- [Adafruit CPY SSD1306 lib](https://github.com/adafruit/Adafruit_CircuitPython_DisplayIO_SSD1306/releases) (Download `adafruit-circuitpython-displayio-ssd1306-x.x-mpy-x.x.x.zip`

Unzip and move `/lib/adafruit_displayio_ssd1306.mpy` to `/lib` of your microcontroller

- [Adafruit CPY DIsplay Text lib](https://github.com/adafruit/Adafruit_CircuitPython_Display_Text/releases) (Download `adafruit-circuitpython-display-text-x.x-mpy-x.x.x.zip`

Unzip and move `/lib/adafruit_display_text` to `/lib` of your microcontroller

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
├─ boot.py
```
