import copy


def rotate(key, m):
    rotate_key = [[-1] * m for _ in range(m)]

    for n in range(m):
        for i in range(m):
            rotate_key[n][i] = key[m - 1 - i][n]

    return rotate_key


def is_fit(st_i, st_j, m, n, key, extnd_lock):
    result = copy.deepcopy(extnd_lock)

    for i in range(m):
        for j in range(m):
            if result[st_i + i][st_j + j] == -1:
                continue
            elif result[st_i + i][st_j + j] + key[i][j] == 1:
                result[st_i + i][st_j + j] = 1
            else:
                return False

    for k in range(n):
        for l in range(n):
            if result[n + k][n + l] != 1:
                return False

    return True


def solution(key, lock):
    # answer = True
    m = len(key)
    n = len(lock)
    extnd_lock = [[-1] * n * 3 for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            extnd_lock[n + i][n + j] = lock[i][j]

    for _ in range(4):
        for k in range(1, n * 2):
            for l in range(1, n * 2):
                if is_fit(k, l, m, n, key, extnd_lock):
                    return True
        key = rotate(key, m)

    return False