from PIL import Image, ImageFilter

def blur_background(image: Image.Image, **kwargs) -> Image.Image:
    radius = kwargs.get('radius', 10)
    threshold = kwargs.get('threshold', 240)
    orig = image.convert('RGBA')
    blurred = orig.filter(ImageFilter.GaussianBlur(radius=radius))
    datas = orig.getdata()
    mask = Image.new('L', orig.size, 0)
    mask_data = []
    for item in datas:
        if item[0] >= threshold and item[1] >= threshold and item[2] >= threshold:
            mask_data.append(255)
        else:
            mask_data.append(0)
    mask.putdata(mask_data)
    return Image.composite(blurred, orig, mask)
