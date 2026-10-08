from PIL import Image, ImageEnhance

def sharpness(image: Image.Image, **kwargs) -> Image.Image:
    factor = kwargs.get('factor', 1.5)
    return ImageEnhance.Sharpness(image).enhance(factor)
