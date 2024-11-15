import cv2

# Read the image
image = cv2.imread('cat1.jpg')

# Check if image is loaded properly
if image is None:
    print("Error: Image not found!")
else:
    # Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Display the blurred image
    cv2.imshow('Blurred Image', blurred_image)

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Optionally, save the blurred image
    cv2.imwrite('blurred_example.jpg', blurred_image)
