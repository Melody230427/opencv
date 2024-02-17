import cv2

src = cv2.imread("chae_soobin.jpg", cv2.IMREAD_COLOR)
dst_not = cv2.bitwise_not(src)
dst_and = cv2.bitwise_and(src, src)
dst_or = cv2.bitwise_or(src, src)
dst_xor = cv2.bitwise_xor(src, src)

cv2.imshow("src", src)
cv2.imshow("not", dst_not)
cv2.imshow("and", dst_and)
cv2.imshow("or", dst_or)
cv2.imshow("xor", dst_xor)

cv2.waitKey()
cv2.destroyAllWindows()