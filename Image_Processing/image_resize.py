import cv2 as cv

# ORIGINAL IMAGE
#stores the image as a matrix 
dogpic = cv.imread("/Users/ryanrahul/Documents/CV_ISEF_Project/Photos/dogspic.jpg")
#displays the image 
cv.imshow("twodogs" ,dogpic)

# RESIZING IMAGE using dsize
original_height = dogpic.shape[0]
original_width = dogpic.shape[1]

new_height = original_height * 0.1
new_width = original_width * 0.1

resized_image = cv.resize(dogpic, (int(new_width), int(new_height)))

cv.imshow("Resized Image using dsize", resized_image)

#RESIZING IMAGE using scaling factor
sf_image = cv.resize(dogpic, None, fx=0.05, fy=0.05)
cv.imshow("sf_image", sf_image)

#shows how much time the image will be dislplayed for, etc: 0 = infinite time
cv.waitKey(0)
cv.destroyAllWindows()