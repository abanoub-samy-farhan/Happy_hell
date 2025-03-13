import matplotlib.pyplot as plt
import random

# Function to generate random points
def generate_points(n, xlim=(0, 10), ylim=(0, 10)):
    return [(random.uniform(*xlim), random.uniform(*ylim)) for _ in range(n)]

# Compute the orientation of three points
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else -1  # Clockwise or Counterclockwise

# Graham's Scan Algorithm to find the Convex Hull
def graham_scan(points):
    points = sorted(points)  # Sort by x, then y
    hull = [] 

    # Build lower hull
    for p in points:
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], p) != -1:
            hull.pop()
        hull.append(p)

    # Build upper hull
    upper_hull = []
    for p in reversed(points):
        while len(upper_hull) >= 2 and orientation(upper_hull[-2], upper_hull[-1], p) != -1:
            upper_hull.pop()
        upper_hull.append(p)

    return hull[:-1] + upper_hull[:-1]  # Remove duplicates

# Generate random points
num_points = 50
points = generate_points(num_points)

# Compute the convex hull
hull = graham_scan(points)

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(*zip(*points), label="Random Points", color="blue", s=20)
plt.plot(*zip(*(hull + [hull[0]])), 'r-', label="Convex Hull", linewidth=2)  # Close the hull
plt.legend()
plt.show()
