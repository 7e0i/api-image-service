import os

def delete_image(filename: str, **kwargs) -> bool:
    db_path = kwargs.get('db_path') or os.getenv('imagedb_path', './data/imagedb')
    full_path = os.path.join(db_path, filename)
    if os.path.exists(full_path):
        os.remove(full_path)
        return True
    return False
