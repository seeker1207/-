
def divide(x, y, d1, d2):
    # 1번선거구
    for r in range(1, x+d1):
        for c in range(1, y+1):
            T[r][c] = 1

    # 2번선거구
    for c in range(y+1, N+1):
        for r in range(1, x+d2+1):
            T[r][c] = 2

    # 3번선거구
    for c in range(1, y-d1+d2):
        for r in range(x + d1, N+1):
            T[r][c] = 3

    # 4번 선거구
    for r in range(x + d2 + 1, N+1):
        for c in range(y - d1 + d2, N+1):
            T[r][c] = 4

    # 5번 선거구


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
divide(2, 4, 2, 2)
for t in T:
    print(t)