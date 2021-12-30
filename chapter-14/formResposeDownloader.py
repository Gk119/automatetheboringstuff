import ezsheets, os

os.chdir("./chapter-14")
formid = input("Enter the form ID: ")
ss = ezsheets.Spreadsheet(formid)
emailList = []
for rowNum in range(2, ss[0].rowCount):
    email = ss[0].getRow(rowNum)[2]
    if(email != ''):
        emailList.append(email)

print(emailList)
file = open("emailist.txt", 'w')
file.write('\n'.join(emailList))
file.close()