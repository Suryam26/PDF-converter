import tabula
import win32com.client
import os
import pythoncom


def Convert(fileName, convertFormat):
    pythoncom.CoInitialize()

    pdfs_path = "convert\\temp\\pdf\\"
    reqs_path = "convert\\temp\\word\\"

    in_file = os.path.abspath(pdfs_path+fileName+'.pdf')
    out_file = os.path.abspath(
        reqs_path + fileName + convertFormat)

    # WORD:
    if convertFormat == '.docx':
        word = win32com.client.Dispatch('Word.Application')
        wb = word.Documents.Open(in_file)
        wb.SaveAs2(out_file, FileFormat=16)
        wb.Close()
        word.Quit()

    # CSV:
    if convertFormat == '.csv':
        tabula.convert_into(in_file, out_file, output_format="csv",
                            stream=True, pages='all')

    os.remove(in_file)
