import time
from pynput import mouse
control_mouse = mouse.Controller()
time.sleep(5)
print(control_mouse.position)



# control_mouse.position = (1462, 508)
# control_mouse.press(mouse.Button.left)
# control_mouse.release(mouse.Button.left)

