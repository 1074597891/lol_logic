import time
import keyboard
from pynput import mouse


time.sleep(5)
control_mouse = mouse.Controller()
control_mouse.position = (1462, 508)
control_mouse.press(mouse.Button.left)
control_mouse.release(mouse.Button.left)

time.sleep(5)
keyboard.press_and_release("y")
time.sleep(5)
keyboard.press_and_release("t")
time.sleep(5)
keyboard.press_and_release("enter")