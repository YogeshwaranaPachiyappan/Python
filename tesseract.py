import pytesseract
from PIL import Image
img = Image.open('sample.jpg')
text = pytesseract.image_to_string(img)
print(text)
