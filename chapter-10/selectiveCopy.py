import os, shutil, re
import pathlib

#print(pathlib.Path.home())
cwd = os.getcwd()
dest = cwd + '/dest'

source = input("Enter the source folder path: ")
ext = input("Enter the extensions(with the '.') separated by space: ")
ext = ext.split()
regex = "(\\" + "|\\".join(ext) + ")$"

filelist = []

reg = re.compile(regex)

for folderName, subfolders, filenames in os.walk(source):

    for filename in filenames:
        mf = reg.search(filename)
        if mf:
            print('FILE INSIDE ' + folderName + ': '+ filename)
            filelist.append(folderName + '/' + filename)

if not pathlib.Path(dest).is_dir():
    os.mkdir(dest)

print("Copying files to " + dest)
for file in filelist:
    shutil.copy(file,dest)

print("Copying succesful")