import uuid
from pathlib import Path


def generate_unique_file_name(instance, filename) -> str:
    return f"{uuid.uuid4()}{Path(filename).suffix}"
