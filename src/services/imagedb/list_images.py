import os

def list_images(**kwargs) -> list:
    db_path = kwargs.get('db_path') or os.getenv('imagedb_path', './data/imagedb')
    if not os.path.exists(db_path):
        return []
    return [f for f in os.listdir(db_path) if os.path.isfile(os.path.join(db_path, f))]
