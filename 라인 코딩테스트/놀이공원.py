import heapq

def solution(n, k, num_list):
    temp = []
    heapq.heapify(temp)
    for i in range(k):
        heapq.heappush(temp, num_list[i])

    for num in num_list[k:]:
        min_num = heapq.heappop(temp)
        heapq.heappush(temp, num + min_num)

    return max(temp)

# print(solution(5, 2, [4, 3, 5, 2, 8]))
print(solution(8, 4, [5, 4, 2, 3, 5, 7, 8, 9]))