import time
import board
import digitalio
import payload
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# GP11 input with pull-up
gp11 = digitalio.DigitalInOut(board.GP11)
gp11.direction = digitalio.Direction.INPUT
gp11.pull = digitalio.Pull.UP

time.sleep(0.05)  # let pin settle

if not gp11.value:
    payload.payload()
