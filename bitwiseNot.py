# # bitwise_not() : This function will flips the pixels of an image.
# All pixel values that are greater than ZERO will be set to ZERO.
# All fixel values that are equal to ZERO will be set to 255.
# It will create inversion of an image.


import cv2

img = cv2.imread("C:\\Users\\tanuj\\OneDrive\\Pictures\\opencv-img\\imwrite1.jpg")
res_img = cv2.bitwise_not(img)
cv2.imwrite("C:\\Users\\tanuj\\OneDrive\\Pictures\\opencv-img\\res_img.jpg", res_img)