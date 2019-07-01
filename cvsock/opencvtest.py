import numpy as np
import cv2

img = cv2.imread('image.jpg',1)
#canny_img = cv2.Canny(img,200,400)
cv2.imshow("image",img)
cv2.waitKey()
print(img)


