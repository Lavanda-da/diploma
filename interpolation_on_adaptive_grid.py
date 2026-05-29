import json
import time


points = None
with open('points_ad_0001_42.json', 'r') as f:
    points = json.load(f)

for i in range(len(points)):
    time_points = []
    for elem in points[i]:
        time_points += [tuple(elem)]
    points[i] = time_points

triags_list = None
with open('triags_list_ad_0001_42.json', 'r') as f:
    triags_list = json.load(f)

for i in range(len(triags_list)):
    time_triags = []
    for elem in triags_list[i]:
        time_triags += [tuple(elem)]
    triags_list[i] = time_triags

triag_grinding = None
with open('triag_grinding_ad_0001_42.json', 'r') as f:
    triag_grinding = json.load(f)

for i in range(len(triag_grinding)):
    time_triag_grinding = {}
    for elem in triag_grinding[i].keys():
        time_triag_grinding[tuple(map(int, elem.split()))] = [tuple(tr) for tr in triag_grinding[i][elem]]
    triag_grinding[i] = time_triag_grinding


random_points = None
nums_of_triag = None
bar_coords = None

with open('random_points.json', 'r') as f:
    random_points = json.load(f)
for i in range(len(random_points)):
    random_points[i] = tuple(random_points[i])

with open('nums_of_triag_42.json', 'r') as f:
    nums_of_triag = json.load(f)

with open('bar_koords_42.json', 'r') as f:
    bar_coords = json.load(f)
for i in range(len(bar_coords)):
    bar_coords[i] = tuple(bar_coords[i])


all_res = []

start_time = time.time()

for elem in range(len(random_points)):
    print(elem)
    alfa, beta, gama = bar_coords[elem]
    x, y = random_points[elem]
    num_of_triags = nums_of_triag[elem]
    triag_in_point = triags_list[0][num_of_triags]
    res = []
    for i in range(len(triags_list)):
        while triag_in_point in triag_grinding[i].keys():
            for j in range(len(triag_grinding[i][triag_in_point])):
                triag = triag_grinding[i][triag_in_point][j]

                x1, y1 = points[i - 1][triag[0]][0], points[i - 1][triag[0]][1]
                x2, y2 = points[i - 1][triag[1]][0], points[i - 1][triag[1]][1]
                x3, y3 = points[i - 1][triag[2]][0], points[i - 1][triag[2]][1]
                delta = x2 * y3 + x3 * y1 + x1 * y2 - \
                        (x2 * y1 + x3 * y2 + x1 * y3)

                alfa_new = x2 * y3 + x3 * y + x * y2 - \
                       (x2 * y + x3 * y2 + x * y3)
                beta_new = x * y3 + x3 * y1 + x1 * y - \
                       (x * y1 + x3 * y + x1 * y3)
                gama_new = x2 * y + x * y1 + x1 * y2 - \
                       (x2 * y1 + x * y2 + x1 * y)
                alfa_new /= delta
                beta_new /= delta
                gama_new /= delta

                if alfa_new >= 0 and beta_new >= 0 and gama_new >= 0:
                    alfa, beta, gama = alfa_new, beta_new, gama_new
                    triag_in_point = triag
                    break

        num_of_triags = triags_list[i].index(triag_in_point)
        x = alfa * points[i][triags_list[i][num_of_triags][0]][0] + \
            beta * points[i][triags_list[i][num_of_triags][1]][0] + \
            gama * points[i][triags_list[i][num_of_triags][2]][0]
        y = alfa * points[i][triags_list[i][num_of_triags][0]][1] + \
            beta * points[i][triags_list[i][num_of_triags][1]][1] + \
            gama * points[i][triags_list[i][num_of_triags][2]][1]
        res += [(i, x, y)]
    all_res += [res]


end_time = time.time()

print(f"{end_time - start_time:.40f}, секунд")

with open('points_inter_ad.json', 'w') as f:
    json.dump(all_res, f)
