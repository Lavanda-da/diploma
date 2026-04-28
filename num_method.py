import math
import matplotlib.pyplot as plt


t0 = 0
t1 = 8
h = 0.1
n = int((t1 - t0) / h)
r = 1
EPS = 0.01
points = [[(-2, 2), (-2, -2), (2, -2), (2, 2), (-2.0, 1.5), (-2.0, 1.0), (-2.0, 0.5), (-2.0, 0.0), (-2.0, -0.5), (-2.0, -1.0), (-2.0, -1.5), (-1.5, -2.0), (-1.0, -2.0), (-0.5, -2.0), (0.0, -2.0), (0.5, -2.0), (1.0, -2.0), (1.5, -2.0), (2.0, -1.5), (2.0, -1.0), (2.0, -0.5), (2.0, 0.0), (2.0, 0.5), (2.0, 1.0), (2.0, 1.5), (1.5, 2.0), (1.0, 2.0), (0.5, 2.0), (0.0, 2.0), (-0.5, 2.0), (-1.0, 2.0), (-1.5, 2.0), (-1.5, 1.25), (-1.5, 0.25), (-1.5, -0.75), (-1.25, -1.5), (-0.25, -1.5), (0.75, -1.5), (1.5, -1.25), (1.5, -0.25), (1.5, 0.75), (1.25, 1.5), (0.25, 1.5), (-0.75, 1.5), (-1.0, 0.75), (-1.0, -0.25), (-0.9006583509747431, -0.966886116991581), (0.25, -1.0), (0.966886116991581, -0.9006583509747431), (1.0, 0.25), (0.9006583509747431, 0.966886116991581), (-0.25, 1.0), (-0.5, 0.25)]]
edges = [(0, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 1), (1, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 2), (2, 18), (18, 19), (19, 20), (20, 21), (21, 22), (22, 23), (23, 24), (24, 3), (3, 25), (25, 26), (26, 27), (27, 28), (28, 29), (29, 30), (30, 31), (31, 0), (0, 31), (31, 4), (4, 32), (32, 5), (5, 32), (32, 6), (6, 33), (33, 7), (7, 33), (33, 8), (8, 34), (34, 9), (9, 34), (34, 10), (10, 11), (11, 1), (11, 35), (35, 12), (12, 35), (35, 13), (13, 36), (36, 14), (14, 36), (36, 15), (15, 37), (37, 16), (16, 37), (37, 17), (17, 18), (18, 2), (18, 38), (38, 19), (19, 38), (38, 20), (20, 39), (39, 21), (21, 39), (39, 22), (22, 40), (40, 23), (23, 40), (40, 24), (24, 25), (25, 3), (25, 41), (41, 26), (26, 41), (41, 27), (27, 42), (42, 28), (28, 42), (42, 29), (29, 43), (43, 30), (30, 32), (32, 31), (31, 32), (32, 4), (32, 33), (33, 6), (33, 34), (34, 8), (34, 35), (35, 10), (10, 35), (35, 11), (35, 36), (36, 13), (36, 37), (37, 15), (37, 38), (38, 17), (17, 38), (38, 18), (38, 39), (39, 20), (39, 40), (40, 22), (40, 41), (41, 24), (24, 41), (41, 25), (41, 42), (42, 27), (42, 43), (43, 29), (43, 32), (32, 30), (32, 44), (44, 33), (33, 45), (45, 34), (34, 46), (46, 35), (35, 46), (46, 36), (36, 47), (47, 37), (37, 48), (48, 38), (38, 48), (48, 39), (39, 49), (49, 40), (40, 50), (50, 41), (41, 50), (50, 42), (42, 51), (51, 43), (43, 44), (44, 32), (44, 45), (45, 33), (45, 46), (46, 34), (46, 47), (47, 36), (47, 48), (48, 37), (48, 49), (49, 39), (49, 50), (50, 40), (50, 51), (51, 42), (51, 44), (44, 43), (44, 52), (52, 45), (45, 47), (47, 46), (47, 49), (49, 48), (49, 51), (51, 50), (51, 52), (52, 44), (52, 47), (47, 45), (47, 52), (52, 49), (49, 52), (52, 51)]
triags = [(0, 31, 4), (4, 32, 5), (5, 32, 6), (6, 33, 7), (7, 33, 8), (8, 34, 9), (9, 34, 10), (10, 11, 1), (11, 35, 12), (12, 35, 13), (13, 36, 14), (14, 36, 15), (15, 37, 16), (16, 37, 17), (17, 18, 2), (18, 38, 19), (19, 38, 20), (20, 39, 21), (21, 39, 22), (22, 40, 23), (23, 40, 24), (24, 25, 3), (25, 41, 26), (26, 41, 27), (27, 42, 28), (28, 42, 29), (29, 43, 30), (30, 32, 31), (31, 32, 4), (32, 33, 6), (33, 34, 8), (34, 35, 10), (10, 35, 11), (35, 36, 13), (36, 37, 15), (37, 38, 17), (17, 38, 18), (38, 39, 20), (39, 40, 22), (40, 41, 24), (24, 41, 25), (41, 42, 27), (42, 43, 29), (43, 32, 30), (32, 44, 33), (33, 45, 34), (34, 46, 35), (35, 46, 36), (36, 47, 37), (37, 48, 38), (38, 48, 39), (39, 49, 40), (40, 50, 41), (41, 50, 42), (42, 51, 43), (43, 44, 32), (44, 45, 33), (45, 46, 34), (46, 47, 36), (47, 48, 37), (48, 49, 39), (49, 50, 40), (50, 51, 42), (51, 44, 43), (44, 52, 45), (45, 47, 46), (47, 49, 48), (49, 51, 50), (51, 52, 44), (52, 47, 45), (47, 52, 49), (49, 52, 51)]

edges_dict = {}

for i in range(len(edges)):
    key = edges[i]
    if key[1] < key[0]:
        key = (key[1], key[0])
    edges_dict[key] = ['able']


for i in range(len(triags)):
    key = sorted([triags[i][0], triags[i][1], triags[i][2]])
    triags[i] = (key[0], key[1], key[2])

now_points = []
for i in range(len(points[-1])):
    now_points += [(points[-1][i][1], points[-1][i][1] * h + points[-1][i][0])]
points += [now_points]


for i in range(2, n + 1):
    print(i, n)
    j = 0

    while j < len(triags):
        x, y = (points[-1][triags[j][0]][0] + points[-1][triags[j][1]][0] + points[-1][triags[j][2]][0]) / 3, \
                        (points[-1][triags[j][0]][1] + points[-1][triags[j][1]][1] + points[-1][triags[j][2]][1]) / 3  # control_point

        x1, y1 = points[-1][triags[j][0]][0], points[-1][triags[j][0]][1]
        x2, y2 = points[-1][triags[j][1]][0], points[-1][triags[j][1]][1]
        x3, y3 = points[-1][triags[j][2]][0], points[-1][triags[j][2]][1]
        delta = x2 * y3 + x3 * y1 + x1 * y2 - \
                (x2 * y1 + x3 * y2 + x1 * y3)

        alfa = x2 * y3 + x3 * y + x * y2 - \
               (x2 * y + x3 * y2 + x * y3)
        beta = x * y3 + x3 * y1 + x1 * y - \
               (x * y1 + x3 * y + x1 * y3)
        gama = x2 * y + x * y1 + x1 * y2 - \
               (x2 * y1 + x * y2 + x1 * y)
        alfa /= delta
        beta /= delta
        gama /= delta

        new_value1 = 0.3 * h ** 2 * math.cos(i * h) + (2 + 0.25 * h + h ** 2) * points[-1][triags[j][0]][1] - points[-1][triags[j][0]][1] ** 3 * h ** 2 - points[-1][triags[j][0]][0]
        new_value2 = 0.3 * h ** 2 * math.cos(i * h) + (2 + 0.25 * h + h ** 2) * points[-1][triags[j][1]][1] - points[-1][triags[j][1]][1] ** 3 * h ** 2 - points[-1][triags[j][1]][0]
        new_value3 = 0.3 * h ** 2 * math.cos(i * h) + (2 + 0.25 * h + h ** 2) * points[-1][triags[j][2]][1] - points[-1][triags[j][2]][1] ** 3 * h ** 2 - points[-1][triags[j][2]][0]
        new_control_value = 0.3 * h ** 2 * math.cos(i * h) + (2 + 0.25 * h + h ** 2) * y - \
                     y ** 3 * h ** 2 - x

        interpolation_value = alfa * new_value1 + beta * new_value2 + gama * new_value3

        if abs(interpolation_value - new_control_value) < EPS:
            j += 1
        else:
            triag = triags[j]

            mid1 = ((points[-1][triag[0]][0] + points[-1][triag[1]][0]) / 2,
                    (points[-1][triag[0]][1] + points[-1][triag[1]][1]) / 2)  # 0, 1 points
            mid2 = ((points[-1][triag[1]][0] + points[-1][triag[2]][0]) / 2,
                    (points[-1][triag[1]][1] + points[-1][triag[2]][1]) / 2)  # 0, 2 points
            mid3 = ((points[-1][triag[0]][0] + points[-1][triag[2]][0]) / 2,
                    (points[-1][triag[0]][1] + points[-1][triag[2]][1]) / 2)  # 0, 2 points
            ind_mid1, ind_mid2, ind_mid3 = None, None, None
            if mid1 not in points[-1]:
                points[-1] += [mid1]
                ind_mid1 = len(points[-1]) - 1
            else:
                ind_mid1 = points[-1].index(mid1)
            if mid2 not in points[-1]:
                points[-1] += [mid2]
                ind_mid2 = len(points[-1]) - 1
            else:
                ind_mid2 = points[-1].index(mid2)
            if mid3 not in points[-1]:
                points[-1] += [mid3]
                ind_mid3 = len(points[-1]) - 1
            else:
                ind_mid3 = points[-1].index(mid3)

            edges_dict[(triag[0], triag[1])] = ['disable', ind_mid1]
            edges_dict[(triag[1], triag[2])] = ['disable', ind_mid2]
            edges_dict[(triag[0], triag[2])] = ['disable', ind_mid3]

            del triags[j]

            if tuple(sorted([triag[0], ind_mid1])) not in edges_dict:
                edges_dict[tuple(sorted([triag[0], ind_mid1]))] = ['able']
            if tuple(sorted([triag[0], ind_mid3])) not in edges_dict:
                edges_dict[tuple(sorted([triag[0], ind_mid3]))] = ['able']
            if tuple(sorted([ind_mid1, ind_mid3])) not in edges_dict:
                edges_dict[tuple(sorted([ind_mid1, ind_mid3]))] = ['able']
            triags += [tuple(sorted([triag[0], ind_mid1, ind_mid3]))]

            if tuple(sorted([triag[2], ind_mid2])) not in edges_dict:
                edges_dict[tuple(sorted([triag[2], ind_mid2]))] = ['able']
            if tuple(sorted([triag[2], ind_mid3])) not in edges_dict:
                edges_dict[tuple(sorted([triag[2], ind_mid3]))] = ['able']
            if tuple(sorted([ind_mid2, ind_mid3])) not in edges_dict:
                edges_dict[tuple(sorted([ind_mid2, ind_mid3]))] = ['able']
            triags += [tuple(sorted([triag[2], ind_mid2, ind_mid3]))]

            if tuple(sorted([triag[1], ind_mid1])) not in edges_dict:
                edges_dict[tuple(sorted([triag[1], ind_mid1]))] = ['able']
            if tuple(sorted([triag[1], ind_mid2])) not in edges_dict:
                edges_dict[tuple(sorted([triag[1], ind_mid2]))] = ['able']
            if tuple(sorted([ind_mid1, ind_mid2])) not in edges_dict:
                edges_dict[tuple(sorted([ind_mid1, ind_mid2]))] = ['able']
            triags += [tuple(sorted([triag[1], ind_mid1, ind_mid2]))]

            if tuple(sorted([ind_mid1, ind_mid3])) not in edges_dict:
                edges_dict[tuple(sorted([ind_mid1, ind_mid3]))] = ['able']
            if tuple(sorted([ind_mid2, ind_mid3])) not in edges_dict:
                edges_dict[tuple(sorted([ind_mid2, ind_mid3]))] = ['able']
            if tuple(sorted([ind_mid1, ind_mid2])) not in edges_dict:
                edges_dict[tuple(sorted([ind_mid1, ind_mid2]))] = ['able']
            triags += [tuple(sorted([ind_mid1, ind_mid2, ind_mid3]))]

    j = 0

    while j < len(triags):
        point1 = triags[j][0]
        point2 = triags[j][1]
        point3 = triags[j][2]
        edge1 = (point1, point2)
        edge2 = (point1, point3)
        edge3 = (point2, point3)

        if edges_dict[edge1][0] == 'able' and \
           edges_dict[edge2][0] == 'able' and \
           edges_dict[edge3][0] == 'able':
            j += 1
        else:
            if edges_dict[edge1][0] != 'able':
                triags += [tuple(sorted([point1, point3, edges_dict[edge1][1]])), tuple(sorted([point2, point3, edges_dict[edge1][1]]))]
                edges_dict[tuple(sorted([point3, edges_dict[edge1][1]]))] = ['able']
                del triags[j]
            elif edges_dict[edge2][0] != 'able':
                triags += [tuple(sorted([point1, point2, edges_dict[edge2][1]])), tuple(sorted([point2, point3, edges_dict[edge2][1]]))]
                edges_dict[tuple(sorted([point2, edges_dict[edge2][1]]))] = ['able']
                del triags[j]
            elif edges_dict[edge3][0] != 'able':
                triags += [tuple(sorted([point1, point2, edges_dict[edge3][1]])), tuple(sorted([point1, point3, edges_dict[edge3][1]]))]
                edges_dict[tuple(sorted([point1, edges_dict[edge3][1]]))] = ['able']
                del triags[j]
            else:
                print("Smth wrong")


    now_points = []
    for j in range(len(points[-1])):
        new_value = 0.3 * h ** 2 * math.cos(i * h) + (2 + 0.25 * h + h ** 2) * points[-1][j][1] - points[-1][j][1] ** 3 * h ** 2 - points[-1][j][0]
        now_points += [(points[-1][j][1], new_value)]
    points += [now_points]

    if i == 10:
        break


time_moment = int((1 - t0) / h)

points = points[time_moment]


for edge in edges_dict.keys():
    if edges_dict[edge][0] == 'able':
        x_coords = [points[edge[0]][0], points[edge[1]][0]]
        y_coords = [points[edge[0]][1], points[edge[1]][1]]

        plt.plot(x_coords, y_coords, linewidth=1, color='black')

for i in range(len(points)):
    plt.plot(points[i][0], points[i][1], 'ro', markersize=8, color='black')

# plt.axis('equal')
plt.grid(True)
plt.show()
