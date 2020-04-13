from collections import deque


def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    is_ok = [0] * n
    pg = deque(progresses)
    sp = deque(speeds)

    while pg:
        ok_cnt = 0
        for i in range(len(pg)):
            pg[i] += sp[i]
        # print(list(pg), answer)
        while pg:
            if pg[0] >= 100:
                ok_cnt += 1
                pg.popleft()
                sp.popleft()
            else:
                break

        if ok_cnt:
            answer.append(ok_cnt)

    return answer