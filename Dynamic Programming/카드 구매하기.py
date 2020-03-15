import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

dp = [0] * (N+1)
dp[1] = P[0]

for i in range(1, N+1):
    for p_idx, p_val in enumerate(P):
        if i - (p_idx + 1) >= 0:
            dp[i] = max(dp[i], dp[i - (p_idx+1)] + p_val)

print(dp[N])
