from PIL import Image, ImageOps

def pad(image: Image.Image, **kwargs) -> Image.Image:
    width = kwargs.get('width', 300)
    height = kwargs.get('height', 300)
    color = kwargs.get('color', (0, 0, 0))
    return ImageOps.pad(image, (width, height), color=color)
