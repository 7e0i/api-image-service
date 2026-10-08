from PIL import Image, ImageDraw, ImageFont

def text_watermark(image: Image.Image, **kwargs) -> Image.Image:
    text = kwargs.get('text', 'ROMIX')
    opacity = kwargs.get('opacity', 128)
    position = kwargs.get('position', (10, 10))
    image = image.convert('RGBA')
    overlay = Image.new('RGBA', image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    font = ImageFont.load_default()
    draw.text(position, text, fill=(255, 255, 255, opacity), font=font)
    return Image.alpha_composite(image, overlay)
