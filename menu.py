from tkinter import Tk, BOTH
from tkinter.ttk import *
from tkinter import Button,RIGHT,Listbox
import threading
import subprocess
import os
global a
a=0

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Giam sat an ninh")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)
        label = Label(self, text=" Menu ")
        label.pack(pady=25)
        button1 = Button(self, text="Train", command=self.train,width=15)
        button2 = Button(self, text="Start camera",command=self.statcamera,width=15)
        button3 = Button(self, text="Add face",command=self.addface,width=15)
        button4 = Button(self, text="Camera History",command=self.camerahistory,width=15)
        button5 = Button(self, text="Close", command=self.tl_close,width=15)
        button1.pack(pady=3)
        button2.pack(pady=3)
        button3.pack(pady=3)
        button4.pack(pady=3)
        button5.pack(pady=3)

    def train(self):
        tr = Train()
        tr.start()

    def statcamera(self):
        tr = StartCamera()
        tr.start()

    def addface(self):
        tr = AddFace()
        tr.start()

    def camerahistory(self):
        tr = cameraHistory()
        tr.start()

    def tl_close(self):
        exit = thietlap_exit()
        exit.start()
        os._exit(0)

class Train(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self._stop = threading.Event()

    def run(self):
        global p
        global a
        if a == 1:
            p.kill()
        a=1
        p = subprocess.Popen('python train.py')
class StartCamera(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self._stop = threading.Event()

    def run(self):
        global p
        global a
        if a == 1:
            p.kill()
        a=1
        p = subprocess.Popen('python detection.py')
class AddFace(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self._stop = threading.Event()

    def run(self):
        global p
        global a
        if a == 1:
            p.kill()
        a=1
        p = subprocess.Popen('python addface.py')
class cameraHistory(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self._stop = threading.Event()

    def run(self):
        global p
        global a
        if a == 1:
            p.kill()
        a=1
        p = subprocess.Popen('python camerahistory.py')
class thietlap_exit(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self._stop = threading.Event()

    def run(self):
        global p
        global a
        if a == 1:
            p.kill()

root = Tk()
root.geometry("200x300")
app = Example(root)
root.mainloop()