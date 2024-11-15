import os
from PIL import Image
import numpy as np
import cv2
import concurrent.futures

# Define the input and output folders
image_folder = 'images'  # Replace with the path to your images
output_folder = 'path_to_save_processed_images'  # Replace with the path to save processed images

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)


def process_image(filename):
    try:
        # Define the full path for each image
        image_path = os.path.join(image_folder, filename)

        # Load the image
        analog_image = Image.open(image_path)

        # Convert to grayscale
        gray_image = analog_image.convert("L")

        # Convert to a NumPy array for OpenCV processing
        gray_array = np.array(gray_image)

        # Apply binary threshold
        _, binary_image = cv2.threshold(gray_array, 128, 255, cv2.THRESH_BINARY)

        # Save the processed image directly to the output folder
        output_path = os.path.join(output_folder, f"processed_{filename}")
        cv2.imwrite(output_path, binary_image)
        print(f"Processed and saved: {filename}")

    except Exception as e:
        # Handle any issues (file format, corruption, etc.)
        print(f"Error processing {filename}: {e}")


# Use ThreadPoolExecutor to process images in parallel
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Get a list of valid image files (adjust extensions if needed)
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]

    # Process each image file in parallel
    executor.map(process_image, image_files)
