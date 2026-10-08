import os
from PIL import Image

def get_image(filename: str, **kwargs) -> Image.Image:
    db_path = kwargs.get('db_path') or os.getenv('imagedb_path', './data/imagedb')
    full_path = os.path.join(db_path, filename)
    if not os.path.exists(full_path):
        raise FileNotFoundError(f'Image not found: {filename}')
    return Image.open(full_path)
