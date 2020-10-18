# extract_doc_info.py

from PyPDF2 import PdfFileReader
def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        # get the first page
        page = pdf.getPage(0)
        #print('Page type: {}'.format(str(type(page))))
        text = page.extractText()
        print(text)
if __name__ == '__main__':
    path = r"C:\Users\user\Documents\Dr Galad - Research and Academia\Remdesivir1.pdf"
    text_extractor(path)
