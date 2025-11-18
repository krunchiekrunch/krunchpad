import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.modules.macros import Macros, Press, Release, Tap
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
macros = Macros()
mouse = MouseKeys()
encoder_handler = EncoderHandler()
keyboard.modules.append(macros)
keyboard.modules.append(MouseKeys())
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(encoder_handler)
keyboard.modules.append(Layers())

# matrix
keyboard.row_pins = (board.D10, board.D9, board.D8)
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

_______ = KC.TRNS
xxxxxxx = KC.NO
Fn = KC.MO(1)

keyboard.keymap = [
    [
        KC.Q,     KC.W,   KC.D, KC.PGUP,
        KC.T,     KC.S,   KC.M,    KC.H,
        KC.COMMA, KC.DOT, KC.C,      Fn,
    ],
    
    [
        KC.MUTE, KC.MPRV, KC.MPLY, KC.MNXT, 
        xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx,
        xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx,
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
        TextEntry(text="""
Q W D PU     ZOOM/VOL
T S M H     krunchpad
< > C Fn      HW v1.1
        """),
    ],
    height=32,
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
