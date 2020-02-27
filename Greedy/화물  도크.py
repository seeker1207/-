for i in range(int(input())):
    container, truck = map(int, input().split())
    weight_list = list(map(int, input().split()))
    truck_weights = list(map(int, input().split()))

    sum = 0
    weight_list.sort()
    weight_list.reverse()
    print(weight_list)
    for weight in weight_list:
        for idx, truck_weight in enumerate(truck_weights):
            if weight <= truck_weight:
                truck_weights.pop(idx)
                sum += weight
                break
        if not truck_weights:
            break
    print(f'#{i+1} {sum}')

    
