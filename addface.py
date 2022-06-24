from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import cv2
import os
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from playsound import playsound
from time import sleep
from threading import Thread
global photo
global entry


def save():
    global photo,entry
    c = 0
    a = entry.get()
    thumuc = "your_face/" + a
    print(thumuc)
    if not os.path.exists(thumuc):
        print("true")
        os.makedirs(thumuc)
    else:
        filelist = [file for file in os.listdir(thumuc) if (file.endswith('.jpg') or file.endswith('.png'))]
        c = len(filelist)
    c = c + 1
    cv2.imwrite(thumuc + "/" + str(c) + ".jpg", anh)
    playsound('thongbao.wav')

def update_frame():
    global canvas, photo,anh
    # Doc tu camera
    ret, frame = video.read()
    anh = frame
    # Chuyen he mau
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Convert hanh image TK
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    # Show
    canvas.create_image(0,0, image = photo, anchor=tkinter.NW)
    self.after(15, update_frame)
def close():
    self.quit()

self = Tk()
self.title("Add Face")
video = cv2.VideoCapture(0)
canvas_w = video.get(cv2.CAP_PROP_FRAME_WIDTH)
canvas_h = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
canvas = Canvas(self, width = canvas_w, height= canvas_h)
canvas.pack()
closeButton = Button(self, text="Close", command=close)
closeButton.pack(side=RIGHT, padx=5, pady=5)
saveButton = Button(self, text="Save", command=save)
saveButton.pack(side=RIGHT,padx=5, pady=5)
label = Label(self, text="  Name  ")
label.pack(side=LEFT, padx=5,pady=5)
entry = Entry(self)
entry.pack( side=LEFT,pady=5, padx=5)
photo = None
update_frame()
self.mainloop()