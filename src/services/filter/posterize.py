from PIL import Image, ImageOps

def posterize(image: Image.Image, **kwargs) -> Image.Image:
    bits = kwargs.get('bits', 4)
    rgb = image.convert('RGB')
    return ImageOps.posterize(rgb, bits)
