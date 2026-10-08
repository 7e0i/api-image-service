from PIL import Image, ImageFilter

def radial_blur(image: Image.Image, **kwargs) -> Image.Image:
    radius = kwargs.get('radius', 4)
    return image.filter(ImageFilter.GaussianBlur(radius=radius))
