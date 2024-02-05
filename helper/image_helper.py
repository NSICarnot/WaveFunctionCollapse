import os

from PIL import Image


def cut_in_n_times_n(image: Image.Image, n: int = 3) -> None:
    """
    Cut the image in n*n pixels
    """
    assert type(n) is int, "Argument n must be an integer"
    
    if image.width % 3 != 0 or image.height % 3 != 0:
        image.resize((image.width - image.width % 3, image.height - image.height % 3))
    
    for y in range(image.height // 3):
        for x in range(image.width // 3):
            ...
