import cv2
import numpy as np
from skimage.morphology import opening

img = cv2.imread("../images/objets3.jpg")
kernel = np.ones((5, 5), np.uint8)

# Bước 1: Chuyển về ảnh xám
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Bước 2: Làm mờ ảnh
blur = cv2.GaussianBlur(gray, (1, 1), 1)
cv2.imshow('new', blur)

# Bước 3: Lọc nhiễu
new = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, -5)

# Bước 4: Opening
opening = cv2.morphologyEx(new, cv2.MORPH_OPEN, kernel)

# Bước 5: Đếm
contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Kiểm tra kết quả
cv2.drawContours(img, contours, -1, (255, 0, 0), 3)
cv2.imshow('opening', opening)
print("Count: " + str(len(contours)))
cv2.waitKey(0)
cv2.destroyAllWindows()
