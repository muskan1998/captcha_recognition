from os import listdir
from os.path import isfile, join
import pytesseract
import cv2
import os
import numpy as np

mypath='image'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = np.empty(len(onlyfiles), dtype=object)
count =0 
for n in range(0, len(onlyfiles)):
  
  count=count+1
  images[n] = cv2.imread( join(mypath,onlyfiles[n]) )
  
  images[n] = cv2.dilate(images[n], None, iterations=1)
  images[n] = cv2.resize(images[n], (300,120))
  images[n] = cv2.GaussianBlur(images[n],(5,5),0)
  
  
  cv2.imshow("Image", images[n])
  text = pytesseract.image_to_string(images[n],config=' -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz')
  print(text)
  out = open('out2.csv', 'a')
  l=[text]
  for row in l:
      out.write('%str' % row)
  out.write('\n')
  out.close()
  cv2.waitKey(0)
