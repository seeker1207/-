def hoare_partition(A, l, r):
    p = A[l]
    i = l + 1
    j = r
    while i <= j:
        while i <= j and A[i] <= p: i += 1
        while i <= j and A[j] >= p: j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]

    return j


def romuto_partition(A, l, r):
    p = A[r]
    i = l - 1
    for j in range(l,r):
        if A[j] <= p:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quick_sort(A, l, r):
    if l < r:
        # s = hoare_partition(A, l, r)
        s = romuto_partition(A, l, r)
        quick_sort(A, l, s-1)
        quick_sort(A, s+1, r)


for t in range(1, int(input())):
    N = int(input())
    a_list = list(map(int, input().split()))
    quick_sort(a_list, 0, len(a_list)-1)
    print(a_list)
    print(f'#{t} {a_list[N//2]}')
