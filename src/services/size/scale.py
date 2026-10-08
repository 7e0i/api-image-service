from PIL import Image

def scale(image: Image.Image, **kwargs) -> Image.Image:
    factor = kwargs.get('factor', 1.0)
    w = int(image.width * factor)
    h = int(image.height * factor)
    return image.resize((w, h), Image.Resampling.LANCZOS)
