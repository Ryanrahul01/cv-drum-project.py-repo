import cv2 as cv

face_pic = cv.imread("/Users/ryanrahul/Documents/CV_ISEF_Project/Photos/MomandRishaan.jpg")

cv.imshow("Person_Picture" , face_pic)

gray = cv.cvtColor(face_pic, cv.COLOR_BGR2GRAY)



haar_cascade = cv.CascadeClassifier('/Users/ryanrahul/Documents/CV_ISEF_Project/haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=8)

print(f"The number of faces found = {len(faces_rect)}")
print(faces_rect)

for (x,y,w,h) in faces_rect:
 
    cv.rectangle(face_pic, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', face_pic)
cv.waitKey(0)
cv.destroyAllWindows()
