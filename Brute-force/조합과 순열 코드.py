# 조합과 순열 코드의 경우 재귀함수로 만들수 있고
# 파이썬에서는 yield 키워드로 제너레이터를 만들어 더 직관적인 코드작성이 가능하다.

def combinations(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:],r-1):
                yield [arr[i]] + next

def permutation(arr, n, k):
    for i in range(n, len(arr)):
        if n == k-1:
            yield [arr[i]]
        else:
            arr[n], arr[i] = arr[i], arr[n]
            for next in permutation(arr, n+1, k):
                yield [arr[n]] + next
            arr[n], arr[i] = arr[i], arr[n]


arr = [1, 2, 3, 4]
k = 3
for result in permutation(arr, 0, k):
    print(result)

print()
for result in combinations(arr, k):
    print(result)