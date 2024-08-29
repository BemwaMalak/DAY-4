import cv2

# Open the video file
cap = cv2.VideoCapture('video_file.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        # Display the frame
        cv2.imshow('Frame', frame)
        
        # Wait for a key press to proceed
        key = cv2.waitKey(0)  # Wait indefinitely for a key press
        
        # Press 'q' to exit the video display
        if key == ord('q'):
            break
    else:
        break

# Release the video capture object and close windows
cap.release()
cv2.destroyAllWindows()
