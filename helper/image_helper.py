import os

from PIL import Image


class ImageHelper:
    def __init__(self, path: str) -> None:
        assert os.path.exists(path), "Image doesn't exist !"
        self.__path: str = path
        self.__image = Image.open(path)
        
    def rotate_image(self, angle: int) -> None:
        self.__image.rotate(angle)

    def get_image_path(self) -> str:
        return self.__path
    
    def get_image(self) -> Image:
        return self.__image
