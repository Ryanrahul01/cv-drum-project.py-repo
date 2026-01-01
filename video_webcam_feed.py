import cv2 as cv

haar_cascade = cv.CascadeClassifier('/Users/ryanrahul/Documents/CV_ISEF_Project/Photos/haar_face.xml')

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    frame = cv.flip(frame, 1)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #cv.imshow("Grayscale Webcam Feed", gray)

    webcam_feed_rec = haar_cascade.detectMultiScale(gray, scaleFactor=1.07, minNeighbors=4)

    for (x,y,w,h) in webcam_feed_rec:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0, 255, 0), thickness=2)
    cv.imshow("Grayscale Webcam Feed", frame)

    
    key = cv.waitKey(20)

    if key == ord('r'):
        break

capture.release()

cv.destroyAllWindows()

