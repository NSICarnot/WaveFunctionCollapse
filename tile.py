import constants as c
import random as r


class Tile:
    def __init__(self) -> None:
        self.tile = None
        self.possible_tiles: dict = {x: True for x in c.TILES.keys()}
        self.entropy: int = len({tile: value for tile, value in self.possible_tiles.items() if value})
        
    def recalculate_entropy(self) -> None:
        self.entropy: int = len({tile: value for tile, value in self.possible_tiles.items() if value})
        
    def recalculate_neighbors(self) -> None:
        ...
        
    def collapse(self) -> None:
        self.tile = r.choice([x for x, y in self.possible_tiles.items() if y])
        
    def get_entropy(self) -> int:
        return self.entropy