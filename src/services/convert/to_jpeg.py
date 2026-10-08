from PIL import Image

def to_jpeg(image: Image.Image, **kwargs) -> Image.Image:
    if image.mode in ('RGBA', 'P', 'LA'):
        return image.convert('RGB')
    return image
