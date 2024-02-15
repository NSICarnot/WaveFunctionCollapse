import constants as c
import random as r


class Tile:
    def __init__(self) -> None:
        self.tile = None
        self.is_collapsed: bool = False
        self.possible_tiles: dict = {x: True for x in c.TILES.keys()}
        self.entropy: int = len({tile: value for tile, value in self.possible_tiles.items() if value})
        
    def recalculate_entropy(self) -> None:
        self.entropy: int = len({tile: value for tile, value in self.possible_tiles.items() if value})
        
    def recalculate_neighbors(self, wave: list[list["Tile"]], x: int, y: int) -> None:
        def update(w):
            self.possible_tiles = {t: False for t in self.possible_tiles.keys() if not t in c.VALID_NEIGHBORS[w.tile]}
        
        # y-1 -> y+1 | x-1 -> x+1
        if y > 0 and wave[y-1][x].is_collapsed:
            update(wave[y-1][x])
        if y < c.OUTPUT_HEIGHT - 1 and wave[y+1][x].is_collapsed:
            update(wave[y+1][x])
        if x > 0 and wave[y][x-1].is_collapsed:
            update(wave[y][x-1])
        if x < c.OUTPUT_WIDTH - 1 and wave[y][x+1].is_collapsed:
            update(wave[y][x+1])
        
    def collapse(self) -> None:
        self.tile = r.choice([x for x, y in self.possible_tiles.items() if y])
        
    def get_entropy(self) -> int:
        return self.entropy