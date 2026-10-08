from PIL import Image, ImageColor

def solid_background(image: Image.Image, **kwargs) -> Image.Image:
    color = kwargs.get('color', '#ffffff')
    image = image.convert('RGBA')
    bg_rgb = ImageColor.getrgb(color)
    bg = Image.new('RGBA', image.size, bg_rgb + (255,))
    return Image.alpha_composite(bg, image)
