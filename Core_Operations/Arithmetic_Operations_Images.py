"""
Goal
*  Learn several arithmetic operations on images like addition, subtraction, bitwise operations etc.
*  You will learn these functions:cv2.add(), cv2.addWeighted()etc.
*  bitwise AND, OR, NOT and XOR operations.

"""
import cv2
from Basic_Operations_on_Images import show_img

ml = 'ml.jpg'
opencv = './opencv.jpg'
messi = 'messi4.jpg'

img1 = cv2.imread(ml)
img2 = cv2.imread(opencv)
img3 = cv2.imread(messi)


def Blending_Image(img1, img2):
    """
    Both images should be of same depth and type,
    or second image can just be a scalar value
    :param img1:
    :param img2:
    :return:
    """
    h, w, c = img1.shape
    #  改变img2的大小，使得其和img1 same size
    img2 = cv2.resize(img2, (w, h), interpolation=cv2.INTER_CUBIC)
    dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

    cv2.imshow('dst', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def Bitwise_Operations(img1, img2):
    """
    This includes bitwise AND, OR, NOT and XOR operations.
    They will be highly useful while extracting any part of the image,
    defining and working with non-rectangular ROI etc.
    定义和使用非矩形ROI
    :return:
    """
    # create a ROI
    rows, cols, channes = img1.shape
    roi = img2[0:rows, 0:cols]

    # Now create a mask of logo and create its inverse mask also
    img1gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img1gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    # Now black-out the area of logo in ROI
    img2_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

    # Take only region of logo from logo image
    img1_fg = cv2.bitwise_and(img1, img1, mask=mask)

    # Put logo in ROI and modify the main image
    dst = cv2.add(img2_bg, img1_fg)
    img2[:rows, 0:cols] = dst

    show_img(img1_fg)
    show_img(img2_bg)
    show_img(img2)


if __name__ == '__main__':
    Bitwise_Operations(img2, img3)
