import openpyxl,sys

wb = openpyxl.Workbook()
sheet = wb.active

for i in range(1,len(sys.argv)):
    file = open(sys.argv[i], 'r')
    lines = file.readlines()
    for j in range(len(lines)):
        sheet.cell(row= j + 1, column= i).value = lines[j]

wb.save('tst.xlsx')
