import os
import mimetypes
import hashlib
from datetime import datetime
import stat

def get_file_full_metadata(file_path):
    try:
        stats = os.stat(file_path)

        metadata = {
            "File Path": file_path,
            "File Name": os.path.basename(file_path),
            "Size (Bytes)": stats.st_size,
            "File Type": mimetypes.guess_type(file_path)[0] or "Unknown",
            "Created On": datetime.fromtimestamp(stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S'),
            "Last Modified": datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
            "Last Accessed": datetime.fromtimestamp(stats.st_atime).strftime('%Y-%m-%d %H:%M:%S'),
            "File Permissions": stat.filemode(stats.st_mode),
            "Owner (UID)": stats.st_uid,  # Optional: on Windows may just be 0 or current user ID
            "Hash SHA256": calculate_hash(file_path)
        }

        return metadata

    except Exception as e:
        return {"Error": str(e)}

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()
