import math
import matplotlib.pyplot as plt
import json
import time
import numpy as np
import random


# def runge_kutty(x_pred, y_pred, i, h):
#     # k1_y = y_pred
#     # k2_y = y_pred + h / 2 * k1_y
#     # k3_y = y_pred + h / 2 * k2_y
#     # k4_y = y_pred + h * k3_y
#     # new_value_y = y_pred + h / 6 * (k1_y + 2 * k2_y + 2 * k3_y + k4_y)
#     #
#     # k1_x = x_pred - 0.25 * y_pred - x_pred ** 3 + 0.3 * math.cos(i * h)
#     # k2_x = x_pred + h / 2 * k1_x - 0.25 * (y_pred + h / 2 * k1_y) - (x_pred + h / 2 * k1_x) ** 3 + 0.3 * math.cos(i * h + h / 2)
#     # k3_x = x_pred + h / 2 * k2_x - 0.25 * (y_pred + h / 2 * k2_y) - (x_pred + h / 2 * k2_x) ** 3 + 0.3 * math.cos(i * h + h / 2)
#     # k4_x = x_pred + h * k3_x - 0.25 * (y_pred + h * k3_y) - (x_pred + h * k3_x) ** 3 + 0.3 * math.cos(i * h + h)
#     # new_value_x = x_pred + h / 6 * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)
#
#     new_value_x = y_pred
#     new_value_y = (0.3 * h ** 2 * math.cos(i * h) + (2 + 0.25 * h + h ** 2) * y_pred - y_pred ** 3 * h ** 2 - x_pred) / (1 + 0.25 * h)
#
#     return new_value_x, new_value_y



def det(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    n = len(matrix)
    res = 0
    for i in range(n):
        res_now = (-1) ** i * matrix[0][i]
        new_matrix = []
        for ii in range(1, n):
            string = []
            for jj in range(i):
                string += [matrix[ii][jj]]
            for jj in range(i + 1, n):
                string += [matrix[ii][jj]]
            new_matrix += [string]
        res_now *= det(new_matrix)
        res += res_now
    return res


t0 = 0
t1 = 3
h = 0.1
n = int((t1 - t0) / h)
r = 1
# EPS = 0.00000007
EPS = 0.0001

# points = [[(2.0, 0.0), (1.9375, 0.4960783708246107), (1.75390625, 0.9611518434726833), (1.460693359375, 1.366153325903713), (1.0761871337890625, 1.685770225465761), (0.6244192123413084, 1.9000264859361988), (0.13362509012222248, 1.995531091035624), (-0.36552060022950233, 1.9663150029453227), (-0.8418212530668833, 1.8142042271709387), (-1.265508077587584, 1.5487056871983707), (-1.6101006472590604, 1.1864130417759047), (-1.8540619264768459, 0.7499695812424444), (-1.982144335289828, 0.26665302188133133), (-1.986342723147196, -0.2333293513473649), (-1.866394690807864, -0.7187286401168509), (-1.6297969902930405, -1.1592073888790335), (-1.2913369778849024, -1.527235675836276), (-0.8721684043589575, -1.799811733053752), (-0.39848930556057766, -1.959899556955368), (0.10009537483533833, -1.9974936585472738), (0.5924240943040456, -1.9102444064799748), (1.04772630787875, -1.7036048790076772), (1.4375456272110325, -1.3904900465973997), (1.7375183448426255, -0.9904695862747847), (1.9288961659215542, -0.5285447768099955), (1.9997179766303856, -0.03358591879458159), (1.4726716291753892, 0.18553918541230535), (0.9488233470199834, 1.1414555500987995), (-0.08673166696333853, 1.4817773566387489), (-1.0755117170008563, 1.0229667948156613), (-1.4842611559898158, 0.01246344740961529), (-1.0925386971317286, -1.0047615199495161), (-0.111602863770714, -1.4801119273554053), (0.929521135134614, -1.1572281434702563), (1.1629696694104137, -0.41966452671343685), (0.7722709255976863, 0.4232094068873816), (0.2749410369429952, 0.8366098318847246), (-0.3706663787153766, 0.7988210189344706), (-0.8163709548761247, 0.33022272580202733), (-0.8218012538588062, -0.3164668762407379), (-0.3840286793614819, -0.7924837903890227), (0.2608531121059386, -0.8411089337928371), (-1.02, 0.9915)]]
# edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 20), (20, 21), (21, 22), (22, 23), (23, 24), (24, 25), (25, 0), (0, 26), (26, 1), (1, 26), (26, 2), (2, 26), (26, 3), (3, 27), (27, 4), (4, 27), (27, 5), (5, 27), (27, 6), (6, 28), (28, 7), (7, 28), (28, 8), (8, 28), (28, 9), (9, 29), (29, 10), (10, 29), (29, 11), (11, 29), (29, 12), (12, 30), (30, 13), (13, 30), (30, 14), (14, 30), (30, 15), (15, 31), (31, 16), (16, 31), (31, 17), (17, 31), (31, 18), (18, 32), (32, 19), (19, 32), (32, 20), (20, 32), (32, 21), (21, 33), (33, 22), (22, 33), (33, 23), (23, 33), (33, 24), (24, 26), (26, 25), (25, 26), (26, 0), (26, 27), (27, 3), (27, 28), (28, 6), (28, 29), (29, 9), (29, 30), (30, 12), (30, 31), (31, 15), (31, 32), (32, 18), (32, 33), (33, 21), (33, 34), (34, 24), (24, 34), (34, 26), (26, 35), (35, 27), (27, 36), (36, 28), (28, 37), (37, 29), (29, 38), (38, 30), (30, 39), (39, 31), (31, 40), (40, 32), (32, 41), (41, 33), (33, 41), (41, 34), (34, 35), (35, 26), (35, 36), (36, 27), (36, 37), (37, 28), (37, 38), (38, 29), (38, 39), (39, 30), (39, 40), (40, 31), (40, 41), (41, 32), (41, 35), (35, 34), (35, 41), (41, 36), (36, 41), (41, 37), (37, 41), (41, 38), (38, 41), (41, 39), (39, 41), (41, 40)]
# triags = [(0, 26, 1), (1, 26, 2), (2, 26, 3), (3, 27, 4), (4, 27, 5), (5, 27, 6), (6, 28, 7), (7, 28, 8), (8, 28, 9), (9, 29, 10), (10, 29, 11), (11, 29, 12), (12, 30, 13), (13, 30, 14), (14, 30, 15), (15, 31, 16), (16, 31, 17), (17, 31, 18), (18, 32, 19), (19, 32, 20), (20, 32, 21), (21, 33, 22), (22, 33, 23), (23, 33, 24), (24, 26, 25), (25, 26, 0), (26, 27, 3), (27, 28, 6), (28, 29, 9), (29, 30, 12), (30, 31, 15), (31, 32, 18), (32, 33, 21), (33, 34, 24), (24, 34, 26), (26, 35, 27), (27, 36, 28), (28, 37, 29), (29, 38, 30), (30, 39, 31), (31, 40, 32), (32, 41, 33), (33, 41, 34), (34, 35, 26), (35, 36, 27), (36, 37, 28), (37, 38, 29), (38, 39, 30), (39, 40, 31), (40, 41, 32), (41, 35, 34), (35, 41, 36), (36, 41, 37), (37, 41, 38), (38, 41, 39), (39, 41, 40)]

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

# now_points = []
# for i in range(len(points[-1])):
#     now_points += [(points[-1][i][0], points[-1][i][1] * h + points[-1][i][0])]
# points += [now_points]
# triags_list += [triags[:]]
# triag_grinding = [{}, {}]


for i in range(n):
    print(i, n)
    # print("start", len(points[i]), len(triags_list[i]), len(triag_grinding[i]))
    j = 0
    triags = triags_list[-1][:]
    triag_grinding_now = {}
    while j < len(triags):
        print(i, j, len(triags), len(points[-1]))
        # print(j)
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

        # mid_center1 = (points[-1][triags[j][0]][0] + x) / 2, (points[-1][triags[j][0]][1] + y) / 2
        # mid_center2 = (points[-1][triags[j][1]][0] + x) / 2, (points[-1][triags[j][1]][1] + y) / 2
        # mid_center3 = (points[-1][triags[j][2]][0] + x) / 2, (points[-1][triags[j][2]][1] + y) / 2

        # control11 = (mid1[0] + points[-1][triags[j][0]][0]) / 2, (mid1[1] + points[-1][triags[j][0]][1]) / 2
        # control12 = (mid1[0] + points[-1][triags[j][1]][0]) / 2, (mid1[1] + points[-1][triags[j][1]][1]) / 2
        # control21 = (mid2[0] + points[-1][triags[j][0]][0]) / 2, (mid2[1] + points[-1][triags[j][0]][1]) / 2
        # control22 = (mid2[0] + points[-1][triags[j][2]][0]) / 2, (mid2[1] + points[-1][triags[j][2]][1]) / 2
        # control31 = (mid3[0] + points[-1][triags[j][1]][0]) / 2, (mid3[1] + points[-1][triags[j][1]][1]) / 2
        # control32 = (mid3[0] + points[-1][triags[j][2]][0]) / 2, (mid3[1] + points[-1][triags[j][2]][1]) / 2
        #
        # controls = [control11, control12, control21, control22, control31, control32]


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

        # d = [1, mid_center1[0], mid_center1[1], mid_center1[0] * mid_center1[1], mid_center1[0] ** 2, mid_center1[1] ** 2]
        # koef_mid_center_1 = []
        # for jj in range(len(matrix)):
        #     new_matrix = []
        #     for ii in range(len(matrix)):
        #         new_string = matrix[ii][:]
        #         new_string[jj] = d[ii]
        #         new_matrix += [new_string]
        #     koef_mid_center_1 += [det(new_matrix) / delta]
        #
        # d = [1, mid_center2[0], mid_center2[1], mid_center2[0] * mid_center2[1], mid_center2[0] ** 2,
        #      mid_center2[1] ** 2]
        # koef_mid_center_2 = []
        # for jj in range(len(matrix)):
        #     new_matrix = []
        #     for ii in range(len(matrix)):
        #         new_string = matrix[ii][:]
        #         new_string[jj] = d[ii]
        #         new_matrix += [new_string]
        #     koef_mid_center_2 += [det(new_matrix) / delta]
        #
        # d = [1, mid_center3[0], mid_center3[1], mid_center3[0] * mid_center3[1], mid_center3[0] ** 2,
        #      mid_center3[1] ** 2]
        # koef_mid_center_3 = []
        # for jj in range(len(matrix)):
        #     new_matrix = []
        #     for ii in range(len(matrix)):
        #         new_string = matrix[ii][:]
        #         new_string[jj] = d[ii]
        #         new_matrix += [new_string]
        #     koef_mid_center_3 += [det(new_matrix) / delta]

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



        # alfa1 = x2 * y3 + x3 * mid1[1] + mid1[0] * y2 - \
        #        (x2 * mid1[1] + x3 * y2 + mid1[0] * y3)
        # beta1 = mid1[0] * y3 + x3 * y1 + x1 * mid1[1] - \
        #        (mid1[0] * y1 + x3 * mid1[1] + x1 * y3)
        # gama1 = x2 * mid1[1] + mid1[0] * y1 + x1 * y2 - \
        #        (x2 * y1 + mid1[0] * y2 + x1 * mid1[1])
        #
        # alfa1 /= delta
        # beta1 /= delta
        # gama1 /= delta
        #
        # alfa2 = x2 * y3 + x3 * mid2[1] + mid2[0] * y2 - \
        #         (x2 * mid2[1] + x3 * y2 + mid2[0] * y3)
        # beta2 = mid2[0] * y3 + x3 * y1 + x1 * mid2[1] - \
        #         (mid2[0] * y1 + x3 * mid2[1] + x1 * y3)
        # gama2 = x2 * mid2[1] + mid2[0] * y1 + x1 * y2 - \
        #         (x2 * y1 + mid2[0] * y2 + x1 * mid2[1])
        #
        # alfa2 /= delta
        # beta2 /= delta
        # gama2 /= delta
        #
        # alfa3 = x2 * y3 + x3 * mid3[1] + mid3[0] * y2 - \
        #         (x2 * mid3[1] + x3 * y2 + mid3[0] * y3)
        # beta3 = mid3[0] * y3 + x3 * y1 + x1 * mid3[1] - \
        #         (mid3[0] * y1 + x3 * mid3[1] + x1 * y3)
        # gama3 = x2 * mid3[1] + mid3[0] * y1 + x1 * y2 - \
        #         (x2 * y1 + mid3[0] * y2 + x1 * mid3[1])
        #
        # alfa3 /= delta
        # beta3 /= delta
        # gama3 /= delta

        point = points[-1][triags[j][0]]

        k1_x, k1_y = point[1], point[0] - 0.25 * point[1] - point[0] ** 3 + 0.3 * math.cos(i * h)
        k2_x, k2_y = point[1] + h / 2 * k1_y, point[0] + h / 2 * k1_x - 0.25 * (point[1] + h / 2 * k1_y) - (point[0] + h / 2 * k1_x) ** 3 + 0.3 * math.cos(i * h + h / 2)
        k3_x, k3_y = point[1] + h / 2 * k2_y, point[0] + h / 2 * k2_x - 0.25 * (point[1] + h / 2 * k2_y) - (point[0] + h / 2 * k2_x) ** 3 + 0.3 * math.cos(i * h + h / 2)
        k4_x, k4_y = point[1] + h * k3_y, point[0] + h * k3_x - 0.25 * (point[1] + h * k3_y) - (point[0] + h * k3_x) ** 3 + 0.3 * math.cos(i * h + h)

        new_value_x = point[0] + h / 6 * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)
        new_value_y = point[1] + h / 6 * (k1_y + 2 * k2_y + 2 * k3_y + k4_y)

        new_value1 = new_value_x, new_value_y

        point = points[-1][triags[j][1]]

        k1_x, k1_y = point[1], point[0] - 0.25 * point[1] - point[0] ** 3 + 0.3 * math.cos(i * h)
        k2_x, k2_y = point[1] + h / 2 * k1_y, point[0] + h / 2 * k1_x - 0.25 * (point[1] + h / 2 * k1_y) - (
                    point[0] + h / 2 * k1_x) ** 3 + 0.3 * math.cos(i * h + h / 2)
        k3_x, k3_y = point[1] + h / 2 * k2_y, point[0] + h / 2 * k2_x - 0.25 * (point[1] + h / 2 * k2_y) - (
                    point[0] + h / 2 * k2_x) ** 3 + 0.3 * math.cos(i * h + h / 2)
        k4_x, k4_y = point[1] + h * k3_y, point[0] + h * k3_x - 0.25 * (point[1] + h * k3_y) - (
                    point[0] + h * k3_x) ** 3 + 0.3 * math.cos(i * h + h)

        new_value_x = point[0] + h / 6 * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)
        new_value_y = point[1] + h / 6 * (k1_y + 2 * k2_y + 2 * k3_x + k4_y)

        new_value2 = new_value_x, new_value_y

        point = points[-1][triags[j][2]]

        k1_x, k1_y = point[1], point[0] - 0.25 * point[1] - point[0] ** 3 + 0.3 * math.cos(i * h)
        k2_x, k2_y = point[1] + h / 2 * k1_y, point[0] + h / 2 * k1_x - 0.25 * (point[1] + h / 2 * k1_y) - (
                    point[0] + h / 2 * k1_x) ** 3 + 0.3 * math.cos(i * h + h / 2)
        k3_x, k3_y = point[1] + h / 2 * k2_y, point[0] + h / 2 * k2_x - 0.25 * (point[1] + h / 2 * k2_y) - (
                    point[0] + h / 2 * k2_x) ** 3 + 0.3 * math.cos(i * h + h / 2)
        k4_x, k4_y = point[1] + h * k3_y, point[0] + h * k3_x - 0.25 * (point[1] + h * k3_y) - (
                    point[0] + h * k3_x) ** 3 + 0.3 * math.cos(i * h + h)

        new_value_x = point[0] + h / 6 * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)
        new_value_y = point[1] + h / 6 * (k1_y + 2 * k2_y + 2 * k3_y + k4_y)

        new_value3 = new_value_x, new_value_y

        point = mid1

        k1_x, k1_y = point[1], point[0] - 0.25 * point[1] - point[0] ** 3 + 0.3 * math.cos(i * h)
        k2_x, k2_y = point[1] + h / 2 * k1_y, point[0] + h / 2 * k1_x - 0.25 * (point[1] + h / 2 * k1_y) - (
                    point[0] + h / 2 * k1_x) ** 3 + 0.3 * math.cos(i * h + h / 2)
        k3_x, k3_y = point[1] + h / 2 * k2_y, point[0] + h / 2 * k2_x - 0.25 * (point[1] + h / 2 * k2_y) - (
                    point[0] + h / 2 * k2_x) ** 3 + 0.3 * math.cos(i * h + h / 2)
        k4_x, k4_y = point[1] + h * k3_y, point[0] + h * k3_x - 0.25 * (point[1] + h * k3_y) - (
                    point[0] + h * k3_x) ** 3 + 0.3 * math.cos(i * h + h)

        new_value_x = point[0] + h / 6 * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)
        new_value_y = point[1] + h / 6 * (k1_y + 2 * k2_y + 2 * k3_y + k4_y)

        new_mid1 = new_value_x, new_value_y

        point = mid2

        k1_x, k1_y = point[1], point[0] - 0.25 * point[1] - point[0] ** 3 + 0.3 * math.cos(i * h)
        k2_x, k2_y = point[1] + h / 2 * k1_y, point[0] + h / 2 * k1_x - 0.25 * (point[1] + h / 2 * k1_y) - (
                    point[0] + h / 2 * k1_x) ** 3 + 0.3 * math.cos(i * h + h / 2)
        k3_x, k3_y = point[1] + h / 2 * k2_y, point[0] + h / 2 * k2_x - 0.25 * (point[1] + h / 2 * k2_y) - (
                    point[0] + h / 2 * k2_x) ** 3 + 0.3 * math.cos(i * h + h / 2)
        k4_x, k4_y = point[1] + h * k3_y, point[0] + h * k3_x - 0.25 * (point[1] + h * k3_y) - (
                    point[0] + h * k3_x) ** 3 + 0.3 * math.cos(i * h + h)

        new_value_x = point[0] + h / 6 * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)
        new_value_y = point[1] + h / 6 * (k1_y + 2 * k2_y + 2 * k3_y + k4_y)

        new_mid2 = new_value_x, new_value_y

        point = mid3

        k1_x, k1_y = point[1], point[0] - 0.25 * point[1] - point[0] ** 3 + 0.3 * math.cos(i * h)
        k2_x, k2_y = point[1] + h / 2 * k1_y, point[0] + h / 2 * k1_x - 0.25 * (point[1] + h / 2 * k1_y) - (
                    point[0] + h / 2 * k1_x) ** 3 + 0.3 * math.cos(i * h + h / 2)
        k3_x, k3_y = point[1] + h / 2 * k2_y, point[0] + h / 2 * k2_x - 0.25 * (point[1] + h / 2 * k2_y) - (
                    point[0] + h / 2 * k2_x) ** 3 + 0.3 * math.cos(i * h + h / 2)
        k4_x, k4_y = point[1] + h * k3_y, point[0] + h * k3_x - 0.25 * (point[1] + h * k3_y) - (
                    point[0] + h * k3_x) ** 3 + 0.3 * math.cos(i * h + h)

        new_value_x = point[0] + h / 6 * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)
        new_value_y = point[1] + h / 6 * (k1_y + 2 * k2_y + 2 * k3_y + k4_y)

        new_mid3 = new_value_x, new_value_y

        point = x, y

        k1_x, k1_y = point[1], point[0] - 0.25 * point[1] - point[0] ** 3 + 0.3 * math.cos(i * h)
        k2_x, k2_y = point[1] + h / 2 * k1_y, point[0] + h / 2 * k1_x - 0.25 * (point[1] + h / 2 * k1_y) - (
                    point[0] + h / 2 * k1_x) ** 3 + 0.3 * math.cos(i * h + h / 2)
        k3_x, k3_y = point[1] + h / 2 * k2_y, point[0] + h / 2 * k2_x - 0.25 * (point[1] + h / 2 * k2_y) - (
                    point[0] + h / 2 * k2_x) ** 3 + 0.3 * math.cos(i * h + h / 2)
        k4_x, k4_y = point[1] + h * k3_y, point[0] + h * k3_x - 0.25 * (point[1] + h * k3_y) - (
                    point[0] + h * k3_x) ** 3 + 0.3 * math.cos(i * h + h)

        new_value_x = point[0] + h / 6 * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)
        new_value_y = point[1] + h / 6 * (k1_y + 2 * k2_y + 2 * k3_y + k4_y)

        new_control_value = new_value_x, new_value_y

        new_cntr_values = []
        for cntr in random_cntr_points:
            point = cntr

            k1_x, k1_y = point[1], point[0] - 0.25 * point[1] - point[0] ** 3 + 0.3 * math.cos(i * h)
            k2_x, k2_y = point[1] + h / 2 * k1_y, point[0] + h / 2 * k1_x - 0.25 * (point[1] + h / 2 * k1_y) - (
                    point[0] + h / 2 * k1_x) ** 3 + 0.3 * math.cos(i * h + h / 2)
            k3_x, k3_y = point[1] + h / 2 * k2_y, point[0] + h / 2 * k2_x - 0.25 * (point[1] + h / 2 * k2_y) - (
                    point[0] + h / 2 * k2_x) ** 3 + 0.3 * math.cos(i * h + h / 2)
            k4_x, k4_y = point[1] + h * k3_y, point[0] + h * k3_x - 0.25 * (point[1] + h * k3_y) - (
                    point[0] + h * k3_x) ** 3 + 0.3 * math.cos(i * h + h)

            new_value_x = point[0] + h / 6 * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)
            new_value_y = point[1] + h / 6 * (k1_y + 2 * k2_y + 2 * k3_y + k4_y)

            new_cntr_values += [(new_value_x, new_value_y)]

        # point = mid_center1
        #
        # k1_y = point[1]
        # k2_y = point[1] + h / 2 * k1_y
        # k3_y = point[1] + h / 2 * k2_y
        # k4_y = point[1] + h * k3_y
        # new_value_y = point[1] + h / 6 * (k1_y + 2 * k2_y + 2 * k3_y + k4_y)
        #
        # k1_x = point[0] - 0.25 * point[1] - point[0] ** 3 + 0.3 * math.cos(i * h)
        # k2_x = point[0] + h / 2 * k1_x - 0.25 * (point[1] + h / 2 * k1_y) - (
        #         point[0] + h / 2 * k1_x) ** 3 + 0.3 * math.cos(i * h + h / 2)
        # k3_x = point[0] + h / 2 * k2_x - 0.25 * (point[1] + h / 2 * k2_y) - (
        #         point[0] + h / 2 * k2_x) ** 3 + 0.3 * math.cos(i * h + h / 2)
        # k4_x = point[0] + h * k3_x - 0.25 * (point[1] + h * k3_y) - (
        #         point[0] + h * k3_x) ** 3 + 0.3 * math.cos(i * h + h)
        # new_value_x = point[0] + h / 6 * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)
        #
        # new_mid_center1 = new_value_x, new_value_y
        #
        # point = mid_center2
        #
        # k1_y = point[1]
        # k2_y = point[1] + h / 2 * k1_y
        # k3_y = point[1] + h / 2 * k2_y
        # k4_y = point[1] + h * k3_y
        # new_value_y = point[1] + h / 6 * (k1_y + 2 * k2_y + 2 * k3_y + k4_y)
        #
        # k1_x = point[0] - 0.25 * point[1] - point[0] ** 3 + 0.3 * math.cos(i * h)
        # k2_x = point[0] + h / 2 * k1_x - 0.25 * (point[1] + h / 2 * k1_y) - (
        #         point[0] + h / 2 * k1_x) ** 3 + 0.3 * math.cos(i * h + h / 2)
        # k3_x = point[0] + h / 2 * k2_x - 0.25 * (point[1] + h / 2 * k2_y) - (
        #         point[0] + h / 2 * k2_x) ** 3 + 0.3 * math.cos(i * h + h / 2)
        # k4_x = point[0] + h * k3_x - 0.25 * (point[1] + h * k3_y) - (
        #         point[0] + h * k3_x) ** 3 + 0.3 * math.cos(i * h + h)
        # new_value_x = point[0] + h / 6 * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)
        #
        # new_mid_center2 = new_value_x, new_value_y
        #
        # point = mid_center3
        #
        # k1_y = point[1]
        # k2_y = point[1] + h / 2 * k1_y
        # k3_y = point[1] + h / 2 * k2_y
        # k4_y = point[1] + h * k3_y
        # new_value_y = point[1] + h / 6 * (k1_y + 2 * k2_y + 2 * k3_y + k4_y)
        #
        # k1_x = point[0] - 0.25 * point[1] - point[0] ** 3 + 0.3 * math.cos(i * h)
        # k2_x = point[0] + h / 2 * k1_x - 0.25 * (point[1] + h / 2 * k1_y) - (
        #         point[0] + h / 2 * k1_x) ** 3 + 0.3 * math.cos(i * h + h / 2)
        # k3_x = point[0] + h / 2 * k2_x - 0.25 * (point[1] + h / 2 * k2_y) - (
        #         point[0] + h / 2 * k2_x) ** 3 + 0.3 * math.cos(i * h + h / 2)
        # k4_x = point[0] + h * k3_x - 0.25 * (point[1] + h * k3_y) - (
        #         point[0] + h * k3_x) ** 3 + 0.3 * math.cos(i * h + h)
        # new_value_x = point[0] + h / 6 * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)
        #
        # new_mid_center3 = new_value_x, new_value_y


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
            if flag_interpolation == False and i == 15:
                print(1, flag_interpolation, cntr_interpolation_value[ind_inter], new_cntr_values[ind_inter][0])

        # interpolation_value1 = koef_mid_center_1[0] * new_value1[0] + koef_mid_center_1[1] * new_value2[0] + koef_mid_center_1[2] * new_value3[0] + \
        #                        koef_mid_center_1[3] * new_mid1[0] + koef_mid_center_1[4] * new_mid2[0] + koef_mid_center_1[5] * new_mid3[0]
        #
        # interpolation_value2 = koef_mid_center_2[0] * new_value1[0] + koef_mid_center_2[1] * new_value2[0] + \
        #                        koef_mid_center_2[2] * new_value3[0] + \
        #                        koef_mid_center_2[3] * new_mid1[0] + koef_mid_center_2[4] * new_mid2[0] + \
        #                        koef_mid_center_2[5] * new_mid3[0]
        #
        # interpolation_value3 = koef_mid_center_3[0] * new_value1[0] + koef_mid_center_3[1] * new_value2[0] + \
        #                        koef_mid_center_3[2] * new_value3[0] + \
        #                        koef_mid_center_3[3] * new_mid1[0] + koef_mid_center_3[4] * new_mid2[0] + \
        #                        koef_mid_center_3[5] * new_mid3[0]

        # interpolation_value = koef[0] * new_value1[0] + koef[1] * new_value2[0] + koef[2] * new_value3[0] + \
        #                       koef[3] * new_mid1[0] + koef[4] * new_mid2[0] + koef[5] * new_mid3[0], \
        #                       koef[0] * new_value1[1] + koef[1] * new_value2[1] + koef[2] * new_value3[1] + \
        #                       koef[3] * new_mid1[1] + koef[4] * new_mid2[1] + koef[5] * new_mid3[1],

        interpolation_value = alfa * new_value1[0] + beta * new_value2[0] + gama * new_value3[0], \
                              alfa * new_value1[1] + beta * new_value2[1] + gama * new_value3[1]


        # interpolation_value1 = alfa1 * new_value1[0] + beta1 * new_value2[0] + gama1 * new_value3[0]
        # interpolation_value2 = alfa2 * new_value1[0] + beta2 * new_value2[0] + gama2 * new_value3[0]
        # interpolation_value3 = alfa3 * new_value1[0] + beta3 * new_value2[0] + gama3 * new_value3[0]

        # interpolation_mid1 = 0.5 * new_value1[0] + 0.5 * new_value2[0]
        # interpolation_mid2 = 0.5 * new_value2[0] + 0.5 * new_value3[0]
        # interpolation_mid3 = 0.5 * new_value1[0] + 0.5 * new_value3[0]

        # print(interpolation_value1 - new_mid_center1[0])

        # print(i, interpolation_value - new_control_value, j, len(triags))

        # if abs(cntr_interpolation_value[0]) > 10:
        #     print(triags[j], ":", points[-1][triags[j][0]], points[-1][triags[j][1]], points[-1][triags[j][2]])

        # print(1, flag_interpolation, cntr_interpolation_value[0], new_cntr_values[0][0])
        # print(2, abs(interpolation_value[0] - new_control_value[0]) < EPS, interpolation_value, new_control_value[0], interpolation_value - new_control_value[0])

        if abs(interpolation_value[0] - new_control_value[0]) < EPS and flag_interpolation:
        # if flag_interpolation:
           # abs(interpolation_value1 - new_mid1[0]) < EPS and \
           # abs(interpolation_value2 - new_mid2[0]) < EPS and \
           # abs(interpolation_value3 - new_mid3[0]) < EPS:
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


            point = prev_points[j]

            k1_x, k1_y = point[1], point[0] - 0.25 * point[1] - point[0] ** 3 + 0.3 * math.cos(i * h + h_new * num_ind)
            k2_x, k2_y = point[1] + h_new / 2 * k1_y, point[0] + h_new / 2 * k1_x - 0.25 * (point[1] + h_new / 2 * k1_y) - (
                        point[0] + h_new / 2 * k1_x) ** 3 + 0.3 * math.cos(i * h + h_new * num_ind + h_new / 2)
            k3_x, k3_y = point[1] + h_new / 2 * k2_y, point[0] + h_new / 2 * k2_x - 0.25 * (point[1] + h_new / 2 * k2_y) - (
                        point[0] + h_new / 2 * k2_x) ** 3 + 0.3 * math.cos(i * h + h_new * num_ind + h_new / 2)
            k4_x, k4_y = point[1] + h_new * k3_y, point[0] + h_new * k3_x - 0.25 * (point[1] + h_new * k3_y) - (
                        point[0] + h_new * k3_x) ** 3 + 0.3 * math.cos(i * h + h_new * num_ind + h_new)

            new_value_x = point[0] + h_new / 6 * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)
            new_value_y = point[1] + h_new / 6 * (k1_y + 2 * k2_y + 2 * k3_y + k4_y)

            new_value = new_value_x, new_value_y

            now_points += [new_value]
        prev_points = now_points[:]
        now_points = []
    points += [prev_points]

    # print("start", len(points[i]), len(triags_list[i]), len(triag_grinding[i]))
    # if i >= 14:
    #     break

end_time = time.time()
print(end_time - start_time, "секунд")

# print(points)
# print(triags_list)
# print(triag_grinding)
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

print(len(triags_list[1]), len(points[0]))

with open('points_ad.json', 'w') as f:
    json.dump(points[0], f)
with open("triags_list_ad.json", "w") as f:
    json.dump(triags_list[1], f)

time_moment = int((3 - t0) / h)

# for time_it in range(10, -1, -1):
#
time_moment = -1

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

# for i in range(len(point_to_build)):
#     ax.plot(point_to_build[i][0], point_to_build[i][1], 'ro', markersize=8, color='black')

# plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
ax.grid(True)

# plt.show()

for i in range(len(points)):
    print(i, len(points[i]))
print(len(points[0]))
print(len(points[-1]))
print(len(triag_grinding), len(triags_list))
