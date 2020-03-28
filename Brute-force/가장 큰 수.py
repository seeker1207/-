
def find_max(n):
    global N, K, str_list

    if N == n:
        return 0

    start = n
    for i in range(start, N):
        ret = find_max(i+1) + int(str_list[i])
        max_ret = max(ret, max_ret)

    return max_ret



N, K = map(int, input().split())
str_list = list(input())
max_val = 0
find_max()
# for i in range(N-K+1):
#     val = int("".join(str_list[i:i+K]))
#     max_val = max(val, max_val)






