from PIL import Image
import numpy as np

"""
The algorythm of finding valid neighbors is different according to the simulation demands.

So the chosen algorythm is about a colors. For being a valid neighbor, the tile next to itself must have the same colors. 
Then a dictionary with each tiles is creating and inside it, a new dictionary is created which contains top, left, bottom and right valid tiles.

Algorythm:

1 - Load all tiles pixels list on a numpy list Then save them in a dictionary.
2 - For each tiles. Compute all other tiles and check their validity.
"""
