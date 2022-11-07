
import cv2

img = cv2.imread("D:\\pc_to_pc\\my_python_project\\lol_autologic\\image\\qq_statue.png")


def click_info(event, x, y, flags, param):
    # 只处理双击事件
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print('坐标', x, y)
        b, g, r = img[y, x]     # 获取b, g, r
        print("像素点的bgr值", r, b, g)

cv2.namedWindow('image')
cv2.setMouseCallback('image',  click_info)

while True:
    cv2.imshow("image", img)
    # 点击 esc键
    if cv2.waitKey(20) & 0xFF ==27:
        break

cv2.destroyAllWindows()
