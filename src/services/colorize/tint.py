from PIL import Image, ImageOps

def tint(image: Image.Image, **kwargs) -> Image.Image:
    color = kwargs.get('color', '#ff5733')
    gray = ImageOps.grayscale(image)
    return ImageOps.colorize(gray, black='black', white=color)
