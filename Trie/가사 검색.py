class Node:
    def __init__(self, child, last_point=False):
        self.count = 0
        self.child = child
        self.last_point = last_point


class Trie:
    def __init__(self):
        self.head = Node({})

    def add(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Node({})
            cur.count += 1
            cur = cur.child[ch]

        cur.last_point = True

    def search(self, query):
        cur = self.head

        for ch in query:
            if ch == '?':
                print(cur.child, cur.count)
                return cur.count
            if ch not in cur.child:
                return 0

            cur = cur.child[ch]

        ## query에 ?없는 경우
        return 1 if cur.last_point else 0


def solution(words, queries):
    answer = []
    tries = [Trie() for _ in range(100001)]
    revers_tries = [Trie() for _ in range(100001)]

    for word in words:
        tries[len(word)].add(word)
        revers_tries[len(word)].add(reversed(word))

    for query in queries:
        answer_cnt = 0
        l = len(query)
        if query[-1] == '?':
            answer_cnt = tries[l].search(query)
        elif query[0] == '?':
            answer_cnt = revers_tries[l].search(reversed(query))
        else:
            answer_cnt = tries[l].search(query)
        answer.append(answer_cnt)

    print(answer)
    return answer


solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
# w_list = list("hello")
# trie = Trie()
# revers_trie = Trie()
# trie.add("hello")
# revers_trie.add("hell")
#
# print(id(trie), id(revers_trie))
# print(trie.search("hello"))
# print(trie.search("hell"))
# print(revers_trie.search("hell"))