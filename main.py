from PIL import Image

class Image:
    def __init__(self, path: str) -> None:
        self.__path: str = path
        self.__image = ...
