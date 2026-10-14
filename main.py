import time
import os
import string
import shutil
import msvcrt
import subprocess
import webbrowser

def check_rpi_rp2(drive_name, print_message):
    for letter in string.ascii_uppercase:
        drive = f"{letter}:\\"

        if os.path.exists(drive):
            try:
                label = os.popen(
                    f'vol {letter}:'
                ).read()

                if str(drive_name) in label.upper():
                    if print_message:
                        print("[FOUND] " + str(drive_name) + f" is connected at {drive}")
                    return drive

            except OSError:
                pass

    return False

print("Welcome to the official NotAKeyboard builder")
print("Press any key to continue...\n")
msvcrt.getch()
print("Please plug in your RPI Pico while holding the BOOTSEL button.")
while True:
    if check_rpi_rp2("RPI-RP2", True):
        break

# First format the pico

print("Formating Pico")
shutil.copy2("format/flash_nuke.uf2", str(check_rpi_rp2("RPI-RP2", False)))

time.sleep(2)

print("Waiting for Pico....")

while True:
    if check_rpi_rp2("RPI-RP2", True):
        break

print("Formated Pico")

# Now we add the software

print("Adding the software")
shutil.copy2("software/adafruit-circuitpython-raspberry_pi_pico-en_US-9.1.1.uf2", str(check_rpi_rp2("RPI-RP2", True)))
print("Waiting for the software to copy...")
time.sleep(10)

print("Waiting for Pico...")

while True:
    if check_rpi_rp2("CIRCUITPY", True):
        break

print("Installed software on pico\n")

print ("Starting to copy code and libraries...")

# Now copy the libraries
lib_dir = str(check_rpi_rp2("CIRCUITPY", False) + "/lib")
shutil.copytree("lib", lib_dir, dirs_exist_ok=True)
print("Copied libraries, wait...")

time.sleep(2)

# Now copy scripts
print("Please ensure that the switch on the pico is off then press any key...")
msvcrt.getch()
shutil.copytree("scripts", check_rpi_rp2("CIRCUITPY", True), dirs_exist_ok=True)
print("Copied scripts")

# Ejecting drive
drive = check_rpi_rp2("CIRCUITPY", False)

if drive:
    subprocess.run([
        "powershell", "-NoProfile", "-Command",
        f'$s=New-Object -ComObject Shell.Application; $s.Namespace(17).ParseName("{drive}").InvokeVerb("Eject")'
    ], check=False)
    print("Eject command sent")
    print("Please check if device is actualy ejected and press any key...\n")
    msvcrt.getch()
else:
    print("Drive not found")


# Exiting

response1 = input("Do you want to open a converter website (y/n): ").strip().lower()
response2 = input("Do you want to open the official documentation (y/n): ").strip().lower()

if response1 in ("y", "yes"):
    webbrowser.open("https://ddconverter.github.io/")

if response2 in ("y", "yes"):
    webbrowser.open("https://simplehost.onrender.com/notakeyboard/")

if response1 in ("n", "no") and response2 in ("n", "no"):
    print("Press any key to exit...")
    msvcrt.getch()
    exit()



