from PIL import Image

# Open the image file (ensure 'cat.jpg' is in the same directory or provide the full path)
image = Image.open('cat1.jpg')

# Resize the image to 128x128 pixels
resized_image = image.resize((128, 128))

# Display the resized image
resized_image.show()

