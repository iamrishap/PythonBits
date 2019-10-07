import sys
from collections import namedtuple


def median(L, j):
    '''
    >>> L = [7, 10, 4, 3, 20, 15]
    >>> median(L, 2)
    7
    '''
    if len(L) < 10:
        L.sort()
        return L[j]
    S = []
    lIndex = 0
    while lIndex + 5 < len(L) - 1:
        S.append(L[lIndex:lIndex + 5])
        lIndex += 5
    S.append(L[lIndex:])
    Meds = []
    for subList in S:
        # Meds.append(median(subList, int((len(subList) - 1) / 2)))
        Meds.append(median(subList.sort()[(len(subList) - 1) / 2]))  # Choose median of each sublist
    med = median(Meds, int((len(Meds) - 1) / 2))  # O(n/5)
    L1 = []
    L2 = []
    L3 = []
    for i in L:
        if i < med:
            L1.append(i)
        elif i > med:
            L3.append(i)
        else:
            L2.append(i)
    if j < len(L1):
        return median(L1, j)
    elif j < len(L2) + len(L1):
        return L2[0]
    else:
        return median(L3, j - len(L1) - len(L2))


def binary_search_iterative(A, val):
    '''
    >>> A = [-11, -2, 0, 3, 14, 55, 61]
    >>> binary_search_iterative(A, 14)
    4
    '''
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (low + high) // 2
        if A[mid] == val:
            return mid
        elif A[mid] > val:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def binary_search_recursive(a):
    pass


def sum_nearest_zero(A):
    '''
    >>> A = [1, 60, - 10, 70, -80, 85]
    >>> sum_nearest_zero(A)
    [-80, 85]
    >>> A = [10, 8, 3, 5, -9, -7, 6]
    >>> sum_nearest_zero(A)
    [-9, 10]
    '''
    A.sort()
    low = 0
    high = len(A) - 1
    down_index = [0, 0]
    up_index = [0, 0]
    min_down = sys.maxsize
    min_up = sys.maxsize
    while low <= high: # should instead use if(abs(minSum) > abs(sumNow)):
        if A[high] + A[low] <= 0:
            if A[high] + A[low] < min_down:
                min_down = A[high] + A[low]
                down_index[0] = A[low]
                down_index[1] = A[high]
            high -= 1
        if A[high] + A[low] >= 0:
            if A[high] + A[low] < min_up:
                min_up = A[high] + A[low]
                up_index[0] = A[low]
                up_index[1] = A[high]
            low += 1
    if min_down <= min_up:
        return down_index
    else:
        return up_index


def three_to_sum_k(A, k):
    pass # find three numbers in Array which sum to K

def order_even_odd(A):
    pass

def sort012_dutch_flag(A):
    pass

def find_max_difference(A):
    pass

def missing_n_to_m(A):
    pass
