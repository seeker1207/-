T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
result = []

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    charge_list = list(map(int, input().split()))
    now_K = K
    now_stop = 0
    charge_count = 0

    while now_stop != N:
        if now_stop + now_K == N:
            now_stop += now_K
            break
        elif now_stop + now_K in charge_list:
            now_stop += now_K
            charge_count += 1
            now_K = K
        else:
            now_K -= 1
            if now_K == 0:
                charge_count = 0
                break

    result.append(charge_count)

for n in range(1, T + 1):
    print("#{0} {1}".format(n, result[n-1]))


























