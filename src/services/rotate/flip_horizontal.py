from PIL import Image

def flip_horizontal(image: Image.Image, **kwargs) -> Image.Image:
    return image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
