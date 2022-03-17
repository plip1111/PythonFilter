import logging
import threading
import time
import cv2 
import numpy as np
import matplotlib.pyplot as plt


def thread_function(name, age):
    logging.info("Thread %s: starting", name)
    time.sleep(age)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    img = cv2.imread("C:/ws_intern/src/PythonFilter/Sea-Turtle-PNG-Clipart.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Fixes color read issue

    av3 = cv2.blur(img,(3,3))
    av5 = cv2.blur(img,(5,5))
    # Plot the image. This code is excluded for the rest of the article.
    plt.gcf().set_size_inches(25,25)
    plt.subplot(131),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(132),plt.imshow(av3),plt.title('Averaging - 3x3')
    plt.xticks([]), plt.yticks([])
    plt.subplot(133),plt.imshow(av5),plt.title('Averaging - 5x5')
    plt.xticks([]), plt.yticks([])
    plt.show()

    cv2.imwrite("C:/ws_intern/src/PythonFilter/output.png", img)
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,2,))
    y = threading.Thread(target=thread_function, args=(2,4,))
    logging.info("Main    : before running thread")
    x.start()
    y.start()
    logging.info("Main    : wait for the thread to finish")
    y.join()
    x.join()
    logging.info("Main    : all done")