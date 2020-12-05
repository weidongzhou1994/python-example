#!D:/Python/Anaconda/python.exe
# -*- encoding: utf-8 -*-
'''
@文件        :merge
@说明        :和要转 PDF 的 word 文件放置在同一个文件夹下
@时间        :2020/12/05 17:46:42
@作者        :周卫东
@版本        :1.0
'''
import os, docx2pdf
from PyPDF2 import PdfFileMerger

wordfiles = []
pdffiles = []

'''
word 转 pdf
'''
for filename in os.listdir('.'):
    if filename.endswith('.docx'):
        wordfiles.append(filename)

for filename in wordfiles:
    filename1 = os.path.abspath(filename)
    filename1 = filename1.split('.')[0]
    docx2pdf.convert(filename, f"{filename1}.pdf")


'''
pdf 合并
'''
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdffiles.append(filename)

file_merger = PdfFileMerger()

for pdffile in pdffiles:
    file_merger.append(pdffile)

file_merger.write("./merge.pdf")