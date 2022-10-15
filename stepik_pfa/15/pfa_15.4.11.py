import turtle


def distance(i):
    return (i[0]**2 + i[1]**2) ** 0.5


points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2),
          (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]

print(sorted(points, key=turtle.distance))
points.sort(key=distance)

print(points)
