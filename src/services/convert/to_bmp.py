from PIL import Image

def to_bmp(image: Image.Image, **kwargs) -> Image.Image:
    if image.mode in ('RGBA', 'P', 'LA'):
        return image.convert('RGB')
    return image
