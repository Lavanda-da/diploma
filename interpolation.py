points = [(2, 5), (6, 3), (9, 4.5), (8, 9), (3, 9), (2.8944271909999157, 4.552786404500042), (3.7888543819998315, 4.105572809000084), (4.683281572999748, 3.658359213500126), (6.894427190999916, 3.447213595499958), (7.7888543819998315, 3.8944271909999157), (8.783069542181345, 5.476187060183953), (8.566139084362687, 6.452374120367906), (8.349208626544032, 7.428561180551858), (7.0, 9.0), (6.0, 9.0), (5.0, 9.0), (4.0, 9.0), (2.757464374963667, 8.029857499854668), (2.514928749927334, 7.059714999709336), (2.272393124891001, 6.089572499564005), (3.788854381999831, 5.223606797749979), (5.788854381999832, 4.223606797749979), (7.698417253088064, 5.747350132457273), (7.198417253088064, 7.9973501324572736), (5.5, 8.0), (3.6063390625908323, 7.302250624745668), (6.951259128357985, 5.045741220468715), (5.236067977499789, 5.618033988749895), (6.472230192904112, 6.655419674638616), (4.898911895800069, 6.712795830055065)]
edges = [(0, 5), (5, 6), (6, 7), (7, 1), (1, 8), (8, 9), (9, 2), (2, 10), (10, 11), (11, 12), (12, 3), (3, 13), (13, 14), (14, 15), (15, 16), (16, 4), (4, 17), (17, 18), (18, 19), (19, 0), (0, 19), (19, 5), (5, 20), (20, 6), (6, 20), (20, 7), (7, 21), (21, 1), (1, 21), (21, 8), (8, 21), (21, 9), (9, 10), (10, 2), (10, 22), (22, 11), (11, 22), (22, 12), (12, 23), (23, 3), (3, 23), (23, 13), (13, 23), (23, 14), (14, 24), (24, 15), (15, 24), (24, 16), (16, 17), (17, 4), (17, 25), (25, 18), (18, 25), (25, 19), (19, 20), (20, 5), (20, 21), (21, 7), (21, 26), (26, 9), (9, 22), (22, 10), (22, 23), (23, 12), (23, 24), (24, 14), (24, 25), (25, 16), (16, 25), (25, 17), (25, 20), (20, 19), (20, 27), (27, 21), (21, 27), (27, 26), (26, 22), (22, 9), (22, 28), (28, 23), (23, 28), (28, 24), (24, 29), (29, 25), (25, 27), (27, 20), (27, 28), (28, 26), (26, 28), (28, 22), (28, 29), (29, 24), (29, 27), (27, 25), (27, 29), (29, 28)]
triags = [(0, 19, 5), (5, 20, 6), (6, 20, 7), (7, 21, 1), (1, 21, 8), (8, 21, 9), (9, 10, 2), (10, 22, 11), (11, 22, 12), (12, 23, 3), (3, 23, 13), (13, 23, 14), (14, 24, 15), (15, 24, 16), (16, 17, 4), (17, 25, 18), (18, 25, 19), (19, 20, 5), (20, 21, 7), (21, 26, 9), (9, 22, 10), (22, 23, 12), (23, 24, 14), (24, 25, 16), (16, 25, 17), (25, 20, 19), (20, 27, 21), (21, 27, 26), (26, 22, 9), (22, 28, 23), (23, 28, 24), (24, 29, 25), (25, 27, 20), (27, 28, 26), (26, 28, 22), (28, 29, 24), (29, 27, 25), (27, 29, 28)]

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
print(triags_on_edges)


x, y = map(int, input().split())
alfa, beta, gama = None, None, None
num_of_triag = None

i = 0
while True:
    x1, y1 = points[triags[i][0]][0], points[triags[i][0]][1]
    x2, y2 = points[triags[i][1]][0], points[triags[i][1]][1]
    x3, y3 = points[triags[i][2]][0], points[triags[i][2]][1]
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
        num_of_triag = i
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

print(num_of_triag)
print(alfa, beta, gama)
