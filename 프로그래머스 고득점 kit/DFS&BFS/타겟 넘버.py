import queue


def solution(numbers, target):
    q = queue.Queue()
    q.put(numbers[0])
    q.put(- numbers[0])
    cnt = 1
    while cnt < len(numbers):
        for _ in range(1 << cnt):
            now = q.get()
            q.put(now + numbers[cnt])
            q.put(now - numbers[cnt])
        cnt += 1

    result = [q.get() for _ in range(q.qsize())]
    # print(result)

    return result.count(target)