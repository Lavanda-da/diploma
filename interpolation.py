import time
import json


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


random_points = None
with open('random_points.json', 'r') as f:
    random_points = json.load(f)
for i in range(len(random_points)):
    random_points[i] = tuple(random_points[i])


alfa, beta, gama = None, None, None
num_of_triag = None

nums_of_triag = []
bar_koords = []
for point in random_points:
    x, y = point
    i = 0
    while True:
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

            bar_koords += [(alfa, beta, gama)]
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

print(f"Время выполнения: {end_time - start_time:.40f} секунд")


with open('nums_of_triag_100.json', 'w') as f:
    json.dump(nums_of_triag, f)
with open('bar_koords_100.json', 'w') as f:
    json.dump(bar_koords, f)
