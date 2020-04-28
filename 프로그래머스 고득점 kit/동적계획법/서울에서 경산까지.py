# cache[i][k] 구간i를 거쳤을때 시간이 k인경우 모을수 있는 모금액의 최대값
# cache[i][k] = cache[i-1][k-t1] + v1, cache[i-1][k-t2] + v2

def solution(K, travel):
    answer = 0
    cache = [[0] * (K + 1) for _ in range(len(travel) + 1)]
    start_t = 0

    for i in range(1, len(travel) + 1):
        for k in range(0, K + 1):

            walk_t, walk_v = travel[i - 1][0], travel[i - 1][1]
            bicycle_t, bicycle_v = travel[i - 1][2], travel[i - 1][3]

            if walk_t <= k and i == 1:
                cache[i][k] = cache[i - 1][k - walk_t] + walk_v
            if walk_t <= k and i > 1 and cache[i - 1][k - walk_t]:
                cache[i][k] = cache[i - 1][k - walk_t] + walk_v

            if bicycle_t <= k and i == 1:
                cache[i][k] = max(cache[i][k], cache[i - 1][k - bicycle_t] + bicycle_v)
            if bicycle_t <= k and i > 1 and cache[i - 1][k - bicycle_t]:
                cache[i][k] = max(cache[i][k], cache[i - 1][k - bicycle_t] + bicycle_v)

    answer = cache[len(travel)][K]

    return answer