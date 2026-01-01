import cv2 as cv
import dlib
import face_utils as fu

capture = cv.VideoCapture(0)
detector = dlib.get_frontal_face_detector()

while True:
    isTrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = detector(gray)


    for face in faces:
        (x ,y, w, h) = fu.rect_to_bb(face)
        cv.rectangle(frame, (x,y), (x+w,y+h), (0, 255, 0), thickness=2)
    cv.imshow("Grayscale Webcam Feed", frame)
    
    key = cv.waitKey(20)

    if key == ord('r'):
        break

capture.release()
cv.destroyAllWindows()

