from PIL import Image

def web_compress(image: Image.Image, **kwargs) -> Image.Image:
    quality = kwargs.get('quality', 70)
    return image
