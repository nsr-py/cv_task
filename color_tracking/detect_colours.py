import numpy as np 
import cv2


# this is because I don't have a webcam and use my ohine as one
cap = cv2.VideoCapture("http://192.168.43.1:8080/video") 


while(1):
	_, image = cap.read()
	img = image
	imgray = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(imgray, np.array([1, 120, 100]), np.array([150, 200, 255]))
	ret,thresh = cv2.threshold(mask,150, 151, cv2.THRESH_BINARY)
	contours,hierarchy = cv2.findContours(thresh, 1, 2)
	# cnt = contours[0]
	


	for cnt in contours:
		x,y,w,h = cv2.boundingRect(cnt)
		if w>100 and h>100:
			img = cv2.rectangle(img,(x-2,y-2),(x+w+4,y+h+4),(0,0,0),2)

	cv2.imshow('img',img)	
	cv2.imshow('thresh',thresh)	


	k = cv2.waitKey(10) 
	if k == 27: 
		break
