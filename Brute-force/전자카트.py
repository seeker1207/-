def perm_and_find_min(min_sum=0, k=1):
    global N, p, result, e

    if k == N:
        min_sum += e[p[-1]][0]
        result = min(result, min_sum)
        return

    for j in range(k, N):
        p[k], p[j] = p[j], p[k]
        start, end = p[k-1], p[k]
        min_sum += e[start][end]

        perm_and_find_min(min_sum, k+1)
        min_sum -= e[start][end]
        p[k], p[j] = p[j], p[k]


for i in range(int(input())):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]
    result = 10000
    p = [x for x in range(N)]
    perm_and_find_min()
    print(f'#{i+1} {result}')

def combination(arr, r):
    # 1.
    arr = sorted(arr)

    # 2.
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return

    	# 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()
    generate([])

combination('ABCDE', 3)
