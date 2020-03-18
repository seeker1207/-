def is_correct(u):
    stack = []
    if u[0] == ')':
        return False

    for br in u:
        if br == ')':
            if not stack:
                return False
            else:
                stack.pop()
        else:
            stack.append(br)

    if not stack:
        return True
    else:
        return False


def change_correct(v):
    left_cnt, right_cnt = 0, 0

    if not v:
        return ""
    for idx, br in enumerate(v):
        if br == '(':
            left_cnt += 1
        else:
            right_cnt += 1
        if left_cnt == right_cnt:
            slice_idx = idx + 1
            break

    u = v[:slice_idx]
    v = v[slice_idx:]

    if is_correct(u):
        return u + change_correct(v)
    else:
        ret = '(' + change_correct(v) + ')'
        u_removed = list(u[1:len(u) - 1])

        for idx, br in enumerate(u_removed):
            if br == '(':
                u_removed[idx] = ')'
            else:
                u_removed[idx] = '('
        ret += ''.join(u_removed)
        return ret


def solution(p):
    answer = ''

    return change_correct(p)