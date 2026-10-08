from PIL import Image, ImageFilter

def gaussian_blur(image: Image.Image, **kwargs) -> Image.Image:
    radius = kwargs.get('radius', 2)
    return image.filter(ImageFilter.GaussianBlur(radius=radius))
