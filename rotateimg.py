import cv2
import numpy as np
from dispImg import cv2_imshow

img = cv2.imread('C:\\Users\\hegde\\OneDrive\\Desktop\\imageProcessing\\car.jpg')

# First we need to obtain the center of original image by dividing height and width by 2
height, width = img.shape[:2]
print("Height and width of original image", height, width)

# get the coordinates of the center of the image to create the 2D rotation matrix
center = (width/2, height/2)

# using cv2.getRotationMatrix2D() to get the rotation matrix
rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=180, scale=1)

# rotate the image using cv2.warpAffine
rotated_image = cv2.warpAffine(src=img, M=rotate_matrix, dsize=(width, height))

print("Original Image")
cv2_imshow(img)
print("Rotated Image")
cv2_imshow(rotated_image)