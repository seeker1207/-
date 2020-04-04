def solution(triangle):
    answer = 0
    cache = [[0] * i for i in range(1, len(triangle) + 1)]
    cache[0][0] = triangle[0][0]

    for r in range(1, len(triangle)):
        for c in range(r + 1):
            if c == 0:
                cache[r][c] = cache[r - 1][c] + triangle[r][c]
            elif c == r:
                cache[r][c] = cache[r - 1][c - 1] + triangle[r][c]
            else:
                cache[r][c] = max(cache[r - 1][c - 1], cache[r - 1][c]) + triangle[r][c]

    return max(cache[len(triangle) - 1])