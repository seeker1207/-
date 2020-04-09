
# 처음엔 리스트의 완전검색을 통하여 풀었으나, stack을 통해 풀수도 있다는것을 확인했다.
# 스택에 push 하면서 가장 최근에 푸쉬된 탑의높이와 현재의 탑의높이를 비교한다.
# 현재의 탑의높이가 크면 현재 스택에서 최근에 푸쉬된 탑을 pop 한다.

def solution(heights):
    answer = [0] * len(heights)
    stack = []

    for i in reversed(range(len(heights))):
        while stack and stack[-1][1] < heights[i]:
            idx, height = stack.pop()
            answer[idx] = i + 1
        stack.append((i, heights[i]))

    return answer



# def solution(heights):
#     answer = [0]*len(heights)

#     for idx, height in enumerate(heights):
#         for idx2 in range(idx - 1, -1, -1):
#             if heights[idx2] > height:
#                 answer[idx] = idx2 + 1
#                 break

#     # print(answer)
#     return answer