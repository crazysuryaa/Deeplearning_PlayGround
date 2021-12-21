import numpy as np
import cv2 as cv2
from os import path

import os

def reshape(dirpath,newsize):
    
    
    newdir = os.path.join(dirpath, "reshapeddataset"+str(newsize))  
    try:
        os.makedirs(newdir, exist_ok = True) 
        print("Directory  created successfully" ) 
    except OSError as error: 
        print("Directory  can not be created")
#        
    reshaped = []
    for i in sorted(os.listdir(dirpath)):
#        print(i)
        imgpath = dirpath+"/"+i
        
        reshapedpath = newdir +"/"+ i
        if path.isdir(imgpath) == False and (imgpath.endswith(".png") or imgpath.endswith(".jpg") ):
            print(imgpath)
            img = cv2.imread(imgpath)
            reimg = cv2.resize(img,(newsize,newsize))
            reshaped.append(reimg)
            
            cv2.imwrite(reshapedpath,reimg)
            print(reshapedpath)
    return newdir

#
#kivypathpass("D:/Desktop/akshay",256)
