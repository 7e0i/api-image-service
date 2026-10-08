from PIL import Image, ImageEnhance

def color_balance(image: Image.Image, **kwargs) -> Image.Image:
    factor = kwargs.get('factor', 1.3)
    return ImageEnhance.Color(image).enhance(factor)
