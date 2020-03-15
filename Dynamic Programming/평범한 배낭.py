import sys
input = sys.stdin.readline

N, K = map(int, input().split())
W, V = [-1], [-1]
dp = [[-1]*(K+1) for _ in range(N+1)]

for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

# 0번까지의 물건을 고려하는 경우, 무게가 0인 경우 모두 0으로 초기화.
for i in range(N+1):
    dp[i][0] = 0
for k in range(K+1):
    dp[0][k] = 0

# dp[n][k] n번의 물건까지 고려하고 k무게일때의 가치 최대값.
for n in range(1, N+1):
    for k in range(1, K+1):
        if W[n] > k:
            # 현재 넣을 물건의 무게가 넣을수 있는 가방의 무게보다 크므로 넣을수 없음.
            dp[n][k] = dp[n-1][k]
        else:
            # 물건을 넣었을 경우와 넣지 않았을 경우 둘중 최대값.
            dp[n][k] = max(dp[n-1][k - W[n]] + V[n], dp[n-1][k])

print(dp[N][K])