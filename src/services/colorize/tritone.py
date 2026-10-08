from PIL import Image, ImageOps

def tritone(image: Image.Image, **kwargs) -> Image.Image:
    black = kwargs.get('black', '#1a1a1a')
    mid = kwargs.get('mid', '#e74c3c')
    white = kwargs.get('white', '#f1c40f')
    gray = ImageOps.grayscale(image)
    return ImageOps.colorize(gray, black=black, white=white, mid=mid)
