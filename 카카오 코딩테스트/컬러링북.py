
def color_dfs(i, j, visited):
    global m, n
    color = P[i][j]
    cnt = 0
    stack = [(i, j)]

    while stack:
        a, b = stack.pop()
        if 0 <= a < m and 0 <= b < n:
            if color == P[a][b] and not visited[a][b]:
                cnt += 1
                visited[a][b] = 1
                stack.append((a+1, b))
                stack.append((a, b+1))
                stack.append((a, b-1))
                stack.append((a-1, b))

    return cnt

def find_area():
    visited = [[0]*n for _ in range(m)]
    area_cnt = 0
    max_area = 0
    for i in range(m):
        for j in range(n):
            if P[i][j] != 0 and not visited[i][j]:
                area_cnt += 1
                max_area = max(max_area, color_dfs(i, j, visited))

    return area_cnt, max_area


# m, n = map(int, input().split())
# P = [list(map(int, input().split())) for _ in range(m)]
m, n = 13, 16
P = [[0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0], [0, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 3, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 3, 1, 0], [0, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 0], [0, 0, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]]
print(find_area())


