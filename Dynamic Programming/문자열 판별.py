import sys
input = sys.stdin.readline

s = input().strip()
n = int(input().strip())
A = [input().strip() for _ in range(n)]

dp = [0]*(len(s) + 1)
dp[0] = 1

for i in range(1, len(s) + 1):
    for word in A:
        if i - len(word) >= 0 and s[i - len(word):i] == word:
            dp[i] = dp[i - len(word)] and 1
        if dp[i]: break


print(dp[-1])
