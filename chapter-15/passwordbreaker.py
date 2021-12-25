
import PyPDF2

file = input("Enter the filename including the path: ")
dict = open("dictionary.txt", 'r')
words = dict.readlines()

pdfReader = PyPDF2.PdfFileReader(open(file, 'rb'))

for word in words:
    if pdfReader.decrypt(word.lower()) == 1:
        print("the password is: " + word.lower())
    elif pdfReader.decrypt(word.upper()) == 1:
        print("the password is: " + word.upper())
