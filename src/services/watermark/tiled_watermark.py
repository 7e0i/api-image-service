from PIL import Image, ImageDraw, ImageFont

def tiled_watermark(image: Image.Image, **kwargs) -> Image.Image:
    text = kwargs.get('text', 'ROMIX')
    opacity = kwargs.get('opacity', 64)
    image = image.convert('RGBA')
    overlay = Image.new('RGBA', image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    font = ImageFont.load_default()
    step_x = kwargs.get('step_x', 150)
    step_y = kwargs.get('step_y', 100)
    for y in range(0, image.height, step_y):
        for x in range(0, image.width, step_x):
            draw.text((x, y), text, fill=(255, 255, 255, opacity), font=font)
    return Image.alpha_composite(image, overlay)
