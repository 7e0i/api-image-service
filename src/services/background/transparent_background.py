from PIL import Image

def transparent_background(image: Image.Image, **kwargs) -> Image.Image:
    color = kwargs.get('color', (255, 255, 255))
    tolerance = kwargs.get('tolerance', 30)
    image = image.convert('RGBA')
    datas = image.getdata()
    new_data = []
    for item in datas:
        if all(abs(item[i] - color[i]) <= tolerance for i in range(3)):
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
    image.putdata(new_data)
    return image
