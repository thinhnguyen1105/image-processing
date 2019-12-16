import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("../images/objets4.jpg")
fig, axs = plt.subplots(2, 3)

axs[0, 0].set_title('Original')
axs[0, 0].imshow(image, cmap="gray", vmin=0, vmax=255)

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
axs[0, 1].set_title('Grayscale')
axs[0, 1].imshow(grayImage, cmap="gray", vmin=0, vmax=255)

gray_correct = np.array(255 * (grayImage / 255) ** 1.2, dtype='uint8')
axs[0, 2].set_title('Gamma 1.2')
axs[0, 2].imshow(gray_correct, cmap="gray", vmin=0, vmax=255)

# gray_equ = cv2.equalizeHist(grayImage)
# axs[0, 2].set_title('Histogram')
# axs[0, 2].imshow(gray_correct, cmap="gray", vmin=0, vmax=255)

thresh = cv2.adaptiveThreshold(gray_correct, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 255, 10)
thresh = cv2.bitwise_not(thresh)
axs[1, 0].set_title('Threshold')
axs[1, 0].imshow(thresh, cmap="gray", vmin=0, vmax=255)

kernel = np.ones((15, 15), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)
img_erode = cv2.erode(img_dilation, kernel, iterations=1)
img_erode = cv2.medianBlur(img_erode, 7)
axs[1, 1].set_title('Dilatation + erosion')
axs[1, 1].imshow(img_erode, cmap="gray", vmin=0, vmax=255)

ret, labels = cv2.connectedComponents(img_erode)
label_hue = np.uint8(179 * labels / np.max(labels))
cv2.imshow("Image Equalization", label_hue)
blank_ch = 255 * np.ones_like(label_hue)
labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)
labeled_img[label_hue == 0] = 0

axs[1, 2].set_title('Objects counted:' + str(ret - 1))
axs[1, 2].imshow(labeled_img)

print('objects number is:', ret - 1)

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')

for ax in axs.flat:
    ax.label_outer()

plt.show()
