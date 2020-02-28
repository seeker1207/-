

n, k = map(int, input().split())
coin_list = [int(input()) for _ in range(n)]
dp = [float('inf')]*(k+1)

dp[0] = 0

for i in range(k - min(coin_list)):
    for coin in coin_list:
        if i+coin <= k:
            dp[i+coin] = min(dp[i+coin], dp[i] + 1)

if dp[k] == float('inf'):
    print(-1)
else:
    print(dp[k])

    
