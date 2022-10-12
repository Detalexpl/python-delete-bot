from pynput.keyboard import Key, Controller
import time
keyboard = Controller()


time.sleep(10)
while True:
    time.sleep(0.001)
    keyboard.press(Key.delete)
    keyboard.pressed(Key.delete)