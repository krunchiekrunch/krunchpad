import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.modules.macros import Macros, Press, Release, Tap, Delay
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.tapdance import TapDance

keyboard = KMKKeyboard()
macros = Macros()
mouse = MouseKeys()
tapdance = TapDance()
tapdance.tap_time = 250
encoder_handler = EncoderHandler()
keyboard.modules.append(macros)
keyboard.modules.append(MouseKeys())
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(encoder_handler)
keyboard.modules.append(Layers())
keyboard.modules.append(tapdance)

# matrix
keyboard.row_pins = (board.D10, board.D9, board.D8)
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

m1 = KC.MACRO("macro 2", Delay(500), Tap(KC.ENTER),)
m2 = KC.MACRO(Tap(KC.SLASH), Delay(300), "macro 1", Delay(300), Tap(KC.ENTER),)
dm = KC.TD(KC.D, KC.M)

_______ = KC.TRNS
xxxxxxx = KC.NO
xxxx = KC.NO
Fn = KC.MO(1)

keyboard.keymap = [
    [
        KC.Q,     KC.W,   dm,   xxxx,
        KC.T,     KC.S,   KC.H, Fn,
        KC.COMMA, KC.DOT, KC.C, KC.PGUP,
    ],
    
    [
        KC.ESC,  KC.TAB,  m2,      m1, 
        KC.MPRV, KC.MPLY, KC.MNXT, _______,
        KC.F1,   KC.F2,   KC.F11,  KC.DEL,
    ],
]

# volume knob
encoder_handler.pins = ((board.D6, board.D7),)
encoder_handler.map = [
    ((KC.MW_DN, KC.MW_UP),), # Mouse wheel zooming
    ((KC.VOLD, KC.VOLU),),   # Volume control
    ]

# 128x32 OLED display
display = Display(
    display=SSD1306(sda=board.D4, scl=board.D5),
    entries=[
        ImageEntry(image="up.bmp", x=-8, y=0, layer=0),
        
        ImageEntry(image="down.bmp", x=-8, y=0, layer=1),
        
        TextEntry(text="""
Q   W   D/M      +/-
T   S   H   Fn
<   >   C   PU
        """, layer=2),
        
        TextEntry(text="""
ESC TAB m1  m2   VOL
|<  ||  >|  Fn
F1  F2  F11 DEL
        """, layer=3),
    ],
    height=32,
    brightness=1,
)
keyboard.extensions.append(display)

# Onboard Neopixel
neopixel = RGB(
    pixel_pin=board.NEOPIXEL,
    num_pixels=1,
    val_limit=100,
    hue_default=170, # hue
    sat_default=60, # satuation
    val_default=45, # brightness/value
    animation_mode=AnimationModes.STATIC,
)
# keyboard.extensions.append(neopixel)

if __name__ == '__main__':
    keyboard.go()
