import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/light.png',0)

hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_m = np.ma.masked_equal(cdf,0)
# I'(i,j) = 255*(I(i,j)-min)/max-min
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
print(cdf_m)
cdf = np.ma.filled(cdf_m,0).astype('uint8')
print(cdf)
img2 = cdf[img]

plt.plot(cdf, color = 'b')
plt.hist(img2.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

cv2.imshow("Image Equalization", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()