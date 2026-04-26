import matplotlib.pyplot as plt


points = [(-2, 2), (-2, -2), (2, -2), (2, 2)]  # # (index_start, index_end)
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]  # (index_start, index_end)
triags_point = []  # (point_1, point_2, point_3)

r = 0.5
EPS = 1e-5

# разбиение отрезков границы на подотрезки длиной приближительно равной r
for i in range(len(edges)):
    a_x, a_y = points[edges[0][0]][0], points[edges[0][0]][1]
    b_x, b_y = points[edges[0][1]][0], points[edges[0][1]][1]
    prev_ind_point = edges[0][0]
    end_ind_point = edges[0][1]
    del edges[0]
    size = ((a_x - b_x) ** 2 + (a_y - b_y) ** 2) ** 0.5
    normal_x = (b_x - a_x) / size
    normal_y = (b_y - a_y) / size
    n_add_edges = int(size / r)
    for j in range(1, n_add_edges):
        points += [(a_x + normal_x * (r * j), a_y + normal_y * (r * j))]
        edges += [(prev_ind_point, len(points) - 1)]
        prev_ind_point = len(points) - 1
    edges += [(prev_ind_point, end_ind_point)]

front_edges = edges[:]

while len(front_edges) > 0:
    cur_edge = front_edges[0]

    a_x, a_y = points[cur_edge[0]][0], points[cur_edge[0]][1]
    b_x, b_y = points[cur_edge[1]][0], points[cur_edge[1]][1]
    m_x, m_y = (a_x + b_x) / 2, (a_y + b_y) / 2
    n_x, n_y = -(b_y - a_y), b_x - a_x
    n_size = (n_x ** 2 + n_y ** 2) ** 0.5
    n_x, n_y = n_x / n_size * r, n_y / n_size * r
    c_x, c_y = m_x + n_x, m_y + n_y

    flag = True
    correct_points = []  # (num_edge: j, distance, num_point)

    for j in range(1, len(front_edges)):
        a1_x, a1_y = points[front_edges[j][0]][0], points[front_edges[j][0]][1]
        b1_x, b1_y = points[front_edges[j][1]][0], points[front_edges[j][1]][1]
        n1_x, n1_y = -(b1_y - a1_y) + c_x, b1_x - a1_x + c_y

        p_x, p_y = None, None

        if abs(a1_x - b1_x) > EPS and abs(c_x - n1_x) > EPS:
            k1, b1 = (a1_y - b1_y) / (a1_x - b1_x), a1_y - (a1_y - b1_y) / (a1_x - b1_x) * a1_x
            k2, b2 = (c_y - n1_y) / (c_x - n1_x), c_y - (c_y - n1_y) / (c_x - n1_x) * c_x
            p_x, p_y = (b2 - b1) / (k1 - k2), k1 * (b2 - b1) / (k1 - k2) + b1
        elif abs(a1_x - b1_x) <= EPS and abs(c_x - n1_x) > EPS:
            k2, b2 = (c_y - n1_y) / (c_x - n1_x), c_y - (c_y - n1_y) / (c_x - n1_x) * c_x
            p_x, p_y = a1_x, k2 * a1_x + b2
        elif abs(c_x - n1_x) <= EPS and abs(a1_x - b1_x) > EPS:
            k1, b1 = (a1_y - b1_y) / (a1_x - b1_x), a1_y - (a1_y - b1_y) / (a1_x - b1_x) * a1_x
            p_x, p_y = c_x, k1 * c_x + b1
        else:
            continue

        if front_edges[j][0] == front_edges[0][0] and front_edges[j][1] == front_edges[0][1]:
            continue
        if front_edges[j][1] == front_edges[0][0] and front_edges[j][0] == front_edges[0][1]:
            continue

        if ((p_x >= a1_x and p_x <= b1_x) or \
            (p_x <= a1_x and p_x >= b1_x)) and \
            ((p_y >= a1_y and p_y <= b1_y) or \
             (p_y <= a1_y and p_y >= b1_y)):

            if (p_x - c_x) ** 2 + (p_y - c_y) ** 2 <= r ** 2:
                flag = False
                if front_edges[j][0] == front_edges[0][0] or front_edges[j][0] == front_edges[0][1]:
                    here_point = points[front_edges[j][1]]
                    correct_points += [(j, (here_point[0] - c_x) ** 2 + (here_point[1] - c_y) ** 2, front_edges[j][1])]
                elif front_edges[j][1] == front_edges[0][0] or front_edges[j][1] == front_edges[0][1]:
                    here_point = points[front_edges[j][0]]
                    correct_points += [(j, (here_point[0] - c_x) ** 2 + (here_point[1] - c_y) ** 2, front_edges[j][0])]
                elif ((a1_x - a_x) ** 2 + (a1_y - a_y) ** 2) ** 0.5 + \
                    ((a1_x - b_x) ** 2 + (a1_x - b_y) ** 2) ** 0.5 <= \
                    ((b1_x - a_x) ** 2 + (b1_y - a_y) ** 2) ** 0.5 + \
                    ((b1_x - b_x) ** 2 + (b1_x - b_y) ** 2) ** 0.5:
                    here_point = points[front_edges[j][0]]
                    correct_points += [(j, (here_point[0] - c_x) ** 2 + (here_point[1] - c_y) ** 2, front_edges[j][0])]
                else:
                    here_point = points[front_edges[j][1]]
                    correct_points += [(j, (here_point[0] - c_x) ** 2 + (here_point[1] - c_y) ** 2, front_edges[j][1])]
        else:
            if (a1_x - c_x) ** 2 + (a1_y - c_y) ** 2 <= r ** 2:
                flag = False
                correct_points += [(j, (a1_x - c_x) ** 2 + (a1_y - c_y) ** 2, front_edges[j][0])]
            if (b1_x - c_x) ** 2 + (b1_y - c_y) ** 2 <= r ** 2:
                flag = False
                correct_points += [(j, (b1_x - c_x) ** 2 + (b1_y - c_y) ** 2, front_edges[j][1])]
    if flag == True:
        points += [(c_x, c_y)]
        edges += [(front_edges[0][0], len(points) - 1), (len(points) - 1, front_edges[0][1])]
        triags_point += [(front_edges[0][0], len(points) - 1, front_edges[0][1])]
        front_edges += [(front_edges[0][0], len(points) - 1), (len(points) - 1, front_edges[0][1])]
        del front_edges[0]
    else:
        sorted_correct_points = sorted(correct_points, key=lambda x: x[1])
        now_point = sorted_correct_points[0][2]
        edges += [(front_edges[0][0], now_point), (now_point, front_edges[0][1])]
        triags_point += [(front_edges[0][0], now_point, front_edges[0][1])]
        del front_edges[0]
        x, y = edges[-2][1], edges[-2][0]
        if (x, y) not in front_edges:
            front_edges += [(y, x)]
        else:
            del front_edges[front_edges.index((x, y))]
        x, y = edges[-1][1], edges[-1][0]
        if (x, y) not in front_edges:
            front_edges += [(y, x)]
        else:
            del front_edges[front_edges.index((x, y))]


print(points)
print(edges)
print(front_edges)
print(triags_point)


for i in range(len(edges)):
    edge = edges[i]
    x_coords = [points[edge[0]][0], points[edge[1]][0]]
    y_coords = [points[edge[0]][1], points[edge[1]][1]]

    plt.plot(x_coords, y_coords, linewidth=2, color='black')

    # mid_x = (points[edge[0]][0] + points[edge[1]][0]) / 2
    # mid_y = (points[edge[0]][1] + points[edge[1]][1]) / 2
    #
    # # Добавляем номер ребра
    # plt.text(mid_x, mid_y, str(i),
    #          fontsize=10, fontweight='bold',
    #          color='red',
    #          bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))

# for point in points:
#     plt.plot(point[0], point[1], 'ro', markersize=8)

for i, (x, y) in enumerate(points):
    plt.plot(x, y, 'ro', markersize=8, color='black')
    plt.text(x + 0.1, y + 0.1, str(i), fontsize=12, fontweight='bold')

plt.axis('equal')
plt.grid(True)
plt.show()
