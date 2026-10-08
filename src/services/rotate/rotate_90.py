from PIL import Image

def rotate_90(image: Image.Image, **kwargs) -> Image.Image:
    return image.transpose(Image.Transpose.ROTATE_90)
