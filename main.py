import tkinter
import os

from PIL import Image

from helper import image_helper as ih
    
if not os.path.exists("image/temp"):
    os.mkdir("image/temp")
    
temp_files = [name for name in os.listdir("image/temp")]
for f in temp_files:
    os.remove(f"image/temp/{f}")
del temp_files
    
ih.cut_in_n_times_n(Image.open("image/capture.png"))
