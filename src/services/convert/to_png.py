from PIL import Image

def to_png(image: Image.Image, **kwargs) -> Image.Image:
    return image.convert('RGBA')
