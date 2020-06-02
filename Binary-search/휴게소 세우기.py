"""
백준 1477번 [휴게소 세우기]
휴게소가 없는 구간의 최솟값은 1, 최대값은 max(휴게소 사이 거리들)

1. 휴게소 사이 거리 값을 계산하며 탐색한다.
2. 휴게소가 없는 구간의 최대값을 중간값으로 가정하고,
    휴게소사이의 거리값이 그 중간값보다 크면 그 구간에 휴게소를 세워야 하므로 count +1을 한다.
3. 세울수 있는 휴게소의 갯수가 입력된 M보다 작거나 같으면 구간 최대거리를 더 줄여본다.
    (같지 않아도 되는 이유는 세울수 있는 갯수가 작으면
    모자란만큼 더 지어도 휴게소 사이의 거리값이 원래의 거리값을 넘지않는다.)
    더 크다면 구간 최대거리를 늘려본다.
"""

N, M, L = map(int, input().split())
rest_places = list(map(int, input().split())) + [L]
rest_places.sort()

result = float('inf')
prev = rest_places[0]
rest_dts = [prev]

for rp in rest_places[1:]:
    rest_dts.append(rp - prev)
    prev = rp

left, right = 1, L
# print(rest_dts)
while left <= right:
    middle = (left + right) // 2
    cnt = 0
    # print("middle =", middle)
    for dt in rest_dts:
        if dt > middle:
            if dt % middle == 0:
                cnt += (dt // middle) - 1
            else:
                cnt += dt // middle

        # print("dt =", dt, "cnt =", cnt)
    if cnt <= M:
        result = min(result, middle)
        right = middle - 1
    else:
        left = middle + 1

print(result)














