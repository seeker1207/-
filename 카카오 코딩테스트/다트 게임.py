import re

bonus = {'S': lambda x: x, 'D': lambda x: x * x, 'T': lambda x: x * x * x}


def solution(dartResult):
    dart_result_list = re.findall('(\d+)([SDT])([*#]?)', dartResult)
    print(dart_result_list)
    score = []

    for idx, val in enumerate(dart_result_list):
        s, b, o = int(val[0]), val[1], val[2]
        print(s, b, o)
        if not o:
            score.append(bonus[b](s))
        elif o[0] == '*':
            if idx == 0:
                score.append(bonus[b](s) * 2)
            else:
                score[idx - 1] *= 2
                score.append(bonus[b](s) * 2)
        elif o[0] == '#':
            score.append(bonus[b](s) * -1)

    return sum(score)