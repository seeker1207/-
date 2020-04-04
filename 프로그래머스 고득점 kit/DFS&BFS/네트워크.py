from collections import defaultdict


def solution(n, computers):
    stack = [0]
    visited = set()
    adj = [set() for _ in range(n)]

    for i, com in enumerate(computers):
        for j, b in enumerate(com):
            if b and i != j:
                adj[i].add(j)
    net_cnt = 0

    while True:
        while stack:
            top = stack.pop()
            if top not in visited:
                visited.add(top)
                stack.extend(adj[top] - visited)

        net_cnt += 1
        if len(visited) == n:
            break

        for i in range(n):
            if i not in visited:
                stack = [i]
                break

    return net_cnt