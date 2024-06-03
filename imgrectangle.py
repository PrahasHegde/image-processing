#Drawing a rectangle on the image
import cv2
import numpy as np
from dispImg import cv2_imshow

img = cv2.imread('C:\\Users\\hegde\\OneDrive\\Desktop\\imageProcessing\\car.jpg')

# make a copy 
imageRectangle = img.copy()

# define the starting and end points of the rectangle
start_point =(600,40)
end_point =(770,250)
# draw the rectangle
cv2.rectangle(imageRectangle, start_point, end_point, (0, 0, 255), thickness= 3, lineType=cv2.LINE_8)

# display 
cv2_imshow(imageRectangle)



# Add text to image
imageText = img.copy()
text = 'Majestic, Fierce and Free'
org = (50,150) #position of text on the image
cv2.putText(imageText, text, org, fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale = 5.5, color = (0,0,0))
cv2_imshow(imageText)