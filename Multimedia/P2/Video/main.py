import cv2

# Open the video file
cap = cv2.VideoCapture('video_file.mp4')

# Get the resolution of the video
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Print the resolution
print(f'Resolution: {width}x{height}')

# Print the frame rate
print(f'Frame Rate: {fps} fps')

# Release the video capture object
cap.release()