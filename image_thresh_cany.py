import numpy as np
import cv2

img = cv2.imread("minhaFoto.jpg", cv2.IMREAD_GRAYSCALE)
ret, otsu_ant = cv2.threshold(img,0,255,cv2.THRESH_OTSU)

median = cv2.blur(img,(5,5))
ret,otsu_med = cv2.threshold(median,0,255,cv2.THRESH_OTSU)

gaussian = cv2.GaussianBlur(img,(5,5),0)
ret,otsu_gaussian = cv2.threshold(gaussian,0,255,cv2.THRESH_OTSU)

edges = cv2.Canny(img,100,200)

cv2.imshow("Original", img)
cv2.imshow("Otsu Ant", otsu_ant)
cv2.imshow("Otsu Median", otsu_med)
cv2.imshow("Otsu Gaussian", otsu_gaussian)
cv2.imshow("Canny", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
