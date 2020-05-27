"""
1. n개의 바위를 제거해서 바위 간 간격의 최솟값이 x보다 크거나 같게 되는 집합이 존재하는가를 살펴보는것이 핵심 포인트.
2. 존재한다면 x를 더 크게해서 살펴보고 그렇지 않다면 x를 더 작게해서 살펴본다.
3. 그런경우가 존재하는지 어떻게 살펴보지?
    - 바위 위치 배열을 순회하면서 현재 바위와 제거 하지않은 그 이전의 바위 사이 간격이 x보다 작으면 현재 바위를 제거.
    - 제거한 바위의 개수가 n보다 작거나 같으면 n개의 바위를 제거하는 경우가 존재함을 의미.
"""

def solution(distance, rocks, n):
    answer = 0
    left, right = 1, distance
    rocks.sort()

    while left <= right:
        cnt = 0
        prev = 0
        middle = (left + right) // 2

        for rock in rocks[:-1]:
            if rock - prev < middle:
                cnt += 1
                continue
            prev = rock

        if rocks[-1] - prev < middle or distance - rocks[-1] < middle:
            cnt += 1

        if cnt <= n:
            # print(middle, cnt)
            answer = max(answer, middle)
            left = middle + 1
        else:
            right = middle - 1

    return answer