from PIL import Image

def crop_aspect_ratio(image: Image.Image, **kwargs) -> Image.Image:
    ratio_w = kwargs.get('ratio_w', 16)
    ratio_h = kwargs.get('ratio_h', 9)
    target_ratio = ratio_w / ratio_h
    current_ratio = image.width / image.height
    if current_ratio > target_ratio:
        new_w = int(image.height * target_ratio)
        offset = (image.width - new_w) // 2
        return image.crop((offset, 0, offset + new_w, image.height))
    else:
        new_h = int(image.width / target_ratio)
        offset = (image.height - new_h) // 2
        return image.crop((0, offset, image.width, offset + new_h))
