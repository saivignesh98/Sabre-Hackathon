'''import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

image = cv2.imread("bca.jpg")


decodedObjects = pyzbar.decode(image)
for obj in decodedObjects:
    print("obj", obj)
    print("Type:", obj.type)
    print("Data: ", obj.data, "\n")

cv2.imshow("Frame", image)
cv2.waitKey(0)
'''
from pillow import Image
from tesseract import image_to_string
print( image_to_string(Image.open('IMG_20200116_151537__01.jpg')) )
print( image_to_string(Image.open('IMG_20200116_151537__01.jpg'), lang='eng') )
