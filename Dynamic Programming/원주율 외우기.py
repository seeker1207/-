C = int(input())


# num_list[a:b]의 난이도를 반환.
def classify(a, b):
    S = num_list[a:b]
    if S == [S[0]] * len(S):
        return 1

    progressive = True
    for i in range(len(S)-1):
        if S[i + 1] - S[i] != S[1] - S[0]:
            progressive = False
            break

    if progressive and abs(S[1] - S[0]) == 1:
        return 2

    alternating = True
    for j in range(len(S)):
        if S[j] != S[j % 2]:
            alternating = False

    if alternating: return 4
    if progressive: return 5
    return 10


def find_pi_difficulty(num_idx):
    global num_list, cache

    if num_idx == len(num_list): return 0
    if cache[num_idx] != -1:
        return cache[num_idx]

    ret = float('inf')

    for incrs in range(3, 6):
        if num_idx + incrs <= len(num_list):
            ret = min(ret, find_pi_difficulty(num_idx + incrs) \
                      + classify(num_idx, num_idx + incrs))

    return ret

for c in range(C):
    num_list = list(map(int, input()))
    cache = [-1] * (len(num_list) + 1)
    print(find_pi_difficulty(0))