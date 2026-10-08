import os
from PIL import Image

def save_image(image: Image.Image, **kwargs) -> str:
    db_path = kwargs.get('db_path') or os.getenv('imagedb_path', './data/imagedb')
    filename = kwargs.get('filename', 'image.png')
    os.makedirs(db_path, exist_ok=True)
    full_path = os.path.join(db_path, filename)
    image.save(full_path)
    return full_path
