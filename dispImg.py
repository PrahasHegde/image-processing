# First import the libraries cv2 and matplotlib
import cv2
import matplotlib.pyplot as plt

# Read an image file using cv2
img = cv2.imread("C:\\Users\\hegde\\OneDrive\\Desktop\\imageProcessing\\car.jpg")

# Then below function can display your cv2 image using matplotlib.pyplot.
def cv2_imshow(img):
    plt.figure(figsize=(18,18))
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()

cv2_imshow(img=img)

# # You can also configure the figure size and other properties of the display.
# def cv2_imshow(img):
#   plt.figure(figsize=(18,18))
#   plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#   plt.axis('off')
#   plt.show()