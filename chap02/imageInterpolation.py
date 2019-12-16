import cv2
import numpy as np

img = cv2.imread('../images/apple.jpg', 1)
near_img = cv2.resize(img, None, fx=10, fy=10, interpolation=cv2.INTER_NEAREST)
bilinear_img = cv2.resize(img, None, fx=10, fy=10, interpolation=cv2.INTER_LINEAR)
bicubic_img = cv2.resize(img, None, fx=10, fy=10, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Result', bilinear_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
