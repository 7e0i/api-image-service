from PIL import Image

def rotate_custom(image: Image.Image, **kwargs) -> Image.Image:
    degrees = kwargs.get('degrees', 45)
    expand = kwargs.get('expand', True)
    return image.rotate(degrees, expand=expand)
