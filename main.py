from time import process_time_ns
import pytesseract
from pytesseract import Output
import PIL.Image
import cv2
import json 
from colorama import Fore
from colorama import Style  

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\10088271\AppData\Local\Tesseract-OCR\tesseract.exe'

myconfig = r"--psm 12 --oem 3"

# text = pytesseract.image_to_string(PIL.Image.open("sample.jpg"), config=myconfig)

# print(text)
# cv2.namedWindow("output", cv2.WINDOW_NORMAL)
img = cv2.imread("sample3.jpeg")
# height, width, _ = img.shape

data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)

amount = len(data['text'])


for i in range(amount):
    if float(data['conf'][i]) > 85:
        print(f"{Fore.GREEN}", data['text'][i], f"{Style.RESET_ALL}")
    elif float(data['conf'][i]) > 65:
        print(f"{Fore.YELLOW}", data['text'][i], f"{Style.RESET_ALL}")
    elif float(data['conf'][i]) > 45:
        print(f"{Fore.RED}", data['text'][i], f"{Style.RESET_ALL}")




# while("" in data['text']) :
#     data['text'].remove("")

# json_string = json.dumps(data)

# print(json_string)

        # (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        # img = cv2.rectangle(img, (x,y), (x+width, y+height), (0,255,0), 2)
        # img = cv2.putText(img, data['text'][i], (x, y+height+20), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 8, cv2.LINE_AA)
# img2 = cv2.resize(img, (960,540))
# cv2.imshow("output", img2)
# cv2.waitKey(0)
