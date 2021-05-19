import os
import shutil
import time

def main():
    deletedFolders = 0
    deletedFiles = 0
    
    path = input('Input the path')
    
    days = input('Input the days')
    
    seconds = time.time() - (days * 24 * 60 * 60)
    
    if os.path.exists(path):
        for rootFolders, folders, files in os.walk(path):
            if seconds >= getFileOrFolderAge(rootFolders) :
                removeFolder(rootFolders)
                deletedFolders += 1
                break
            
            else:
                for folder in folders:
                    folderPath = os.path.join(rootFolders,folder)
                
                    if seconds >= getFileOrFolderAge(folder):
                        removeFolder(folderPath)
                        deletedFolders += 1
                    
                for file in files:
                    filePath = os.path.join(rootFolders,file)
                    
                    if seconds >= getFileOrFolderAge(file):
                        removeFile(filePath)
                        deletedFiles += 1
                        
        else:
            if seconds >= getFileOrFolderAge(path):
                removeFile(path)
                deletedFiles += 1
                
        print("Total folders deleted: " + deletedFolders)
        print("Total files deleted: " + deletedFiles)
                
    else:
        print('Cannot find ' + path)
        
            
def removeFolder(path):
    if not shutil.rmtree(path):
        print('Removed successfully' + path)
        
    else:
        print('Unable to remove ' + path)
            
def removeFile(path):
    if not os.remove(path):
        print('Removed successfully' + path)
        
    else:
        print('Unable to remove' + path)
                
def getFileOrFolderAge(path):
    ctime = os.stat(path).st_ctime
    return ctime

if __name__ == '__main__':
    main()