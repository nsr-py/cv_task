# this is because I don't have a webcam and use my ohine as one
import urllib.request
import cv2
import numpy as np
import time
URL = "http://192.168.43.1:8080/video"
cap = cv2.VideoCapture(URL)

while True:


	ret, frame = cap.read()
	if frame is not None:
		cv2.imshow('frame',frame)
	q = cv2.waitKey(1)
	if q == ord("q"):
		break

