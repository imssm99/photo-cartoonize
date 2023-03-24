import cv2

def cartoonify(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply median blur to the grayscale image
    gray = cv2.medianBlur(gray, 5)

    # Detect edges in the image
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # Apply bilateral filter to the image
    color = cv2.bilateralFilter(img, 9, 250, 250)

    # Combine the color image with the edges
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Display the resulting image
    cv2.imshow("Cartoon", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Test the function with an image file
cartoonify("./data/lena.tif")
