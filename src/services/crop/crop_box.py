from PIL import Image

def crop_box(image: Image.Image, **kwargs) -> Image.Image:
    left = kwargs.get('left', 0)
    top = kwargs.get('top', 0)
    right = kwargs.get('right', image.width)
    bottom = kwargs.get('bottom', image.height)
    return image.crop((left, top, right, bottom))
