import numpy as np
import cv2

img = cv2.imread("lena.jpeg", cv2.IMREAD_GRAYSCALE)

ret,binary = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,trunc = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,tozero = cv2.threshold(img,0,255,cv2.THRESH_TOZERO)
ret,otsu = cv2.threshold(img,0,255,cv2.THRESH_OTSU)

cv2.imshow("Original", img)
cv2.imshow("Binary", binary)
cv2.imshow("Trunc", trunc)
cv2.imshow("ToZero", tozero)
cv2.imshow("Otsu", otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()
