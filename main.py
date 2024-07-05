import os

def getFiles(dirPath):
    if os.path.isdir(dirPath):
        files = []
        countDirs = 0
        countFiles = 0
        nonAcessible = 0
        c = 0
        for i in os.walk(dirPath):
            if c < 5:
                print("|" + '#' * c, end='\r')
                c += 1
            elif c >= 5:
                c = 0
            countDirs += len(i[1])
            countFiles += len(i[2])
            try:
                for j in i[2]:
                    absPath = i[0]
                    files.append(os.path.join(absPath, j))
            
            except os.PermissionError:
                nonAcessible += 1
                pass
        print(f'\nNumber of Dirs present : {str(countDirs)}\nNumber of Files Present : {str(countFiles)}')
        return files
    else:
        print('Invallid Directory...')
        exit(-1)

files = getFiles("C:\\")

