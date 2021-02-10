import glob
import win32com.client
import os
import sys
import pythoncom


def Convert():
    pythoncom.CoInitialize()
    word = win32com.client.Dispatch("Word.Application")
    word.visible = 0

    pdfs_path = "convert/temp/pdf/"
    reqs_path = "convert/temp/word/"
    for i, doc in enumerate(glob.iglob(pdfs_path+"*.pdf")):
        filename = doc.split('\\')[-1]
        in_file = os.path.abspath(doc)
        wb = word.Documents.Open(in_file)
        out_file = os.path.abspath(
            reqs_path + filename[0:-4] + ".docx".format(i))
        wb.SaveAs2(out_file, FileFormat=16)
        wb.Close()

    word.Quit()
