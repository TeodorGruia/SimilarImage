"""Similar image finder
sam goldberg
"""
from PIL import ImageStat as iss
from PIL import Image
import glob
import re
def main():
    print("Python similar image finder")
    Images = get_images()
    for f in Images[15:20]:
        x = iss.Stat(f).sum
        t = re.findall("[3]", str(x[0]))
        if t:
            Image._show(f)

       
def get_images():
    pic_list = []
    path = r'C:\\Users\\sjtg1\\Dropbox\\Screenshots\\rwby\\*.png'
    for filename in glob.glob(path):
        im = Image.open(filename)
        pic_list.append(im)
    return pic_list

    
    
    
if __name__ == '__main__': main()