import numpy as np
import matplotlib.pyplot as plt
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array

# Directory to save augmented images
save_dir = 'augmented_images'

# Check if the directory exists, if not, create it
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Initialize the ImageDataGenerator with augmentation parameters
image_gen = ImageDataGenerator(rotation_range=20,
                               width_shift_range=0.2,
                               height_shift_range=0.2,
                               horizontal_flip=True)

# Load an example image to demonstrate augmentation
img = load_img('cat1.jpg')  # Replace with your image path
x = img_to_array(img)        # Convert image to numpy array
x = np.expand_dims(x, axis=0)  # Add batch dimension

# Generate augmented images
i = 0
for batch in image_gen.flow(x, batch_size=1, save_to_dir=save_dir, save_prefix='aug', save_format='jpeg'):
    plt.figure(i)
    imgplot = plt.imshow(batch[0].astype('uint8'))
    i += 1
    if i % 5 == 0:  # Stop after generating 5 images
        break

plt.show()
