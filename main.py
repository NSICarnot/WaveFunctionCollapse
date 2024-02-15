import tkinter
import os
import random as r
import constants as c

from PIL import Image
from helper import image_helper as ih
from helper import tiles_helper as th
from tile import Tile
    
if not os.path.exists(c.TEMP_DIR):
    os.mkdir(c.TEMP_DIR)
    
temp_files = [name for name in os.listdir(c.TEMP_DIR)]
for f in temp_files:
    os.remove(f"{c.TEMP_DIR}/{f}")
del temp_files

ih.cut_in_n_times_n(Image.open("image/Flowers.png"))
c.VALID_NEIGHBORS = th.find_valid_neighbors(c.TEMP_DIR)
print(c.VALID_NEIGHBORS)

def main():
    wave: list[list[Tile]] = [[Tile() for _ in range(c.OUTPUT_WIDTH)] for _ in range(c.OUTPUT_HEIGHT)]
    
    wave[r.randint(0, c.OUTPUT_HEIGHT)][r.randint(0, c.OUTPUT_WIDTH)].tile = r.choice([x for x in c.VALID_NEIGHBORS.keys()])
    while True:
        min_tile_entropy: Tile = wave[0][0]
        for y in wave:
            for x in y:
                if x.get_entropy() < min_tile_entropy.get_entropy() and not x.is_collapsed():
                    min_tile_entropy = x
        if not min_tile_entropy.get_entropy() - 1:
            break
        print(min_tile_entropy.get_entropy())
        min_tile_entropy.collapse()
        for y_co, y in enumerate(wave):
            for x_co, x in enumerate(y):
                x.recalculate_neighbors(wave, x_co, y_co)
                x.recalculate_entropy()
        
    print("Fini")
        
    
if __name__ == "__main__":
    main()
