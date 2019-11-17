"""
You are given an array A having N integers.

You have to perform the following steps in a given order.

generate all subarrays of A.
take the maximum element from each subarray of A and insert it into a new array G.
replace every element of G with the product of their divisors mod 1e9 + 7.
sort G in descending order
perform Q queries
In each query, you are given an integer K, where you have to find the Kth element in G.

Note: Your solution will run on multiple test cases so do clear global variables after using them.


Input Format

The first argument given is an Array A, having N integers.
The second argument given is an Array B, where B[i] is the ith query.
Output Format

Return an Array X, where X[i] will have the answer for the ith query.
Constraints

1 <= N <= 1e5
1 <= A[i] <= 1e5
1 <= Q <= 1e5
1 <= k <= (N * (N + 1))/2
For Example

Input:
    A = [1, 2, 4]
    B = [1, 2, 3, 4, 5, 6]
Output:
    X = [8, 8, 8, 2, 2, 1]

Explanation:
    subarrays of A	  maximum element
    ------------------------------------
    1. [1]							1
    2. [1, 2]						2
    3. [1, 2, 4]					4
    4. [2]							2
    5. [2, 4]						4
    6. [4]							4

    original
    G = [1, 2, 4, 2, 4, 4]
    after changing every element of G with product of their divisors
    G = [1, 2, 8, 2, 8, 8]
    after sorting G in descending order
    G = [8, 8, 8, 2, 2, 1]
"""

# We can solve this problem by doing the binary search for each query.
# How?
# First, you need to find that how many times an element will appear in array G. i.e in
# how many subarrays an element is the greatest one.
# You can find that by finding the next greater element for the current element in both sides and
# then by multiplying them.
# Once you found the frequency of each element in an array G, you can sort the pairs(product_of_divisors_of_element,
# frequency) according to there value in descending order followed by taking the prefix sum of there frequencies
# you can do the binary search for each query.
# Please refer complete solution for more insight.

from collections import defaultdict
from math import sqrt
import bisect


def getDivsProd(n):
    mod = 1000000007
    p = 1
    for i in range(1, int(n ** 0.5 + 1)):
        if n % i == 0:
            if n / i == i:
                p = (p * i) % mod
            else:
                p = (p * i) % mod
                p = (p * (n / i)) % mod
    return int(p % mod)


def getFrequency(A):
    N = len(A)
    L = [1] * N
    R = [1] * N
    S = []
    top = -1
    for i in range(N):
        while (top >= 0 and A[S[top]] <= A[i]):
            S.pop()
            top -= 1
        if (top >= 0):
            L[i] = i - S[top]
        else:
            L[i] = i + 1
        S.append(i)
        top += 1
    S = []
    top = -1
    for i in range(N - 1, -1, -1):
        while (top >= 0 and A[S[top]] < A[i]):
            S.pop()
            top -= 1
        if (top >= 0):
            R[i] = S[top] - i
        else:
            R[i] = N - i
        S.append(i)
        top += 1
    for i in range(N):
        L[i] *= R[i]
    return L


class Solution:
    def solve(self, A, B):
        N = len(A)
        freq = getFrequency(A)
        for i in range(N):
            A[i] = getDivsProd(A[i])
        keys = []
        values = []
        prev = 0
        for i in sorted(zip(A, freq), reverse=True):
            keys.append(i[0])
            prev += i[1]
            values.append(prev)
        res = []
        for i in B:
            res.append(keys[bisect.bisect_left(values, i)])
        return res
