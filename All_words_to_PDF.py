'''
Author: Sohrab
git: https://github.com/sohrabganjian

The following is the code for converting
all the word documents ending with '.doc' and '.docx'
to pdf in the same directory with the same name
'''

## importing packages
import sys
import os
import comtypes.client

cwd = os.getcwd() # saving current directory

list_cwd = os.listdir(cwd) # saving data in current directory as a list

for i in range (len(list_cwd)):
    if list_cwd[i].endswith('.doc') or list_cwd[i].endswith('.docx'):
        # print(f[i]) # it will show the name of files

        wdFormatPDF = 17 # change word to PDF

        in_file = os.path.abspath(list_cwd[i]) # name of the word document
        out_file = os.path.abspath(os.path.splitext(list_cwd[i])[0]) # used for using the same name 
        # os.path.splitext(path) Split the pathname path into a pair (root, ext) such that root + ext == path,
        # and ext is empty or begins with a period and contains at most one period.
        # Leading periods on the basename are ignored; splitext('.cshrc') returns ('.cshrc', '').

        word = comtypes.client.CreateObject('Word.Application')
        doc = word.Documents.Open(in_file)
        doc.SaveAs(out_file, FileFormat=wdFormatPDF)
        doc.Close()
        word.Quit()
