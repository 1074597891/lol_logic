import time

import aircv as ac
import cv2
import win32api
from pynput import mouse

import match_QQlogin
import ScreenCapture

LOL = "D:\\游戏\\英雄联盟\\TCLS\\Client.exe"
win32api.ShellExecute(0, 'open', LOL, '', '', 1)
while 1:
    IMSRC = "./client_src.png"
    IMOBJ = "./client_obj.png"
    imsrc = cv2.imread(IMSRC)
    imobj = cv2.imread(IMOBJ)
    qq_src = cv2.imread("./src.png")
    ScreenCapture.ScreenCapture()
    time.sleep(1)
    print(ac.find_template(imsrc, imobj, 0.99))
    print(ac.find_template(imsrc, qq_src, 0.9))
    if (ac.find_template(imsrc, imobj, 0.99) and ac.find_template(imsrc, qq_src, 0.9)) is None:
        print("最终没能匹配到：" + IMSRC)
        continue
    else:
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
        qq_y = pos_y + 300
        control_mouse.position = (pos_x, qq_y)
        control_mouse.press(mouse.Button.left)
        control_mouse.release(mouse.Button.left)
        time.sleep(1)
        identify_y = pos_y + 250
        control_mouse.position = (pos_x, identify_y)
        control_mouse.press(mouse.Button.left)
        control_mouse.release(mouse.Button.left)
        time.sleep(2)

        if ac.find_template(imsrc, cv2.imread("./select_region.png"), 0.9) is None:
            ScreenCapture.ScreenCapture()
            time.sleep(2)
            if ac.find_template(imsrc, cv2.imread("./select_region.png"), 0.9):
                Select_region_y = pos_y + 250 + 270
                Select_region_x = pos_x - 230
                control_mouse.position = (Select_region_x, Select_region_y)
                control_mouse.press(mouse.Button.left)
                control_mouse.release(mouse.Button.left)
            else:
                print("未加载出界面，等待5s")
                time.sleep(5)
                Select_region_y = pos_y + 250 + 70
                Select_region_x = pos_x - 230
                print(Select_region_x, Select_region_y)
                control_mouse.position = (Select_region_x, Select_region_y)
                control_mouse.press(mouse.Button.left)
                control_mouse.release(mouse.Button.left)

        break
