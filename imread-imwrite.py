# imread() used to read the image from the system
# syntax = imread(path, flag)
# flag =i)  cv2.IMREAD_COLOR       - 1 for colorImage (default)
#       ii) cv2.IMREAD_GRAYSCALE   - 0 for grayscale

# imwrite() used to display the image on the system
# syntax = imwrite(path, image)

import cv2
img = cv2.imread("C:\\Users\\tanuj\\OneDrive\\Pictures\\Screenshots\\Screenshot (379).png", 0)
cv2.imwrite("C:\\Users\\tanuj\\OneDrive\\Pictures\\imwrite2.jpg", img)