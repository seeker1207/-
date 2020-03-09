
# 삼각형 위의 최대경로의 합(최대값)을 찾는 문제.
def find_path(y, x, row):

    if y > N-1 or x > row:
        return 0

    if cache[y][x] != -1: return cache[y][x]

    cache[y][x] = max(find_path(y+1, x, row+1), find_path(y+1, x+1, row+1)) + grid[y][x]

    return cache[y][x]


N = int(input())
grid = [list(map(int, input().split()))for _ in range(N)]
cache = [[-1]*N for _ in range(N)]
# print(cache)
print(find_path(0, 0, 0))
# print(grid)

