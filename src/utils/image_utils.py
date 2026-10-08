import io
from PIL import Image

def bytes_to_image(image_bytes: bytes) -> Image.Image:
    return Image.open(io.BytesIO(image_bytes))

def image_to_bytes(image: Image.Image, format: str = "PNG", **kwargs) -> bytes:
    buffer = io.BytesIO()
    if format.upper() in ["JPEG", "JPG"] and image.mode in ("RGBA", "P"):
        image = image.convert("RGB")
    image.save(buffer, format=format, **kwargs)
    return buffer.getvalue()
