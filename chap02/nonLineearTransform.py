import cv2
import numpy as np
from matplotlib import pyplot as plt

# Open the image.
img = cv2.imread('../images/light.png', 0)
# Trying 4 gamma values.
for gamma in [0.1, 0.5, 1.2, 2.2]:
    # Apply gamma correction.
    gamma_corrected = np.array(255 * (img / 255) ** gamma, dtype='uint8')

    # Save edited images.
    cv2.imwrite('./result/gamma_transformed' + str(gamma) + '.jpg', gamma_corrected)
cv2.destroyAllWindows()
