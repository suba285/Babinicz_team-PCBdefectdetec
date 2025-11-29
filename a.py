from PIL import Image 
import glob
import string
import os
import random
import math

folders=["test","train","valid"]

text = 'The sky is blue.'
new_text = text.replace('blue', 'red')
print(new_text)
for j in range(len(folders)):

    
    labels=glob.glob("./"+folders[j]+"/labels/*")


    for i in range(len(labels)):
        
        # x = open(labels[i])
        # s=x.read().replace("\n0 ", "\n1 " )
        # x.close()
        # x=open(labels[i],"w")
        # x.write(s)
        # x.close
        x = open(labels[i])
        s=x.read().replace("0 ", "3 ") 
        x.close()
        x=open(labels[i],"w")
        x.write(s)
        x.close
