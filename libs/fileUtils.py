import os

def get_files_data(root_path):
    files = {}
    count = 0
    for root, dirs, files_list in os.walk(root_path):
        for file in files_list:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                size = round(os.path.getsize(file_path) / (1024 ** 2), 2)  # Size in MB
                files[file_path] = size
                count += 1
    return count, files

# Example Usage
    noFiles, files = get_files_data("c:\\")
