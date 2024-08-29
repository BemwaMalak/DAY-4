import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    x_inc = dx / steps
    y_inc = dy / steps
    
    x, y = x1, y1
    line_points = [(x, y)]
    for _ in range(int(steps)):
        x += x_inc
        y += y_inc
        line_points.append((round(x), round(y)))
    return line_points

# Define start and end points
x1, y1 = 0, 0
x2, y2 = 2, 4

# Get the line points using DDA algorithm
line_points = dda_line(x1, y1, x2, y2)

# Plot the line
x_coords, y_coords = zip(*line_points)
plt.plot(x_coords, y_coords, marker='o')
plt.title('DDA Line Drawing')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()