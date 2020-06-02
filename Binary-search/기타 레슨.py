"""
블루레이의 길이가 될수 있는
최소값은 max(기타레슨의 길이들), 최대값은 기타레슨의 길이들을 모두 더한 값.

1. 기타레슨의 길이의 리스트를 앞에서부터 탐색하면서 값들의 합을 구한다.
2. 블루레이의 길이를 중간값으로 가정하고 그 중간값보다 작거나 같을때까지만 합을 반복한다.
3. 그렇게 나눠진 블루레이의 갯수가 입력된 블루레이 갯수보다 작거나 같으면
    블루레이의 길이를 작게해보고,
    만약 크다면 길이를 크게해본다.
"""

N, M = map(int, input().split())
ls_lens = list(map(int, input().split()))
left, right = max(ls_lens), sum(ls_lens)
result = float('inf')

while left <= right:
    middle = (left + right) // 2
    len_sum = 0
    cnt = 0
    for ls_len in ls_lens:
        if len_sum + ls_len <= middle:
            len_sum += ls_len
        else:
            cnt += 1
            len_sum = ls_len
    # print(left, right, middle, cnt)
    if cnt + 1 <= M:
        result = min(result, middle)
        right = middle - 1
    else:   # cnt > M
        left = middle + 1

print(result)





