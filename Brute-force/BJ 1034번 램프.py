def switch(col):
    for row in range(N):
        T[row][col] = not T[row][col]

def get_on_row():
    is_on = True
    cnt = 0

    for row in range(N):
        for col in range(M):
            if not T[row][col]:
                is_on = False
                break
        cnt = cnt + 1 if is_on else cnt
        is_on = True

    return cnt

def search_max(press_cnt):
    if press_cnt == K:
        return get_on_row()

    max_cnt = 0

    for col in range(M):
        switch(col)
        on_row_cnt = search_max(press_cnt + 1)
        max_cnt = max(max_cnt, on_row_cnt)
        switch(col)

    return max_cnt


N, M = map(int, input().split())
T = [list(map(int, list(input()))) for _ in range(N)]
K = int(input())

print(search_max(0))