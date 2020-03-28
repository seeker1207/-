def is_identified(relation, r_idx):

    tpl_list = []
    for tpl in relation:
        tpl_list.append([tpl[r] for r in r_idx])
    # print(tpl_list)
    for tpl_idx in range(len(tpl_list)):
        fixed_val = tpl_list[tpl_idx]
        for tpl2 in tpl_list[tpl_idx+1:]:
            if tpl2 == fixed_val:
                # print("f")
                return False
    # print("t")
    return True

def solution(relation):
    answer = 0
    n = len(relation[0])
    row_idx = []
    candidate_cnt = 0
    candidate_list = []
    for i in range(1, 1 << n):
        for j in range(len(format(i, 'b'))):
            if i & (1 << j):
                row_idx.append(j)
        # print(row_idx)
        if is_identified(relation, row_idx):
            if len(row_idx) == 1:
                candidate_list.append(row_idx)
            else:
                is_min = True
                for candidate in candidate_list:
                    if set(candidate).issubset(set(row_idx)):
                        is_min = False
                        break
                    else:
                        # print(candidate, row_idx)
                        is_min = True

                if is_min:
                    candidate_list.append(row_idx)
        row_idx = []

    return len(candidate_list)


# 다른 사람들의 풀이 훨씬 간결하고
# 부분집합인지 확인하는 부분이 인상깊다.
def solution(relation):
    answer_list = list()
    for i in range(1, 1 << len(relation[0])):
        tmp_set = set()
        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                if i & (1 << k):
                    tmp += str(relation[j][k])
            tmp_set.add(tmp)

        if len(tmp_set) == len(relation):
            not_duplicate = True
            for num in answer_list:
                if (num & i) == num:    # 부분집합인지 확인할때 and 로 자기자신이 나오는지 확인함으로써 체크할수있다.
                    not_duplicate = False
                    break
            if not_duplicate:
                answer_list.append(i)
    return len(answer_list)