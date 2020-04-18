def solution(arrangement):
    stack = [arrangement[0]]
    idx = 1
    cur = 1
    sum_cnt = 0
    # print(stack)
    while len(arrangement) != idx:
        br = arrangement[idx]
        pre_br = arrangement[idx - 1]
        if br == "(":
            stack.append(br)
            cur += 1
        elif br == ")" and pre_br == "(":
            stack.pop()
            cur -= 1
            sum_cnt += cur
        elif br == ")" and pre_br == ")":
            stack.pop()
            sum_cnt += 1
            cur -= 1
        else:
            stack.pop()
        # print(stack, cur, sum_cnt)
        idx += 1

    return sum_cnt