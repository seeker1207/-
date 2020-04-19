def solution(m, n, puddles):
    cache = [[-1] * m for _ in range(n)]

    for i in range(m):
        cache[0][i] = 1
    for j in range(n):
        cache[j][0] = 1

    for puddle in puddles:
        r, c = puddle[1], puddle[0]
        if r - 1 == 0:
            for i in range(c, m):
                cache[0][i] = 0
        elif c - 1 == 0:
            for j in range(r, n):
                cache[j][0] = 0
        cache[r - 1][c - 1] = 0

    for r in range(1, n):
        for c in range(1, m):
            if cache[r][c] != 0:
                cache[r][c] = cache[r - 1][c] + cache[r][c - 1]

    return cache[n - 1][m - 1] % 1000000007