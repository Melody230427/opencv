import cv2

cap = cv2.VideoCapture(0)
gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)

if not cap.isOpened():
    print("Could not open camera")
    exit()

w = 640
h = 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret is False:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break