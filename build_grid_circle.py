import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import math
import time
import json


points = []  # (index_start, index_end)
edges = []  # (index_start, index_end)
triags_point = []  # (point_1, point_2, point_3)

r = 0.028
EPS = 1e-5

radius = 2
Pi = math.acos(-1)

start_time = time.time()
delta_phi = 2 * math.asin(r / (2 * radius))
phi = 0

while phi < 2 * Pi:
    points_on_circle = (radius * math.cos(phi), radius * math.sin(phi))
    vector_kasat_x, vector_kasat_y = -points_on_circle[1], points_on_circle[0]
    len_vector_kasat = (vector_kasat_x ** 2 + vector_kasat_y ** 2) ** 0.5
    vector_kasat_x, vector_kasat_y = vector_kasat_x / len_vector_kasat, vector_kasat_y / len_vector_kasat
    new_point = (points_on_circle[0] + r / 2 * vector_kasat_x, points_on_circle[1] + r / 2 * vector_kasat_y)
    points += [new_point]
    if phi > 0:
        edges += [(len(points) - 2, len(points) - 1)]
    phi += delta_phi

del points[-1]
del edges[-1]
edges += [(len(points) - 1, 0)]

now_edge = None
front_edges = edges[:]

count_ind = 0

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
                else:
                    here_point = points[front_edges[j][0]]
                    correct_points += [(j, (here_point[0] - c_x) ** 2 + (here_point[1] - c_y) ** 2, front_edges[j][0])]
                    here_point = points[front_edges[j][1]]
                    correct_points += [(j, (here_point[0] - c_x) ** 2 + (here_point[1] - c_y) ** 2, front_edges[j][1])]
        else:
            if (a1_x - c_x) ** 2 + (a1_y - c_y) ** 2 <= r ** 2:
                flag = False
                correct_points += [(j, (a1_x - c_x) ** 2 + (a1_y - c_y) ** 2, front_edges[j][0])]
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

end_time = time.time()

print(f"Время выполнения: {end_time - start_time:.40f} секунд")


with open("start_points_100.json", "w") as f:
    json.dump([points], f)
with open("start_edges_100.json", "w") as f:
    json.dump(edges, f)
with open("start_triags_100.json", "w") as f:
    json.dump(triags_point, f)


fig, ax = plt.subplots()

for i in range(len(edges)):
    edge = edges[i]
    x_coords = [points[edge[0]][0], points[edge[1]][0]]
    y_coords = [points[edge[0]][1], points[edge[1]][1]]

    ax.plot(x_coords, y_coords, linewidth=2, color='black')

for i in range(len(front_edges)):
    edge = front_edges[i]
    x_coords = [points[edge[0]][0], points[edge[1]][0]]
    y_coords = [points[edge[0]][1], points[edge[1]][1]]

    ax.plot(x_coords, y_coords, linewidth=2, color='black')


for i, (x, y) in enumerate(points):
    plt.plot(x, y, 'ro', markersize=8, color='black')

circle = Circle((0, 0), radius=2, fill=False, edgecolor='red', linewidth=2)
ax.add_patch(circle)

plt.axis('equal')
plt.xlabel('x(0)')
plt.ylabel('y(0)')
plt.grid(True)
plt.show()
