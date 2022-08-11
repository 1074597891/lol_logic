# Python图片识别找坐标（appium通过识别图片点击坐标）
# 如果只想了解图片相似度识别，直接看第一步即可
# 如果想了解appium根据图片识别点击坐标，需要看第一、二、三步
# 自定义的UI控件，appium识别不到。所以考虑通过识别图片找坐标，进而通过点击坐标解决问题

# confidence：匹配相似率
# rectangle：匹配图片在原始图像上四边形的坐标
# result：匹配图片在原始图片上的中心坐标点，也就是我们要找的点击点
import os
import time

import aircv as ac
import cv2
import pyautogui


def match(IMSRC, IMOBJ):
    # 匹配图标位置
    imsrc = cv2.imread(IMSRC)
    imobj = cv2.imread(IMOBJ)
    pos = ac.find_template(imsrc, imobj, 0.7)
    if pos == None:
        print("最终没能匹配到：" + imsrc)
    else:
        try:
            show_and_save(IMSRC, pos)
        except Exception as e:
            print("保存匹配结果show_and_save这里出错，错误原因为{}".format(e))
        print(pos)
        point = pos['result']
        pyautogui.moveTo(point)
        print("匹配成功：{}".format(IMSRC))
        time.sleep(0.5)
        return (point)


def show_and_save(imgPath, pos):
    print("Img:", imgPath)
    img = cv2.imread(imgPath)
    # 画矩形
    cv2.rectangle(img, pos['rectangle'][0], pos['rectangle'][3], (0, 0, 255), 2)  # 红
    # 画中心点
    cv2.circle(img, tuple(map(int, pos['result'])), 3, (255, 0, 0), -1)  # -1表示填充

    time_now = time.strftime('%Y-%m-%d--%H-%M-%S', time.localtime(time.time()))
    imgpath = os.getcwd()
    save_jpg = imgpath + "\\" + time_now + '.jpg'
    print("path:", save_jpg)
    cv2.imwrite(save_jpg, img)


if __name__ == '__main__':
    match("./client_obj.png", "./client_src.png")
