import matplotlib.pyplot as plt
import random

def generate_points(n, xlim=(0, 10), ylim=(0, 10)):
    points = []
    while len(points) < n:
        p = (random.uniform(*xlim), random.uniform(*ylim))
        if all(orientation(points[i], points[j], p) != 0 for i in range(len(points)) for j in range(i+1, len(points))):
            points.append(p)
    return points

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  
    return 1 if val > 0 else -1  

def graham_scan(points):
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

num_points = 17
points = generate_points(num_points)
hull1 = graham_scan(points)
remaining_points = [p for p in points if p not in hull1]

hull2 = graham_scan(remaining_points) if len(remaining_points) >= 3 else []

print("Number of sides of the first convex hull:", len(hull1))
print("Number of sides of the second convex hull:", len(hull2) if hull2 else "N/A")

plt.figure(figsize=(8, 6))
plt.scatter(*zip(*points), label="Random Points", color="blue", s=20)
plt.plot(*zip(*(hull1 + [hull1[0]])), 'r-', label="First Convex Hull", linewidth=2)
if hull2:
    plt.plot(*zip(*(hull2 + [hull2[0]])), 'g-', label="Second Convex Hull", linewidth=2)
plt.legend()
plt.show()

print("Number of sides of the first convex hull:", len(hull1))
print("Number of sides of the second convex hull:", len(hull2) if hull2 else "N/A")

print("\nCoordinates of all points:")
for point in points:
    print(point)

print("\nCoordinates of the first convex hull:")
for point in hull1:
    print(point)

if hull2:
    print("\nCoordinates of the second convex hull:")
    for point in hull2:
        print(point)
else:
    print("\nNo second convex hull found.")
