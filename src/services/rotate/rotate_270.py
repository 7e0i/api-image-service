from PIL import Image

def rotate_270(image: Image.Image, **kwargs) -> Image.Image:
    return image.transpose(Image.Transpose.ROTATE_270)
