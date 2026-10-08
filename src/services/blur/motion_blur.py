from PIL import Image, ImageFilter

def motion_blur(image: Image.Image, **kwargs) -> Image.Image:
    return image.filter(ImageFilter.BLUR)
