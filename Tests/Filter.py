import cv2
import numpy as np

class Filter():
    def __init__(self, doFilter, color):
        self.doFilter = doFilter
        self.color = color


def add_100(num):
    if num <=155:
        return num+100
    else:
        return 255

def apply_color(rgb, img, i, j):
    green = cv2.imread('C:\ws_intern\src\PythonFilter\Tests\img\green.png')
    r,g,b = img[i,j]
    if rgb == 2:
        img[i,j]=[add_100(r),g,b]
        return
    if rgb == 1:
        img = img + green
        return
    if rgb == 0:
        img[i,j]=[r,g,add_100(b)]
        return


def filter(img,color):
    rows, cols ,_= img.shape
    if(color == 1):
        filtercolor = cv2.imread("Tests/img/red.png")
        filtercolor = cv2.resize(filtercolor, [cols, rows])
    elif(color == 2):
        filtercolor = cv2.imread("Tests/img/green.png")
        filtercolor = cv2.resize(filtercolor, [cols, rows])
    elif(color == 3):
        filtercolor = cv2.imread("Tests/img/blue.png")
        filtercolor = cv2.resize(filtercolor, [cols, rows])
    else:
        return img
    img = cv2.bitwise_and(img,filtercolor)

    return img
