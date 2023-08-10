import board

from kmk.bootcfg import bootcfg

bootcfg(
    sense=board.GP0,
    source=board.GP11,
    cdc=False,
    consumer_control=True,
    keyboard=True,
    midi=True,
    mouse=True,
    nkro=False,
    pan=False,
    storage=False,
    usb_id=('qwail56', 'Split Ergo KMK Keyboard'),
)
