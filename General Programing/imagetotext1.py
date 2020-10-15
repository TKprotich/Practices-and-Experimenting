from PIL import Image
import pytesseract
from pytesseract import image_to_string
#"C:\Users\user\Documents\Practice\text.JPG"
#print(image_to_string(Image.open('text.JPG')))
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"
print(image_to_string(Image.open('test.jpg'), lang='eng'))
print(image_to_string(Image.open(PATH), lang='eng'))
