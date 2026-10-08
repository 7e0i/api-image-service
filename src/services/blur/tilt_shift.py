from PIL import Image, ImageFilter

def tilt_shift(image: Image.Image, **kwargs) -> Image.Image:
    radius = kwargs.get('radius', 5)
    blurred = image.filter(ImageFilter.GaussianBlur(radius=radius))
    mask = Image.new('L', image.size, 0)
    for y in range(image.height):
        if y < image.height * 0.3 or y > image.height * 0.7:
            for x in range(image.width):
                mask.putpixel((x, y), 255)
    return Image.composite(blurred, image, mask)
