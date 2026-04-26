points = [(-2, 2), (-2, -2), (2, 2)]
triags = [(0, 1, 2)]

i = 0
triag = triags[i]

mid1 = ((points[triag[0]][0] + points[triag[1]][0]) / 2, (points[triag[0]][1] + points[triag[1]][1]) / 2)  # 0, 1 points
mid2 = ((points[triag[1]][0] + points[triag[2]][0]) / 2, (points[triag[1]][1] + points[triag[2]][1]) / 2)  # 0, 2 points
mid3 = ((points[triag[0]][0] + points[triag[2]][0]) / 2, (points[triag[0]][1] + points[triag[2]][1]) / 2)  # 0, 2 points
points += [mid1, mid2, mid3]

del triags[i]
triags += [(0, len(points) - 1), (len(points) - 1, len(points) - 3), (0, len(points) - 3)]
triags += [(1, len(points) - 1), (len(points) - 1, len(points) - 2), (1, len(points) - 2)]
triags += [(2, len(points) - 3), (len(points) - 3, len(points) - 2), (2, len(points) - 2)]
triags += [(len(points) - 1, len(points) - 3), (len(points) - 3, len(points) - 2), (len(points) - 1, len(points) - 2)]
