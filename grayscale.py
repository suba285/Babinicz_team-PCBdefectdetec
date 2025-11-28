from PIL import Image 
import glob
import string
import os
import random
import math

folders=["test","train","valid"]

for j in range(len(folders)):

    images=glob.glob("./data/"+folders[j]+"/images/b*")
    
    for i in range(len(images)):
        image = Image.open(images[i]);
        width, height = image.size;
        newheight=(300*height)/width;
        new_image = image.resize((300, int(newheight)));
        print(("./newdata/"+folders[j]+"/images/"+images[i][14+1+len(folders[j])::]))
        new_image.save(("./newdata/"+folders[j]+"/images/"+images[i][14+1+len(folders[j])::]));
    
    labels=glob.glob("./data/"+folders[j]+"/labels/b*")
    for i in range(len(labels)):
        os.system("cp "+labels[i]+" ./newdata/"+folders[j]+"/labels/"+labels[i][14+1+len(folders[j])::])
    
    
    images=glob.glob("./newdata/"+folders[j]+"/images/b*")
    for i in range(len(images)):
        if i%3==0:
            print(images[i])
            image_file = Image.open(images[i]) 
            image_file = image_file.convert('LA')
            image_file.save(("./newdata/"+folders[j]+"/images/grayscale-"+images[i][17+1+len(folders[j]):len(images[i])-3:]+".png"))
        else:
            image = Image.open(images[i])
            width, height = image.size;
            new_image = image.resize((int(math.floor(random.randrange(7,15)*width/13)),int(math.floor(random.randrange(7,13)*height/10))));
            new_image.save(("./newdata/"+folders[j]+"/images/squed-"+images[i][17+1+len(folders[j])::]));
    
    
    
    labels=glob.glob("./newdata/"+folders[j]+"/labels/b*")
    for i in range(len(labels)):
        if i%3==0:
            os.system("cp "+labels[i]+" ./newdata/"+folders[j]+"/labels/grayscale-"+labels[i][17+1+len(folders[j])::])
        else:
            os.system("cp "+labels[i]+" ./newdata/"+folders[j]+"/labels/squed-"+labels[i][17+1+len(folders[j])::])


