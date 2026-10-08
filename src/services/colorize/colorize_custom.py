from PIL import Image, ImageOps

def colorize_custom(image: Image.Image, **kwargs) -> Image.Image:
    black = kwargs.get('black', 'black')
    white = kwargs.get('white', 'white')
    gray = ImageOps.grayscale(image)
    return ImageOps.colorize(gray, black=black, white=white)
