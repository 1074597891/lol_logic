import time

import win32con
import win32gui


def ScreenCapture():
    def get_window_pos(name):
        name = name
        handle = win32gui.FindWindow(0, name)
        # 获取窗口句柄
        if handle == 0:
            time.sleep(2)
            print("未找到英雄联盟")
            while 1:
                name = name
                handle = win32gui.FindWindow(0, name)
                if handle == 0:
                    time.sleep(2)
                    print("未找到英雄联盟")
                else:
                    break
            time.sleep(2)
            return win32gui.GetWindowRect(handle), handle

        else:
            # 返回坐标值和handle
            return win32gui.GetWindowRect(handle), handle

    (x1, y1, x2, y2), handle = get_window_pos('英雄联盟登录程序')

    win32gui.ShowWindow(handle, win32con.SW_RESTORE)
    # 设置为当前活动窗口
    win32gui.SetForegroundWindow(handle)
    time.sleep(1)
    from PIL import ImageGrab

    img_ready = ImageGrab.grab((x1, y1, x2, y2))
    img_ready.save('client_src.png')
    return x1, y1, x2, y2
    # 截图


if __name__ == '__main__':
    ScreenCapture()
