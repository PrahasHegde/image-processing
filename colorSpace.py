#Working with Color spaces in OpenCV
#let us load an image, by default it will have BGR color space
import cv2
from dispImg import cv2_imshow
import numpy as np

img = cv2.imread('C:\\Users\\hegde\\OneDrive\\Desktop\\imageProcessing\\car.jpg')

#Convert BGR color space to LAB color space
imgLAB = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2_imshow(imgLAB)

##Convert BGR color space to HSV color space
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2_imshow(imgHSV)

#Image Segmentation
#Let us segment the image using color spaces
bgr = [100, 150, 1] #target color in BGR format
thresh = 140 #threshold value for color segmentation

#lower bound for color segmentation in BGR
minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
#upper bound for color segmentation in BGR
maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])
#a binary mask where the pixels within a specific range are set to white and others are set to black
maskBGR = cv2.inRange(img,minBGR,maxBGR)
#do bitwiseAND between image and mask to only keep the pixels in the specified color range
resultBGR = cv2.bitwise_and(img, img, mask = maskBGR)
cv2_imshow(resultBGR)