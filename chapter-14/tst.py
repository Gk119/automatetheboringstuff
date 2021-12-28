import ezsheets
import os

os.chdir('./chapter-14')
ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
print(type(ss))

ss.downloadAsCSV()