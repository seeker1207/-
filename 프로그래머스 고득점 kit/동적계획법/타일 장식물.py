def solution(N):
    answer = 0
    dp = [-1]*(N+1)
    if N > 3:
        dp[1] = 1
        dp[2] = 1
        for i in range(3, N+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[N] * 3 + dp[N-1] * 2 + dp[N-2] * 2 + dp[N-3]
    elif N == 3:
        return 10
    elif N == 2:
        return 6
    else:
        return 4