
def fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    if memo[n] != -1: return memo[n]

    memo[n] = fibonacci(n-1) + fibonacci(n-2)

    return memo[n]


N = int(input())
memo = [-1] * (N+1)
print(fibonacci(N))