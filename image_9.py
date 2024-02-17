import cv2
import numpy as np

src = cv2.imread("tomato.jpg", cv2.IMREAD_COLOR)
b = src[:, :, 0]
g = src[:, :, 1]
r = src[:, :, 2]
inverse = cv2.merge((r, g, b))
height, width, channel = src.shape
zero = np.zeros((height, width, 1), dtype=np.uint8)

cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)
cv2.imshow("inverse", inverse)
cv2.imshow("zero", zero)

cv2.waitKey()
cv2.destroyAllWindows()