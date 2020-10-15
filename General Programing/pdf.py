from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import docx
from docx import Document
from docx.shared import Inches

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()
    document = Document()
    p = document.add_paragraph(text)
    document.save(r'C:\Users\user\Desktop\2020-Kalkaal Speciality Hospital\Abdullah\output.docx')
    fp.close()
    device.close()
    retstr.close()
    print('Done!')


convert_pdf_to_txt(r'C:\Users\user\Desktop\2020-Kalkaal Speciality Hospital\Abdullah\Specimen_collection_other_than_blood_and_transportation_policy_1_04212011_121213.pdf')

    
    
    