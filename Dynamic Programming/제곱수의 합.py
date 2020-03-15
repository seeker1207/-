
# def min_sqr_sum(sum):
#
#     if sum == N:
#         return 0
#     elif sum > N:
#         return float('inf')
#
#     if not cache[sum]:
#         return cache[sum]
#     ret = float('inf')
#
#     for sqr in sqr_list:
#         ret = min(ret, min_sqr_sum(sum + sqr) + 1)
#
#     cache[sum] = ret
#     return ret

N = int(input())
cache = [float('inf')]*(N+1)
# cache = [-1]*(N+1)
sqr_list = [i*i for i in range(1, N+1) if i*i <= N]
# print(sqr_list)
# print(min_sqr_sum(0))

cache[0] = 0
for n in range(N+1):
    for sqr in sqr_list:
        if n + sqr < N + 1:
            cache[n + sqr] = min(cache[n + sqr], cache[n]+1)
        else:
            break

print(cache[N])