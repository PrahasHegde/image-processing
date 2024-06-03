#@title Image Normalization
import cv2
import numpy as np
from dispImg import cv2_imshow

def normalize_image(image):
    # Convert the image to float32
    img_float32 = image.astype(np.float32)

    # Normalize the image to the range [100, 200] 
    # the intensity values of all pixels now will range from 100 to 200 only instead of 0 to 255
    normalized_image = cv2.normalize(img_float32, None, 100, 255, cv2.NORM_MINMAX)

    return normalized_image

# Read an image from file
img = cv2.imread('C:\\Users\\hegde\\OneDrive\\Desktop\\imageProcessing\\car.jpg')

# Ensure the image is not empty
if img is not None:
    # Display the original image
    cv2_imshow(img)

    # Normalize the image
    normalized_img = normalize_image(img)

    # Display the normalized image
    cv2_imshow(normalized_img)   