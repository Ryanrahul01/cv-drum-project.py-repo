import cv2 as cv

# ORIGINAL IMAGE
#stores the image as a matrix 
dogpic = cv.imread("/Users/ryanrahul/Documents/CV_ISEF_Project/Photos/dogspic.jpg")
#displays the image 

sf_image = cv.resize(dogpic, None, fx=0.05, fy=0.05)
cv.imshow("sf_image", sf_image)

#Blurring regularly
blurred_dog_pic = cv.blur(sf_image, (7, 7))
cv.imshow("Blurred Dog Pic", blurred_dog_pic)

#Gaussian Blur
gaussian_blur_img = cv.GaussianBlur(sf_image, (7,7), 0)
cv.imshow("Gaussian img", gaussian_blur_img)

#Bilateral Blur
bilateral_blur = cv.bilateralFilter(sf_image, 7, 100, 7)
cv.imshow("Bilateral Blur",bilateral_blur)

#shows how much time the image will be displayed for, etc: 0 = infinite time
cv.waitKey(0)
cv.destroyAllWindows()