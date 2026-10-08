from PIL import Image

def image_watermark(image: Image.Image, **kwargs) -> Image.Image:
    watermark_img = kwargs.get('watermark_img')
    position = kwargs.get('position', (0, 0))
    if not watermark_img:
        return image
    image = image.convert('RGBA')
    watermark_img = watermark_img.convert('RGBA')
    image.paste(watermark_img, position, watermark_img)
    return image
