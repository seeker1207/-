
N, M = map(int, input().split())
T = [input() for _ in range(N)]
K = int(input())
dic = {}

for row in T:
    dic[row] = dic.get(row, 0) + 1

max_cnt = 0
max_row = []

for row in dic.keys():
    off_cnt = list(row).count('0')
    row_cnt = dic[row]
    if off_cnt <= K \
            and row_cnt > max_cnt and K%2 == off_cnt%2:
        max_cnt = dic[row]
        max_row = row

print(max_cnt)