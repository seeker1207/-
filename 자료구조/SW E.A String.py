# # '''
# # 알고리즘 연습
# # String
# # '''
# #
#

# T = int(input())
# string_text = [(input(), input()) for _ in range(T)]
#
# #print(string_text[0][1])
#
# for i in range(T):
#     text = string_text[i][1]
#     pattern = string_text[i][0]
#     text_len = len(string_text[i][1])
#     pattern_len = len(string_text[i][0])
#     skip_array = list(pattern)
#     skip_array.reverse()
#     now_idx = pattern_len - 1
#     result = False
#
#     while now_idx < text_len and not result:
#         if text[now_idx] != pattern[pattern_len - 1]:
#             if text[now_idx] in skip_array:
#                 now_idx += skip_array.index(text[now_idx])
#             else:
#                 now_idx += pattern_len
#
#         else:
#             for j in range(pattern_len):
#                 if text[now_idx - j] == pattern[-(j+1)]:
#                     result = True
#                 else:
#                     result = False
#                     now_idx = now_idx - j
#                     break
#
#     if result:
#         print(f'#{i+1} 1')
#     else:
#         print(f'#{i+1} 0')

# """3일차 - 회문"""
#
#
# def search_palindrome(input_grid):
#     for k in range(len(input_grid)):
#         result = 0
#         pivot = 0
#         while pivot + M <= len(input_grid[k]):
#             if input_grid[k][pivot:pivot + M] == list(reversed(input_grid[k][pivot:pivot + M])):
#                 result = 1
#                 palindrome = input_grid[k][pivot:pivot + M]
#                 return palindrome
#             else:
#                 result = 0
#             pivot += 1
#         if result:
#             break
#
#     return -1
#
#
#
# for i in range(int(input())):
#     N, M = map(int, input().split())
#     grid = [list(input()) for _ in range(N)]
#     grid_transposed = list(map(list, list(zip(*grid))))
#     # for j in range(len(grid)):
#     #     print(grid[j])
#     palindrome_result = search_palindrome(grid)
#     if palindrome_result != -1:
#         print(f'#{i + 1} {"".join(palindrome_result)}')
#     else:
#         print(f'#{i + 1} {"".join(search_palindrome(grid_transposed))}')

for i in range(int(input())):
    N = input()
    M = input()
    dic = {}
    for val in N:
        if val not in dic:
            dic[val] = M.count(val)
    print(dic)
    print(f'#{i+1} {max(list(dic.values()))}')






