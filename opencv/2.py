from os import listdir
from os.path import isfile, join
import pytesseract
import cv2
import os
import numpy as np
import imutils
import os.path
import glob

mypath='image'


captcha_image_files = glob.glob(os.path.join(mypath, "*"))
counts = {}

for (i, captcha_image_file) in enumerate(captcha_image_files):

  filename = os.path.basename(captcha_image_file)
    
  captcha_correct_text = os.path.splitext(filename)[0]

  image = cv2.imread(captcha_image_file)
  
  image = cv2.resize(image, (300,120))
  image = cv2.dilate(image, None, iterations=1)
  image = cv2.GaussianBlur(image,(1,9),0)
  image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
  image = cv2.medianBlur(image,5)
  cv2.imshow("Image", image)
  #text = pytesseract.image_to_string(images[n])
  text =pytesseract.image_to_string(image,config='--psm 8 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz')
  print(text)
  out = open('final.csv', 'a')
  l=[captcha_correct_text,text]
  for row in l:
      out.write('%str' %row)
      out.write('\n')
  out.write('\n')
  out.close()
  cv2.waitKey(0)
