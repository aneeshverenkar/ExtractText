import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

def extractText(image):
  im = image
  im = im.filter(ImageFilter.MedianFilter())
  enhancer = ImageEnhance.Contrast(im)
  im = enhancer.enhance(2)
  im = im.convert('1')
  im.save('temp2.jpg')  # image from which you want to extract text
  text = pytesseract.image_to_string(Image.open('temp2.jpg'))
  return text

img = Image.open("/dir/image.png")  # input image
print(extractText(img))


