"""Stack 자료구조"""

"""4일차 - 종이 붙이기"""

# for i in range(int(input())):
#     N = int(input())
#     n = N // 10 - 2
#     DP = [1, 3]
#
#     for j in range(n):
#         DP.append(2*DP[j] + DP[j + 1])
#
#     print(f'#{i+1} {DP.pop(-1)}')


"""4일차 - 괄호검사"""


# def check_bracket(input_text):
#
#     bracket_stack = []
#
#     for st in input_text:
#         if st == '{' or st == '(':
#             bracket_stack.append(st)
#         elif st == '}':
#             if not bracket_stack:
#                 return 0
#             elif bracket_stack[-1] == '{':
#                 bracket_stack.pop(-1)
#             else:
#                 return 0
#         elif st == ')':
#             if not bracket_stack:
#                 return 0
#             if bracket_stack[-1] == '(':
#                 bracket_stack.pop(-1)
#             else:
#                 return 0
#
#     if not bracket_stack:
#         return 1
#     else:
#         return 0
#
#
# for i in range(int(input())):
#     text = input()
#     result = check_bracket(text)
#     print(f'#{i+1} {result}')

""" 4일차 - 그래프 경로 """

# for i in range(int(input())):
#     V, E = map(int, input().split())
#
#     path_grid = [[0 for _ in range(V)] for _ in range(V)]
#     visit = [0 for _ in range(V)]
#     stack = []
#
#     for j in range(E):
#         X, Y = map(int, input().split())
#         path_grid[X-1][Y-1] = 1
#
#     # for k in range(V):
#     #     print(path_grid[k])
#
#     S, G = map(int, input().split())
#     now = S - 1
#     # stack.append(S - 1)
#
#     while now != G - 1:
#         for idx, val in enumerate(path_grid[now]):
#             if val == 1 and not visit[idx]:
#                 visit[idx] = 1
#                 stack.append(now)
#                 now = idx
#                 flag = True
#                 break
#             flag = False
#
#         if flag:
#             continue
#
#         if stack:
#             now = stack.pop()
#         else:
#             break
#
#     if flag:
#         print(f'#{i + 1} 1')
#     else:
#         print(f'#{i + 1} 0')

""" 4일차 - 반복문자 지우기 """

for i in range(int(input())):
    str_list = list(input())
    stack = []
    idx = 0

    for idx in range(len(str_list)):
        if stack:
            if stack[-1] == str_list[idx]:
                stack.pop()
                idx += 1
                continue

        stack.append(str_list[idx])
        idx += 1
    print("".join(stack))
    print(f'#{i+1} {len(stack)}')



