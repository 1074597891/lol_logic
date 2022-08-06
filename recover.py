import  win32con, win32gui


def recover():
    def get_window_pos(name):
        name = name
        handle = win32gui.FindWindow(0, name)
        # 获取窗口句柄
        if handle == 0:
            return None
        else:
            return win32gui.GetWindowRect(handle), handle

    (x1, y1, x2, y2), handle = get_window_pos('league of legends')
    win32gui.ShowWindow(handle, win32con.SW_RESTORE)

if __name__ == '__main__':
    recover()