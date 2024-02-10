from PIL import Image
import numpy as np

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
    
    return valid_neighbors
