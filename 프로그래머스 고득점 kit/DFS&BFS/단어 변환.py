from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    change_dic = {}
    si_cnt = 0

    for word1 in words + [begin]:
        for word2 in words:
            for i in range(len(word1)):
                if word1[i] == word2[i]:
                    si_cnt += 1
            if si_cnt == len(word1) - 1:
                change_dic[word1] = change_dic.get(word1, []) + [word2]
            si_cnt = 0
    # print(change_dic)

    queue = deque([[begin, 0]])
    visited = set()

    while queue:
        front, degree = queue.popleft()
        degree += 1
        for w in change_dic[front]:
            if w == target:
                return degree
            elif w not in visited and degree < len(words):
                visited.add(w)
                queue.append([w, degree])

    return 0