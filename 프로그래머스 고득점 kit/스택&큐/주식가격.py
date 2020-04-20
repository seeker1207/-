def solution(prices):
    answer = [-1] * (len(prices))
    stack_dic_list = []
    prices += [float('-inf')]

    for sec, price in enumerate(prices, start=1):
        if price == float('-inf'):
            sec -= 1
        while stack_dic_list and stack_dic_list[-1]['p'] > price:
            ret_dic = stack_dic_list.pop()
            answer[ret_dic['enter_T'] - 1] = sec - ret_dic['enter_T']
            # print(stack_dic_list, answer)

        dic = {'p': price, 'enter_T': sec}
        stack_dic_list.append(dic)
        # print(stack_dic_list, answer)

    return answer