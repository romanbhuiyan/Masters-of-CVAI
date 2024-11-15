import cv2

# Load the original image
image_path = 'cat2.jpeg'  # Replace with the path to your image
original_image = cv2.imread(image_path)

# Convert to grayscale
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Save the grayscale image
cv2.imwrite('gray_image1.jpg', gray_image)
print("Grayscale image saved as 'gray_image.jpg'")
