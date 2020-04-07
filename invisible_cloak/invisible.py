import cv2
import numpy as np

# this is because I don't have a webcam and use my ohine as one
cap = cv2.VideoCapture("http://192.168.43.1:8080/video")


_, background = cap.read()

while(True):

	_, frame = cap.read()
	# Convert BGR to HS

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_red = np.array([105, 40, 40])
	upper_red = np.array([210, 255, 255])

	mask = cv2.inRange(hsv, lower_red, upper_red)



	kernel = np.ones((8,8),np.uint8)
	erosion = cv2.erode(mask,kernel,iterations = 1)
	dilation = cv2.dilate(mask,kernel,iterations = 1)
	e_d = cv2.dilate(erosion,kernel,iterations = 1)

	
	mask = e_d

	mask_3_channel = cv2.merge((mask,mask,mask))

	stack = cv2.addWeighted(frame, 1, mask_3_channel, 1, 0) 
	stack = np.remainder(stack, 255)
	# stacked = np.add(mask_3_channel,frame)

	binary_mask = mask_3_channel//255
	overlay = np.multiply(binary_mask,background)-255

	stacked = cv2.addWeighted(stack, 1, overlay, 1, 0) 
	cv2.imshow('stacked',stacked)
	# cv2.imshow('overlays',overlay)
	
	q = cv2.waitKey(1)
	if q == ord("q"):
		break
