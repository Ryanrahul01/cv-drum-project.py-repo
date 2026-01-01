import cv2 as cv
import dlib
import face_utils as fu


# Load image
face_pic = cv.imread("/Users/ryanrahul/Documents/CV_ISEF_Project/Photos/MomandRishaan.jpg")

# Convert to grayscale (dlib works with grayscale too)
gray = cv.cvtColor(face_pic, cv.COLOR_BGR2GRAY)

# Load dlib's built-in frontal face detector (NO file download needed)
detector = dlib.get_frontal_face_detector()

# Detect faces
faces = detector(gray)
print(faces)
print(f"The number of faces found = {len(faces)}")

# Draw bounding boxes using OpenCV
for face in faces:
    (x ,y, w, h) = fu.rect_to_bb(face)
    cv.rectangle(face_pic, (x,y), (x+w,y+h), (0, 255, 0), thickness=2)
    

# Show result
cv.imshow("Detected Faces", face_pic)
cv.waitKey(0)
cv.destroyAllWindows()

