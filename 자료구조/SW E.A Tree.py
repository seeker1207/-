"""
알고리즘 연습
Tree

"""

""" 8일차 - subtree """

# def traverse(root_node):
#     global tree
#     global cnt
#     cnt += 1
#     if tree[0][root_node]:
#         traverse(tree[0][root_node])
#     if tree[1][root_node]:
#         traverse(tree[1][root_node])
#
#
# for i in range(int(input())):
#     E, N = map(int, input().split())
#     e_list = list(map(int, input().split()))
#
#     tree = [[0]*(E+2) for _ in range(2)]
#     e = []
#     e_tpl_list = [e_list[j:j+2] for j in range(0, len(e_list), 2)]
#     # print(e_tpl_list)
#     cnt = 0
#     for parent, child in e_tpl_list:
#         if not tree[0][parent]:
#             tree[0][parent] = child
#         else:
#             tree[1][parent] = child
#
#     traverse(N)
#     # print(tree)
#     print(f'#{i+1} {cnt}')

# """ 8일차 - 이진탐색"""
#
# def make_complete_binary_tree(node_idx):
#     global tree
#     global idx_cnt
#
#     if node_idx > len(tree)-1:
#         return
#
#     next_node_idx = node_idx * 2
#     make_complete_binary_tree(next_node_idx)
#     idx_cnt += 1
#     tree[node_idx] = idx_cnt
#     make_complete_binary_tree(next_node_idx+1)
#
#
# for i in range(int(input())):
#     N = int(input())
#     tree = [0]*(N+1)
#     idx_cnt = 0
#     make_complete_binary_tree(1)
#     print(f"#{i+1} {tree[1]} {tree[N//2]}")
#

""" 8일차 - 이진 힙 """

# for i in range(int(input())):
#     N = int(input())
#     num_list = list(map(int, input().split()))
#     tree = [0]
#     for num in num_list:
#         tree.append(num)
#         new_idx = len(tree)-1
#         while new_idx != 1:
#             parent_idx = new_idx//2
#             if tree[new_idx] < tree[parent_idx]:
#                 tree[new_idx], tree[parent_idx] = tree[parent_idx], tree[new_idx]
#                 new_idx = parent_idx
#             else:
#                 break
#     # print(tree)
#     now_idx = len(tree) - 1
#     sum_val = 0
#     while now_idx != 1:
#         now_idx = now_idx // 2
#         sum_val += tree[now_idx]
#
#     print(f'#{i+1} {sum_val}')

""" 8일차 - 노드의 합 """

def post_order_traversal_insert(tree_idx):

    if tree_idx <= len(T) - 1:
        if T[tree_idx]:
            return T[tree_idx]
    if tree_idx > len(T)-1:
        return 0

    left_val = post_order_traversal_insert(tree_idx*2)
    right_val = post_order_traversal_insert(tree_idx*2+1)

    T[tree_idx] = left_val + right_val
    return T[tree_idx]


for i in range(int(input())):
    N, M, L = map(int, input().split())
    T = [0]*(N+1)
    for _ in range(M):
        idx, num = map(int, input().split())
        T[idx] = num
    # print(T)
    post_order_traversal_insert(1)
    print(f'# {i+1} {T[L]}')

