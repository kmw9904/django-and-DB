import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def quick_sort(lst, start, end):
    if start > end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 왼쪽으로부터 pivot 보다 큰 값
        while left <= end and int(lst[left][1]) >= int(lst[pivot][1]):
            if int(lst[left][1]) == int(lst[pivot][1]):
                if int(lst[left][2]) < int(lst[pivot][2]):
                    left += 1

                elif int(lst[left][2]) > int(lst[pivot][2]):
                    break

                elif int(lst[left][2]) == int(lst[pivot][2]):
                    if int(lst[left][3]) > int(lst[pivot][3]):
                        left += 1

                    elif int(lst[left][3]) < int(lst[pivot][3]):
                        break

                    elif int(lst[left][3]) == int(lst[pivot][3]):
                        a = ord(lst[left][0][0])
                        b = ord(lst[pivot][0][0])
                        if lst[left][0] < lst[pivot][0][0]:
                            left += 1
                        break

            else:
                left += 1

        while right > start and int(lst[right][1]) <= int(lst[pivot][1]):
            if int(lst[right][1]) == int(lst[pivot][1]):
                if int(lst[right][2]) > int(lst[pivot][2]):
                    right -= 1

                elif int(lst[right][2]) < int(lst[pivot][2]):
                    break

                elif int(lst[right][2]) == int(lst[pivot][2]):
                    if int(lst[right][3]) < int(lst[pivot][3]):
                        right -= 1

                    elif int(lst[right][3]) > int(lst[pivot][3]):
                        break

                    elif int(lst[right][3]) == int(lst[pivot][3]):
                        a = ord(lst[right][0][0])
                        b = ord(lst[pivot][0][0])
                        if lst[right][0][0] > lst[pivot][0][0]:
                            right -= 1
                        break
            else:
                right -= 1

        if left > right:
            lst[right], lst[pivot] = lst[pivot], lst[right]
        else:
            lst[left], lst[right] = lst[right], lst[left]

    quick_sort(lst, start, right - 1)
    quick_sort(lst, right + 1, end)


N = int(input().rstrip())
lst = []
for _ in range(N):
    a = list(input().rstrip().split())
    lst.append(a)

quick_sort(lst, 0, N - 1)
for i in range(N):
    print(lst[i][0])
