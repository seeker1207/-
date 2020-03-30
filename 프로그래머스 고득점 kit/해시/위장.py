def solution(clothes):
    dic = {}
    answer = 1

    for cloth in clothes:
        cloth_name, cloth_kind = cloth[0], cloth[1]
        dic[cloth_kind] = dic.get(cloth_kind, 0) + 1

    for val in dic.values():
        answer *= (val + 1)

    return answer - 1