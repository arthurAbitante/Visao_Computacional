import numpy as np
import cv2

img = cv2.imread("opencv_1.jpeg", cv2.IMREAD_UNCHANGED)

blur_average = cv2.blur(img,(5,5))
blur_gaussian = cv2.GaussianBlur(img,(5,5),0)

cv2.imgshow("Original", img)
cv2.imgshow("Average", blur_average)
cv2.imgshow("Gaussian", blur_gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()
