from PIL import Image 
import glob
import string
import os

images=glob.glob("./data/images/b*")
for i in range(len(images)):
    print(images[i])
    image_file = Image.open(images[i]) 
    image_file = image_file.convert('LA')
    image_file.save(("./data/images/grayscale-"+images[i][15:len(images[i])-3:]+".png"))

labels=glob.glob("./data/labels/b*")
for i in range(len(labels)):
    os.system("cp "+labels[i]+" ./data/labels/grayscale-"+labels[i][15::])
