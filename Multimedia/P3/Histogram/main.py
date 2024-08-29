import cv2  # OpenCV library for image processing
import numpy as np  # NumPy library for numerical operations
import matplotlib.pyplot as plt  # Matplotlib library for plotting

# Load the input image in grayscale
image = cv2.imread('input_image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply histogram equalization to enhance the contrast of the image
equalized_image = cv2.equalizeHist(image)

# Create a figure with 2x2 subplots to display images and histograms
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Display the original image
axes[0, 0].imshow(image, cmap='gray')
axes[0, 0].set_title('Original Image')
axes[0, 0].axis('off')  # Hide the axis

# Display the equalized image
axes[0, 1].imshow(equalized_image, cmap='gray')
axes[0, 1].set_title('Equalized Image')
axes[0, 1].axis('off')  # Hide the axis

# Display the histogram of the original image
axes[1, 0].hist(image.ravel(), bins=256, range=(0, 256))
axes[1, 0].set_title('Original Histogram')

# Display the histogram of the equalized image
axes[1, 1].hist(equalized_image.ravel(), bins=256, range=(0, 256))
axes[1, 1].set_title('Equalized Histogram')

# Adjust the layout to prevent overlapping of subplots
plt.tight_layout()
plt.show()