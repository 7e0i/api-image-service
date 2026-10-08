import os
from PIL import Image

def metadata(filename: str, **kwargs) -> dict:
    db_path = kwargs.get('db_path') or os.getenv('imagedb_path', './data/imagedb')
    full_path = os.path.join(db_path, filename)
    if not os.path.exists(full_path):
        raise FileNotFoundError(f'Image not found: {filename}')
    with Image.open(full_path) as img:
        return {
            'filename': filename,
            'format': img.format,
            'mode': img.mode,
            'size': img.size,
            'width': img.width,
            'height': img.height,
            'file_size_bytes': os.path.getsize(full_path)
        }
