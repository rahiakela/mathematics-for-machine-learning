import os
from PyPDF2 import PdfFileReader, PdfFileWriter


def pdf_splitter(path):
  pdf_in_file = open(path, "rb")
  pdf = PdfFileReader(pdf_in_file)
  for page in range(pdf.numPages):
      inputpdf = PdfFileReader(pdf_in_file)
      output = PdfFileWriter()
      output.addPage(inputpdf.getPage(page))
      with open("document-page%s.pdf" % page, "wb") as outputStream:
          output.write(outputStream)
      print('Created: {}'.format(outputStream))


if __name__ == '__main__':
    pdf_splitter("orig.pdf")
