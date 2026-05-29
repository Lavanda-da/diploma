import math
import matplotlib.pyplot as plt
import json
import time
import numpy as np
import random


def runge_kutty(point, t, h):
    k1_x, k1_y = point[1], point[0] - 0.25 * point[1] - point[0] ** 3 + 0.3 * math.cos(t)
    k2_x, k2_y = point[1] + h / 2 * k1_y, point[0] + h / 2 * k1_x - 0.25 * (point[1] + h / 2 * k1_y) - (
                point[0] + h / 2 * k1_x) ** 3 + 0.3 * math.cos(t + h / 2)
    k3_x, k3_y = point[1] + h / 2 * k2_y, point[0] + h / 2 * k2_x - 0.25 * (point[1] + h / 2 * k2_y) - (
                point[0] + h / 2 * k2_x) ** 3 + 0.3 * math.cos(t + h / 2)
    k4_x, k4_y = point[1] + h * k3_y, point[0] + h * k3_x - 0.25 * (point[1] + h * k3_y) - (
                point[0] + h * k3_x) ** 3 + 0.3 * math.cos(t + h)

    new_value_x = point[0] + h / 6 * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)
    new_value_y = point[1] + h / 6 * (k1_y + 2 * k2_y + 2 * k3_y + k4_y)

    return new_value_x, new_value_y


t0 = 0
t1 = 3
h = 0.1
n = int((t1 - t0) / h)
EPS = 0.0001

points = None
with open('start_points_42.json', 'r') as f:
    points = json.load(f)
for i in range(len(points[-1])):
    points[-1][i] = tuple(points[-1][i])

edges = None
with open('start_edges_42.json', 'r') as f:
    edges = json.load(f)
for i in range(len(edges)):
    edges[i] = tuple(edges[i])

triags = None
with open('start_triags_42.json', 'r') as f:
    triags = json.load(f)
for i in range(len(triags)):
    triags[i] = tuple(triags[i])


start_time = time.time()

edges_dict = {}

for i in range(len(edges)):
    key = edges[i]
    if key[1] < key[0]:
        key = (key[1], key[0])
    edges_dict[key] = ['able']


for i in range(len(triags)):
    key = sorted([triags[i][0], triags[i][1], triags[i][2]])
    triags[i] = (key[0], key[1], key[2])

triags_list = [triags[:]]
triag_grinding = [{}]


for i in range(n):
    j = 0
    triags = triags_list[-1][:]
    triag_grinding_now = {}
    while j < len(triags):
        x, y = (points[-1][triags[j][0]][0] + points[-1][triags[j][1]][0] + points[-1][triags[j][2]][0]) / 3, \
                        (points[-1][triags[j][0]][1] + points[-1][triags[j][1]][1] + points[-1][triags[j][2]][1]) / 3  # control_point

        x1, y1 = points[-1][triags[j][0]][0], points[-1][triags[j][0]][1]
        x2, y2 = points[-1][triags[j][1]][0], points[-1][triags[j][1]][1]
        x3, y3 = points[-1][triags[j][2]][0], points[-1][triags[j][2]][1]
        mid1 = ((points[-1][triags[j][0]][0] + points[-1][triags[j][1]][0]) / 2,
                (points[-1][triags[j][0]][1] + points[-1][triags[j][1]][1]) / 2)  # 0, 1 points
        mid2 = ((points[-1][triags[j][1]][0] + points[-1][triags[j][2]][0]) / 2,
                (points[-1][triags[j][1]][1] + points[-1][triags[j][2]][1]) / 2)  # 1, 2 points
        mid3 = ((points[-1][triags[j][0]][0] + points[-1][triags[j][2]][0]) / 2,
                (points[-1][triags[j][0]][1] + points[-1][triags[j][2]][1]) / 2)  # 0, 2 points

        random_cntr_points = []
        for ind_random_cntr_point in range(0):
            r1 = random.random()
            r2 = random.random()

            if r1 + r2 > 1:
                r1 = 1 - r1
                r2 = 1 - r2

            a = r1
            b = r2
            c = 1 - a - b

            random_x = a * x1 + b * x2 + c * x3
            random_y = a * y1 + b * y2 + c * y3

            random_cntr_points += [(random_x, random_y)]

        # matrix = np.array([[1, 1, 1, 1, 1, 1],
        #                   [x1, x2, x3, mid1[0], mid2[0], mid3[0]],
        #                   [y1, y2, y3, mid1[1], mid2[1], mid3[1]],
        #                   [x1 * y1, x2 * y2, x3 * y3, mid1[0] * mid1[1], mid2[0] * mid2[1], mid3[0] * mid3[1]],
        #                   [x1 ** 2, x2 ** 2, x3 ** 2, mid1[0] ** 2, mid2[0] ** 2, mid3[0] ** 2],
        #                   [y1 ** 2, y2 ** 2, y3 ** 2, mid1[1] ** 2, mid2[1] ** 2, mid3[1] ** 2]])
        #
        # delta = np.linalg.det(matrix)
        #
        # d = [1, x, y, x * y, x ** 2, y ** 2]
        # koef = []
        # for jj in range(matrix.shape[0]):
        #     new_matrix = matrix.copy()
        #     for ii in range(matrix.shape[1]):
        #         new_matrix[ii, jj] = d[ii]
        #     koef += [np.linalg.det(new_matrix) / delta]
        #
        #
        # cntr_koefs = []
        # for cntr in random_cntr_points:
        #     d = [1, cntr[0], cntr[1], cntr[0] * cntr[1], cntr[0] ** 2, cntr[1] ** 2]
        #     cntr_koef = []
        #     for jj in range(matrix.shape[0]):
        #         new_matrix = matrix.copy()
        #         for ii in range(matrix.shape[1]):
        #             new_matrix[ii, jj] = d[ii]
        #         cntr_koef += [np.linalg.det(new_matrix) / delta]
        #     cntr_koefs += [cntr_koef]


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


        cntr_koefs = []
        for cntr in random_cntr_points:
            alfa = x2 * y3 + x3 * cntr[1] + cntr[0] * y2 - \
                   (x2 * cntr[1] + x3 * y2 + cntr[0] * y3)
            beta = cntr[0] * y3 + x3 * y1 + x1 * cntr[1] - \
                   (cntr[0] * y1 + x3 * cntr[1] + x1 * y3)
            gama = x2 * cntr[1] + cntr[0] * y1 + x1 * y2 - \
                   (x2 * y1 + cntr[0] * y2 + x1 * cntr[1])

            alfa /= delta
            beta /= delta
            gama /= delta

            cntr_koefs += [(alfa, beta, gama)]


        new_value1 = runge_kutty(points[-1][triags[j][0]], i * h, h)
        new_value2 = runge_kutty(points[-1][triags[j][1]], i * h, h)
        new_value3 = runge_kutty(points[-1][triags[j][2]], i * h, h)

        # new_mid1 = runge_kutty(mid1, i * h, h)
        # new_mid2 = runge_kutty(mid2, i * h, h)
        # new_mid3 = runge_kutty(mid3, i * h, h)

        new_control_value = runge_kutty((x, y), i * h, h)

        new_cntr_values = []
        for cntr in random_cntr_points:
            new_cntr_values += [runge_kutty(cntr, i * h, h)]


        # interpolation_value = koef[0] * new_value1[0] + koef[1] * new_value2[0] + koef[2] * new_value3[0] + \
        #                       koef[3] * new_mid1[0] + koef[4] * new_mid2[0] + koef[5] * new_mid3[0], \
        #                       koef[0] * new_value1[1] + koef[1] * new_value2[1] + koef[2] * new_value3[1] + \
        #                       koef[3] * new_mid1[1] + koef[4] * new_mid2[1] + koef[5] * new_mid3[1]

        cntr_interpolation_value = []
        for cntr_ind in cntr_koefs:
            cntr_interpolation_value += [cntr_ind[0] * new_value1[0] + cntr_ind[1] * new_value2[0] + cntr_ind[2] * new_value3[0]]
            # cntr_interpolation_value += [cntr_ind[0] * new_value1[0] + cntr_ind[1] * new_value2[0] + cntr_ind[2] * new_value3[0] + \
            #                              cntr_ind[3] * new_mid1[0] + cntr_ind[4] * new_mid2[0] + cntr_ind[5] * new_mid3[0]]

        flag_interpolation = True
        for ind_inter in range(len(cntr_interpolation_value)):
            flag_interpolation = flag_interpolation and abs(cntr_interpolation_value[ind_inter] - new_cntr_values[ind_inter][0]) < EPS

        interpolation_value = alfa * new_value1[0] + beta * new_value2[0] + gama * new_value3[0], \
                              alfa * new_value1[1] + beta * new_value2[1] + gama * new_value3[1]

        if abs(interpolation_value[0] - new_control_value[0]) < EPS and flag_interpolation:
            j += 1
        else:
            triag = triags[j]

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

            triag_grinding_now[triag] = [triags[-1], triags[-2], \
                                         triags[-3], triags[-4]]

    j = 0

    while j < len(triags):
        triag = triags[j]
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
            triag_grinding_now[triag] = [triags[-1], triags[-2]]

    triags_list += [triags]
    triag_grinding += [triag_grinding_now]

    prev_points = points[-1][:]
    now_points = []
    for num_ind in range(200):
        for j in range(len(prev_points)):
            h_new = h / 200
            now_points += [runge_kutty(prev_points[j], i * h + h_new * num_ind, h_new)]
        prev_points = now_points[:]
        now_points = []
    points += [prev_points]


end_time = time.time()

print(f"Время выполнения: {end_time - start_time:.40f} секунд")

with open('points_ad_0001_42.json', 'w') as f:
    json.dump(points, f)
with open("triags_list_ad_0001_42.json", "w") as f:
    json.dump(triags_list, f)
triag_grinding_new = []
for i in range(len(triag_grinding)):
    triag_grinding_new_now = {}
    for elem in triag_grinding[i].keys():
        triag_grinding_new_now[' '.join(map(str, elem))] = triag_grinding[i][elem]
    triag_grinding_new += [triag_grinding_new_now]
with open("triag_grinding_ad_0001_42.json", "w") as f:
    json.dump(triag_grinding_new, f)


with open('points_ad.json', 'w') as f:
    json.dump(points[0], f)
with open("triags_list_ad.json", "w") as f:
    json.dump(triags_list[1], f)

time_moment = int((3 - t0) / h)

point_to_build = points[time_moment]
triags = triags_list[time_moment]

edges_build = []
for i in range(len(triags)):
    edge1 = triags[i][0], triags[i][1]
    edge2 = triags[i][0], triags[i][2]
    edge3 = triags[i][1], triags[i][2]
    if edge1 not in edges_build:
        edges_build += [edge1]
    if edge2 not in edges_build:
        edges_build += [edge2]
    if edge3 not in edges_build:
        edges_build += [edge3]

fig, ax = plt.subplots()

for i in range(len(edges_build)):
    x_coords = [point_to_build[edges_build[i][0]][0], point_to_build[edges_build[i][1]][0]]
    y_coords = [point_to_build[edges_build[i][0]][1], point_to_build[edges_build[i][1]][1]]

    ax.plot(x_coords, y_coords, linewidth=1, color='black')

for i in range(len(point_to_build)):
    ax.plot(point_to_build[i][0], point_to_build[i][1], 'ro', markersize=8, color='black')

plt.xlabel('x')
plt.ylabel('y')
ax.grid(True)

plt.show()
