import cv2 as cv
import dlib
import face_utils as fu


# Load image
face_pic = cv.imread("/Users/ryanrahul/Documents/CV_ISEF_Project/Photos/person.jpg")

# Convert to grayscale (dlib works with grayscale too)
gray = cv.cvtColor(face_pic, cv.COLOR_BGR2GRAY)

# Load dlib's built-in frontal face detector (NO file download needed)
detector = dlib.get_frontal_face_detector()
facial_landmarks = dlib.shape_predictor("/Users/ryanrahul/Documents/CV_ISEF_Project/dlib_library_code/shape_predictor_68_face_landmarks.dat")

# Detect faces
rects = detector(gray)
print(f"The number of faces found = {len(rects)}")

for (i, rect) in enumerate(rects):
	# convert dlib's rectangle to a OpenCV-style bounding box
	# [i.e., (x, y, w, h)], then draw the face bounding box
	(x, y, w, h) = fu.rect_to_bb(rect)
	cv.rectangle(face_pic, (x, y), (x + w, y + h), (0, 255, 0), 2)
	# show the face number
	cv.putText(face_pic, "Face #{}".format(i + 1), (x - 10, y - 10),
		cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
	# determine the facial landmarks for the face region, then
	# convert the facial landmark (x, y)-coordinates to a NumPy
	# array
	landmark = facial_landmarks(gray, rect)
	shape = fu.shape_to_np(landmark)
	# loop over the (x, y)-coordinates for the facial landmarks
	# and draw them on the image
	for (x, y) in shape:
		cv.circle(face_pic, (x, y), 1, (255, 0, 0), -1)
    

# Show result
cv.imshow("Detected Faces", face_pic)
cv.waitKey(0)
cv.destroyAllWindows()

