import json


point_exact = None
with open('points_exact.json', 'r') as f:
    point_exact = json.load(f)

point = None
with open('points_inter.json', 'r') as f:
    point = json.load(f)


error = []
for j in range(len(point)):
    error_now = 0
    for i in range(len(point[-1])):
        if abs(point[j][i][-2] - point_exact[j][i][-2]) / abs(point_exact[j][i][-2]) > error_now:
            error_now = abs(point[j][i][-2] - point_exact[j][i][-2])
    error += [error_now]


print("Abs")
print(max(error))
print(sum(error) / len(error))
