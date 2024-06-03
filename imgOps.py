#Imports
import cv2
import numpy as np
from dispImg import cv2_imshow

img = cv2.imread('C:\\Users\\hegde\\OneDrive\\Desktop\\imageProcessing\\car.jpg')

print("Shape of original image",img.shape)
cv2_imshow(img)

#changing image dimensions
new_width = 150
new_height = 150
new_points = (new_width, new_height)
rescaled_img = cv2.resize(img, new_points, interpolation= cv2.INTER_LINEAR)

print("shape of rescaled image", rescaled_img.shape)
# Display images
cv2_imshow(rescaled_img)


# # Read the image 
# img = cv2.imread('lion2.jpg')
# cv2_imshow(img)


# Read the image as grayscale
img_gray = cv2.imread('C:\\Users\\hegde\\OneDrive\\Desktop\\imageProcessing\\car.jpg', 0)
cv2_imshow(img_gray)


#Cropping an area of the mage

print("Original image shape", img.shape) # Print image shape
print("Original image")
cv2_imshow(img)

# Cropping an image
cropped_image = img[50:250, 550:750]

# Display cropped image
print("cropped image shape", cropped_image.shape) # Print image shape
print("Cropped image")
cv2_imshow(cropped_image)

