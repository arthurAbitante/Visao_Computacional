import numpy as np
import cv2

img = cv2.imread("lena.jpeg", cv2.IMREAD_UNCHANGED)



#res = cv2.resize(img, None, fx=90, fy=90,interpolation = cv2.INTER_CUBIC)
print img.shape
height, width = img.shape[:2]
res = cv2.resize(img,(4*width, 4*height), interpolation = cv2.INTER_CUBIC)


cv2.imshow("Original", img)
cv2.imshow("Scaled", res)
cv2.waitKey(0)

cv2.destroyAllWindows()
