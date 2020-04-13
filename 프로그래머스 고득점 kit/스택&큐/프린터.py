from collections import deque

def solution(priorities, location):
    answer = 0
    prior_dic = {}

    for idx, p in enumerate(priorities):
        prior_dic[idx] = p

    queue = deque([i for i in range(len(priorities))])
    print_cnt = 0
    is_print = False

    while queue:
        front = queue.popleft()
        for key in prior_dic:
            if key != front and prior_dic[front] < prior_dic[key]:
                queue.append(front)
                is_print = False
                break
            else:
                is_print = True
        # print(queue)
        if is_print:
            print_cnt += 1
            prior_dic.pop(front)
            if front == location:
                return print_cnt

    return answer