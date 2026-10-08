from PIL import Image, ImageOps

def duotone(image: Image.Image, **kwargs) -> Image.Image:
    black = kwargs.get('black', '#000080')
    white = kwargs.get('white', '#ffcc00')
    gray = ImageOps.grayscale(image)
    return ImageOps.colorize(gray, black=black, white=white)
