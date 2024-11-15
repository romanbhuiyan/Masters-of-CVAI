import cv2
import numpy as np

# Read the image in grayscale
image = cv2.imread('cat1.jpg', 0)

# Ensure that the image is in the appropriate format (binary or grayscale)
# Optionally, apply thresholding if the image is not binary
_, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

# Define the kernel for dilation
kernel = np.ones((5, 5), np.uint8)

# Apply dilation to the binary image
dilated_image = cv2.dilate(binary_image, kernel, iterations=3)

# Show the original and dilated images
cv2.imshow('Original Image', binary_image)
cv2.imshow('Dilated Image', dilated_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
