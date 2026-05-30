import os

def get_project_files(folder_path):
    files = []

    for root, dirs, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.endswith(".py"):
                files.append(
                    os.path.join(root, filename)
                )

    return files


def read_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()