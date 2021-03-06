import os
import sys


def quicksort(lst, left, right):

    if right - left > 0:
        p = partition(lst, left, right)
        quicksort(lst, left, (p - 1))
        quicksort(lst, (p + 1), right)


def partition(lst, left, right):

    pivot = choose_pivot(lst, left, right)
    i = left + 1
    for j in range(i, right+1):
        if lst[j] < pivot:
            lst[j], lst[i] = lst[i], lst[j]
            i += 1
    lst[left], lst[i-1] = lst[i-1], lst[left]
    return i - 1

def choose_pivot(lst, left, right):
    middle = find_middle(lst, left, right)
    if lst[left] < lst[middle]:
        if lst[middle] < lst[right]:
            lst[left], lst[middle] = lst[middle], lst[left]
            return lst[left]
        elif lst[left] < lst[right]:
            lst[left], lst[right] = lst[right], lst[left]
            return lst[left]
        else:
            return lst[left]
    else:
        if lst[left] < lst[right]:
            return lst[left]
        elif lst[right] < lst[middle]:
            lst[left], lst[middle] = lst[middle], lst[left]
            return lst[left]
        else:
            lst[left], lst[right] = lst[right], lst[left]
            return lst[left]

def find_middle(lst, left, right):
    sublist_len = right - left + 1
    if sublist_len % 2 is 0:
        middle = sublist_len // 2 - 1
    else:
        middle = sublist_len // 2
    return middle + left


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        file_lst = [ int(x) for x in f.read().split('\n') if x ]
        quicksort(file_lst, 0, len(file_lst) - 1)
        print('here is the final list: {}\n'.format(
            file_lst
            )
        )
