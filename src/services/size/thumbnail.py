from PIL import Image

def thumbnail(image: Image.Image, **kwargs) -> Image.Image:
    size = kwargs.get('size', (128, 128))
    clone = image.copy()
    clone.thumbnail(size, Image.Resampling.LANCZOS)
    return clone
