from PIL import Image, ImageFilter

def box_blur(image: Image.Image, **kwargs) -> Image.Image:
    radius = kwargs.get('radius', 2)
    return image.filter(ImageFilter.BoxBlur(radius=radius))
