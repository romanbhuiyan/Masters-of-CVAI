import cv2
import numpy as np

# Read the image
image = cv2.imread('cat2.jpeg')

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found.")
else:
    # Define the gamma correction value
    gamma = 2.2

    # Create the lookup table for gamma correction
    look_up_table = np.array([((i / 255.0) ** gamma) * 255 for i in np.arange(0, 256)]).astype('uint8')

    # Apply gamma correction using LUT (Look-Up Table)
    gamma_corrected_image = cv2.LUT(image, look_up_table)

    # Show the original and gamma-corrected images
    cv2.imshow('Original Image', image)
    cv2.imshow('Gamma Corrected Image', gamma_corrected_image)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
