from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge_sum = 0
    sec = 0
    tw = deque(truck_weights)
    enter_time = deque([])
    on_bridge = deque([])
    pass_bridge = deque([])

    while len(pass_bridge) != len(truck_weights):
        sec += 1

        if enter_time:
            if sec - enter_time[0] == bridge_length:
                bridge_sum -= on_bridge[0]
                pass_bridge.append(on_bridge.popleft())
                enter_time.popleft()
        if tw:
            if bridge_sum + tw[0] <= weight:
                bridge_sum += tw[0]
                on_bridge.append(tw.popleft())
                enter_time.append(sec)

        # print(pass_bridge, on_bridge, tw, "sec", sec)

    return sec