"""
Goal
* To measure the performance of your code.
* Some tips to improve the performance of your code.
* You will see these fuctions: cv2.getTickCount, cv2.getTickFrequency etc.
* python module  time and profile.
"""
import cv2
import numpy as np
from Basic_Operations_on_Images import show_img

img1= cv2.imread('messi4.jpg')


def Measuring_Performance(img):
    """
    cv2.getTickCount,
    cv2.getTickFrequency
    使用OpenCV检测性能
    :param img:
    :return:
    """
    newimg = np.array(img)
    e1 = cv2.getTickCount()

    for i in range(3, 50, 2):
        # 中值滤波将图像的每个像素用邻域
        # (以当前像素为中心的正方形区域)像素的中值代替
        img1 = cv2.medianBlur(newimg, i)

    e2 = cv2.getTickCount()
    t = (e2 - e1)/cv2.getTickFrequency()
    print("t: ", t)

    # cv2.namedWindow("img")
    # cv2.imshow("img", img)
    show_img(newimg)


if __name__ == '__main__':
    # Measuring_Performance(img1)
    print(cv2.useOptimized())




