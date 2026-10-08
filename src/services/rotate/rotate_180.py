from PIL import Image

def rotate_180(image: Image.Image, **kwargs) -> Image.Image:
    return image.transpose(Image.Transpose.ROTATE_180)
