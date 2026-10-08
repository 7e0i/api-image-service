from PIL import Image, ImageOps

def grayscale(image: Image.Image, **kwargs) -> Image.Image:
    return ImageOps.grayscale(image)
