from cartoonize import cartoonize
import cv2 as cv

# Load the image
img = cv.imread("./data/lena.tif")

# Display the resulting image
cv.imshow("Photo Cartoonize", cartoonize(img))
cv.waitKey(0)
cv.destroyAllWindows()