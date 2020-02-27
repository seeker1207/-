def merge_two_list(left, right):
    result = []
    l_idx, r_idx = 0, 0

    while l_idx != len(left) or r_idx != len(right):
        if l_idx == len(left):
            result.extend(right[r_idx:])
            break
        if r_idx == len(right):
            result.extend(left[l_idx:])
            break
        if left[l_idx] >= right[r_idx]:
            result.append(right[r_idx])
            r_idx += 1
        else:   # l_first < r_first
            result.append(left[l_idx])
            l_idx += 1
    return result


def merge_sort(L, start, end):
    global cnt
    middle = (end - start) // 2 + start
    if (start + 1) == end:
        return [L[start]]

    left = merge_sort(L, start, middle)
    right = merge_sort(L, middle, end)
    # print(left, '+', right)
    if left[-1] > right[-1]:
        cnt += 1
    return merge_two_list(left, right)


# print(merge_two_list([2,4,5,8,9],[1,2,3,7,10]))
for i in range(int(input())):
    N = int(input())
    input_L = list(map(int, input().split()))
    cnt = 0
    # print(merge_sort(input_L, 0, N))
    result_L = merge_sort(input_L, 0, N)
    print(f'#{i+1} {result_L[N//2]} {cnt}')
