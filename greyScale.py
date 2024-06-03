#convert original image to greyscale and black and white

import cv2
import matplotlib.pyplot as plt
# from dispImg import cv2_imshow

#cv2 function to display image
def cv2_imshow(img):
    plt.figure(figsize=(18,18))
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()


img = cv2.imread("C:\\Users\\hegde\\OneDrive\\Desktop\\imageProcessing\\car.jpg") # Read the image as it is
print("original image")
cv2_imshow(img)

#Convert to grayscale
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("grayscaled image")
cv2_imshow(grayscale)

#Convert grayscale to black and white
(thresh, img_bw) = cv2.threshold(grayscale, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print('black and white image')
cv2_imshow(img_bw)
