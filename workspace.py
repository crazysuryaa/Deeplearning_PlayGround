import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import tkinter as tk
from tkinter import *
from datetime import datetime
import random
import re
from tkinter import messagebox
from tkinter.font import Font
from tkinter import font  as tkfont  # python 3
from tkinter import filedialog
import textwrap
from random import choice
from PIL import Image, ImageTk, ImageSequence
from itertools import count
from contextlib import redirect_stdout
import tkinter
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from numpy import expand_dims

# In[2]:


import tensorflow.keras as keras
import tensorflow as tf
from tensorflow.keras.layers import *
from tensorflow.keras.utils import plot_model
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import *
from text_editor import  Editor
# In[ ]:


# In[ ]:


# In[3]:


client = wolframalpha.Client('QAEXLK-RY9HY2PHAT')
import pyttsx3

engine = pyttsx3.init()
# engine.say("In supervised machine learning, a crazy man just runs away what is deep learning")
engine.setProperty('volume', 1)
engine.setProperty('rate', 170)
engine.setProperty('voice', 'english+f4')
# engine.setProperty('voice', voices[1].id)
engine.runAndWait()

# In[4]:


name = "crazy"

questions = []
file1 = open('/mnt/DATA/UI/questions.txt', 'r')
Lines = file1.readlines()
count = 0
for line in Lines:
    #     print(line)
    questions.append(line[:-1])

answers = []
file1 = open('/mnt/DATA/UI/answers.txt', 'r')
Lines = file1.readlines()
count = 0
for line in Lines:
    answers.append(line[:-1])

weblinks = []
file1 = open('/mnt/DATA/UI/weblinks.txt', 'r')
Lines = file1.readlines()
count = 0
for line in Lines:
    weblinks.append(line[:-1])

# In[5]:


layerdic = [{"name": None, "args": [], "defs": []} for i in range(20)]
layernames = [None] * 20

folderpath = "/mnt/DATA/UI/layers/"
for i, layer in enumerate(os.listdir(folderpath)):
    layernames[i] = layer[:-4]
    layerpath = folderpath + layer
    file1 = open(layerpath, 'r')
    Lines = file1.readlines()

    for ind, line in enumerate(Lines[:-2]):
        if ind == 0:
            layerdic[i]["name"] = line[:-2]
        else:
            k = 0
            m = 0
            for ind, char in enumerate(line[:-2]):
                if char == "=":
                    k = ind
            layerdic[i]["args"].append(line[4:k])
            layerdic[i]["defs"].append(line[k + 1:-2])

# In[6]:


import sys
#
# sys.path.insert(1, '/mnt/DATA/UI/ide/crossviper-master')
# sys.path.insert(1, '/mnt/DATA/DeeplearningUI/')
# sys.path.insert(1, '/mnt/DATA/UI/labelImgmaster')
sys.path.insert(1, '/mnt/DATA/UI/ide/crossviper-master')
sys.path.insert(1, '/mnt/DATA/DeeplearningUI/')
sys.path.insert(1, '/mnt/DATA/UI/labelImgmaster')



from FlattenDialog import *
from AddDialog import *
from CodeImageDialog import *
from CompileDialog import *
from ConvDialog import *
from DenseDialog import *
from plotgraphDialog import *
from summaryDialog import *
from tokoDialog import *
from trainDialog import *
from InputDialog import *
from OutputDialog import *
from ideDialog import *
# from StartPage import *
# from Existing import *
# from NewProject import *
# from ImageClassification import *
# from ObjectDetection import *

from labelImg import main as labelmain
from reshapeimages import reshape

# In[7]:


widgetspath = '/mnt/DATA/UI/widgets/inactive/'
buttonspath = '/mnt/DATA/UI/buttons/'
bgpath = '/mnt/DATA/UI/backgrounds/'

# In[ ]:


# In[8]:


dic = [{} for i in range(20)]
graph = [[] for i in range(20)]
invgraph = [[] for i in range(20)]
nodes = []
connectionsdic = [[] for i in range(20)]


# In[9]:


def getplotimage():
    plot = ImageTk.PhotoImage(Image.open("/mnt/DATA/UI/modelplot.png"))
    return plot


open('model.py', 'w').close()
with open("model.py", "a") as myfile:
    myfile.write("import tensorflow as tf\n")
    myfile.write("import numpy as np\n")
    myfile.write(" \n")
    myfile.write("def mymodel():\n")


class Window(Frame):

    def __init__(self, buttonsbg, root, master=None):
        Frame.__init__(self, master)

        # self.traindatagen = root.traindatagen
        # self.testdatagen = root.testdatagen

        # obj = next(self.traindatagen)
        # print(obj[0], obj[1])

        self.master = master
        global layerdic, layernames, buttonspath, bgpath, widgetspath, dic, graph, invgraph, nodes, connectionsdic

        self.dic = dic
        self.graph = graph
        self.invgraph = invgraph
        self.nodes = nodes
        self.connectionsdic = connectionsdic

        self.layerdic = layerdic
        self.layernames = layernames
        self.tensorlist = []

        defaultbutton = buttonsbg[0]
        buttonsbgarray = buttonsbg[1]

        plotbg, trainbg, codebg, buildbg = buttonsbg[2]

        toko = buttonsbg[3]
        code = buttonsbg[5]
        self.plot = buttonsbg[4]
        self.t1, self.t2, self.t3, self.t4, self.t5 = buttonsbg[6]

        self._drag_data = {"x": 0, "y": 0, "item": None}
        self.currenty = 400
        self.currentx = 20
        self.ccnt = 0
        self.dcnt = 0
        self.acnt = 0
        self.icnt = 0
        self.ocnt = 0
        self.cnt = 0

        self.codelines = []
        self.invgraph = [[] for i in range(20)]
        self.graph = [[] for i in range(20)]
        self.dic = [{} for i in range(20)]
        self.coonectionsdic = [[] for i in range(20)]
        self.nodes = []

        self.nodescnt = 0
        self.objectscnt = 0
        self.pathscnt = 0
        self.path = []
        self.buttonsarray = []

        self.plottry = ImageTk.PhotoImage(Image.open("/mnt/DATA/UI/modelplot.png"))
        self.frame1 = tk.Frame(self.master, background="black")
        self.frame1.place(relwidth=1, relheight=0.17, relx=0, rely=0.83)

        totalbuttons = 22

        self.currentavailablebuttons = [{} for i in range(totalbuttons)]

        c1 = 0
        c2 = 0
        pathlist = ["input", "conv", "dense", "act", "output", "flatten", "add"]

        for i, bpath in enumerate(pathlist):
            bg, bga = self.getwidgets("input", bpath + ".png")
            self.currentavailablebuttons[i] = {"name": bpath[:-4], "bg": bg, "bga": bga, "count": 0}
            self.buttonsarray.append(Button(self.frame1, image=buttonsbgarray[i], activebackground="#32CD32"
                                            , relief=RAISED, borderwidth=4))

            self.buttonsarray[i].bind("<ButtonPress-1>", lambda event, a=self.currentx, b=self.currenty,
                                                                d=bpath, bg=bg, bga=bga: self.create_token(a, b, d, bg,
                                                                                                           bga))

            if i % 2 == 0:
                self.buttonsarray[i].grid(row=0, column=c1)
                c1 += 1
            elif i % 2 == 1:
                self.buttonsarray[i].grid(row=1, column=c2)
                c2 += 1

        buttonnames = ["Separable Conv2D","DW Conv2D","Conv1D" ,"Conv3D","MaxPooling2D","AveragePooling2D"
                       ,"GlobalMaxPooling2D", "GlobalAveragePooling2D","BatchNormalization","Dropout","Reshape","UpSampling2D"
                       ,"LSTM layer","ConvLSTM2D","SpatialDropout","GlobalMaxPooling1D"]

        for j in range(i + 1, totalbuttons, 1):
            #             print("button",j,c1,c2)
            print(buttonnames[j-7])
            # self.buttonsarray.append(Button(self.frame1, image=defaultbutton, activebackground="#32CD32"
            #                                 , relief=RAISED, borderwidth=4))

            pixelVirtual = tk.PhotoImage(width=1, height=1)

            # buttonExample1 = tk.Button(app,
            #                            text="Increase",
            #                            image=pixelVirtual,
            #                            width=100,
            #                            height=100,
            #                            compound="c")
            self.buttonsarray.append(Button(self.frame1,text = buttonnames[j-7],image = pixelVirtual,compound = "c",
                                            activebackground="#32CD32"
                                            , relief=RAISED, borderwidth=4,height = 60 , width = 60,bg = "white"))
            if j % 2 == 0:
                self.buttonsarray[j].grid(row=0, column=c1)
                c1 += 1
            elif j % 2 == 1:
                self.buttonsarray[j].grid(row=1, column=c2)
                c2 += 1

        self.b8 = Button(self.frame1, image=plotbg, activebackground="#32CD32", relief=RAISED, borderwidth=4)
        self.b9 = Button(self.frame1, image=trainbg, activebackground="#32CD32", relief=RAISED, borderwidth=4)
        self.b11 = Button(self.frame1, image=codebg, activebackground="#32CD32", relief=RAISED, borderwidth=4)
        self.b12 = Button(self.frame1, image=buildbg, activebackground="#32CD32", relief=RAISED, borderwidth=4)

        self.b8.bind("<ButtonPress-1>", self.plotclicked)
        self.b9.bind("<ButtonPress-1>", self.trainclicked)
        self.b11.bind("<ButtonPress-1>", self.codeclicked)
        self.b12.bind("<ButtonPress-1>", self.compilemodel)

        self.b8.place(rely=0, relx=0.84)
        self.b9.place(rely=0, relx=0.92)
        self.b11.place(rely=0, relx=0.68)
        self.b12.place(rely=0, relx=0.76)

        self.myFont = Font(family="clearlyu pua", size=12)
        self.python = Frame(self.frame1, bg="black", width=280, height=140)
        self.python.place(rely=0, relx=0.433, relwidth=0.245, relheight=0.95)
        entryframe = Frame(self.python, bg="red", width=455, height=40)
        entryframe.grid(row=1)

        enterbutton = Button(entryframe, text="ENTER")
        addbutton = Button(entryframe, text="add")
        self.codeentry = Entry(entryframe, font=("Calibri 12 bold"))
        self.codeentry.place(relx=0, rely=0, relwidth=0.9, relheight=1)
        enterbutton.place(relx=0.9, rely=0, relwidth=0.1, relheight=1)
        enterbutton.bind("<Button-1>", self.insertcode)
        #         addbutton.place(relx = 0.9,rely = 0,relwidth = 0.1,relheight = 1)
        #         add.bind("<Button-1>",add)

        self.scrollcanvas = Canvas(self.python, height=125, width=450, bg="black")
        self.scrollcanvas.grid(row=0)

        self.scrollcanvasFrame = Frame(self.scrollcanvas, bg="black")
        self.scrollcanvas.create_window(0, 0, window=self.scrollcanvasFrame, anchor='nw')

        yscrollbar = Scrollbar(self.python, orient=VERTICAL)
        yscrollbar.config(command=self.scrollcanvas.yview)
        self.scrollcanvas.config(yscrollcommand=yscrollbar.set)
        yscrollbar.grid(row=0, column=1, sticky="ns")

        self.scrollcanvasFrame.bind("<Configure>", lambda event: self.scrollcanvas.configure(
            scrollregion=self.scrollcanvas.bbox("all")))

        self.frame7 = tk.Frame(self.master, background="yellow")
        self.canvas = tk.Canvas(self.frame7, bg="black")

        self.canvas.tag_bind("token", "<ButtonPress-1>", self.drag_start)
        self.canvas.tag_bind("token", "<ButtonRelease-1>", self.drag_stop)
        self.canvas.tag_bind("token", "<B1-Motion>", self.drag)
        self.canvas.bind("<Shift-Button-3>", self.clickedcanvas)

        self.frame7.place(relwidth=1, relheight=0.83, relx=0, rely=0.0)
        self.canvas.place(relheight=1, relwidth=1)

        self.toggle = Button(self.canvas, activebackground="#32CD32", relief=RAISED, borderwidth=3, height=90)
        self.toggle.place(relwidth=0.03, relx=0.5, rely=0, relheight=0.03)
        #         self.toggle.bind("<Double-Button-1>",self.togglebg1)

        self.toko = Button(self.canvas, image=toko, activebackground="#32CD32", relief=RAISED, borderwidth=3, height=90)
        self.toko.place(relwidth=0.05, relx=0.005, rely=0.85)
        self.toko.bind("<Double-Button-1>", self.tokoclicked)

        self.ide = Button(self.canvas, image=code, activebackground="#32CD32", relief=RAISED, borderwidth=3, height=90)
        self.ide.place(relwidth=0.04, relheight=0.1, relx=0.95, rely=0.0)
        self.ide.bind("<Button-1>", self.ideclicked)

        self.sequence = [ImageTk.PhotoImage(img)
                         for img in ImageSequence.Iterator(
                Image.open(
                    bgpath + 'ai3.gif'))]

        self.backgroundimage1 = ImageTk.PhotoImage(Image.open("/mnt/DATA/UI/backgrounds/bg2.jpg"))
        self.backgroundimage2 = ImageTk.PhotoImage(Image.open("/mnt/DATA/UI/backgrounds/background1.jpg"))
        self.image = self.canvas.create_image(0,0, image=self.backgroundimage1,anchor = NW)
        # self.image = self.canvas.create_image(0, 0, image=self.sequence[0], anchor=NW)
        # self.animatecount = 0
        # self.animate(1)
        # self.change = False

    # def animate(self, counter):
    #     self.canvas.itemconfig(self.image, image=self.sequence[counter])
    #     self.master.after(38, lambda: self.animate((counter + 1) % len(self.sequence)))
    #     self.animatecount += 1
    #     if self.animatecount == 2:
    #         self.startspeak()

    #     def animatedestroy(self, counter):
    #         self.master.after(1,lambda : _show('Title', 'Prompting after 5 seconds'))
    #         self.canvas.itemconfig(self.image, image=self.backgroundimage1)

    #     def togglebg1(self,event):
    #         if self.change == True:
    #             self.canvas.itemconfig(self.image, image=self.sequence[0])
    #             self.animate(1)
    #             self.change = False
    #         else:
    #             self.canvas.delete(self.image)
    #             self.image = self.canvas.create_image(0,0, image=self.backgroundimage1,anchor = NW)
    #             self.change = True
    #             animatedestroy

    def ideclicked(self, event):
        # obj = Ide(self.canvas)
        self.editorobj = Editor(self.canvas)
        self.editorobj.frame.mainloop()
        self.updatecodecanvas("the code is saved as model.py format")

    def startspeak(self):
        self.updatecodecanvas("Welcome to deeplearning self.graphical interface")
        self.updatecodecanvas("For any queries click on the Toko Button ")
        self.updatecodecanvas("-----------------------------")
        self.updatecodecanvas("start by adding Input layer")
        engine.say("Welcome to deep learning self.graphical interface")
        engine.say("For any queries click on the Toko Button")
        engine.runAndWait()

    def updatecodecanvas(self, s):
        label = Label(self.scrollcanvasFrame, text=s, bg="black", foreground="white", font="Courier 12")
        label.pack()
        self.codelines.append(label)
        self.scrollcanvas.update_idletasks()
        self.scrollcanvas.yview_moveto('1.5')

    def insertcode(self, event):
        s = self.codeentry.get()
        self.updatecodecanvas(s)
        self.codeentry.delete(0, 'end')
        if s == "clear":
            for i in range(len(self.codelines)):
                self.codelines[i].destroy()
            self.scrollcanvas.yview_moveto('0')

    def getwidgets(self, s, path):
        widgetsactivepath = '/mnt/DATA/UI/widgets/active/'
        widgetspath = '/mnt/DATA/UI/widgets/inactive/'
        image = Image.open(widgetspath + path)
        bg = ImageTk.PhotoImage(image)
        s = widgetsactivepath + path[:-4] + "active" + path[-4:]
        image = Image.open(s)
        bga = ImageTk.PhotoImage(image)
        return bg, bga

    def drag_start(self, event):
        self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def drag_stop(self, event):
        """End drag of an object"""
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0
        #         i = event.widget.find_withtag('current')[0]

        canvas_item_id = event.widget.find_withtag('current')[0]
        n1 = self.nodes.index(canvas_item_id)
        self.dic[n1]["x"] = event.x
        self.dic[n1]["y"] = event.y
        lines = self.coonectionsdic[n1]
        print("selected ", n1, "lines ==", lines)
        for j in range(len(lines)):
            #             print("connectionsself.dic before",self.coonectionsdic[:4])
            line = lines[0]
            n2 = line.get("nodeid")
            lineid1 = line.get("lineid")

            ind = [self.coonectionsdic[n2][i].get("nodeid") for i in range(len(self.coonectionsdic[n2]))].index(n1)
            lineid2 = self.coonectionsdic[n2][ind]["lineid"]

            self.canvas.delete(lineid2)
            self.canvas.delete(lineid1)

            self.addline(n1, n2)
            self.coonectionsdic[n1].pop(0)
            self.coonectionsdic[n2].pop(ind)

    #             print("connectionsself.dic after",self.coonectionsdic[:4])

    def drag(self, event):
        """Handle dragging of an object"""
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        self.canvas.move(self._drag_data["item"], delta_x, delta_y)
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def create_token(self, x, y, label, bg, bga):
        #         print("button ",label," is pressed")
        x = self.currentx
        y = self.currenty
        self.nodescnt += 1

        if label == "conv":
            self.updatecodecanvas("conv2d object is created, double-click to initialize")
            self.ccnt += 1
            self.currentx += 160
            name = "conv"

        elif label == "dense":
            self.updatecodecanvas("dense object is created, double-click to initialize")
            self.currentx += 80
            y = y - 50
            name = "dense"

        elif label == "act":
            self.updatecodecanvas("activation object is created, double-click to initialize")
            self.currentx += 120
            y = y
            name = "activation"

        elif label == "input":
            self.updatecodecanvas("input object is created, double-click to initialize")
            self.updatecodecanvas("start adding layers")
            if self.icnt >= 1:
                y = self.currenty - 120 * self.icnt
                x = 20
                self.icnt += 1
            else:
                self.currentx += 120
                self.icnt += 1
            name = "input"

        elif label == "output":
            self.updatecodecanvas("output object is created, double-click to initialize")
            y = self.currenty - 120 * self.ocnt
            x = 1800
            self.ocnt += 1
            name = "output"


        elif label == "flatten":
            self.updatecodecanvas("flatten object is created, double-click to initialize")
            self.currentx += 80
            y = y - 50
            name = "flatten"

        elif label == "add":
            self.updatecodecanvas("add object is created, double-click to initialize")
            self.currentx += 110
            name = "add"

        token = self.canvas.create_image(x, y, image=bg, anchor=NW, tags=("token",), activeimage=bga)
        self.nodes.append(token)
        self.tensorlist.append(None)
        self.dic[self.cnt] = {"x": x, "y": y, "name": name, "Node": None, "param": [None]}
        self.canvas.tag_bind(token, '<Double-Button-1>', self.itemClicked)
        self.canvas.tag_bind(token, "<Shift-Button-1>", self.connect)
        self.cnt += 1

    def connect(self, event):
        canvas_item_id = event.widget.find_withtag('current')[0]
        try:
            self.path.index(canvas_item_id)
        #             print("Node already added")
        except:
            self.path.append(canvas_item_id)

    #         print(self.path)

    def clickedcanvas(self, event):
        if len(self.path) > 1:
            for i in range(len(self.path) - 1):
                n1 = self.nodes.index(self.path[i])
                n2 = self.nodes.index(self.path[i + 1])
                self.graph[n1].append(n2)
                self.invgraph[n2].append(n1)
                self.addline(n1, n2)
                self.pathscnt += 1
            print("added path")
        self.path = []
        print(self.path)
        if self.pathscnt == self.nodescnt - 1:
            self.updatecodecanvas("path is created build now")

    def addline(self, n1, n2):
        x1 = self.dic[n1]["x"]
        y1 = self.dic[n1]["y"]
        x2 = self.dic[n2]["x"]
        y2 = self.dic[n2]["y"]
        lineid1 = self.canvas.create_line(x1, y1, x2, y2, fill="white", width=3)
        lineid2 = self.canvas.create_line(x2, y2, x1, y1, fill="white", width=3)
        self.coonectionsdic[n1].append({"nodeid": n2, "lineid": lineid1})
        self.coonectionsdic[n2].append({"nodeid": n1, "lineid": lineid2})

    def itemClicked(self, event):

        canvas_item_id = event.widget.find_withtag('current')[0]
        print('Item', canvas_item_id, 'Clicked!')
        ind = self.nodes.index(canvas_item_id)
        self.objectscnt += 1

        if self.dic[ind]["name"].startswith("conv"):
            print("conv")
            self.updatecodecanvas(str(canvas_item_id) + ":tensorflow.keras.layers.Conv2D(**args) is created")

            ConvDialog(self.canvas, self, event.x, event.y, ind)
            dic = self.dic

        elif self.dic[ind]["name"].startswith("dense"):
            print("dense")
            self.updatecodecanvas(str(canvas_item_id) + ":tensorflow.keras.layers.Dense(**args) is created")
            DenseDialog(self.canvas, self, event.x, event.y, ind)
            dic = self.dic

        elif self.dic[ind]["name"].startswith("input"):
            print("input")
            self.updatecodecanvas(str(canvas_item_id) + ":tensorflow.keras.layers.Input(**args) is created")
            InputDialog(self.canvas, self, event.x, event.y, ind)
            dic = self.dic

        elif self.dic[ind]["name"].startswith("output"):
            print("output")
            self.updatecodecanvas(str(canvas_item_id) + ":tensorflow.keras.layers.Dense(**args) is created")
            OutputDialog(self.canvas, self, event.x, event.y, ind)
            dic = self.dic

        elif self.dic[ind]["name"].startswith("add"):
            print("add")
            self.updatecodecanvas(str(canvas_item_id) + ":tensorflow.keras.layers.Add(**args) is created")
            AddDialog(self.canvas, self, event.x, event.y, ind)
            dic = self.dic

        #         elif self.dic[ind]["name"].startswith("act"):
        #             print("activation")
        #             self.updatecodecanvas(str(canvas_item_id)+":tensorflow.keras.layers.Activation(**args) is created")
        #             actDialog(self.canvas,event.x,event.y,ind)

        elif self.dic[ind]["name"].startswith("flatten"):
            print("flatten")
            self.updatecodecanvas(str(canvas_item_id) + ":tensorflow.keras.layers.Flatten(**args) is created")
            FlattenDialog(self.canvas, self, event.x, event.y, ind)
            dic = self.dic

        if self.objectscnt >= self.nodescnt:
            self.updatecodecanvas("---all objects are created.---")
            self.updatecodecanvas("--- you can add paths now---")
            self.updatecodecanvas("hold shift + left mouse click to add paths")
            self.updatecodecanvas("hold shift + right mouse click to connect paths")
            self.updatecodecanvas(" ")

    #         print(self.dic)

    def tokoclicked(self, event):
        obj = TokoDialog(self.canvas)

    def plotclicked(self, event):
        global getplotimage
        obj = ModelplotDialog(self.canvas, getplotimage())
        self.updatecodecanvas("plot is self.graphical representation in image format")

    def codeclicked(self, event):
        # obj = ModelcodeDialog(self.canvas)
        obj = Editor(self.canvas)
        obj.frame.mainloop()
        self.updatecodecanvas("the code is saved as model.py format")

    def summaryclicked(self):
        obj = ModelsummaryDialog(self.canvas)
        self.updatecodecanvas("summary is the architecture of model")
        self.updatecodecanvas("built successful")
        self.updatecodecanvas("you can train model now")
        self.updatecodecanvas("remember to compile model first")

    def trainclicked(self, event):
        obj = Train(self.canvas, [self.t1, self.t2, self.t3, self.t4, self.t5], self.model, self)

    def printdict(self, event):
        print(self.nodes)
        print(self.dic)

    def addtocode(self, node, xlist):
        name = self.dic[node]["name"]
        params = self.dic[node]["param"]
        print("params = ", params)
        if name.startswith("conv"):
            self.updatecodecanvas("     {} = tf.keras.layers.Conv2d(**args)(x)")
            with open("model.py", "a") as myfile:
                myfile.write(
                    "     {} = tf.keras.layers.Conv2d(filters={},kernel_size={},strides={},padding= '{}',dilation_rate= {},activation= '{}')({})\n".format(
                        "x" + str(node), params[0], params[1], params[2], params[3], params[4], params[5], xlist))

        elif name.startswith("dense"):
            self.updatecodecanvas("x = tf.keras.layers.Dense(**args)(x)")
            with open("model.py", "a") as myfile:
                myfile.write("     {} = tf.keras.layers.Dense(units = {},activation= '{}',use_bias=  {})({})\n".format(
                    "x" + str(node), params[0], params[1], params[2], xlist))

        elif name.startswith("output"):
            self.updatecodecanvas("x = tf.keras.layers.Dense(**args)(x)")
            with open("model.py", "a") as myfile:
                myfile.write("     {} = tf.keras.layers.Dense(units = {},activation= '{}',use_bias=  {})({})\n".format(
                    "x" + str(node), params[0], params[1], params[2], xlist))
        elif name.startswith("flatten"):
            self.updatecodecanvas("x = tf.keras.layers.Flatten(**args)(x)")
            with open("model.py", "a") as myfile:
                myfile.write("     {} = tf.keras.layers.Flatten()({})\n".format("x" + str(node), xlist))
        elif name.startswith("act"):
            self.updatecodecanvas("x = tf.keras.layers.Activation(**args)(x)")
            with open("model.py", "a") as myfile:
                myfile.write("     {} = tf.keras.layers.Activation()({})\n".format("x" + str(node), xlist))
        elif name.startswith("add"):
            self.updatecodecanvas("x = tf.keras.layers.Add(**args)(x)")
            with open("model.py", "a") as myfile:
                myfile.write("     {} = tf.keras.layers.Add(**args)({})\n".format("x" + str(node), xlist))
        elif name.startswith("input"):
            self.updatecodecanvas("x = tf.keras.layers.Add(**args)(x)")
            with open("model.py", "a") as myfile:
                myfile.write("     {} = tf.keras.layers.Input(shape =  {})\n".format("x" + str(node), params[0]))


    def rec(self, node):
        if node == 0:
            self.tensorlist[0] = self.dic[0]["Node"]
            self.addtocode(node, 0)
            return self.tensorlist[0]
        else:
            lis = [self.rec(i) for i in self.invgraph[node]]
            xlist = ["x" + str(i) for i in self.invgraph[node]]
            if len(lis) == 1:
                self.tensorlist[node] = self.dic[node]["Node"](lis[0])
                self.addtocode(node, xlist[0])
            else:
                self.tensorlist[node] = self.dic[node]["Node"](lis)
                self.addtocode(node, xlist)
            print(self.dic[node]["Node"], self.dic[node]["name"])
            return self.tensorlist[node]

    def compilemodel(self, event):
        for i in range(len(self.nodes)):
            if len(self.graph[i]) == 0:
                end = i

        self.rec(i)
        self.model = tf.keras.models.Model(self.tensorlist[0], self.tensorlist[i])
        self.model.summary()
        plot_model(self.model, "modelplot.png")
        with open('modelsummary.txt', 'w') as f:
            with redirect_stdout(f):
                self.model.summary()

        with open("model.py", "a") as myfile:
            myfile.write(
                "     return tf.keras.models.Model(inputs = {} , outputs = {})\n\n".format("x" + str(0), "x" + str(i)))
            myfile.write("\n")
            myfile.write("model = mymodel()\n")
            myfile.write("model.summary()")
        # self.editorobj.root.destroy()
        # self.editorobj = Editor(self.canvas)
        # self.editorobj.frame.mainloop()
        self.editorobj.first_open("model.py")
        self.updatecodecanvas("the code is saved as model.py format")
        self.summaryclicked()


class Mainclass:
    def __init__(self):
        # self.sroot = sroot

        # self.traindatagen = sroot.traingen
        # self.testdatagen = sroot.testgen
        # self.traindatagen = []
        # self.testdatagen = []

        # sroot.controller.root.destroy()

        self.window = tk.Tk()
        self.window.attributes('-zoomed', True)
        self.fullScreenState = False
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)
        self.window.title("DEEP-LEARNING UI")
        b = self.getbuttonimages()
        app = Window(b, root=self, master=self.window)

        self.window.mainloop()

    def getbuttonimages(self):
        # ["input","conv","dense","act","output","flatten","add"]

        default = self.buttonimage("later")

        bg1 = self.buttonimage("input")
        bg2 = self.buttonimage("conv")
        bg3 = self.buttonimage("dense")
        bg4 = self.buttonimage("act")
        bg5 = self.buttonimage("output")
        bg6 = self.buttonimage("flatten")
        bg7 = self.buttonimage("add")

        bg8 = self.buttonimage("embedding")
        # bg9 = self.buttonimage("add")
        # bg10 = self.buttonimage("add")
        # bg11 = self.buttonimage("add")
        # bg12 = self.buttonimage("add")
        # bg13 = self.buttonimage("add")
        # bg14 = self.buttonimage("add")
        # bg15 = self.buttonimage("add")
        # bg16 = self.buttonimage("add")




        # fg1 = ImageTk.PhotoImage(Image.open("/mnt/DATA/UI/buttons/plotbutton3.png"))
        fg1 = self.buttonimage("plotlarge")
        fg2 = self.buttonimage("train")
        fg3 = self.buttonimage("codelarge")
        fg4 = self.buttonimage("buildlarge")
        # fg3 = ImageTk.PhotoImage(Image.open("/mnt/DATA/UI/buttons/codebutton3.png"))
        # fg4 = ImageTk.PhotoImage(Image.open("/mnt/DATA/UI/buttons/buildbutton3.png"))

        toko = self.buttonimage("toko")
        code = self.buttonimage("code")

        plot = ImageTk.PhotoImage(Image.open("/mnt/DATA/UI/modelplot.png"))

        train1 = ImageTk.PhotoImage(Image.open("/mnt/DATA/UI/buttons/trainingbutton.png"))
        train2 = ImageTk.PhotoImage(Image.open("/mnt/DATA/UI/buttons/predbutton.png"))
        train3 = ImageTk.PhotoImage(Image.open("/mnt/DATA/UI/buttons/databutton.png"))
        train4 = ImageTk.PhotoImage(Image.open("/mnt/DATA/UI/buttons/compilebutton1.png"))
        train5 = ImageTk.PhotoImage(Image.open("/mnt/DATA/UI/buttons/databutton.png"))
        return [default, [bg1, bg2, bg3, bg4, bg5, bg6, bg8], [fg1, fg2, fg3, fg4], toko, plot, code,
                [train1, train2, train3, train4, train5]]

    def buttonimage(self, s, resize=False):
        path = buttonspath +"edited/"+ s + "button2.png"
        image = Image.open(path)
        if resize == True:
            image = image.resize((200, 140), Image.ANTIALIAS)
        bg = ImageTk.PhotoImage(image)
        return bg

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-zoomed", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-zoomed", self.fullScreenState)


def toggleFullScreen(event):
    fullScreenState = not fullScreenState
    root.attributes("-zoomed", fullScreenState)


def quitFullScreen(event):
    fullScreenState = False
    root.attributes("-zoomed", fullScreenState)

from PIL import Image, ImageTk, ImageSequence
# sroot = Tk()
# sroot.minsize(height=1000, width=1000)
# sroot.title("Loading.....")
# sroot.configure()
# spath = "/mnt/DATA/UI/backgrounds/"
Mainclass()
# sroot.mainloop()
