"""
You are given an array (zero indexed) of N non-negative integers, A0, A1 ,…, AN-1.
Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order) that sub array, then the whole array should get sorted.
If A is already sorted, output -1.
Example :
Input 1:
A = [1, 3, 2, 4, 5]
Return: [1, 2]
Input 2:
A = [1, 2, 3, 4, 5]
Return: [-1]
In the above example(Input 1), if we sort the subarray A1, A2, then whole array A should get sorted.
"""
# Assume that Al, …, Ar is the minimum-unsorted-subarray which is to be sorted.
# then min(Al, …, Ar) >= max(A0, …, Al-1)
# and max(Al, …, Ar) <= min(Ar+1, …, AN-1)


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        si = -1
        ei = 0
        max1 = 0
        min1 = max(A)
        minind = -1
        for i in range(1, len(A)):
            if A[i] < A[i - 1] or A[i] < max1:
                if si == -1:
                    si = i - 1
                ei = i
                min1 = min(min1, A[i])
            max1 = max(max1, A[i])

        if si == -1:
            return [-1]
        else:
            for i in range(0, si):
                if A[i] > min1:
                    minind = i
                    break
            if minind < si and minind != -1:
                si = minind
            return [si, ei]

