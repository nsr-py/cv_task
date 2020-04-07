
import cv2
import numpy as np
img = cv2.imread('basic.jpg')

# resize image
scale_percent = 50 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
image = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

kernel_h = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 1))
h = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel_h, iterations=2)
contours = cv2.findContours(h, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(contours) == 2:
    contours = contours[0] 
else: 
    contours[1]

for cnt in contours:
    cv2.drawContours(image, [cnt], -1, (255, 255, 255), 5)


kernel_v = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 40))
v = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel_v, iterations=2)
contours = cv2.findContours( v, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(contours) == 2:
    contours = contours[0] 
else: 
    contours[1]

for cnt in contours:
    cv2.drawContours(image, [cnt], -1, (255, 255, 255), 5)

# cv2.imshow('image', image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

mask = cv2.threshold(image, 130, 255, cv2.THRESH_BINARY_INV)[1]
mask = cv2.dilate(mask, np.ones((4, 4), np.uint8), iterations=2)
mask = cv2.erode(mask,np.ones((3, 3), np.uint8),iterations = 1)
cont = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

result= cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

for c in cont:
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(result, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow('result', result)
cv2.imwrite('final.png', result)
cv2.waitKey()