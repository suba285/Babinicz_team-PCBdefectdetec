from PIL import Image 
import glob
import string
import os
import random
import math

images=glob.glob("./data/images/b*")

for i in range(len(images)):
    image = Image.open(images[i]);
    width, height = image.size;
    newheight=(300*height)/width;
    new_image = image.resize((300, int(newheight)));
    print(("./newdata/images/"+images[i][14::]))
    new_image.save(("./newdata/images/"+images[i][14::]));

labels=glob.glob("./data/labels/b*")
for i in range(len(labels)):
    os.system("cp "+labels[i]+" ./newdata/labels/"+labels[i][14::])


images=glob.glob("./newdata/images/b*")
for i in range(len(images)):
    if i%3==0:
        print(images[i])
        image_file = Image.open(images[i]) 
        image_file = image_file.convert('LA')
        image_file.save(("./newdata/images/grayscale-"+images[i][17:len(images[i])-3:]+".png"))
    else:
        image = Image.open(images[i])
        width, height = image.size;
        new_image = image.resize((int(math.floor(random.randrange(7,15)*width/13)),int(math.floor(random.randrange(7,13)*height/10))));
        new_image.save(("./newdata/images/squed-"+images[i][17::]));



labels=glob.glob("./newdata/labels/b*")
for i in range(len(labels)):
    if i%3==0:
        os.system("cp "+labels[i]+" ./newdata/labels/grayscale-"+labels[i][17::])
    else:
        os.system("cp "+labels[i]+" ./newdata/labels/squed-"+labels[i][17::])


