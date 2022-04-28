from random import randint
import cv2
import threading

class Filter():
    def __init__(self, doFilter, color):
        self.doFilter = doFilter
        self.color = color
        
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
    elif(color==4):
        filter_parallel(img,1)
        return img
    elif(color==5):
        filter_parallel(img,2)
        return img
    elif(color==6):
        filter_parallel(img,3)
        return img
    elif(color==7):
        filter_parallel(img,4)
        return img
    else:
        return img
    img = cv2.bitwise_and(img,filtercolor)

    return img

def filter_parallel(img,color):
    rows, cols ,_= img.shape
    size = 3
    threads = []
    initialcolor = color
    for x in range(size):
        for y in range(size):    
            if(initialcolor == 4):
                color = randint(1,3)
            xstart = int(rows/size*x)
            xend = int(rows/size*(x+1))
            ystart = int(cols/size*y)
            yend = int(cols/size*(y+1))
            threads.append(threading.Thread(target=apply_filter, args=(xstart,xend,ystart,yend,color,img)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join() 
    return img

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

