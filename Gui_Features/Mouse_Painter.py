
"""
Gui Features in OpenCV
Learn to handle mouse events in OpenCV
learn functions : cv2.setMouseCallback()
cv2.getTrackbarPos();    cv2.createTrackbar()

we create a simple application which draws a circle on an image  wherever we double-click on it.
"""

import cv2
import numpy as np

img = []
drawing = False # true if mouse is pressed
mode = True  # if True, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1


def Events_list():
    """
    列出所有可用的可用事件
    :return:
    """
    events = [i for i in dir(cv2) if 'EVENT' in i]
    print("events["+str(len(events))+"]:", events)


def draw_circle(event, x, y, flags, param):
    """
    创建鼠标回调函数
    :param event:
    :param x:
    :param y:
    :param flags:
    :param param:
    :return:
    """
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 50, (255, 0, 0), -1)


def draw_dragging(event, x, y, flags, param):
    """
    通过拖动鼠标实现画画，
    这个例子帮助创建和理解一些互动的应用，
    比如目标追踪，图像分割etc.
    :param event:
    :param x:
    :param y:
    :param flags:
    :param param:
    :return:
    """
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    if event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y),(0, 255, 0), -1)
            else:
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)


def Creat_image(Callback):
    """
    创建一个黑色图片，一个窗口并绑定鼠标回调函数到窗口
    :param Callback    鼠标回调函数
    :return:
    """
    global img, mode

    img = np.zeros((512, 512, 3), np.uint8)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', Callback)   # 绑定回调函数

    while(True):
        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('m'):
            mode = not mode
        elif k == ord('q'):
            break

    cv2.destroyAllWindows()


def nothing(x):
    pass


def Trackbar_Color_Palette():
    """
    学习绑定一个追踪条到OpenCV窗口
    Learn to bind trackbar to OpenCV windows
    You will learn these functions : cv2.getTrackbarPos(), cv2.createTrackbar() etc.
    :return:
    """
    # Create a black image, a window， 三维数组为0
    img = np.zeros((300, 512, 3), np.uint8)
    cv2.namedWindow('image')

    # create trackbars for color change
    cv2.createTrackbar('R', 'image', 0, 255, nothing)
    cv2.createTrackbar('G', 'image', 0, 255, nothing)
    cv2.createTrackbar('B', 'image', 0, 255, nothing)

    # create switch for ON/OFF functionality
    switch = '0:OFF  1:ON'
    cv2.createTrackbar(switch, 'image', 0, 1, nothing)

    while(True):
        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            break;

        # get current positons of four trackbars
        r = cv2.getTrackbarPos('R', 'image')
        g = cv2.getTrackbarPos('G', 'image')
        b = cv2.getTrackbarPos('B', 'image')
        s = cv2.getTrackbarPos(switch, 'image')

        if s == 0:
            img[:] = 0
        else:
            img[:] = [b, g, r]

    cv2.destroyAllWindows()


if __name__ == '__main__':
    # Creat_image(draw_dragging)
    Trackbar_Color_Palette()