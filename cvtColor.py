# cvtColor() = convert image from one color space to another
# It takes two arguments: i) image   ii) color model / color space
# syntax = cv2.cvtColor(image, color_space)
# color_space can be: 
# i)   cv2.COLOR_BGR2GRAY
# ii)  cv2.COLOR_BGR2HSV
# iii) cv2.COLOR_BGR2RGB


import cv2
img = cv2.imread("C:\\Users\\tanuj\\OneDrive\\Pictures\\Screenshots\\Screenshot (379).png")
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("C:\\Users\\tanuj\\OneDrive\\Pictures\\gray1.png", img1)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imwrite("C:\\Users\\tanuj\\OneDrive\\Pictures\\hsv1.png", img2)
img3 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imwrite("C:\\Users\\tanuj\\OneDrive\\Pictures\\rgb1.png", img3)