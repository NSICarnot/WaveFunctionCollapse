import os

from PIL import Image


def cut_in_n_times_n(image: Image.Image, n: int = 3) -> None:
    """
    Cut the image in n*n pixels
    """
    assert type(n) is int, "Argument n must be an integer"
    
    if image.width % n != 0 or image.height % n != 0:
        image.resize((image.width - image.width % n, image.height - image.height % n))
    
    count: int = 0
    for y in range(0, image.height // n, n):
        for x in range(0, image.width // n, n):
            temp_pattern = Image.new("RGBA", (n, n))
            for i in range(n):
                for j in range(n):
                    temp_pattern.putpixel((j, i), (image.getpixel((x+j, y+i))))
            temp_pattern.save(f"image/temp/temp{count}.png")
            count += 1
