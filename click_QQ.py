import time
import win32gui

def click_QQ():
    def get_window_pos(name):
        name = name
        handle = win32gui.FindWindow(0, name)
        # 获取窗口句柄
        if handle == 0:
            return None
        else:
            return win32gui.GetWindowRect(handle), handle

    from PIL import Image, ImageGrab
    (x1, y1, x2, y2), handle = get_window_pos('英雄联盟登录程序')

    win32gui.SetForegroundWindow(handle)
    time.sleep(1)
    img_ready = ImageGrab.grab((x1, y1, x2, y2))
    img_ready.save('./obj.png')

    from pynput.mouse import Button, Controller
    mouse = Controller()
    mouse.position = (x2 - 200, y2 - 450)  # 登录选项

    print('当前鼠标的位置 {0}'.format(mouse.position))

    mouse.press(Button.left)  # 按下左键 （参数为Button）
    mouse.release(Button.left)



if __name__ == '__main__':
    click_QQ()
