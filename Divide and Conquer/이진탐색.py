
def binary_search(target, l, r, num_list, flag):
    m = (l + r) // 2

    if num_list[m] == target:
        return m+1
    if l > r:
        return False

    if target < num_list[m]:
        if flag == 'R':
            flag = 'L'
            idx = binary_search(target, l, m - 1, num_list, flag)
        else:
            return False

    else:
        if flag == 'L':
            flag = 'R'
            idx = binary_search(target, m + 1, r, num_list, flag)
        else:
            return False
    return idx


for t in range(1, int(input())+1):
    AN, BN = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for b in B:
        if b < A[(0 + len(B)-1) // 2]:
            first_f = 'R'
        else:
            first_f = 'L'
        if binary_search(b, 0, len(A)-1, A, first_f):
            cnt += 1

    print(f'#{t} {cnt}')
