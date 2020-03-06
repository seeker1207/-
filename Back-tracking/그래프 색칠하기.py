

def is_possible(color_val, node):
    is_ok = True
    # 현재 노드와 인접한 노드들중 색칠하려고 하는 색과 같은 색이 있는지 확인.
    for idx, g in enumerate(G[node][:(node+1)]):
        if g:
            if color_val == vcolor[idx]:
                is_ok = False
                break

    return is_ok

# dfs로 그래프를 순환하며 찾는 방법 but, 시간초과
# def can_color(now, cnt):
#     global N, E, M, visited, vcolor
#     ret = 0
#     if cnt == N:
#         return 1
#
#     # 2노드 부터 N 까지 반복
#     for n in range(1, N+1):
#         # 방문하지 않은 노드와 인접노드만 허용
#         if not visited[n] and G[now][n]:
#             # 색을 하나씩 넣어보며 가능성을 확인
#             for color in range(1, M+1):
#                 if is_possible(color, n):
#                     visited[n] = 1
#                     vcolor[n] = color
#                     ret = can_color(n, cnt+1)
#                     # 하나라도 M개로 칠할수 있는 케이스가 나타나면 바로 RETURN.
#                     if ret: return 1
#                     visited[n] = 0
#                     vcolor[n] = 0
#
#     return ret

# 색칠하는 순서는 상관없으므로 하나도 색칠되지 않은상태에서 노드 하나씩 색칠해보며 조합을 구해보는 방법.
def can_color(node):
    global N, E, M, G
    if node > N:
        return 1

    # 모든 색에 대해 가능성을 조사한다.
    for color in range(1, M+1):
        if is_possible(color, node):  # 해당 노드에 색을 칠할수 있는지?
            vcolor[node] = color
            if can_color(node+1):  # 하나의 케이스가 M개의 색으로 색을 칠할수 있었다면 바로 RETURN
                return 1
            vcolor[node] = 0

    return 0



T = int(input())

for t in range(T):
    N, E, M = map(int, input().split())
    G = [[0]*(N+2) for _ in range(N+1)]
    for _ in range(E):
        y, x = map(int, input().split())
        G[y][x] = 1
        G[x][y] = 1
    visited = [0] * (N+1)
    visited[1] = 1
    vcolor = [0] * (N+1)
    # vcolor[1] = 1
    print(f'#{t+1} {can_color(1)}')