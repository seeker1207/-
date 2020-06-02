"""
징검다리를 건널수 있는 사람수의 최대값은 배열 stones의 최대값.

1. 징검다리를 건널 수 있는 사람수를 중간값으로 가정한다.
2. stones 배열을 앞에서부터 탐색하면서
    중간값(건널수 있는 사람수를 가정한 값) - 1 보다 작은 수가 나올때마다 count + 1을 한다.
3. 연속으로 0이 되는 갯수 (count) 을 k와 비교한다. (k는 거리이므로)
    k보다 작거나 같으면, 건널 수 있는 사람수를 더 늘려본다.
    k보다 크면, 건널 수 있는 사람수를 더 줄여본다.

"""

def solution(stones, k):
    answer = 0
    left, right = 1, max(stones)

    while left <= right:
        middle = (left + right) // 2
        cnt = 0
        max_cnt = 0

        for stone in stones:
            if stone <= middle - 1: # 3명의 사람이 건널수 있다면 2보다 작거나 같은 징검다리가 0이 된후 세번째 차례의 사람이 건널수 있다.
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 0

        max_cnt = max(max_cnt, cnt)

        if max_cnt + 1 <= k:
            answer = max(answer, middle)
            left = middle + 1
        else:
            right = middle - 1

    return answer