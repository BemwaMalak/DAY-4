import matplotlib.pyplot as plt
from bresenham import bresenham_line

def draw_rectangle(x1, y1, x2, y2):
    points = []
    # Calculate the other two corners
    x3, y3 = x2, y1
    x4, y4 = x1, y2
    # Draw lines between the corners
    points.extend(bresenham_line(x1, y1, x3, y3))
    points.extend(bresenham_line(x3, y3, x2, y2))
    points.extend(bresenham_line(x2, y2, x4, y4))
    points.extend(bresenham_line(x4, y4, x1, y1))
    return points

# Define the coordinates of two opposite corners
x1, y1 = 2, 3
x2, y2 = 8, 6

# Get the rectangle points
rectangle_points = draw_rectangle(x1, y1, x2, y2)

# Plot the rectangle
x_coords, y_coords = zip(*rectangle_points)
plt.plot(x_coords, y_coords, marker='o')
plt.title('Rectangle Drawing')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()