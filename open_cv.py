import cv2
import numpy as np
"""
函数详解：
addWeighted(InputArray_src1, 
            double_alpha, 
            InputArray_src2, 
            double_beta, 
            double_gamma, 
            OutputArray_dst, 
            int_dtype=-1
            );


一共有七个参数：前4个是两张要合成的图片及它们所占比例，
                            第5个double gamma起微调作用，
                            第6个OutputArray dst是合成后的图片，
                            第7个输出的图片的类型（可选参数，默认-1）
"""


def contrast_img1(img1, c, b):  # 亮度就是每个像素所有通道都加上b
    rows, cols, channels = img1.shape
    img = cv2.imread(r"./a.jpg", cv2.IMREAD_COLOR)
    # 新建全零(黑色)图片数组:np.zeros(img1.shape, dtype=uint8)
    blank = np.zeros([rows, cols, channels], img1.dtype)
    dst = cv2.addWeighted(img1, c, blank, 1 - c, b)
    cv2.imwrite("./b.jpg",dst)

if __name__ == '__main__':
    img = cv2.imread(r"./a.jpg", cv2.IMREAD_COLOR)
    contrast_img1(img, 1.3, 100)




