"""
Library/Module name: tests
For testing functions before deployment. 
Author: Sam Goldberg
"""



import os
from PIL import Image 
def test_PIL():
    im = Image.open('C:\\Users\\sjtg1\\Dropbox\\Screenshots\\rwby\\Screenshot (1001).png')
    print(im)

def list_folder_contents():
    pictures_lib = r'C:\\Users\\sjtg1\\Dropbox\\Screenshots\\rwby'
    for pic in os.listdir(pictures_lib):
        print(pic)