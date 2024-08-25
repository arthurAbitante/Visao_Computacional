# -*- coding: utf-8 -*-
import cv2


try:
	img = cv2.imread("lena.jpeg", cv2.IMREAD_UNCHANGED)
	cv2.imshow("foto", img)
except:
	print ("Nao foi possivel abrir a imagem")
	
cv2.waitKey(0)
cv2.destroyAllWindows()
