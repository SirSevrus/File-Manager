import os
import time

def init(dirPath):
    if os.path.isdir(dirPath):
        files = []
        try:
            for root, dirs, file_names in os.walk(dirPath):
                for file_name in file_names:
                    try:
                        absPath = os.path.join(root, file_name)
                        files.append(absPath)
                    except PermissionError:
                        continue
        except KeyboardInterrupt:
            exit(-1)
        return files
    else:
        print('Invalid Directory...')
        exit(-1)

def getFiles(files):
    countDirs = len(set(os.path.dirname(file) for file in files))
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
