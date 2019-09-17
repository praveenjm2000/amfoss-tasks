import pytesseract
from PIL import Image
from pytesseract import image_to_string
str=pytesseract.image_to_string(Image.open('/home/praveen/Pictures/cap.png'))
n1=int(str[0])
n2=int(str[2])
if str[1]=='+' :
    print(n1+n2)
elif str[1]=='-':
    print(n1-n2)
elif str[1]=='/':
    print(n1/n2)
elif str[1]=='%':
    print(n1%n2)

