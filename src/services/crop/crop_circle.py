from PIL import Image, ImageDraw

def crop_circle(image: Image.Image, **kwargs) -> Image.Image:
    image = image.convert('RGBA')
    side = min(image.width, image.height)
    left = (image.width - side) // 2
    top = (image.height - side) // 2
    cropped = image.crop((left, top, left + side, top + side))
    mask = Image.new('L', (side, side), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, side, side), fill=255)
    output = Image.new('RGBA', (side, side), (0, 0, 0, 0))
    output.paste(cropped, (0, 0), mask)
    return output
