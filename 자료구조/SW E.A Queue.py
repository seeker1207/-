"""
알고리즘 연습
Queue

"""

""" 6일차 - 회전 """

# for i in range(int(input())):
#     N, M = map(int, input().split())
#     num_list = list(map(int, input().split()))
#
#     for _ in range(M):
#         num_list.append(num_list.pop(0))
#
#     print(f'#{i+1} {num_list[0]}')

""" 6일차 - 미로의 거리 """
#
# def is_okay(input_now):
#     global N
#     global visit
#     y, x = input_now[0], input_now[1]
#     return 0 <= y < N and 0 <= x < N and visit[y][x] == 0 and maze[y][x] != '1'
#
#
# for i in range(int(input())):
#     N = int(input())
#     maze = []
#     for j in range(N):
#         maze.append(input())
#         if '3' in maze[j]:
#             goal = (j, maze[j].index('3'))
#         elif '2' in maze[j]:
#             start = (j, maze[j].index('2'))
#
#     visit = [[0] * N for _ in range(N)]
#     distance = [[0] * N for _ in range(N)]
#     Q = [start]
#     visit[start[0]][start[1]] = 1
#     move_list = [(0, -1), (-1, 0), (0, 1), (1, 0)]
#     arrive_flag = False
#
#     while Q:
#         now = Q.pop(0)
#         if now == goal:
#             arrive_flag = True
#             min_distance = distance[now[0]][now[1]]
#             break
#         for move in move_list:
#             search_tpl = tuple(sum(moved_tpl) for moved_tpl in zip(now, move))
#             if is_okay(search_tpl):
#                 Q.append(search_tpl)
#                 visit[search_tpl[0]][search_tpl[1]] = 1
#                 distance[search_tpl[0]][search_tpl[1]] = distance[now[0]][now[1]]+1
#
#     if arrive_flag:
#         print(f'#{i+1} {min_distance-1}')
#     else:
#         print(f'#{i+1} 0')

# """ 6일차 - 피자 굽기 """
# def plus_one(x):
#     if isinstance(x, list):
#         return [x[0], x[1], x[2]+1]
#     else:
#         return x
#
# for i in range(int(input())):
#     N, M = map(int, input().split())
#     C = list(map(int, input().split()))
#     oven = [[C.pop(0), i, 0]for i in range(N)]
#     idx_cnt = N
#
#     while oven.count("empty") != N - 1:
#         while oven[0][0] != 0:
#             first = oven.pop(0)
#             oven.append(first)
#             oven = list(map(plus_one, oven))
#             for pizza in oven:
#                 if isinstance(pizza, list):
#                     if pizza[2] % N == 0:
#                         pizza[0] //= 2
#         if C:
#             oven[0] = [C.pop(0), idx_cnt, 0]
#             idx_cnt += 1
#         else:
#             oven[0] = "empty"
#
#     for oven_elm in oven:
#         if isinstance(oven_elm, list):
#             print(f'가장 마지막까지 남아있던 피자는 {oven_elm[1] + 1}번 피자입니다.')

""" 6일차 - 노드의 거리 """

for i in range(int(input())):
    V, E = map(int, input().split())
    visit = [0 for _ in range(V)]
    E_list = [[0 for _ in range(V)] for _ in range(V)]

    for j in range(E):
        s, g = map(int, input().split())
        E_list[s-1][g-1] = 1
        E_list[g-1][s-1] = 1

    S, G = map(int, input().split())
    Q = [S-1]
    visit[S-1] = 1
    distance = [0]*V
    distance[S-1] = 0

    while Q and not visit[G-1]:
        now = Q.pop(0)
        for k in range(V):
            if E_list[now][k] and not visit[k]:
                Q.append(k)
                visit[now] = 1
                visit[k] = 1
                distance[k] = distance[now] + 1

    print(f'#{i+1} {distance[G-1]}')




