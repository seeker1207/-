import itertools

def make_list(max_cnt):
    global N
    result = []
    cnt = 0
    for num in range(1<<N):
        for n in range(N):
            if num & 1<<n:
                cnt += 1
        if cnt == max_cnt and num != 1:
            result.append(num)
        cnt = 0
    return result

def find_min_cost():
    global N, E
    # D[i][subset]: 시작노드 i일때 거쳐야하는 부분집합이 subset 일때의 최소거리값
    # 부분집합을 이진수로 표현하여 십진수로 전환한값을 인덱스로 활용. {0,1,2} = 111 = 7

    D = [[20000] * ((1 << N)+ 1) for _ in range(N)]  # 부분집합의 개수만큼 크기의 리스트 초기화
    for idx, d in enumerate(D):  # 공집합에 해당하는 값을 미리 초기화
        d[0] = E[idx][0]

    # 부분집합이 N-2 개가 될때까지 반복
    for k in range(1, N-1):
        for subset in make_list(k):  # 원소숫자가 K개인 부분집합 리스트 출력
            for i in range(1, N):  # 첫노드인 0을 제외한 1부터 시작노드를 설정하여 반복
                if not (subset & 1 << i):  # 부분집합안에 첫노드 i가 없는 경우만 반복하도록 한다
                    min_val = float('inf')
                    # 부분집합을 이진수로 바꾸어 그길이만큼 반복
                    for n in range(1, len(format(subset, 'b'))):
                        if subset & 1 << n:  # n만큼 1을 쉬프트했을때 true라면 해당부분집합에 n번노드가 있음을 확인.
                            # subset의 원소 노드를 하나씩 제외하면서 최소값을 탐색
                            min_val = min(min_val, E[i][n] + D[n][subset-(1<<n)])
                            D[i][subset] = min_val

    subset = (1 << N) - 2  # subset을 0을 제외한 부분집합으로 초기화
    min_val = float('inf')
    # 시작노드를 0으로 잡고 답을 구한다
    for n in range(1, len(format(subset, 'b'))):
        if subset & 1 << n :
            min_val = min(min_val, E[0][n] + D[n][subset - (1 << n)])
            D[0][subset] = min_val

    return D[0][subset]

T = int(input())
for t in range(1, T+1):

    N = int(input())
    E = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{t} {find_min_cost()}")
