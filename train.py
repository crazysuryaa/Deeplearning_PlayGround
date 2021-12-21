class Train:
    def __init__(self,parent,b):
        self.parent = parent
        self.parent.geometry("600x1000")
        self.parent.title("TRAIN")
        b1,b2,b3,b4 = b
        self.frame0 = Frame(self.parent)
        self.fig = Figure(figsize=(8, 8), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame0) 
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.frame0)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        self.canvas.mpl_connect("key_press_event", self.on_key_press)
        self.frame0.place(relwidth = 1 ,relheight = 0.85,rely = 0)
        
        self.frame1 = Frame(self.parent,bg = "#423B39")
        self.frame1.place(relwidth = 1 ,relheight = 0.15,rely = 0.85)
        self.trainbutton = tkinter.Button(master=self.frame1, text="Train",image = b1)
        self.compilebutton = tkinter.Button(master=self.frame1, text="compile" , image = b4)
        self.predictbutton = tkinter.Button(master=self.frame1, text="predict" ,image = b2)
        self.quitbutton = tkinter.Button(master=self.frame1, text="FORCE QUIT" ,image = b3)
        # button = tkinter.Button(master=self.frame1, text="Train")
        self.trainbutton.bind("<Button-1>",self.train)
        self.quitbutton.bind("<Button-1>",self.quit)

        self.trainbutton.place(width = 100 ,height = 100,rely = 0.1 ,relx = 0.1)
        self.compilebutton.place(width = 100 ,height = 100,rely = 0.1 , relx = 0.3)
        self.predictbutton.place(width = 100 ,height = 100,rely = 0.1 , relx = 0.5)
        self.quitbutton.place(width = 100 ,height = 100,rely = 0.1 ,relx = 0.7)
        
    def getbuttons(self):

        return b1,b2,b3,b4
    
    def on_key_press(self,event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, self.canvas, self.toolbar)

    def quit(self,event):
        self.parent.quit()     # stops mainloop
        self.parent.destroy()  # this is necessary on Windows to prevent
                        # Fatal Python Error: PyEval_RestoreThread: NULL tstate

    def train(self,event):
        ax1 = self.fig.add_subplot(2,1,1)
        ax2 =self.fig.add_subplot(2,1,2)
        lossx = []
        acc = []
        for i in range(1,100):
            loss = np.random.normal(0,1)
            bacc = np.random.normal(0,1)
            y = np.arange(i)
            lossx.append(loss)
            acc.append(bacc)
            ax1.plot(y, lossx)
            ax1.set(xlabel='step no', ylabel='loss')
            ax2.plot(y,acc)
            ax2.set(xlabel='step no', ylabel='accuracy')
            self.canvas.draw()
