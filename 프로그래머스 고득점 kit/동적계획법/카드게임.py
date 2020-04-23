# cache[a][b] : 왼쪽 카드 더미의 가장 윗 카드의 인덱스가 a인 카드이고,
#               오른쪽 카드 더미의 가장 윗 카드의 인덱스가 b일 때의 점수의 최대값

def solution(left, right):
    answer = 0
    cache = [[-1] * (len(left) + 1) for _ in range(len(right) + 1)]
    cache[0][0] = 0
    result_list = []
    ret = False
    for i in range(1, len(left)):
        if left[i] <= right[i]:
            ret = True
        else:
            ret = False
            break
    if ret:
        return 0

    for i in range(1, len(left) + 1):
        cache[i][0] = 0

    for i, n in enumerate(right, start=1):
        if left[0] > n:
            cache[0][i] = cache[0][i - 1] + n
        else:
            break_point = i
            break

    for i in range(break_point, len(right) + 1):
        cache[0][i] = 0

    result = max(cache[0])

    for i in range(1, len(left) + 1):
        for j in range(1, len(right) + 1):
            if i == len(left) and j == len(right):
                cache[i][j] = cache[i - 1][j - 1]
            elif i == len(left) and j != len(right):
                cache[i][j] = max(cache[i - 1][j], cache[i - 1][j - 1])
            elif i != len(left) and j == len(right):
                if left[i] > right[j - 1]:
                    cache[i][j] = max(cache[i - 1][j - 1], cache[i][j - 1] + right[j - 1])
                else:
                    cache[i][j] = cache[i - 1][j - 1]
            else:
                temp = max(cache[i - 1][j], cache[i - 1][j - 1])
                if left[i] > right[j - 1]:
                    max_val = max(temp, cache[i][j - 1] + right[j - 1])
                else:
                    max_val = temp
                cache[i][j] = max_val

            if i == len(left) or j == len(left):
                result = max(result, cache[i][j])
                result_list.append(cache[i][j])
                max_val = 0

    # print(result_list)
    # print(cache)
    return result