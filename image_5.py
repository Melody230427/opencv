import cv2

src = cv2.imread("chae_soobin.jpg", cv2.IMREAD_COLOR)

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, dst = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
ret, dst2 = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
ret, dst3 = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)


cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)

cv2.waitKey()
cv2.destroyAllWindows()