from PIL import Image
import glob
import imageio
from natsort import natsorted
'''
images=glob.glob("*.png")
image_list = []
for file_name in images:
    image_list.append(imageio.imread(file_name))

imageio.mimwrite('animated_from_images.gif', images)    
'''


import imageio
import os

folder = 'pics' 
files = glob.glob("*.png")
files=natsorted(files)
print(files)

images = [imageio.imread(file) for file in files]
imageio.mimwrite('movie.gif', images, fps=1)
