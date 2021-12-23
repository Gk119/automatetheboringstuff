import os, shutil, re
import pathlib

source = input("Enter the folder path: ")

for folderName, subfolders, filenames in os.walk(source):

    for filename in filenames:
        try:
            filesizeMB = int((os.path.getsize(folderName + '/' + filename))/(1024*1024))
            if  filesizeMB > 100:
                print('FILE: ' + folderName + '/'+ filename + '  with size ' + str(filesizeMB) + 'MB')
        except FileNotFoundError:
            continue