import cv2

cap = cv2.VideoCapture("test.mp4")

if cap.isOpened():
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = int(1000/fps)
    print("FPS: %f, Delay: %dms" %(fps, delay))
    count = 0

    while (cap.isOpened()):
        ret, frame = cap.read()
        resized = cv2.resize(frame, (240, 320))

        if not ret:
            break

        cv2.imshow("Video", frame)
        cv2.waitKey(delay)

        cv2.imshow("resized video", resized)
        
        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)    

        key = cv2.waitKey(1)
        if key & 0xFF == ord('c'):
            cv2.imwrite("test%d.jpg" % count, frame)
            count += 1
        if key & 0xFF == ord('q'):
            break
else:
    print("can't open video")

cap.release()
cv2.destroyAllWindows()
