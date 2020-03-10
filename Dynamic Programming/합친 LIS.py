
def find_jlis(A_idx, B_idx):
    #메모이제이션
    if cache[A_idx][B_idx] != -1:
        return cache[A_idx][B_idx]
    # 기본으로 설정된 값이 2개. A[A_idx], B[_idx]
    # but, -1부터 시작이므로 어차피 2를 빼야한다 그러므로 0부터 시작해도 무방.(-inf,-inf, ...)꼴이므로
    ret = 2
    # A[-1]이면 음의무한대 값을 입력하여 모든 수에대해 루프를 돌게한다.
    a = float('-inf') if A_idx == -1 else A[A_idx]
    b = float('-inf') if B_idx == -1 else B[B_idx]
    # A와 B의 원소중 큰값을 정하고 그 값보다 큰 원소를 탐색한다.
    max_elm = max(a, b)

    for next_A in range(A_idx + 1, len(A)):
        if max_elm < A[next_A]:  # A에서 큰 원소 발견시 +1을 하고 재귀호출
            ret = max(ret, find_jlis(next_A, B_idx) + 1)
    for next_B in range(B_idx + 1, len(B)):
        if max_elm < B[next_B]:  # B에서 큰 원소 발견시 +1을 하고 재귀호출
            ret = max(ret, find_jlis(A_idx, next_B) + 1)

    cache[A_idx][B_idx] = ret
    return ret

C = int(input())

for _ in range(C):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cache = [[-1 for _ in range(101)] for _ in range(101)]
    print(find_jlis(-1, -1)-2)


