import os
import constants as c
from PIL import Image

"""
The algorithm for finding valid neighbors is different according to the simulation demands.

The chosen algorithm therefore concerns the equality of colors. For being a valid neighbor, the tile next to itself must have the same colors. 
Then a dictionary with each tiles is created and inside it, a new dictionary is created which contains top, left, bottom and right valid tiles.

Algorthm:

1 - Load all tiles pixels list on a numpy list Then save them in a dictionary.
2 - For each tiles. Compute all other tiles and check their validity.
"""

def find_valid_neighbors(dir: str) -> dict[dict]:
    valid_neighbors: dict = {}
    tiles: dict = {}
    
    dirs = os.listdir(dir)
    
    for t in dirs:
        t_img = Image.open(f"{dir}/{t}")
        t_pixels: list[list] = []
        
        for y in range(t_img.height):
            t_pixels.append([])
            for x in range(t_img.width):
                t_pixels[y].append(t_img.getpixel((x, y)))
        
        tiles[t] = t_pixels
    
    max_id: int = c.N - 1
    for tile in dirs:
        valid_neighbors[tile] = {"top": [], "left": [], "bottom": [], "right": []}
        for other in dirs:
            
            if tiles[tile][0] == tiles[other][max_id]:
                valid_neighbors[tile]["top"].append(other)
                
            if tiles[tile][max_id] == tiles[other][0]:
                valid_neighbors[tile]["bottom"].append(other)
                
            if [tiles[tile][x][0] for x in range(c.N)] == [tiles[tile][x][max_id] for x in range(c.N)]:
                valid_neighbors[tile]["left"].append(other)
                
            if [tiles[tile][x][max_id] for x in range(c.N)] == [tiles[tile][x][0] for x in range(c.N)]:
                valid_neighbors[tile]["right"].append(other)
    
    c.TILES = tiles
    c.VALID_NEIGHBORS = valid_neighbors
    return valid_neighbors
