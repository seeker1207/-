"""
1. 가장 위에서부터 해당 깊이까지의 최소값이 담긴 배열을 만든다.
2. 피자를 하나씩 넣으면서 넣을 위치를 최소값 배열을 참고하여 이진탐색으로 찾는다.
3. 다음에 찾을 범위는 맨위부터 이진탐색으로 찾은 위치 - 1 까지가 된다.
"""
import sys

def get_oven_idx(st, ed, pizza):
    ret_idx = 0
    start, end = st, ed

    while start <= end:
        middle = (start + end) // 2

        if pizza <= min_oven[middle]:
            ret_idx = max(ret_idx, middle)
            start = middle + 1
        else:
            end = middle - 1

    if not ret_idx:
        return -1
    else:
        return ret_idx


D, N = map(int, sys.stdin.readline().split())
oven = list(map(int, sys.stdin.readline().split()))
pizzas = list(map(int, sys.stdin.readline().split()))
last_pizza = pizzas[-1]
min_oven = []
result = 0
min_temp = float('inf')

for radius in oven:
    min_temp = min(min_temp, radius)
    min_oven.append(min_temp)

# print(min_oven)
oven_st, oven_ed = 0, D - 1

for pizza in pizzas:
    pizza_idx = get_oven_idx(oven_st, oven_ed, pizza)
    # print(pizza_idx)
    if pizza_idx != -1:
        oven_ed = pizza_idx - 1
    else:
        break

if pizza_idx != -1:
    print(pizza_idx + 1)
else:
    print(0)








# while left <= right:
#     middle = (left + right) // 2
#     end_depth = len(oven)
#     is_ok = False
#
#     for pizza in pizzas[:-1]:
#         for idx, radius in enumerate(oven[candidate[middle] + 1:end_depth]):
#             if pizza <= radius:
#                 is_ok = True
#             elif is_ok and pizza > radius:
#                 end_depth = idx - 1 # 이전에 넣어진 피자의 위치
#                 is_ok = False
#             else:
#                 is_ok = False
#                 break
#
#
#     print(candidate[middle], is_ok)
#     if is_ok:   # 피자를 다 넣을수 있었으면 최상단 위치를 내려본다.(인덱스는 증가한다.)
#         left = middle + 1
#         result = max(result, middle)
#     else:
#         right = middle - 1
#
# print(result + 1)