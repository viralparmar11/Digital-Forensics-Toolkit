import hashlib

def generate_hash(file_path, method="sha256"):
    hash_func = getattr(hashlib, method.lower())()

    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            hash_func.update(chunk)

    return hash_func.hexdigest()

def verify_hash(file_path, expected_hash, method="sha256"):
    return generate_hash(file_path, method) == expected_hash
