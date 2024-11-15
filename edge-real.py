import cv2
import numpy as np

# Read the image
image = cv2.imread('cat2.jpeg')  # Replace with your image path

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found.")
else:
    # Convert the image to grayscale (Canny operates on single channel)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise (optional but improves edge detection)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 1.4)

    # Apply Canny Edge Detection
    edges = cv2.Canny(blurred_image, threshold1=50, threshold2=150)

    # Show the original and edge-detected images
    cv2.imshow('Original Image', image)
    cv2.imshow('Edge Detected Image', edges)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
