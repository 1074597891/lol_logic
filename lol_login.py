import time
import win32api
import win32con
import win32gui
import match_QQlogin
import ScreenCapture

LOL = "D:\\英雄联盟\\TCLS\\Client.exe"
win32api.ShellExecute(0, 'open', LOL, '', '', 1)

ScreenCapture.ScreenCapture()

match_QQlogin.match("./client_src.png", "./client_obj.png")



# keyboard.press('z')
# keyboard.release('z')
#
# keyboard.press('y')
# keyboard.release('y')
#
# keyboard.press('x')
# keyboard.release('x')
#
# keyboard.press('1')
# keyboard.release('1')
#
# keyboard.press('0')
# keyboard.release('0')
#
# keyboard.press('7')
# keyboard.release('7')
#
# keyboard.press('4')
# keyboard.release('4')
#
# keyboard.press('5')
# keyboard.release('5')
#
# keyboard.press('9')
# keyboard.release('9')
#
# keyboard.press('7')
# keyboard.release('7')
#
# keyboard.press('8')
# keyboard.release('8')
#
# keyboard.press('9')
# keyboard.release('9')
#
# keyboard.press('1')
# keyboard.release('1')




