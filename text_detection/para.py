import numpy as np 
import cv2

points = []

img = cv2.imread('basic.jpg')
scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, np.array([0,0,0]), np.array([150,150,150]))


e_factor = 2
kernel_e = np.ones((e_factor,e_factor),np.uint8)
erosion = cv2.erode(mask,kernel_e,iterations = 1)

d_factor = 20
kernel_d = np.ones((d_factor,d_factor),np.uint8)
dilation = cv2.dilate(erosion,kernel_d,iterations = 1)


ret,thresh = cv2.threshold(dilation,150, 151, cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(thresh, 1, 2)


cv2.imshow('mask',mask)

cv2.imshow('erosion',erosion)
cv2.imshow('dilation',dilation)

for cnt in contours:
	x,y,w,h = cv2.boundingRect(cnt)
	if w>50 and h>15:
		# print(x,y,w,h)
		# dilation = cv2.rectangle(img,(x-2,y-2),(x+w+4,y+h+4),(0,0,255),1)
		# points.append([(x-2,y-2),(x+w+4,y+h+4)])
		points.append([x,y,w,h])

# this is to avoid two boxes on one para
# you should try it once without this too
for point in points:
	x,y,w,h = point
	for temp in points:

		if abs(point[1]-temp[1])<5 and not point == temp:
			print(temp)
			if point[0]<temp[0]:
				x = point[0]
			else:
				x = temp[0]
			if point[1]<temp[1]:
				y = point[1]
			else:
				y = temp[1]
			
			w = point[2] + temp[2]

			if point[3]>temp[3]:
				h = point[3]

			else:
				h = temp[3]
	dilation = cv2.rectangle(img,(x-2,y-2),(x+w+4,y+h+4),(0,0,255),1)

cv2.imshow('thresh',thresh)

cv2.imshow('img',img)
# print(points)
q = cv2.waitKey(10000000)
if q == ord("q"):
	cv2.destroyAllWindows()
