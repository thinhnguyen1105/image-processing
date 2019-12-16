import cv2
import numpy as np
from matplotlib import pyplot as plt


# Function to map each point of image and check condition
def pixelVal(pix, r1, s1, r2, s2):
    if (0 <= pix and pix <= r1):
        return (s1 / r1) * pix
    elif (r1 < pix and pix <= r2):
        return ((s2 - s1) / (r2 - r1)) * (pix - r1) + s1
    else:
        return ((255 - s2) / (255 - r2)) * (pix - r2) + s2


# Open the image.
img = cv2.imread('../images/light.png', 0)
# Define parameters.
r1 = 70
s1 = 50
r2 = 150
s2 = 200

# Vectorize the function to apply it to each value in the Numpy array.
pixelVal_vec = np.vectorize(pixelVal)

# Apply contrast stretching.
contrast_stretched = pixelVal_vec(img, r1, s1, r2, s2)

# Save edited image.
cv2.imwrite('./result/contrast_stretch.jpg', contrast_stretched)
# cv2.imshow('result', contrast_stretched)
# cv2.waitKey(0)
cv2.destroyAllWindows()
