import tkinter
import os
import constants as c

from PIL import Image
from helper import image_helper as ih
from helper import tiles_helper as th
    
if not os.path.exists(c.TEMP_DIR):
    os.mkdir(c.TEMP_DIR)
    
temp_files = [name for name in os.listdir(c.TEMP_DIR)]
for f in temp_files:
    os.remove(f"{c.TEMP_DIR}/{f}")
del temp_files

ih.cut_in_n_times_n(Image.open("image/Flowers.png"))
print(th.find_valid_neighbors(c.TEMP_DIR))
