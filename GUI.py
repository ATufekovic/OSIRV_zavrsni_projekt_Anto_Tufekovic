import cv2
import numpy as np
#from matplotlib import pyplot as plt

def nothing(x):
    pass

# read the image
file_name = input("What is the file name(either absolute path with '/' or  relative to script):")
try:
    img = cv2.imread(file_name, 0)
except:
    print("File is not an image or does not exist.")
    exit()


# create a named window that will contain everything
window_name = "0-OFF,1-blur,2-gauss,3-median,4-bilateral,ESC to exit"
cv2.namedWindow(window_name)

switch = 'MODE'
cv2.createTrackbar(switch, window_name, 0, 4, nothing)

cv2.createTrackbar('Kernel', window_name, 1, 50, nothing)

# infinite loop until we hit the escape key on keyboard
while(1):
    kernel = cv2.getTrackbarPos('Kernel', window_name)
    if kernel%2 == 0:
        kernel += 1 # this way we ensure that no even numbers get passed for kernels, preventing the program from crashing
    s = cv2.getTrackbarPos(switch, window_name)

    if s == 0:
        modified_img = img
    elif s == 1:
        modified_img = cv2.blur(img, (kernel, kernel))
    elif s == 2:
        modified_img = cv2.GaussianBlur(img, (kernel, kernel),0)#if sigma is zero then we get: sigma = 0.3*((ksize-1)*0.5 - 1) + 0.8
    elif s == 3:
        modified_img = cv2.medianBlur(img, kernel)
    elif s == 4:
        modified_img = cv2.bilateralFilter(img, kernel, 90, 90)

#   display images
    cv2.imshow(window_name, modified_img)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:   # hit escape to quit
        cv2.imwrite("temporary.png", modified_img)
        break

cv2.destroyAllWindows()

exit()
