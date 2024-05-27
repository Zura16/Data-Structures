import random
from Interfaces import List


# Assuming that List has a method size() which returns the size of the ArrayList.

def linear_search(a: List, x):
    for i in range(a.size()):
        if a[i] == x:
            return i
    return None

def binary_search(a: List, x):
    low, high = 0, a.size() - 1

    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return None


def merge(a0, a1, a):
    i0, i1 = 0, 0
    for i in range(len(a)):
        if i0 == len(a0):
            a[i] = a1[i1]
            i1 += 1
        elif i1 == len(a1):
            a[i] = a0[i0]
            i0 += 1
        elif a0[i0] < a1[i1]:
            a[i] = a0[i0]
            i0 += 1
        else:
            a[i] = a1[i1]
            i1 += 1

def merge_sort(a):
    if len(a) <= 1:
        return a
    m = len(a)//2
    a0 = merge_sort(a[0:m])
    a1 = merge_sort(a[m:len(a)])
    merge(a0,a1,a)
    return a


def _quick_sort_f(a: List, start, end):
    if start < end:
        pivot_index = _partition_f(a, start, end)
        _quick_sort_f(a, start, pivot_index - 1)
        _quick_sort_f(a, pivot_index + 1, end)

def _quick_sort_r(a: List, start, end):
    if start < end:
        pivot_index = _partition_r(a, start, end)
        _quick_sort_r(a, start, pivot_index - 1)
        _quick_sort_r(a, pivot_index + 1, end)

def _partition_f(a: List, start, end):
    pivot_index = start
    pivot = a[start]

    for i in range(start + 1, end + 1):
        if a[i] < pivot:
            pivot_index += 1
            a[i], a[pivot_index] = a[pivot_index], a[i]

    a[start], a[pivot_index] = a[pivot_index], a[start]
    return pivot_index

def _partition_r(a: List, start, end):
    pivot_index = random.randint(start, end)
    pivot = a[pivot_index]

    a[pivot_index], a[start] = a[start], a[pivot_index]
    pivot_index = start

    for i in range(start + 1, end + 1):
        if a[i] < pivot:
            pivot_index += 1
            a[i], a[pivot_index] = a[pivot_index], a[i]

    a[start], a[pivot_index] = a[pivot_index], a[start]
    return pivot_index

def quick_sort(a: List, p=True):
    if p:
        _quick_sort_r(a, 0, a.size() - 1)
    else:
        _quick_sort_f(a, 0, a.size() - 1)
