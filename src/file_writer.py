def write_file(file_path, content):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)