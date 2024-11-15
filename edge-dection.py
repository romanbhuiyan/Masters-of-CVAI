import cv2

# Read the image in grayscale
image = cv2.imread('cat1.jpg', 0)

# Apply Canny edge detection
edges = cv2.Canny(image, 50, 50)

# Show the original image
cv2.imshow('Original Image', image)

# Show the edge-detected image
cv2.imshow('Edge Detection', edges)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
