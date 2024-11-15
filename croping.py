from PIL import Image
image = Image.open('cat1.jpg')
cropped_image = image.crop((100, 100, 400, 400))
cropped_image.show()