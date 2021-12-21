
from p2 import *


class info():
    def __init__(self):
        self.info1 = [1,2,3,4,5,6,7,8]
        self.info2 = 'time'
        print('initialised')

class MainFrame():
    def __init__(self):
        a=info()
        print(a.info1)
        b=page1(a)
        print(a.info1)
        c=page2(a)
        print(a.info2)


t=MainFrame()