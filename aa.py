import cv2

cap = cv2.VideoCapture("cctv.mp4")

object_detector = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    
    # 1. Object Detection
    mask = object_detector.apply(frame)
    height, width, _ = frame.shape
    print(height, width)
    roi = frame[280: 720,500: 800]



    #object detection
    mask = object_detector.apply(frame)
    contours,_ = cv2.findContours(mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 50:
            cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2)


    cv2.imshow("roi",roi)
    cv2.imshow("CCTV",frame)
    cv2.imshow("Mask",mask)
    key = cv2.waitKey(30)
    if key == 27:
        break
cap. realease()
cv2.destroyAllWindows()