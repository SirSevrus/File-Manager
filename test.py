# 38 Seconds
import os
import time

def init(dirPath):
    if os.path.isdir(dirPath):
        files = []
        try:
            for entry in os.scandir(dirPath):
                if entry.is_file():
                    files.append(entry.path)
                elif entry.is_dir():
                    files.extend(init(entry.path))  # Recursively scan directories
        except PermissionError:
            pass  # Skip files/directories that raise PermissionError
        except KeyboardInterrupt:
            exit(-1)
        return files
    else:
        print('Invalid Directory...')
        exit(-1)

def getFiles(files):
    dirs = set(os.path.dirname(file) for file in files)
    countDirs = len(dirs)
    countFiles = len(files)

    print(f'\nNumber of Dirs present: {countDirs}')
    print(f'Number of Files present: {countFiles}')

dirPath = "C:\\"
start_time = time.time()
files = init(dirPath)
init_time = time.time()
getFiles(files)
end_time = time.time()

print(f'\nTime taken for init: {init_time - start_time:.2f} seconds')
print(f'Time taken for getFiles: {end_time - init_time:.2f} seconds')
print(f'Total time elapsed: {end_time - start_time:.2f} seconds')
