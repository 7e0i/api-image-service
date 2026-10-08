from PIL import Image, ImageOps

def invert_colors(image: Image.Image, **kwargs) -> Image.Image:
    if image.mode in ('RGBA', 'LA'):
        rgb = image.convert('RGB')
        inv = ImageOps.invert(rgb).convert('RGBA')
        inv.putalpha(image.getchannel('A'))
        return inv
    return ImageOps.invert(image)
