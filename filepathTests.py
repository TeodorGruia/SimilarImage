#from pathlib import Path
import os
#For trying to figure out how to loop thorugh as set of images in a directory with PIL.
#Use glob, specify the extension of the file
import os
from PIL import Image
import glob
path = 'C:\\Users\\sjtg1\\Dropbox\\Screenshots\\rwby\\*.png'
for filename in glob.glob(path):
    im = Image.open(filename)
