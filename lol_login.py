import win32api
import time
from pynput import mouse
from pynput import keyboard

import match_QQlogin
import ScreenCapture

LOL = "D:\\游戏\\英雄联盟\\TCLS\\Client.exe"
win32api.ShellExecute(0, 'open', LOL, '', '', 1)

ScreenCapture.ScreenCapture()
if match_QQlogin.match("./client_obj.png", "./client_src.png") == 0:
    while 1:
        if match_QQlogin.match("./client_obj.png", "./client_src.png"):
            break

(x1, y1, x2, y2) = ScreenCapture.ScreenCapture()
(x1_match, y1_match) = match_QQlogin.match("./client_src.png", "./src.png")

control_mouse = mouse.Controller()
time.sleep(1)
pos_x = x1 + x1_match
pos_y = y1 + y1_match
print(pos_x, pos_y)
control_mouse.position = (pos_x, pos_y)
control_mouse.press(mouse.Button.left)
control_mouse.release(mouse.Button.left)
time.sleep(1)
mm_y = pos_y + 50

control_mouse.position = (pos_x, mm_y)
control_mouse.press(mouse.Button.left)
control_mouse.release(mouse.Button.left)

time.sleep(1)

control_keyboard = keyboard.Controller()


