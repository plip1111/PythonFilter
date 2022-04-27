import threading
from unittest import skip
import cv2
import numpy as np


class Filter():
    def __init__(self, doFilter):
        self.doFilter = doFilter


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


def filter(img):
    
    rows, cols ,_= img.shape
    sizex = 2
    sizey = 2
    for x in range(sizex):
        for y in range(sizey):    
            xstart = int(rows/sizex*x)
            xend = int(rows/sizex*(x+1))
            ystart = int(cols/sizey*y)
            yend = int(cols/sizey*(y+1))
            color=2*x+y
            # if(color == 1):
            #     filtercolor = cv2.imread('C:\ws_intern\src\PythonFilter\Tests\img\red.png')
            #     filtercolor = cv2.resize(filtercolor, (cols, rows))
            # if(color == 2):
            #     filtercolor = cv2.imread('C:\ws_intern\src\PythonFilter\Tests\img\green.png')
            #     filtercolor = cv2.resize(filtercolor, (cols, rows))
            # if(color == 3):
            filtercolor = cv2.imread("Tests\img\red.png", cv2.IMREAD_UNCHANGED)
            filtercolor = cv2.resize(filtercolor, (cols, rows))
            # else : 
            #     continue
            ones = np.ones((rows,cols), dtype="uint8")
            zeros = np.zeros((rows,cols), dtype="uint8")
            cv2.rectangle(zeros, (xstart, ystart), (xend, yend), 255, -1)
            
            copy = cv2.bitwise_and(img,filtercolor,mask=zeros)
            copy[np.where((copy==[0,0,0]).all(axis=2))] = [255,255,255]
            img = cv2.bitwise_and(img, copy,mask=ones)

    return img
