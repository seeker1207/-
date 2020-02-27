'리스트 표현'
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
newlist = [(i,j) for i in range(n) for j in range(m) if mylist[i][j]]
lslist = [(j,i) for i in range(3) for j in range(5)]
print(arr)

'리스트 지그재그 탐색'
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j + (m-1-2*j)*(i%2)])

'부분집합 생성'
arr = [3, 6, 7, 1]
n = len(arr)
bubun_list = []
bubun_elm = []
for i in range(1 << n):  # 부분집합 갯수
    for j in range(n):  # 원소수 만큼 비트 비교
        if i & (1 << j):
            bubun_elm.append(arr[j])
    print(bubun_elm)
    bubun_list.append(bubun_elm)
    bubun_elm = []
    # print()
print(bubun_list)