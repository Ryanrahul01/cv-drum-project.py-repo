import cv2 as cv

# ORIGINAL IMAGE
#stores the image as a matrix 
dogpic = cv.imread("/Users/ryanrahul/Documents/CV_ISEF_Project/Photos/dogspic.jpg")
#displays the image 
cv.imshow("twodogs" ,dogpic)

# CONVERTING TO GRAY SCALE
#stored the grayscale image in a varialbe 
gray = cv.cvtColor(dogpic, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale img", gray)

# CONVERTING TO HSV 
#stored the hsv image in a varialbe 
hsv = cv.cvtColor(dogpic, cv.COLOR_BGR2HSV)
cv.imshow("hsv img", hsv)   

#shows how much time the image will be dislplayed for, etc: 0 = infinite time
cv.waitKey(0)
cv.destroyAllWindows()
