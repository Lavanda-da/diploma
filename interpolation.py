import time
import json


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


points = None
with open('start_points_100.json', 'r') as f:
    points = json.load(f)
for i in range(len(points[-1])):
    points[-1][i] = tuple(points[-1][i])

edges = None
with open('start_edges_100.json', 'r') as f:
    edges = json.load(f)
for i in range(len(edges)):
    edges[i] = tuple(edges[i])

triags = None
with open('start_triags_100.json', 'r') as f:
    triags = json.load(f)
for i in range(len(triags)):
    triags[i] = tuple(triags[i])


start_time = time.time()

for i in range(len(edges)):
    edges[i] = tuple(sorted(list(edges[i])))

for i in range(len(triags)):
    triags[i] = tuple(sorted(list(triags[i])))

random_point = (-0.453, -0.058)
# random_point = (-1.02, 0.9915)

triags_with_edge = []  # (edge_1, edge_2, edge_3)

for i in range(len(triags)):
    triag = []
    point1, point2 = triags[i][0], triags[i][1]
    if point1 > point2:
        point1, point2 = point2, point1
    if (point1, point2) in edges:
        triag += [edges.index((point1, point2))]
    else:
        triag += [edges.index((point2, point1))]
    point1, point2 = triags[i][0], triags[i][2]
    if point1 > point2:
        point1, point2 = point2, point1
    if (point1, point2) in edges:
        triag += [edges.index((point1, point2))]
    else:
        triag += [edges.index((point2, point1))]
    point1, point2 = triags[i][1], triags[i][2]
    if point1 > point2:
        point1, point2 = point2, point1
    if (point1, point2) in edges:
        triag += [edges.index((point1, point2))]
    else:
        triag += [edges.index((point2, point1))]
    triags_with_edge += [triag]


triags_on_edges = [[] for i in range(len(edges))]

for i in range(len(triags_with_edge)):
    triags_on_edges[triags_with_edge[i][0]] += [i]
    triags_on_edges[triags_with_edge[i][1]] += [i]
    triags_on_edges[triags_with_edge[i][2]] += [i]
# print(triags_on_edges)


# x, y = map(int, input().split())
# x, y = random_point


random_points = None
with open('random_points.json', 'r') as f:
    random_points = json.load(f)
for i in range(len(random_points)):
    random_points[i] = tuple(random_points[i])


alfa, beta, gama = None, None, None
num_of_triag = None

nums_of_triag = []
bar_koords = []
ind_point = -1
for point in random_points:
    ind_point += 1
    print(ind_point)
    x, y = point
    i = 0
    while True:
        # print(ind_point, i)
        x1, y1 = points[0][triags[i][0]][0], points[0][triags[i][0]][1]
        x2, y2 = points[0][triags[i][1]][0], points[0][triags[i][1]][1]
        x3, y3 = points[0][triags[i][2]][0], points[0][triags[i][2]][1]
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

        if alfa >= 0 and beta >= 0 and gama >= 0:
            nums_of_triag += [i]

            triag = triags[i]
            mid1 = ((points[0][triag[0]][0] + points[0][triag[1]][0]) / 2,
                    (points[0][triag[0]][1] + points[0][triag[1]][1]) / 2)  # 0, 1 points
            mid2 = ((points[0][triag[1]][0] + points[0][triag[2]][0]) / 2,
                    (points[0][triag[1]][1] + points[0][triag[2]][1]) / 2)  # 0, 2 points
            mid3 = ((points[0][triag[0]][0] + points[0][triag[2]][0]) / 2,
                    (points[0][triag[0]][1] + points[0][triag[2]][1]) / 2)  # 0, 2 points

            matrix = [[1, 1, 1, 1, 1, 1],
                      [x1, x2, x3, mid1[0], mid2[0], mid3[0]],
                      [y1, y2, y3, mid1[1], mid2[1], mid3[1]],
                      [x1 * y1, x2 * y2, x3 * y3, mid1[0] * mid1[1], mid2[0] * mid2[1], mid3[0] * mid3[1]],
                      [x1 ** 2, x2 ** 2, x3 ** 2, mid1[0] ** 2, mid2[0] ** 2, mid3[0] ** 2],
                      [y1 ** 2, y2 ** 2, y3 ** 2, mid1[1] ** 2, mid2[1] ** 2, mid3[1] ** 2]]

            delta = det(matrix)

            d = [1, x, y, x * y, x ** 2, y ** 2]
            koef = []
            for jj in range(len(matrix)):
                new_matrix = []
                for i in range(len(matrix)):
                    new_string = matrix[i][:]
                    new_string[jj] = d[i]
                    new_matrix += [new_string]
                koef += [det(new_matrix) / delta]
            bar_koords += [(tuple(koef), (alfa, beta, gama))]
            break

        point1, point2 = None, None
        if alfa < 0:
            point1, point2 = triags[i][1], triags[i][2]
        elif beta < 0:
            point1, point2 = triags[i][0], triags[i][2]
        elif gama < 0:
            point1, point2 = triags[i][0], triags[i][1]

        ind_edge = None
        if (point1, point2) in edges:
            ind_edge = edges.index((point1, point2))
        else:
            ind_edge = edges.index((point2, point1))

        indexes = triags_on_edges[ind_edge]
        for j in indexes:
            if j != i:
                i = j
                break

end_time = time.time()

print(f"Время выполнения: {end_time - start_time:.20f} секунд")
print(end_time - start_time, "секунд")
# print(len(random_points), random_points)
# print(len(nums_of_triag), nums_of_triag)
# print(len(bar_koords), bar_koords)

with open('nums_of_triag_100.json', 'w') as f:
    json.dump(nums_of_triag, f)
with open('bar_koords_100.json', 'w') as f:
    json.dump(bar_koords, f)


# print(alfa, beta, gama)
