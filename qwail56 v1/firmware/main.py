# qwail56 - 60% ergo split keyboard https://github.com/Galile0-designs/qwail56
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.split import Split, SplitSide

keyboard = KMKKeyboard()

keyboard.col_pins = (
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
)

keyboard.row_pins = (
    board.GP11,
    board.GP12,
    board.GP13,
    board.GP14,
    board.GP15,
)

# YOU MUST UNCOMMENT THE CORRECT split_side BELOW
# split_side = SplitSide.LEFT
# split_side = SplitSide.RIGHT

split = Split(
    split_flip=True,
    uart_flip=True,
    split_target_left=True,
    data_pin=board.GP7,
    use_pio=True,
    )

keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.modules.append(Layers())
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(split)

keyboard.keymap = [

    # base layer
    [
    KC.ESC,    KC.N1,  KC.N2,  KC.N3,   KC.N4,   KC.N5,    KC.NO,      KC.NO,   KC.N6,    KC.N7,   KC.N8,   KC.N9,  KC.N0,   KC.BSPC,
    KC.TAB,    KC.Q,   KC.W,   KC.E,    KC.R,    KC.T,     KC.NO,      KC.NO,   KC.Y,     KC.U,    KC.I,    KC.O,   KC.P,    KC.BSLS,
    KC.LCTRL,  KC.A,   KC.S,   KC.D,    KC.F,    KC.G,     KC.NO,      KC.NO,   KC.H,     KC.J,    KC.K,    KC.L,   KC.QUOT, KC.ENT,
    KC.LSHIFT, KC.Z,   KC.X,   KC.C,    KC.V,    KC.B,     KC.MPLY,    KC.MPLY, KC.N,     KC.M,    KC.COMM, KC.DOT, KC.SLSH, KC.RSFT,
    KC.NO,     KC.NO,  KC.NO,  KC.LGUI, KC.LALT, KC.MO(1), KC.SPC,     KC.SPC,  KC.MO(2), KC.RALT, KC.RCTL, KC.NO,  KC.NO,   KC.NO,
    ],

    # function layer
    [
    KC.F1,     KC.F2,  KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.NO,      KC.NO,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,
    KC.CAPS,   KC.INS, KC.HOME, KC.PGUP, KC.NO,   KC.NO,   KC.NO,      KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.PSCR,
    KC.LCTRL,  KC.DEL, KC.END,  KC.PGDN, KC.NO,   KC.NO,   KC.NO,      KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.UP,   KC.NO,   KC.ENT,
    KC.LSHIFT, KC.NO,  KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.MPLY,    KC.MPLY, KC.NO,   KC.NO,   KC.LEFT, KC.DOWN, KC.RGHT, KC.RSFT,
    KC.NO,     KC.NO,  KC.NO,   KC.LGUI, KC.LALT, KC.TRNS, KC.SPC,     KC.SPC,  KC.TRNS, KC.RALT, KC.RCTL, KC.NO,   KC.NO,   KC.NO,
    ],

    # symbol layer
    [
    KC.ESC,    KC.NO,  KC.NO,  KC.NO,   KC.NO,   KC.NO,    KC.NO,      KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.GRV,  KC.PLUS, KC.BSPC,
    KC.CAPS,   KC.NO,  KC.NO,  KC.NO,   KC.NO,   KC.NO,    KC.NO,      KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.LBRC, KC.RBRC, KC.BSLS,
    KC.LCTRL,  KC.NO,  KC.NO,  KC.NO,   KC.NO,   KC.NO,    KC.NO,      KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.SCLN, KC.ENT,
    KC.LSHIFT, KC.NO,  KC.NO,  KC.NO,   KC.NO,   KC.NO,    KC.MPLY,    KC.MPLY, KC.NO,   KC.NO,   KC.COMM, KC.DOT,  KC.MINUS,KC.RSFT,
    KC.NO,     KC.NO,  KC.NO,  KC.LGUI, KC.LALT, KC.TRNS,  KC.SPC,     KC.SPC,  KC.TRNS, KC.RALT, KC.RCTL, KC.NO,   KC.NO,   KC.NO,
    ],
]

# encoder
encoder_handler.pins = (
    (board.GP16, board.GP17, None, True),
    )

encoder_handler.map = [
    ((KC.VOLU, KC.VOLD, None),),
    ]

if __name__ == "__main__":
    keyboard.go()
