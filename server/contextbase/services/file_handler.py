from fastapi import UploadFile
import os
import uuid

from contextbase.core.config import settings

os.makedirs(settings.UPLOAD_DIR, exist_ok=True)


def save_upload(file: UploadFile):
    """save file, returns (path, original_name, size)"""
    original = file.filename or "unknown"
    ext = os.path.splitext(original)[1] or ".pdf"
    path = os.path.join(settings.UPLOAD_DIR, f"{uuid.uuid4()}{ext}")
    
    content = file.file.read()
    with open(path, "wb") as f:
        f.write(content)
    
    return path, original, len(content)


def delete_upload(path):
    try:
        if os.path.exists(path):
            os.remove(path)
            return True
    except:
        pass
    return False


def format_size(bytes):
    if bytes < 1024:
        return f"{bytes} B"
    elif bytes < 1024 * 1024:
        return f"{bytes/1024:.1f} KB"
    return f"{bytes/(1024*1024):.1f} MB"
