
def grid_traverse(x=0, y=0, min_sum=0):
    global N, grid, result
    if x == N-1 and y == N-1:
        min_sum += grid[y][x]
        result = min(result, min_sum)
        return

    if x < N and y < N:
        min_sum += grid[y][x]
        grid_traverse(x+1, y, min_sum)
        grid_traverse(x, y+1, min_sum)
    else:
        return

for i in range(int(input())):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    print(grid)
    result = 5000
    grid_traverse()
    print(f'#{i+1} {result}')
