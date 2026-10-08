from src.services.background.remove_background import remove_background
from src.services.enhance.sharpness import sharpness
from src.services.size.resize import resize
from src.services.convert.to_jpeg import to_jpeg
from src.services.compress.lossy import lossy
from src.services.filter.grayscale import grayscale
from src.services.watermark.text_watermark import text_watermark
from src.services.blur.gaussian_blur import gaussian_blur
from src.services.rotate.rotate_custom import rotate_custom
from src.services.crop.crop_box import crop_box
from src.services.colorize.colorize_custom import colorize_custom

processor = {
    "background": remove_background,
    "enhance": sharpness,
    "size": resize,
    "convert": to_jpeg,
    "compress": lossy,
    "filter": grayscale,
    "watermark": text_watermark,
    "blur": gaussian_blur,
    "rotate": rotate_custom,
    "crop": crop_box,
    "colorize": colorize_custom
}

def process(operation, image, **kwargs):
    handler = processor.get(operation)
    if not handler:
        raise ValueError(f"unsupported operation: {operation}")
    return handler(image, **kwargs)