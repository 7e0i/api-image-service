from PIL import Image

def remove_background(image: Image.Image, **kwargs) -> Image.Image:
    threshold = kwargs.get('threshold', 240)
    image = image.convert('RGBA')
    datas = image.getdata()
    new_data = []
    for item in datas:
        if item[0] >= threshold and item[1] >= threshold and item[2] >= threshold:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
    image.putdata(new_data)
    return image
