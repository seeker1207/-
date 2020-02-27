"""
알고리즘 연습
Stack 2

"""

""" 5일차 - Forth """

# T = int(input())
#
# for i in range(T):
#     eqn = list(input().split())
#     stack = []
#
#     for st in eqn:
#         if st.isdigit():
#             stack.append(st)
#         elif not stack or (len(stack) == 1 and st != '.'):
#             print(f'#{i+1} error')
#             break
#         elif st == '.':
#             if len(stack) != 1:
#                 print(f'#{i+1} error')
#                 break
#             else:
#                 print(f'#{i+1} {stack.pop()}')
#         else:
#             operand1 = int(stack.pop())
#             operand2 = int(stack.pop())
#             if st == '+':
#                 stack.append(operand2 + operand1)
#             elif st == '-':
#                 stack.append(operand2 - operand1)
#             elif st == '*':
#                 stack.append(operand2 * operand1)
#             elif st == '/':
#                 stack.append(operand2 // operand1)

""" 5일차 - 미로 """
# import copy
#
# def move_candidate(move_type_input, move_origin):
#     candidate_list = copy.deepcopy(move_origin)
#     for k in range(move.index(move_type_input)+1):
#         candidate_list.pop(0)
#
#     return candidate_list
#
# for i in range(int(input())):
#     N = int(input())
#     maze = []
#     zero_count = 0
#     for j in range(N):
#         maze.append(input())
#         if '2' in maze[j]:
#             start = (j, maze[j].index('2'))
#         elif '3' in maze[j]:
#             arrival = (j, maze[j].index('3'))
#         if '0' in maze[j]:
#             zero_count += maze[j].count('0')
#     move = [(0, -1), (-1, 0), (0, 1), (1, 0)]
#     stack = []
#     visit = [[0]*N for _ in range(N)]
#     visit[start[0]][start[1]] = 1
#     now = start
#     move_list = move
#     visit_count = 0
#     arrival_flag = True
#
#     while now != arrival and arrival_flag:
#         for idx, move_type in enumerate(move_list):
#             prior = now
#             now = tuple(sum(elm) for elm in zip(now, move_type))
#             map(int, now)
#             if now[0] < 0 or now[0] >= N or now[1] < 0 or now[1] >= N:
#                 now = prior
#                 pass_flag = False
#             elif maze[now[0]][now[1]] == '1'or visit[now[0]][now[1]] == 1:
#                 now = prior
#                 pass_flag = False
#             else:
#                 stack.append((prior, move_type))
#                 visit[now[0]][now[1]] = 1
#                 visit_count += 1
#                 pass_flag = True
#                 move_list = move
#                 break
#         if not pass_flag:
#             visit[now[0]][now[1]] = 0
#             if visit[start[0]][start[1]] == 0:
#                 arrival_flag = False
#                 continue
#             move_pop = stack.pop()
#             now = move_pop[0]
#             move_list = move_candidate(move_pop[1], move)
#             pass_flag = False
#
#     if arrival_flag:
#         print("도착완료")
#     else:
#         print("도착실패")

""" 5일차 - 토너먼트 카드게임 """
#
# def binary_tournament(start, end, RSP_list):
#
#     if len(RSP_list[start - 1:end]) == 1:
#         return RSP_list[start - 1], start
#     middle = (start + end) // 2
#     # divided_list1 = RSP_list[start - 1:middle]
#     # divided_list2 = RSP_list[middle:end]
#
#     rsp_value1, winner1 = binary_tournament(start, middle, RSP_list)
#     rsp_value2, winner2 = binary_tournament(middle+1, end, RSP_list)
#
#     if (rsp_value1 == 1 and rsp_value2 ==3) or (rsp_value1 == 2 and rsp_value2 == 1)\
#             or (rsp_value1 == 3 and rsp_value2 == 2):
#         return rsp_value1, winner1
#     elif (rsp_value2 == 1 and rsp_value1 == 3) or (rsp_value2 == 2 and rsp_value1 == 1)\
#             or (rsp_value2 == 3 and rsp_value1 == 2):
#         return rsp_value2, winner2
#     else:
#         if min(winner1, winner2) == winner1:
#             return rsp_value1, winner1
#         else:
#             return rsp_value2, winner2
#
# for i in range(int(input())):
#     N = int(input())
#     student_list = list(map(int, input().split()))
#     rsp_value, winner = binary_tournament(1, len(student_list), student_list)
#     print(f'#{i+1} {winner}')

""" 5일차 - 배열 최소 합 """
MIN = 100

def find_min_search(input_N, input_row, input_list, input_check, input_sum):

    global MIN
    if input_row == N:
        if input_sum < MIN:
            MIN = input_sum
        return
    if input_sum > MIN:
        return

    for j in range(N):
        if not check[j]:
            check[j] = True
            input_sum += input_list[input_row][j]
            find_min_search(N, input_row+1, input_list, check, input_sum)
            check[j] = False
            input_sum -= input_list[input_row][j]

    return MIN


for i in range(int(input())):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    sum_num = 0
    check = [False]*N
    find_min_search(N, 0, num_list, check, 0)
    print(f'#{i+1} {MIN}')
    MIN = 100





















