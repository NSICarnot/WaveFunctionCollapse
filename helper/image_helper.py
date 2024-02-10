import os
import constants as c

from PIL import Image

def equals(img1: Image.Image, img2: Image.Image) -> bool:
    assert img1.size == img2.size, "Both images must hav the same size"
    
    root: int = img1.width
    for y in range(root):
        for x in range(root):
            if not img1.getpixel((x, y)) == img2.getpixel((x, y)):
                return False
            
    return True

def folder_image_count(dir: str) -> int:
    return len(os.listdir(dir))

# TODO: Change stuff because it's a 180° rotation
def reflect_image(image: Image.Image) -> Image.Image:
    width: int = image.width
    height: int = image.height
    
    new_image = Image.new("RGBA", (width, height))
    
    for y in range(height):
        for x in range(width):
            new_image.putpixel((width - x - 1, height - y - 1), image.getpixel((x, y)))
    
    return new_image


def remove_duplicate(dir: str) -> None:
    """
    Repeat for all images:
    If an image is equal to an another image. Then remove the duplicate image.
    """
    for image in os.listdir(dir):
        if os.path.exists(f"{dir}/{image}"):
            image_pil = Image.open(f"{dir}/{image}")
            for other in os.listdir(dir):
                other_pil = Image.open(f"{dir}/{other}")
                if equals(image_pil, other_pil):
                    if not image == other:
                        os.remove(f"{dir}/{other}")
        else:
            continue


def cut_in_n_times_n(image: Image.Image, n: int = 3) -> None:
    """
    Cut the image in n*n pixels
    """
    assert type(n) is int, "Argument n must be an integer"
    
    count: int = 0
    for y in range(0, image.height - n + 1):
        for x in range(0, image.width - n + 1):
            temp_pattern = Image.new("RGBA", (n, n))
            for i in range(n):
                for j in range(n):
                    temp_pattern.putpixel((j, i), (image.getpixel((x+j, y+i))))
            temp_pattern.save(f"image/temp/temp{count}.png")
            count += 1
            
            # reflect_image(temp_pattern).save(f"image/temp/temp{count}.png")
            # count += 1
            
            for i in range(1, 4):
                temp_pattern = temp_pattern.rotate(90 * i)
                temp_pattern.save(f"image/temp/temp{count}.png")
       
    remove_duplicate(c.TEMP_DIR)
