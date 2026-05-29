import json


# point_adaptive =
point_exact = None
with open('points_exact.json', 'r') as f:
    point_exact = json.load(f)

point_ad = None
with open('points_inter_ad.json', 'r') as f:
    point_ad = json.load(f)

point_not_ad = None
with open('points_inter_not_ad.json', 'r') as f:
    point_not_ad = json.load(f)

# print(len(point_exact))
# print(len(point))


# error_adaptive = []
# ind_error_ad = []
# for j in range(len(point_adaptive)):
#     error_now = 0
#     ind_error_now = 0
#     for i in range(len(point_adaptive[j])):
#         if abs(point_adaptive[j][i][-1] - point_exact[j][i][-1]) / point_exact[j][i][-1] > error_now:
#             error_now = abs(point_adaptive[j][i][-1] - point_exact[j][i][-1]) / point_exact[j][i][-1]
#             ind_error_now = i
#     error_adaptive += [error_now]
#     ind_error_ad += [ind_error_now]

error = []
# error_otn =[]
# ind_error = []
# ind_error_otn = []
for j in range(len(point_ad)):
    error_ad_now = 0
    error_not_ad_now = 0
    # ind_error_now = 0
    # error_now_otn = 0
    # ind_error_now_otn = 0
    for i in range(len(point_ad[-1])):
        # print(len(point_exact), len(point), len(point_exact[-1]), len(point[-1]))
        # print(abs(point[i][-1] - point_exact[i][-1]), point_exact[i][-1])
        # if abs(point_ad[j][i][-2] - point_exact[j][i][-2]) / abs(point_exact[j][i][-2]) > error_now_otn:
        #     error_now_otn = abs(point[j][i][-2] - point_exact[j][i][-2]) / abs(point_exact[j][i][-2])
        #     ind_error_now_otn = i
        if abs(point_ad[j][i][-2] - point_exact[j][i][-2]) > error_ad_now:
            error_ad_now = abs(point_ad[j][i][-2] - point_exact[j][i][-2])
            # ind_error_now = i
        if abs(point_not_ad[j][i][-2] - point_exact[j][i][-2]) > error_not_ad_now:
            error_not_ad_now = abs(point_not_ad[j][i][-2] - point_exact[j][i][-2])

    if error_ad_now > error_not_ad_now:
        error += [error_ad_now - error_not_ad_now]
    # ind_error += [ind_error_now]
    # error_otn += [error_now_otn]
    # ind_error_otn += [ind_error_now_otn]

# ind = error.index(max(error))
# # ind = 84 # 25
# ind_2 = ind_error[ind]
# # ind_2 = 25
print("Abs")
print(len(error), max(error))
print(sum(error) / len(error))
# print("Otn")
# print(max(error_otn))
# print(sum(error_otn) / len(error_otn))
# print(len(point[-1]), len(point[-1][-1]))
print(point_ad[0])
print(point_not_ad[0])
print(len(point_ad), len(point_ad[0]))
# print(max(error_adaptive))
