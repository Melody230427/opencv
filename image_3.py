import cv2

img = cv2.imread("chae_soobin.jpg")
print(img.shape)

cropped = img[50:450, 100:400]

resized = cv2.resize(img, (825, 1238))

rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Original", img)
cv2.imshow("Cropped image", cropped)

cv2.imwrite("chae_soobin2.png", resized)

cv2.imshow("Rotated image", rotated)

cv2.waitKey()
cv2.destroyAllWindows()