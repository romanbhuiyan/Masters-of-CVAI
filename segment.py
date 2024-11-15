import cv2

# Read the image
image = cv2.imread('cat1.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply binary thresholding
_, segmented_image = cv2.threshold(gray, 50, 100, cv2.THRESH_BINARY)

# Show the original image
cv2.imshow('Original Image', image)

# Show the segmented (thresholded) image
cv2.imshow('Segmented Image', segmented_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
