from PIL import Image, ImageColor

def change_background(image: Image.Image, **kwargs) -> Image.Image:
    color = kwargs.get('color', '#ffffff')
    threshold = kwargs.get('threshold', 240)
    image = image.convert('RGBA')
    bg_color = ImageColor.getrgb(color)
    bg = Image.new('RGBA', image.size, bg_color + (255,))
    datas = image.getdata()
    new_data = []
    for item in datas:
        if item[0] >= threshold and item[1] >= threshold and item[2] >= threshold:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
    image.putdata(new_data)
    return Image.alpha_composite(bg, image)
