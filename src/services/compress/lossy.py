from PIL import Image

def lossy(image: Image.Image, **kwargs) -> Image.Image:
    quality = kwargs.get('quality', 50)
    return image
