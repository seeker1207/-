
# 재귀적 방법
# def find_max(stat, col):
#     global grid, n
#
#     if col > n - 1:
#         return 0
#     if dp[stat][col] != -1:
#         return dp[stat][col]
#     ret = -1
#     if stat == 1 or stat == 2:
#         ret = find_max(0, col+1) + grid[0][col]
#     if stat == 0 or stat == 2:
#         ret = max(ret, find_max(1, col+1) + grid[1][col])
#
#     ret = max(ret, find_max(2, col+1))
#     dp[stat][col] = ret
#
#     return ret
# 반복적 방법
def find_max():
    global dp, grid, n

    dp[0][0] = grid[0][0]
    dp[1][0] = grid[1][0]
    dp[2][0] = 0

    for i in range(1, n):
        dp[0][i] = max(dp[1][i-1], dp[2][i-1]) + grid[0][i]
        dp[1][i] = max(dp[0][i-1], dp[2][i-1]) + grid[1][i]
        dp[2][i] = max(dp[0][i-1], dp[1][i-1], dp[2][i-1])

    return max(dp[0][n-1], dp[1][n-1], dp[2][n-1])

T = int(input())
for t in range(T):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*(n+1) for _ in range(3)]
    print(find_max())
