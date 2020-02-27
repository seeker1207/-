'''
알고리즘 연습
list 2
'''

'리스트 표현'
# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# newlist = [(i,j) for i in range(n) for j in range(m) if mylist[i][j]]
# lslist = [(j,i) for i in range(3) for j in range(5)]
# print(arr)

'리스트 지그재그 탐색'
# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         print(arr[i][j + (m-1-2*j)*(i%2)])

'부분집합 생성'
# arr = [3, 6, 7, 1]
# n = len(arr)
# bubun_list = []
# bubun_elm = []
# for i in range(1 << n):  # 부분집합 갯수
#     for j in range(n):  # 원소수 만큼 비트 비교
#         if i & (1 << j):
#             bubun_elm.append(arr[j])
#     print(bubun_elm)
#     bubun_list.append(bubun_elm)
#     bubun_elm = []
#     # print()
# print(bubun_list)

'2일차. 색칠하기'
# T = int(input())
# grid = [[0]*10 for _ in range(10)]
# print(grid)
# for n in range(T):
#     x1, y1, x2, y2, color = map(int, input().split())
#
#     for i in range(x1, x2+1):
#         for j in range(y1, y2+1):
#             if color == 1 and grid[i][j] == 0:
#                 grid[i][j] += 1
#             elif color == 2 and grid[i][j] == 0:
#                 grid[i][j] += 2
#             else:
#                 grid[i][j] += color
#
# cnt = 0
#
# for k in range(10):
#     for l in range(10):
#         if grid[k][l] >= 3:
#             cnt += 1
#
# for z in range(10):
#     print(grid[z])
# print(cnt)

'2일차. 부분집합의 합'
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# # arr = [1,2,3]
# bubun = []
# bubun_list = []
# n = len(arr)
# cnt = 0
#
# N, K = map(int, input().split())
#
# for i in range(1 << n):
#     for j in range(n):
#         if i & (1 << j):
#             bubun.append(arr[j])
#     # print(bubun, end=" ")
#     if len(bubun) == N and sum(bubun) == K:
#         cnt += 1
#         bubun_list.append(bubun)
#     bubun = []
#
#
# print(bubun_list)
# print(cnt)

'2일차. 이진탐색'
# def binary_search(left, right, goal, cnt=0):
#
#     middle = (left + right) // 2
#
#     if goal == middle:
#         return cnt + 1
#
#     if goal < middle:
#         cnt += 1
#         right = middle
#         cnt = binary_search(left, right, goal, cnt)
#     else:
#         cnt += 1
#         left = middle
#         cnt = binary_search(left, right, goal, cnt)
#
#     return cnt
#
#
# T = int(input())
#
# for i in range(T):
#     P, A, B = map(int, input().split())
#     if binary_search(1, P, B) > binary_search(1, P, A):
#         print(f'#{i+1} A')
#     elif binary_search(1, P, B) < binary_search(1, P, A):
#         print(f'#{i+1} B')
#     else:
#         print(f'#{i+1} 0')
'2일차. 특별한 정렬'

N = int(input())
num_list = list(map(int, input().split()))
sort_list = []
min_num = 101
max_num = 0

for n in range(N):
    if (n+1) % 2 == 1:
        for search_idx in range(n, N):
            if num_list[search_idx] > max_num:
                max_num = num_list[search_idx]
                max_idx = search_idx
        num_list[n], num_list[max_idx] = num_list[max_idx], num_list[n]
        max_num = 0
    else:
        for search_idx in range(n, N):
            if num_list[search_idx] < min_num:
                min_num = num_list[search_idx]
                min_idx = search_idx
        num_list[n], num_list[min_idx] = num_list[min_idx], num_list[n]
        min_num = 101
print(num_list)













