import os
from hasher import calculate_hash


def get_files(folder):
    files = []

    for root, directories, filenames in os.walk(folder):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            files.append(file_path)

    return files


def create_baseline(folder):
    baseline = {}

    files = get_files(folder)

    for file_path in files:
        file_hash = calculate_hash(file_path)
        baseline[file_path] = file_hash

    return baseline


def check_integrity(folder, baseline):
    current_files = get_files(folder)

    current_hashes = {}

    for file_path in current_files:
        current_hashes[file_path] = calculate_hash(file_path)

    modified_files = []
    added_files = []
    deleted_files = []

    for file_path in current_hashes:
        if file_path in baseline:
            if current_hashes[file_path] != baseline[file_path]:
                modified_files.append(file_path)

    for file_path in current_hashes:
        if file_path not in baseline:
            added_files.append(file_path)

    for file_path in baseline:
        if file_path not in current_hashes:
            deleted_files.append(file_path)

    return modified_files, added_files, deleted_files