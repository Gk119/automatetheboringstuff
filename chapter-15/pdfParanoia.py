import os, re
import PyPDF2

reg = re.compile('(\.pdf)$')
source = input("Enter the folder path: ")
opt = input("Enter \n1. To Encrypt \n2. To Decrypt\n")
if opt == '1':
    password = input("Enter the Encryption password: ")


    for folderName, subfolders, filenames in os.walk(source):

        for filename in filenames:
            mf = reg.search(filename)
            if mf:
                print("Encrypting: " + folderName + '/' + filename)
                pdfReader = PyPDF2.PdfFileReader(open(folderName + '/' + filename, 'rb'))
                pdfWriter = PyPDF2.PdfFileWriter()

                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))

                pdfWriter.encrypt(password)
                encryptedpdf = open("File saved as: " + folderName + '/' +  filename.replace('.pdf','') + '_encrypted.pdf', 'wb')
                pdfWriter.write(encryptedpdf)
                encryptedpdf.close()
                print(folderName + '/' +  filename.replace('.pdf','') + '_encrypted.pdf')

elif opt == '2':
    password = input("Enter the Decryption password: ")
    for folderName, subfolders, filenames in os.walk(source):

        for filename in filenames:
            mf = reg.search(filename)
            if mf:
                print("Decrypting: " + folderName + '/' + filename)
                pdfReader = PyPDF2.PdfFileReader(open(folderName + '/' + filename, 'rb'))
                if pdfReader.isEncrypted:
                    pdfReader.decrypt(password)
                    pdfWriter = PyPDF2.PdfFileWriter()
                    
                    for pageNum in range(pdfReader.numPages):
                        pdfWriter.addPage(pdfReader.getPage(pageNum))
                    
                    decryptedpdf = open("File saved as: " + folderName + '/' +  filename.replace('_encrypted.pdf','') + '.pdf', 'wb')
                    pdfWriter.write(decryptedpdf)
                    decryptedpdf.close()
                    print(folderName + '/' +  filename.replace('_encrypted.pdf','') + '.pdf')






