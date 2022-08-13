import cv2
import numpy as np

img = cv2.imread('sample2.png')
median = cv2.medianBlur(img, 3)
compare = np.concatenate((img, median), axis=1) #side by side comparison

cv2.imshow('img', median)
cv2.waitKey(0)
cv2.destroyAllWindows
