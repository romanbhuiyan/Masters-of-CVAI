import cv2

# Read the image
image = cv2.imread('cat2.jpeg')

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found.")
else:
    # Apply Non-Local Means denoising on the colored image
    denoised_image = (cv2.fastNlMeansDenoisingColored
                      (image, None, 10, 10, 7, 21))

    # Show the original and denoised images
    cv2.imshow('Original Image', image)
    cv2.imshow('Denoised Image', denoised_image)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
