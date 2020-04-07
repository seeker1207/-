from collections import deque

def catch_me(c, b):
    queue = deque([[c, b, 0]])

    while queue:
        cony, brown, pre_move = queue.popleft()
        if cony == brown:
            return pre_move
        pre_move += 1
        cony += pre_move
        if 0 < cony < 200000 and 0 < brown < 200000:
            queue.append([cony, brown - 1, pre_move])
            queue.append([cony, brown + 1, pre_move])
            queue.append([cony, brown * 2, pre_move])

    return -1


print(catch_me(6, 3))
