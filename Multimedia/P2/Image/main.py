from PIL import Image

# Open the image file
img = Image.open('imagefile.jpg')

# Get the resolution of the image
width, height = img.size

print(f'Resolution: {width}x{height}')

# Get the color mode of the image
color_mode = img.mode

print(f'Color Mode: {color_mode}')