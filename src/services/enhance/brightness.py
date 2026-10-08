from PIL import Image, ImageEnhance

def brightness(image: Image.Image, **kwargs) -> Image.Image:
    factor = kwargs.get('factor', 1.2)
    return ImageEnhance.Brightness(image).enhance(factor)
