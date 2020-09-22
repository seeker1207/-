from collections import deque


def make_border(x, y, d1, d2):

    # 1번 선거구
    for r in range(1, x):
        index_T[r][y] = 1

    # 2번 선거구
    for c in range(y+d2+1, N+1):
        index_T[x+d2][c] = 2

    # 3번선거구
    for c in range(1, y-d1):
        index_T[x+d1][c] = 3

    # 4번 선거구
    for r in range(x + d1 + d2 + 1, N+1):
        index_T[r][y-d1+d2] = 4

    # 5번 경계선
    for d in range(d1+1):
        index_T[x+d][y-d] = 5
        index_T[x+d2+d][y+d2-d] = 5
    for d in range(d2+1):
        index_T[x+d][y+d] = 5
        index_T[x+d1+d][y-d1+d] = 5


def indexing(index, start):
    visited = set()
    Q = deque([start])

    move_x = [-1, 0, 1, 0]
    move_y = [0, 1, 0, -1]

    if index == 5:
        for r in range(1, N+1):
            for c in range(1, N+1):
                index_T[r][c] = 5 if index_T[r][c] == 0 else index_T[r][c]
        return

    while Q:
        now = Q.popleft()
        now_x, now_y = now

        if 0 < now_x <= N and 0 < now_y <= N:
            if now not in visited and index_T[now_x][now_y] == 0:
                index_T[now_x][now_y] = index
                visited.add(now)
                for i in range(4):
                    Q.append((now_x + move_x[i], now_y + move_y[i]))


def calculate():
    result = [0]*6

    for r in range(1, N+1):
        for c in range(1, N+1):
            idx, value = index_T[r][c], T[r][c]
            result[idx] += value

    return max(result[1:]) - min(result[1:])


N = int(input())
T = [[0] * (N+2)]
index_T = []
min_result = float('inf')

for i in range(1, N+1):
    input_list = list(map(int, input().split()))
    T.append([0] + input_list + [0])
T.append([0]*(N+2))


for d1 in range(1, N-1):
    for d2 in range(1, N-1):
        for x in range(1, N - (d1+d2) + 1):
            for y in range(1 + d1, N - d2 + 1):
                index_T = [[0 for _ in range(N + 2)] for _ in range(N + 2)]
                make_border(x, y, d1, d2)
                indexing(1, (1, 1))
                indexing(2, (1, N))
                indexing(3, (N, 1))
                indexing(4, (N, N))
                indexing(5, (0, 0))

                min_result = min(min_result, calculate())

print(min_result)


