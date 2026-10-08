from PIL import Image, ImageOps

def fit(image: Image.Image, **kwargs) -> Image.Image:
    width = kwargs.get('width', 300)
    height = kwargs.get('height', 300)
    return ImageOps.fit(image, (width, height), Image.Resampling.LANCZOS)
