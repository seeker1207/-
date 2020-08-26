from collections import deque

def make_border(x, y, d1, d2):

    for r in range(1, N+1):
        for c in range(1, N+1):
            T[r][c] = 5

    # 1번선거구
    for r in range(1, x):
        T[r][y] = 1

    # 2번선거구
    for c in range(y+d2+1, N+1):
        T[x+d2][c] = 2

    # 3번선거구
    for c in range(1, y-d1):
        T[x+d1][c] = 3

    # 4번 선거구
    for r in range(x + d1 + d2 + 1, N+1):
        T[r][y-d1+d2] = 4

def indexing(index, start):
    visited = set()
    Q = deque([start])

    move_x = [-1, 0, 1, 0]
    move_y = [0, 1, 0, -1]

    while Q:
        now = Q.popleft()
        if now not in visited:
            visited.add(now)
            for i in range(4):

                Q.append[(now[0]+move_x[i], now[1]+move_y[i])]


N = int(input())
T = [['0'] * (N+2)]

for i in range(1, N+1):
    input_list = input().split()
    T.append(['0'] + input_list + ['0'])

T.append(['0']*(N+2))

# #
# for d1 in range(1, N-1):
#     for d2 in range(1, N-1):
#         for x in range(1, N - (d1+d2)):
#             for y in range(1 + d1, N - d2):
#                 divide(x, y, d1, d2)
make_border(2, 5, 3, 2)

for t in T:
    print(t)