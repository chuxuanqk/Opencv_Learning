"""
Basic Operations on Images
Goal
* Access pixel values and modify them
* Access image properties（访问图片的信息）
* Setting Region of Image(ROI)
* Splitting and Merging images

Almost all the operations in this section is mainly related to Numpy rather than OpenCV.
A good knowledge of Numpy is required to write better optimized code with OpenCV.
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img_path = 'messi4.jpg'
img = cv2.imread(img_path)


src = 0
dst = 0

def EVENT_LBUTTONDOWN(event, x, y, flags, param):
    """
    鼠标移动回调函数， 实现移动鼠标获取当前坐标
    :param event:
    :param x:
    :param y:
    :param flags:
    :param param:
    :return:
    """
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d, %d"%(x, y)
        print("xy: ", xy)


def Accessing_Modifying_pixel(img):
    """
    访问和修改像素点
    You can access a pixel value by its row and column coordinates.
    For BGR image, it returns an array of Blue, Green, Red values.
    For grayscale image, just corresponding intensity is returned.
    :param img:
    :return:
    """
    img_copy = img
    px = img[100, 100]
    print("px: ", px)

    # accessing only blue pixel
    blue = img[100, 100, 0]
    print("blue: ", blue)

    # modify the pixel values
    img[100, 100] = [255, 255, 255]
    print("img[100, 100]: ", img[100, 100])

    # Better pixel accessing and editing method
    item = img_copy.item(10, 10, 2)
    print("item: ", item)

    # modifying RED value
    img_copy.itemset((10, 10, 2), 100)
    item_change = img_copy.item(10, 10, 2)
    print("item_charge: ", item_change)


def Accessing_Image_Properties(img):
    """
    访问图片的基本信息, shape, size, dtype
    :param img:
    :return:
    """
    shape = img.shape
    print("shape: ", shape)
    # Total number of pixels is accessed by img.size
    size = img.size
    print("Total number of pixels: ", size)
    dtype = img.dtype
    print("dtype: ", dtype)


def show_img(img):
    """
    显示图片
    :param img:
    :return:
    """
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', EVENT_LBUTTONDOWN)     # 回调绑定窗口

    while(True):
        cv2.imshow('image', img)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

    cv2.destroyAllWindows()


def Image_ROI(img):
    """
    选择感兴趣的区域
    Sometimes, you will have to play with certain region of images.
    For eye detection in images, first perform face detection over the image until the face is found,
    then search within the face region for eyes.
    This approach improves accuracy (because eyes are always on faces :D )
    and performance (because we search for a small area).
    :param img:
    :return:
    """
    print("img_shape: ", img.shape)
    show_img(img)
    ball = img[290:340, 330:400]
    img[283:333, 120:190] = ball
    show_img(img)


def Splitting_Merging_Image_Channels(img):
    """
    分割或合并图片通道
    :param img:
    :return:
    """
    b, g, r = cv2.split(img)
    show_img(b)
    img_new = cv2.merge((b, g, r))
    show_img(img_new)
    # make all the red pixels to zero
    img_new[:, :, 2] = 0
    show_img(img_new)


def Making_Borders_Images():
    """
    create a bodrer around the image, something like a photo frame
    cv2.copyMakeBorder(), more applications for convolution operation, zero padding.
    :param img:
    :return:
    """
    BLUE = [255, 0, 0]
    img1 = cv2.imread('opencv.jpg')

    replicate = cv2.copyMakeBorder(img1, 10, 10, 10 , 10, cv2.BORDER_REPLICATE)
    reflect = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT)
    reflect101 = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT101)
    wrap = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_WRAP)
    constant = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)

    plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
    plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
    plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
    plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT101')
    plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
    plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

    plt.show()


# if __name__ == '__main__':
#     Accessing_Image_Properties(img)
