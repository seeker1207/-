def precalc():
    # num_list 를 정렬하고 부분합을 미리 구한다.
    global num_list
    num_list.sort()
    p_sum[0] = num_list[0]
    p_sq_sum[0] = num_list[0] * num_list[0]
    for i in range(1, n):
        p_sum[i] = p_sum[i - 1] + num_list[i]
        p_sq_sum[i] = p_sq_sum[i - 1] + (num_list[i] * num_list[i])
    # print(p_sum, p_sq_sum)

def min_error(lo, hi):
    # num_list[lo] ... [hi] 까지의 리스트를 양자화할때의 최소 오차합을 구한다.
    sum = p_sum[hi] - (0 if lo == 0 else p_sum[lo - 1])
    sq_sum = p_sq_sum[hi] - (0 if lo == 0 else p_sq_sum[lo - 1])
    # 평균을 반올림한 값으로 양자화를 한다
    m = int(0.5 + sum / (hi - lo + 1))
    # sum(num_list[i] - m)^2 을 전개한 결과를 부분합으로 구한다.
    ret = sq_sum - 2 * m * sum + m * m * (hi - lo + 1)
    return ret

def quantize(now, parts):
    # 모든 숫자를 다 양자화 했을때 return 0
    if now == n: return 0
    # 리스트에 아직 그룹화 되지 않은 숫자는 남았으나 더이상 묶을수 있는 s가 남아있지 않을 때
    if parts == 0: return float('inf')
    # 메모이제이션된 부분문제인지 확인
    if cache[now][parts] != -1: return cache[now][parts]

    ret = float('inf')
    # 그룹의 크기를 변화시켜가며 최소치를 찾는다.
    for part_size in range(1, n):
        if now + part_size > n: break
        ret = min(ret, min_error(now, now + part_size - 1) + \
                  quantize(now + part_size, parts - 1))

    cache[now][parts] = ret
    return ret


C = int(input())

for c in range(C):
    n, s = map(int, input().split())
    cache = [[-1] * (s+1) for _ in range(n)]
    num_list = list(map(int, input().split()))
    p_sum = [-1] * (n+1)
    p_sq_sum = [-1] * (n+1)

    precalc()
    print(quantize(0, s))