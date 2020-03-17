import sys
input = sys.stdin.readline


N, S = map(int, input().split())
num_set = list(map(int, input().split()))
# print(num_set)
sum_val = 0
cnt = 0

for num in range(1, 1 << N):
    for i in range(len(format(num, 'b'))):
        if num & (1 << i):
            sum_val += num_set[i]
    if sum_val == S:
        cnt += 1
        # print(temp)
    temp = []
    sum_val = 0

print(cnt)



