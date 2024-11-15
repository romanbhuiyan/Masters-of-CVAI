import cv2
import matplotlib.pyplot as plt

# Load the image (ensure 'cat1.jpg' exists in the same directory or provide the full path)
image = cv2.imread('cat1.jpg')

# Check if image is loaded properly
if image is None:
    raise FileNotFoundError("Image not found!")

# Normalize the image by dividing by 255.0
normalized_image = image.astype('float32') / 255.0  # Convert to float32 to prevent data loss

# Display the normalized image using matplotlib
plt.imshow(cv2.cvtColor(normalized_image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for correct color display
plt.axis('off')  # Hide axes
plt.title('Normalized Image')
plt.show()
