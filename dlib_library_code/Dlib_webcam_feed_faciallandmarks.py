import cv2 as cv
import dlib
import face_utils as fu

capture = cv.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
facial_landmarks = dlib.shape_predictor("/Users/ryanrahul/Documents/CV_ISEF_Project/dlib_library_code/shape_predictor_68_face_landmarks.dat")

while True:
    isTrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = detector(gray)


    for face in faces:
        (x ,y, w, h) = fu.rect_to_bb(face)
        cv.rectangle(frame, (x,y), (x+w,y+h), (0, 255, 0), thickness=2)
        landmark = facial_landmarks(gray, face)
        shape = fu.shape_to_np(landmark)
	    # loop over the (x, y)-coordinates for the facial landmarks
	    # and draw them on the image
        for (x, y) in shape:
           cv.circle(frame, (x, y), 1, (0, 0, 255), 2)
    cv.imshow("Grayscale Webcam Feed", frame)
    
    key = cv.waitKey(20)

    if key == ord('r'):
        break

capture.release()

cv.destroyAllWindows()

