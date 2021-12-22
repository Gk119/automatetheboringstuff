import os, shutil, re
import pathlib

print(pathlib.Path.home())
cwd = os.getcwd()
dest = cwd + '/dest'

#os.mkdir(dest)

reg = re.compile('.*?(\.pdf|\.jpg)')

for folderName, subfolders, filenames in os.walk(cwd):
    #print('The current folder is ' + folderName)

    #for subfolder in subfolders:
    #   print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        mf = reg.search(filename)
        #print(mf)
        if mf != None:
            print('FILE INSIDE ' + folderName + ': '+ filename)


    print('')