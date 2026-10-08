from PIL import Image

def resize(image: Image.Image, **kwargs) -> Image.Image:
    width = kwargs.get('width', image.width)
    height = kwargs.get('height', image.height)
    return image.resize((int(width), int(height)), Image.Resampling.LANCZOS)
