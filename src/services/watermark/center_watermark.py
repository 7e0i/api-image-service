from PIL import Image, ImageDraw, ImageFont

def center_watermark(image: Image.Image, **kwargs) -> Image.Image:
    text = kwargs.get('text', 'ROMIX')
    opacity = kwargs.get('opacity', 120)
    image = image.convert('RGBA')
    overlay = Image.new('RGBA', image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    font = ImageFont.load_default()
    pos = (image.width // 2 - len(text) * 4, image.height // 2 - 8)
    draw.text(pos, text, fill=(255, 255, 255, opacity), font=font)
    return Image.alpha_composite(image, overlay)
