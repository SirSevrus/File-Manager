import os

def getFiles(dirPath):
    try:
        if os.path.isdir(dirPath):
            files = []
            countDirs = 0
            countFiles = 0
            nonAccessible = 0
            for root, dirs, file_names in os.walk(dirPath):
                countDirs += len(dirs)
                countFiles += len(file_names)
                for file_name in file_names:
                    try:
                        absPath = os.path.join(root, file_name)
                        files.append(absPath)
                    except PermissionError:
                        nonAccessible += 1
                        continue
            print(f'\nNumber of Dirs present: {countDirs}')
            print(f'Number of Files present: {countFiles}')
            print(f'Number of inaccessible files: {nonAccessible}')
            return files
        else:
            print('Invalid Directory...')
            exit(-1)
    except KeyboardInterrupt:
        exit(-1)

files = getFiles("C:\\")
