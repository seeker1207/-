class Node:
    def __init__(self, is_last=False):
        self.child = {}
        self.is_last = is_last

class Trie:
    def __init__(self, is_last=False):
        self.head = Node()
        self.is_last = is_last

    def add(self, word):
        cur = self.head

        for ch in word:
            if cur.is_last:
                return False
            if ch not in cur.child:
                cur.child[ch] = Node()
            cur = cur.child[ch]

        if cur.child:
            return False

        cur.is_last = True
        return True


t = int(input())
for _ in range(t):
    phones = []
    phone_trie = Trie()
    is_valid = True

    for _ in range(int(input())):
        phones.append(input())

    for num in phones:
        is_valid = phone_trie.add(num)
        if not is_valid:
            break

    result = "YES" if is_valid else "NO"
    print(result)




