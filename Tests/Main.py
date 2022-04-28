import tkinter as tk
import cv2
from PIL import Image, ImageTk
import Filter


# Initialize Window

filter = Filter.Filter(False,0)
root = tk.Tk()
root.wm_title("Filter App")
root.config(background="#000000")
canvas = tk.Canvas(root, width=600, height=700)
canvas.pack()
canvas.grid(row=0, column=0, padx=5, pady=20)

lmain = tk.Label(canvas)
lmain.grid(row=0, column=0, padx=85, pady=119)
cap = cv2.VideoCapture(0)

def get_cam_frame(cam):
    ret, img = cam.read()
    return img

def filterRed():
    filter.doFilter = True
    filter.color = 1

def filterGreen():
    filter.doFilter = True
    filter.color = 2

def filterBlue():
    filter.doFilter = True
    filter.color = 3

def filterParRed():
    filter.doFilter = True
    filter.color = 6

def filterParGreen():
    filter.doFilter = True
    filter.color = 5

def filterParBlue():
    filter.doFilter = True
    filter.color = 4

def filterParRand():
    filter.doFilter = True
    filter.color = 7

def filterFalse():
    filter.doFilter = False

def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if(filter.doFilter):  
        frame = Filter.filter(frame,filter.color)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

sliderFrame = tk.Frame(root, width=500, height=50)
sliderFrame.grid(row = 500, column=0, padx=10, pady=2)
show_frame()

filterbtn = tk.Button(root, width=30, height=30, command=filterRed, text = "Rot", bg = "red")
filterbtn_window = canvas.create_window(100,150,width=100, height=30, anchor='nw', window=filterbtn)

filterbtn = tk.Button(root, width=30, height=30, command=filterGreen, text = "Grün", bg = "green")
filterbtn_window = canvas.create_window(100,200,width=100, height=30, anchor='nw', window=filterbtn)

filterbtn = tk.Button(root, width=30, height=30, command=filterBlue, text = "Blau", bg = "blue")
filterbtn_window = canvas.create_window(100,250,width=100, height=30, anchor='nw', window=filterbtn)

filterbtn = tk.Button(root, width=30, height=30, command=filterParRed, text = "Rot Parallel", bg = "red")
filterbtn_window = canvas.create_window(100,300,width=100, height=30, anchor='nw', window=filterbtn)

filterbtn = tk.Button(root, width=30, height=30, command=filterParGreen, text = "Grün Parallel", bg = "green")
filterbtn_window = canvas.create_window(100,350,width=100, height=30, anchor='nw', window=filterbtn)

filterbtn = tk.Button(root, width=30, height=30, command=filterParBlue, text = "Blau Parallel", bg = "blue")
filterbtn_window = canvas.create_window(100,400,width=100, height=30, anchor='nw', window=filterbtn)

filterbtn = tk.Button(root, width=30, height=30, command=filterParRand, text = "Zufällige Farbe", bg = "pink")
filterbtn_window = canvas.create_window(100,450,width=100, height=30, anchor='nw', window=filterbtn)

filterbtn = tk.Button(root, width=30, height=30, command=filterFalse, text = "Filter aus", bg = "grey")
filterbtn_window = canvas.create_window(100,500,width=100, height=30, anchor='nw', window=filterbtn)

quit_button = tk.Button(root, text = "X", command = root.quit, anchor = 'w',
                    width = 2, bg="red")
quit_button_window = canvas.create_window(680,120, anchor='nw', window=quit_button)



root.mainloop()