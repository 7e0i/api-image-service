from PIL import Image, ImageOps

def auto_contrast(image: Image.Image, **kwargs) -> Image.Image:
    cutoff = kwargs.get('cutoff', 2)
    if image.mode in ('RGBA', 'LA'):
        rgb = image.convert('RGB')
        res = ImageOps.autocontrast(rgb, cutoff=cutoff)
        res = res.convert('RGBA')
        res.putalpha(image.getchannel('A'))
        return res
    return ImageOps.autocontrast(image, cutoff=cutoff)
