from PIL import Image, ImageOps

def solarize(image: Image.Image, **kwargs) -> Image.Image:
    threshold = kwargs.get('threshold', 128)
    rgb = image.convert('RGB')
    return ImageOps.solarize(rgb, threshold=threshold)
