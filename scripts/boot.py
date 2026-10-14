import time
import board
import digitalio
import storage
import usb_hid

# GP11 input with pull-up
gp11 = digitalio.DigitalInOut(board.GP11)
gp11.direction = digitalio.Direction.INPUT
gp11.pull = digitalio.Pull.UP

time.sleep(0.05)  # let pin settle

if not gp11.value:
    # GP11 LOW -> shorted to GND
    storage.disable_usb_drive()
    usb_hid.enable()