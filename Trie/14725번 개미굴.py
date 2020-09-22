class Node:
    def __init__(self):
        self.depth = 0
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node()
        self.depth = 0

    def add(self, foods):
        cur = self.head
        depth = 0
        for food in foods:
            if food not in cur.child:
                cur.child[food] = Node()
            cur = cur.child[food]
            depth += 1
            cur.depth = depth

    def print(self):
        Q = []
        child_keys = sorted(self.head.child.keys(), reverse=True)

        for key in child_keys:
            Q.append((self.head.child[key], key))

        while Q:
            now, food = Q.pop()

            print('--'*(now.depth-1)+food)
            child_keys = sorted(now.child.keys(), reverse=True)

            for key in child_keys:
                Q.append((now.child[key], key))


N = int(input())
ant_trie = Trie()

for _ in range(N):
    food_list = input().split()
    ant_trie.add(food_list[1:])

ant_trie.print()




