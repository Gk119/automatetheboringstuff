import os, re

regex = re.compile(input("Enter the Regex: "))
files = os.listdir()
for filename in files:
    if re.search(r".*txt$", filename):
        file = open(filename, 'r')
        content = file.read()
        for x in regex.findall(content):
            print(x)
#print(files)