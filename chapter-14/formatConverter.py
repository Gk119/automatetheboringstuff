import ezsheets
import os

os.chdir("./chapter-14")
filename = input("Enter the path and filename of the spreadsheet: ")
ss = ezsheets.upload(filename)

ss.downloadAsCSV()
ss.downloadAsODS()