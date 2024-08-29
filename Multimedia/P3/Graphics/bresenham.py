import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    
    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    return points

# Define start and end points
x1, y1 = 0, 0
x2, y2 = 2, 4

# Get the line points using Bresenham's algorithm
line_points = bresenham_line(x1, y1, x2, y2)

# Plot the line
x_coords, y_coords = zip(*line_points)
plt.plot(x_coords, y_coords, marker='o')
plt.title('Bresenham\'s Line Drawing')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()