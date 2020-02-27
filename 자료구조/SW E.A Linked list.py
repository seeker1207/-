"""
알고리즘 연습
liked list

"""

""" 링크리스트 구현 """

class Node:
    def __init__(self, num):
        self.num = num
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_first(self, data):
        if not self.head:
            self.head = Node(data)
            self.tail = Node(data)
            return
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_to_last(self, data):
        if not self.head:
            self.head = Node(data)
            self.tail = self.head
            return
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

    def add(self, seq, data):
        new_node = Node(data)
        current_node = self.head
        if seq == 0:
            self.add_to_first(data)
        else:
            for i in range(seq):
                previous_node = current_node
                current_node = current_node.next
            previous_node.next = new_node
            new_node.next = current_node

    def add_sum_seq(self, seq, k):
        current_node = self.head
        for i in range(k):
            for j in range(seq):  # head 부터 seq 값만큼 다음 노드를 탐색
                previous_node = current_node
                if current_node != self.tail:
                    current_node = current_node.next
                else:   # 연결리스트의 끝이면 맨앞노드부터 다시 시작
                    current_node = self.head
            # 탐색된 노드 앞에 새로운노드를 추가하고 앞의숫자와 뒤의숫자를 더한 데이터를 입력
            new_node = Node(previous_node.num + current_node.num)
            previous_node.next = new_node
            # 만약 이전 노드가 tail 이라면 연결리스트 끝에 새 노드를 추가하고 tail 을 새노드로 변경
            if previous_node == self.tail:
                self.tail = new_node
                current_node = new_node
            else:
                new_node.next = current_node
                current_node = new_node
        # 이 과정을 k만큼 반복

    def add_list(self, node_list):
        current = self.head
        seq = 0
        while current:
            if current.num > node_list[0]:
                for idx in range(len(node_list)-1, -1, -1):
                    self.add(seq, node_list[idx])
                return
            current = current.next
            seq += 1

        for idx, val in enumerate(node_list):
            self.add_to_last(val)

    def delete(self, seq):
        if seq == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(seq):
            previous_node = current
            current = current.next
        previous_node.next = current.next

    def change(self, seq, new_num):
        current = self.head
        for _ in range(seq):
            current = current.next
        current.num = new_num

    def print_data(self):
        current = self.head
        while current:
            print(current.num, end=" ")
            current = current.next
        print()

    def print_data_reverse(self):
        current = self.head
        num_list = []
        while current:
            num_list.append(current.num)
            current = current.next
        num_list.reverse()
        if len(num_list) >= 10:
            print(" ".join(map(str, num_list[:10])))
        else:
            print(" ".join(map(str, num_list)))

    def print_data_10(self):
        current = self.head
        print_list = []
        while current:
            print_list.append(current.num)
            current = current.next
        for k in range(-1, -11, -1):
            print(f'{print_list[k]}', end=" ")


""" 7일차 - 숫자 추가 """

# for i in range(int(input())):
#     N, M, L = map(int, input().split())
#     num_list = list(map(int, input().split()))
#     linked_list = LinkedList(num_list[0])
#
#     for j in range(1, len(num_list)):
#         linked_list.add_to_last(num_list[j])
#
#     for k in range(M):
#         linked_list.add(*map(int, input().split()))
#
#     current = linked_list.head
#     for l in range(L):
#         current = current.next
#     print(f'#{i} {current.num}')


""" 7일차 - 수열 합치기"""

# for i in range(int(input())):
#     N, M = map(int, input().split())
#     lnk_list = LinkedList()
#     num_list = list(map(int, input().split()))
#
#     for num in num_list:
#         lnk_list.add_to_last(num)
#     lnk_list.print_data()
#
#     for j in range(M-1):
#         num_list2 = list(map(int, input().split()))
#         lnk_list.add_list(num_list2)
#         # lnk_list.print_data()
#
#     print(f'#{i+1}', end=" ")
#     lnk_list.print_data_10()
#     print()

""" 7일차 - 암호 """

# for i in range(int(input())):
#     N, M, K = map(int, input().split())
#     initial_list = list(map(int, input().split()))
#
#     lnk_list = LinkedList()
#     for num in initial_list:
#         lnk_list.add_to_last(num)
#
#     lnk_list.add_sum_seq(M, K)
#     print(f'#{i+1}', end=" ")
#     lnk_list.print_data_reverse()

""" 7일차 - 수열편집 """

for i in range(int(input())):
    N, M, L = map(int, input().split())
    initial_list = list(map(int, input().split()))
    lnk_list = LinkedList()

    for num in initial_list:
        lnk_list.add_to_last(num)

    order_switch = {
        'I': lnk_list.add,
        'D': lnk_list.delete,
        'C': lnk_list.change
    }

    for _ in range(M):
        order = input().split()
        if len(order) == 2:
            order_switch[order[0]](int(order[1]))
            # lnk_list.print_data()
        else:
            order_switch[order[0]](int(order[1]), int(order[2]))
            # lnk_list.print_data()

    current = lnk_list.head
    for _ in range(L):
        if not current:
            break
        current = current.next

    if current:
        print(f'#{i+1} {current.num}')
    else:
        print(f'#{i+1} -1')



















