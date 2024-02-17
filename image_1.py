import cv2

img = cv2.imread("chae_soobin.jpg")

cv2.namedWindow("image", cv2.WINDOW_NORMAL)

print(img.shape)

cv2.imshow("image", img)

while True:
    key = cv2.waitKey()
    if key == ord('s'):
        cv2.imwrite("output.png", img)
        break

cv2.destroyAllWindows()