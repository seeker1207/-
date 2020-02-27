# 재귀함수 호출로 푸는방법 , 파이썬에서는 런타임오류(재귀호출 제한 or 스택오버플로우)

# def make_one(n):
#     if n == 1:
#         return 0
#     if memo[n] != -1:
#         return memo[n]
#
#     cnt1, cnt2, cnt3 = float('inf'), float('inf'), float('inf')
#     if n % 3 == 0: cnt1 = make_one(n//3) + 1
#     if n % 2 == 0: cnt2 = make_one(n//2) + 1
#     cnt3 = make_one(n-1) + 1
#     memo[n] = min(cnt1, cnt2, cnt3)
#     return memo[n]

# 바텀업 방식으로 구해가는 방식. but, 런타임오류
# def make_one(input_N):
#     global memo, N
#     memo[1] = 0
#     memo[2] = 1
#     memo[3] = 1
#
#     for n in range(1, N):
#         if n*3 <= N:
#             memo[n*3] = min(memo[n] + 1, memo[n*3])
#         if n*2 <= N:
#             memo[n*2] = min(memo[n] + 1, memo[n*2])
#         memo[n+1] = min(memo[n] + 1, memo[n+1])
#
#     return memo[N]

def make_one(input_N):
    # 인덱스 값을 하나씩 증가시키면서 탐색한다
    for i in range(1, input_N+1):
        memo[i] = memo[i-1] + 1 # 그전의 인덱스에서 +1 카운트한다 (N-1의 경우)

        if i % 2 == 0: # 그 전에 2로 나누어진 인덱스 DP값에서 +1 카운트 (N//2의 경우)
            memo[i] = min(memo[i], memo[i//2]+1)
        if i % 3 == 0: # 그 전에 3으로 나누어진 인덱스 DP값에서 +1 카운트 (N//3의 경우)
            memo[i] = min(memo[i], memo[i//3]+1)
        # 결과적으로 i를 계산했을 때의 최소값이 memo[i]에 저장됨.
    return memo[input_N]

N = int(input())
memo = [-1]*(N+1)
print(make_one(N))

