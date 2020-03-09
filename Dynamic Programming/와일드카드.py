
def match(w, s):
    global W, S, memo
    if memo[w][s] != -1:
        return memo[w][s]

    if w < len(W) and s < len(S) and (W[w] == '?' or W[w] == S[s]):
        memo[w][s] = match(w+1, s+1)
        return memo[w][s]

    if w == len(W):
        if s == len(S):
            memo[w][s] = 1
            return 1
        else:
            memo[w][s] = 0
            return 0

    if W[w] == '*':
        if match(w+1, s) or (s < len(S) and match(w, s+1)):
            memo[w][s] = 1
            return memo[w][s]

    memo[w][s] = 0
    return 0


T = int(input())
for t in range(T):
    W = input()
    S_num = int(input())
    S_list = [input() for _ in range(S_num)]
    # print(S_list)
    for S in S_list:
        memo = [[-1] * 102 for _ in range(101)]
        if match(0, 0):
            print(S)