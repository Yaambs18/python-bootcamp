import PyPDF2

f = open('sample.pdf', 'rb')

pdf_reader = PyPDF2.PdfFileReader(f)

print(pdf_reader.numPages)

page_one = pdf_reader.getPage(0)

page_data = page_one.extractText()

print(page_data)

f.close()