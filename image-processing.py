import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

# Load the image
image_path = 'images/cat1.jpg'
image = cv2.imread(image_path)

# Step 1: Resize the image to a consistent size (e.g., 256x256 pixels)
resized_image = cv2.resize(image, (256, 256))

# Step 2: Convert to grayscale
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply Gaussian Blur to remove noise
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Step 4: Enhance contrast using Histogram Equalization
enhanced_image = cv2.equalizeHist(blurred_image)

# Step 5: Apply thresholding to create a binary image (optional, based on analysis needs)
_, binary_image = cv2.threshold(enhanced_image, 128, 255, cv2.THRESH_BINARY)

# Save the preprocessed images
cv2.imwrite('images/cat1.jpeg', resized_image)
cv2.imwrite('images/cat1.jpeg', gray_image)
cv2.imwrite('images/cat1.jpeg', blurred_image)
cv2.imwrite('images/cat1.jpeg', enhanced_image)
cv2.imwrite('images/cat1.jpeg', binary_image)

print("Preprocessing complete. Images saved.")

# Display the images
images = [resized_image, gray_image, blurred_image, enhanced_image, binary_image]
titles = ["Resized Image", "Grayscale Image", "Blurred Image", "Enhanced Image", "Binary Image"]

plt.figure(figsize=(15, 5))
for i in range(len(images)):
    plt.subplot(1, 5, i + 1)
    plt.imshow(images[i], cmap='gray' if len(images[i].shape) == 2 else None)
    plt.title(titles[i])
    plt.axis('off')

plt.show()