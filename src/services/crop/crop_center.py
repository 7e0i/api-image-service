from PIL import Image

def crop_center(image: Image.Image, **kwargs) -> Image.Image:
    w = kwargs.get('width', image.width // 2)
    h = kwargs.get('height', image.height // 2)
    left = (image.width - w) // 2
    top = (image.height - h) // 2
    return image.crop((left, top, left + w, top + h))
