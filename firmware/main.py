import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.modules.macros import Macros, Press, Release, Tap, Delay
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.tapdance import TapDance

keyboard = KMKKeyboard()
macros = Macros()
mouse = MouseKeys()
encoder_handler = EncoderHandler()
tapdance = TapDance()
tapdance.tap_time = 250
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

_______ = KC.TRNS
xxxxxxx = KC.NO
xxxx = KC.NO
Fn = KC.MO(1)

RST = KC.LCTRL(KC.SPACE)
MV = KC.LSHIFT(KC.SPACE)
RSTMV = KC.TD(RST, MV)

LWIN = KC.LALT(KC.N1)
RWIN = KC.LALT(KC.N3)
FO = KC.LALT(KC.N9)

FULL = KC.LALT(KC.N7)
OVH = KC.LALT(KC.N8)
PED = KC.LALT(KC.N5)
EFB = KC.LALT(KC.N0)

keyboard.keymap = [
    [
        KC.F13, KC.F14, KC.F15, KC.F16,
        RST,    LWIN,   RWIN,   FO,
        FULL,   OVH,    PED,    EFB,
    ],
]

# volume knob
encoder_handler.pins = ((board.D6, board.D7),)
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),),   # Volume control
    ]

# 128x32 OLED display
display = Display(
    display=SSD1306(sda=board.D4, scl=board.D5),
    entries=[
        TextEntry(text="""
REC  CLIP TGLE SS
RST  LWIN RWIN FO
FULL OVHD PED  EFB
        """),
    ],
    width=128,
    height=32,
    brightness=0.1,
)
keyboard.extensions.append(display)

if __name__ == '__main__':
    keyboard.go()
