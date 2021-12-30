import ezsheets, os

os.chdir("./chapter-14")
ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')

for rowNum in range(2, ss[0].rowCount):
    try:
        if not (int(ss[0].getRow(rowNum)[0]) * int(ss[0].getRow(rowNum)[1]) == int(ss[0].getRow(rowNum)[2])):
            print(rowNum)
    except:
        continue


