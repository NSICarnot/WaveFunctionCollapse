import tkinter
import os

from PIL import Image

from helper import image_helper as ih


if not os.path.exists("image/temp"):
    os.mkdir("image/temp")
    
ih.cut_in_n_times_n(Image.open("image/capture.png"))
