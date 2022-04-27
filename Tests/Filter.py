import cv2

class Filter():
    def __init__(self, doFilter, color):
        self.doFilter = doFilter
        self.color = color


def add_100(num):
    if num <=155:
        return num+100
    else:
        return 255

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
