import win32con
import win32gui


def get_window_pos(name):
    name = name
    handle = win32gui.FindWindow(0, name)
    # 获取窗口句柄
    if handle == 0:
        return None
    else:
        # 返回坐标值和handle
        return win32gui.GetWindowRect(handle), handle


(x1, y1, x2, y2), handle = get_window_pos('英雄联盟登录程序')
win32gui.ShowWindow(handle, win32con.SW_RESTORE)
# 设置为当前活动窗口
win32gui.SetForegroundWindow(handle)

from PIL import Image, ImageGrab

img_ready = ImageGrab.grab((x1, y1, x2, y2))
# 截图
img_ready.save('client_src.png')
win32gui.ShowWindow(handle, win32con.SW_HIDE)
