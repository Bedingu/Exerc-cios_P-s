import PyPDF2

pdfFileObj = open (r"C:\Users\bedin\OneDrive\Área de Trabalho\Projetos_Pós\Situação Cadastral.pdf",'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)

print(pageObj.extractText())

pdfFileObj.close()