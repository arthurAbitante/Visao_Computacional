import numpy as np
import cv2

img = cv2.imread("lena.jpeg", cv2.IMREAD_GRAYSCALE)

rows, cols = img.shape

#M = cv2.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0),180,1)
M = cv2.getRotationMatrix2D((0, 0),10,1)


dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow("original", img)
cv2.imshow("rotacionada", dst)
cv2.waitKey(0)

cv2.destroyAllWindows()
