import cv2 as cv

# ORIGINAL IMAGE
#stores the image as a matrix 
dogpic = cv.imread("/Users/ryanrahul/Documents/CV_ISEF_Project/Photos/dogspic.jpg")
#displays the image 
cv.imshow("twodogs" ,dogpic)

#shows how much time the image will be dislplayed for, etc: 0 = infinite time
cv.waitKey(0)
cv.destroyAllWindows()