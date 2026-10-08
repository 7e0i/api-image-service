from PIL import Image

def reduce_palette(image: Image.Image, **kwargs) -> Image.Image:
    colors = kwargs.get('colors', 128)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    return image.quantize(colors=colors).convert('RGB')
