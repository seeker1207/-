# cache[a] : a번째 집까지 훔친 돈의 최대금액.

def solution(money):
    answer = 0
    n = len(money)
    cache = [-1] * n
    cache2 = [-1] * n

    cache[0] = 0
    cache[1] = money[1]
    for i in range(2, n):
        cache[i] = max(cache[i - 2] + money[i], cache[i - 1])

    cache2[0] = money[0]
    cache2[1] = cache2[0]

    for i in range(2, n - 1):
        cache2[i] = max(cache2[i - 2] + money[i], cache2[i - 1])

    answer = max(cache[n - 1], cache2[n - 2])

    return answer