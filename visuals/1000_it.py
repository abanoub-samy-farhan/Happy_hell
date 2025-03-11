import matplotlib.pyplot as plt
import random

def generate_points(n, xlim=(0, 10), ylim=(0, 10)):
    """
    generate_points - Generates random points ensuring no three are collinear

    Args:
        n (int): Number of points to generate
        xlim (tuple): X-axis limits
        ylim (tuple): Y-axis limits

    Returns:
        list: List of generated points
    """
    points = []
    while len(points) < n:
        p = (random.uniform(*xlim), random.uniform(*ylim))
        if all(orientation(points[i], points[j], p) != 0 for i in range(len(points)) for j in range(i+1, len(points))):
            points.append(p)
    return points

def orientation(p, q, r):
    """
    orientation - Determines the orientation of three points

    Args:
        p (tuple): First point
        q (tuple): Second point
        r (tuple): Third point

    Returns:
        int: 0 if collinear, 1 if clockwise, -1 if counterclockwise
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  
    return 1 if val > 0 else -1  

def graham_scan(points):
    """
    graham_scan - Computes the convex hull using Graham's scan algorithm

    Args:
        points (list): List of points

    Returns:
        list: Convex hull as a list of points
    """
    points = sorted(points)  
    
    def build_hull(points):
        hull = []
        for p in points:
            while len(hull) >= 2 and orientation(hull[-2], hull[-1], p) != -1:
                hull.pop()
            hull.append(p)
        return hull
    
    lower_hull = build_hull(points)
    upper_hull = build_hull(reversed(points))
    
    return lower_hull[:-1] + upper_hull[:-1]  

num_points = 32
iterations = 10000
smallest_hull = None
second_smallest_hull = None
smallest_hull_size = float('inf')
second_smallest_hull_size = float('inf')
smallest_points = None
second_smallest_points = None

for _ in range(iterations):
    points = generate_points(num_points)
    hull1 = graham_scan(points)
    hull1_size = len(hull1)
    
    remaining_points = [p for p in points if p not in hull1]
    hull2 = graham_scan(remaining_points) if len(remaining_points) >= 3 else []
    hull2_size = len(hull2)
    
    if hull1_size < smallest_hull_size or (hull1_size == smallest_hull_size and hull2_size < second_smallest_hull_size):
        second_smallest_hull_size = smallest_hull_size
        second_smallest_hull = smallest_hull
        second_smallest_points = smallest_points
        
        smallest_hull_size = hull1_size
        smallest_hull = hull1
        smallest_points = points
    elif hull1_size < second_smallest_hull_size or (hull1_size == second_smallest_hull_size and hull2_size < second_smallest_hull_size):
        second_smallest_hull_size = hull1_size
        second_smallest_hull = hull1
        second_smallest_points = points

print("Number of sides of the smallest convex hull:", len(smallest_hull))
print("Number of sides of the second smallest convex hull:", len(second_smallest_hull) if second_smallest_hull else "N/A")

plt.figure(figsize=(8, 6))
plt.scatter(*zip(*smallest_points), color="blue", s=20, label="Random Points")
plt.plot(*zip(*(smallest_hull + [smallest_hull[0]])), 'r-', linewidth=2, label="Smallest Convex Hull")
if second_smallest_hull:
    plt.plot(*zip(*(second_smallest_hull + [second_smallest_hull[0]])), 'g-', linewidth=2, label="Second Smallest Convex Hull")
plt.legend()
plt.show()