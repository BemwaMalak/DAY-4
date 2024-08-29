import cv2
import matplotlib.pyplot as plt

# Load the input image
image = cv2.imread('input_image.png')

# Apply Gaussian filtering
sigma = 1.5  # Standard deviation
gaussian_filtered_image = cv2.GaussianBlur(image, (5, 5), sigma)

# Plot the original and Gaussian filtered images
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Display original image
axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axes[0].set_title('Original Image')
axes[0].axis('off')

# Display Gaussian filtered image
axes[1].imshow(cv2.cvtColor(gaussian_filtered_image, cv2.COLOR_BGR2RGB))
axes[1].set_title('Gaussian Filtered Image')
axes[1].axis('off')

plt.tight_layout()
plt.show()