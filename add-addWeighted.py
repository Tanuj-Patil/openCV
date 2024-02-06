# add() : This method is used to add two images
# This method takes two arguments(i.e takes two images)

# One condition to add() is both the images should be in the same dimention.

# addWeighted() : This method is used to add two images with required transparency
# It takes 5 arguments:
# i)image1,
# ii)tranparency level of image1 and it should be in between 0 and 1 
# iii)image2
# iv)tranparency level of image2 and it should be in between 0 and 1 
# v)gamma level (brightness)

import cv2

img1 = cv2.imread("C:\\Users\\tanuj\\OneDrive\\Pictures\\opencv-img\\tanuj1.jpg")
img2 = cv2.imread("C:\\Users\\tanuj\\OneDrive\\Pictures\\opencv-img\\tanuj2.jpg")

# res_img1 = cv2.add(img1, img2)
res_img2 = cv2.addWeighted(img1, 1, img2, 0.5, 10)
# cv2.imwrite("C:\\Users\\tanuj\\OneDrive\\Pictures\\opencv-img\\add_img.jpg", res_img1)
cv2.imwrite("C:\\Users\\tanuj\\OneDrive\\Pictures\\opencv-img\\add_img.jpg", res_img2)
