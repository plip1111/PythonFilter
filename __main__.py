import imp
import logging
import threading
import time
import cv2 
import numpy as np
import matplotlib.pyplot as plt
from random import randint

def apply_filter(xstart,xend,ystart,yend,rgb,img):
    for i in range(xstart,xend):
        for j in range(ystart,yend):
            pass
            apply_color(rgb, img, i, j)

def apply_color(rgb, img, i, j):
    r,g,b = img[i,j]
    if rgb == 1:
        img[i,j]=[add_100(r),g,b]
        return
    if rgb == 2:
         img[i,j]=[r,add_100(g),b]
         return
    if rgb == 3:
         img[i,j]=[r,g,add_100(b)]
         return

def add_100(num):
    if num <=155:
        return num+100
    else:
        return 255

# hsv farbraum
if __name__ == "__main__":
    img = cv2.imread("C:/ws_intern/src/PythonFilter/Sea-Turtle-PNG-Clipart.png")

    rows, cols ,_= img.shape
    size = 3

    threads = []
    print(f"size of picture : {rows} x {cols}")
    for x in range(size):
        for y in range(size):    
            xstart = int(rows/size*x)
            xend = int(rows/size*(x+1))
            ystart = int(cols/size*y)
            yend = int(cols/size*(y+1))
            print(f"start = {xstart}, end = {xend}, ystart = {ystart}, yend = {yend}")
            threads.append(threading.Thread(target=apply_filter, args=(xstart,xend,ystart,yend,randint(1,3),img)))

    for thread in threads:
        print(f"Thread {thread} started")
        thread.start()

    for thread in threads:
        thread.join() 
        print(f"Thread {thread} finished")
        
    cv2.imwrite("C:/ws_intern/src/PythonFilter/output.png", img)
    
    cv2.namedWindow("input", cv2.WINDOW_NORMAL)

    cv2.imshow("input", img)
    cv2.waitKey(0)
    logging.info("Main    : all done")