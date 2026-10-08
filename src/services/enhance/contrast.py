from PIL import Image, ImageEnhance

def contrast(image: Image.Image, **kwargs) -> Image.Image:
    factor = kwargs.get('factor', 1.5)
    return ImageEnhance.Contrast(image).enhance(factor)
