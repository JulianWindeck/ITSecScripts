import pyPdf
from pyPdf import PdfFileReader
import os
from optparse import OptionParser

def printMeta(pdf_path):
    pdf = PdfFileReader(file(pdf_path, 'rb'))
    metaData = pdf.getDocumentInfo()

    print '[*] PDF MetaData For: ' + str(pdf_path)
    for metaItem in metaData:
        print '[+] %s: %s' % (metaItem, metaData[metaItem])

def main():
    p = OptionParser(usage='%prog -f <pdfFile>',
                     version='1.0', description='A small script to get the metadata of a pdf file.')
    p.add_option('-f', dest='file', type='string', help='the pdf file you want to analyze')

    options, args = p.parse_args()
    inputFile = options.file
    if inputFile == None:
        print '[-] Please enter a filename'
    else:
        if not os.path.isfile(inputFile):
            print '[-] This file does not exist'
        else:
            printMeta(inputFile)


if __name__ == '__main__':
    main()