import cv2

src = cv2.imread("chae_soobin.jpg", cv2.IMREAD_COLOR)
dst = cv2.blur(src, (9, 9), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)
dst2 = cv2.blur(src, (3, 3), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)
dst3 = cv2.blur(src, (9, 9), anchor=(-1, -1), borderType=cv2.BORDER_REFLECT)

cv2.imshow("kernel size 9, 9", dst)
cv2.imshow("kernel size 3, 3", dst2)
cv2.imshow("borderType = BORDER_REFLECT", dst3)



cv2.waitKey()
cv2.destroyAllWindows()