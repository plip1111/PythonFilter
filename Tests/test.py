from threading import Thread
import tkinter as tk
import cv2
from PIL import Image, ImageTk
from matplotlib.pyplot import show
import Filter


# Initialize Window

filter = Filter.Filter(False)
root = tk.Tk()
root.wm_title("Filter App")
root.config(background="#000000")
canvas = tk.Canvas(root, width=600, height=700)
canvas.pack()
canvas.grid(row=0, column=0, padx=5, pady=20)

lmain = tk.Label(canvas)
lmain.grid(row=0, column=0, padx=85, pady=119)
cap = cv2.VideoCapture(0)
doFilter = True

def get_cam_frame(cam):
    ret, img = cam.read()
    # smaller frame size - things run a lot smoother than a full screen img
    # img = cv2.resize(img, (800, 470))
    return img

def filterTrue():
    filter.doFilter = True

def filterFalse():
    filter.doFilter = False

def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if(filter.doFilter):  
        frame = Filter.filter(frame)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

sliderFrame = tk.Frame(root, width=500, height=50)
sliderFrame.grid(row = 500, column=0, padx=10, pady=2)
show_frame()

filterbtn = tk.Button(root, width=30, height=30, command=filterTrue, text = "filter on", bg = "green")
filterbtn_window = canvas.create_window(100,150,width=100, height=30, anchor='nw', window=filterbtn)

filterbtn = tk.Button(root, width=30, height=30, command=filterFalse, text = "filter off", bg = "red")
filterbtn_window = canvas.create_window(100,200,width=100, height=30, anchor='nw', window=filterbtn)

quit_button = tk.Button(root, text = "X", command = root.quit, anchor = 'w',
                    width = 2, bg="red")
quit_button_window = canvas.create_window(680,120, anchor='nw', window=quit_button)



root.mainloop()