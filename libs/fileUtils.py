import os
import time

def get_files_data(root_path):
    files = {}
    count = 0
    print(f'[+] Starting to Scan Files in directory - {root_path}')
    t1 = time.time()
    for root, dirs, files_list in os.walk(root_path):
        for file in files_list:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                size = round(os.path.getsize(file_path) / (1024 ** 2), 2)  # Size in MB
                files[file_path] = size
                count += 1
    t2 = time.time()
    print(f'[+] File Scanning Finished, Scanned {str(count)} files')
    print(f'[*] Time Elapsed : {(t2 - t1):.2f} Seconds')
    return count, files

# Example Usage
    noFiles, files = get_files_data("c:\\")
