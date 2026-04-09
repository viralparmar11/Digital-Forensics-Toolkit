import os
import datetime
from PIL import Image
from PIL.ExifTags import TAGS

def scan_directory(path):
    file_info_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            info = get_file_metadata(full_path)
            file_info_list.append(info)
    return file_info_list

def get_file_metadata(file_path):
    stats = os.stat(file_path)
    metadata = {
        "File": file_path,
        "Size": stats.st_size,
        "Created": datetime.datetime.fromtimestamp(stats.st_ctime),
        "Modified": datetime.datetime.fromtimestamp(stats.st_mtime)
    }

    if file_path.lower().endswith(('.jpg', '.jpeg', '.png')):
        metadata.update(get_exif_data(file_path))

    return metadata

def get_exif_data(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        readable_exif = {}
        if exif_data:
            for tag, value in exif_data.items():
                decoded = TAGS.get(tag, tag)
                readable_exif[decoded] = value
        return {"EXIF": readable_exif}
    except Exception as e:
        return {"EXIF": str(e)}
