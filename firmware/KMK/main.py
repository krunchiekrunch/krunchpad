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

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)
mouse = MouseKeys()
keyboard.modules.append(MouseKeys())
keyboard.extensions.append(MediaKeys())
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# matrix
keyboard.row_pins = (board.D10, board.D9, board.D8)
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.Q,     KC.W,   KC.MW_UP, KC.MW_DN,
        KC.T,     KC.S,   KC.D,     KC.H,
        KC.COMMA, KC.DOT, KC.C,     KC.PGUP,
    ]
]

# volume knob
encoder_handler.pins = (
    (board.D6, board.D7),
    )
encoder_handler.map = [((KC.VOLD, KC.VOLU),)]

# 128x32 OLED display
display = Display(
    display=SSD1306(sda=board.D4, scl=board.D5),
    entries=[
        TextEntry(text="""
Q W + -    SCR Config
T S D H     krunchpad
< > C PU      HW v1.1
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
    sat_default=0, # satuation
    val_default=100, # brightness/value
    animation_mode=AnimationModes.STATIC,
)
# keyboard.extensions.append(neopixel)

if __name__ == '__main__':
    keyboard.go()

