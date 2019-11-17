#########################	arrays	#########################


#####		Maximum Absolute Difference		#####

"""
You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

For example,

A=[1, 3, -1]

f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

So, we return 5.
f(i, j) = |A[i] - A[j]| + |i - j| can be written in 4 ways (Since we are looking at max value,
we don’t even care if the value becomes negative as long as we are also covering the max value in some way).

(A[i] + i) - (A[j] + j)
-(A[i] - i) + (A[j] - j)
(A[i] - i) - (A[j] - j)
(-A[i] - i) + (A[j] + j) = -(A[i] + i) + (A[j] + j)
Note that case 1 and 4 are equivalent and so are case 2 and 3.

We can construct two arrays with values: A[i] + i and A[i] - i.
Then, for above 2 cases, we find the maximum value possible.
For that, we just have to store minimum and maximum values of expressions A[i] + i and A[i] - i for all i.
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        n = len(A)
        max1 = -9999999999999999
        max2 = -9999999999999999
        min1 = 9999999999999999
        min2 = 999999999999999
        result = -999999999999999

        for i in range(n):
            max1 = max(A[i] + i, max1)
            min1 = min(A[i] + i, min1)

            max2 = max(A[i] - i, max2)
            min2 = min(A[i] - i, min2)

        result = max(max1 - min1, result)
        result = max(max2 - min2, result)

        return result


s = Solution()
print(s.maxArr([1, 3, -1]))

#####		Repeat And Missing Number		#####

"""
You are given a read only array of n integers from 1 to n.
Each integer appears exactly once except A which appears twice and B which is missing.
Return A and B.
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Note that in your output A should precede B.
Example:
Input:[3 1 2 5 3]
Output:[3, 4]
A = 3, B = 4
"""


class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        seen = set()
        len_a = len(A)
        sum_a = (len_a * (len_a + 1)) // 2
        repeated = None

        for i in A:
            if i not in seen:
                seen.add(i)
                sum_a -= i
            else:
                repeated = i
        return repeated, sum_a

    def repeatedNumber2(self, A):
        n = len(A)
        x = sum(range(1, n + 1)) - sum(A)
        y = sum([i ** 2 for i in range(1, n + 1)]) - sum([i ** 2 for i in A])
        b = ((x ** 2) + y) // (2 * x)
        a = (y - (x ** 2)) // (2 * x)
        return a, b


s = Solution()
print(s.repeatedNumber2([3, 1, 2, 5, 3]))

#####		Anti Diagonals		#####

"""
Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.
Example:
Input:
1 2 3
4 5 6
7 8 9
Return the following :
[
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]
Input :
1 2
3 4
Return the following  :
[
  [1],
  [2, 3],
  [4]
]
"""


class Solution:
    # @param a : list of list of integers
    # @return a list of list of integers
    def diagonal(self, a):
        B = [[] for i in range(len(a) * 2)]
        # Done smoothly
        for i in range(len(a)):
            for j in range(len(a)):
                B[i + j].append(a[i][j])
        return B[:-1]


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = Solution()
print(s.diagonal(A)

#####		Wave Array		#####

"""
Given an array of integers, sort the array into a wave like array and return it,
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....
Example
Given [1, 2, 3, 4]
One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]
NOTE : If there are multiple answers possible, return the one that's lexicographically smallest.
So, in example case, you will return [2, 1, 4, 3]
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        # For the answer to be the lexicographically smallest,
        # we want the first element to be the second smallest,
        # the 2nd element to be the smallest, and so on with
        # the rest of the sequence.
        A = sorted(A)
        for i in range(0, len(A) - 1, 2):
            A[i], A[i + 1] = A[i + 1], A[i]
        return A


#####		Merge Intervals		#####

"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.
Example 1:
Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].
Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].
This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
Make sure the returned intervals are also sorted.
"""


# Given all the intervals, you need to figure out the sequence of intervals which intersect with the given newInterval.
# Note that if max(a,c) > min(b,d), then the intervals do not overlap. Otherwise, they overlap.
# Once we figure out the intervals ( interval[i] to interval[j] ) which overlap with newInterval,
# note that we can replace all the overlapping intervals with one interval which would be
# (min(interval[i].start, newInterval.start), max(interval[j].end, newInterval.end)).

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        start = newInterval.start
        end = newInterval.end
        right = left = 0
        while right < len(intervals):
            if start <= intervals[right].end:
                if end < intervals[right].start:
                    break
                start = min(start, intervals[right].start)
                end = max(end, intervals[right].end)
            else:
                left += 1
            right += 1
        return intervals[:left] + [Interval(start, end)] + intervals[right:]


s = Solution()
print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 9]))

#####		Maximum Unsorted Subarray		#####

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


#####		N By Three Times Repeated		#####

"""
You’re given a read only array of n integers.
Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.
If so, return the integer. If not, return -1.
If there are multiple solutions, return any one.
Example :
Input : [1 2 3 1 1]
Output : 1
1 occurs 3 times which is more than 5/3 times.
"""


# It is important to note that if at a given time,
# you have 3 distinct element from the array, if you remove them from the array, your answer does not change.
# Assume that we maintain 2 elements with their counts as we traverse along the array.
# When we encounter a new element, there are 3 cases possible :
# We don’t have 2 elements yet. So add this to the list with count as 1.
# This element is different from the existing 2 elements. As we said before, we have 3 distinct numbers now.
# Removing them does not change the answer. So decrement 1 from count of 2 existing elements.
# If their count falls to 0, obviously its not a part of 2 elements anymore.
# The new element is same as one of the 2 elements. Increment the count of that element.
# Consequently, the answer will be one of the 2 elements left behind.
# If they are not the answer, then there is no element with count > N / 3.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n = len(A)
        l = n / 3

        maj1 = 0
        maj2 = 0
        first = float('inf')
        second = float('inf')

        for i in range(n):
            if first == A[i]:
                maj1 += 1
            elif second == A[i]:
                maj2 += 1
            elif maj1 == 0:
                maj1 += 1
                first = A[i]
            elif maj2 == 0:
                maj2 += 1
                second = A[i]
            else:
                maj1 -= 1
                maj2 -= 1

        maj1 = 0
        maj2 = 0

        for i in range(n):
            if A[i] == first:
                maj1 += 1
            elif A[i] == second:
                maj2 += 1

        if maj1 > l:
            return first
        if maj2 > l:
            return second
        return -1


s = Solution()
print(s.repeatedNumber([1, 2, 3, 1, 1]))
print(s.repeatedNumber([4, 2, 5, 3, 1]))

#####		Add One To The Number		#####

"""
Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

Example:

If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124.

 NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer.
For example, for this problem, following are some good questions to ask :
Q : Can the input have 0’s before the most significant digit. Or in other words, is 0 1 2 3 a valid input?
A : For the purpose of this question, YES
Q : Can the output have 0’s before the most significant digit? Or in other words, is 0 1 2 4 a valid output?
A : For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        num = int(''.join([str(val) for val in A])) + 1
        return [int(val) for val in str(num)]

    def plusOne_editorial(self, A):
        val = 1;
        for i in range(len(A), 0, -1):
            val = val + A[i - 1]
            borrow = int(val / 10)
            if borrow == 0:
                A[i - 1] = val
                break;
            else:
                A[i - 1] = val % 10
                val = borrow
        A = [borrow] + A  # Not sure what this does!
        while A[0] == 0:
            del A[0]
        return A


s = Solution()
print(s.plusOne([1, 2, 3, 4]))
print(s.plusOne([0, 0, 1, 2, 3, 4]))

#####		Find Duplicate In Array		#####

"""
Find Duplicate in Array
Asked in:
Amazon
VMWare
Riverbed
Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.

Sample Input:

[3 4 1 4 1]
Sample Output:

1
If there are multiple possible answers ( like in the sample case above ), output any one.

If there is no duplicate, output -1
"""


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        B = list(A)
        B.append(0)
        for val in B:
            if B[abs(val)] < 0:
                return abs(val)
            else:
                B[abs(val)] *= -1
        return -1

    def repeatedNumber_editorial(self, A):
        if len(A) == 0:
            return -1
        p1 = A[-1]
        p2 = A[p1 - 1]
        while p1 != p2:
            p1 = A[p1 - 1]
            p2 = A[A[p2 - 1] - 1]
        p2 = 0
        while p1 != p2:
            p1 = A[p1 - 1]
            p2 = A[p2 - 1]
        return p2


s = Solution()
print(s.repeatedNumber2([247, 240, 303, 9, 304, 105, 44, 204, 291, 26, 242, 2, 358, 264, 176, 289, 196, 329,
                         189, 102, 45, 111, 115, 339, 74, 200, 34, 201, 215, 173, 107, 141, 71, 125, 6, 241,
                         275, 88, 91, 58, 171, 346, 219, 238, 246, 10, 118, 163, 287, 179, 123, 348, 283, 313,
                         226, 324, 203, 323, 28, 251, 69, 311, 330, 316, 320, 312, 50, 157, 342, 12, 253, 180,
                         112, 90, 16, 288, 213, 273, 57, 243, 42, 168, 55, 144, 131, 38, 317, 194, 355, 254, 202,
                         351, 62, 80, 134, 321, 31, 127, 232, 67, 22, 124, 271, 231, 162, 172, 52, 228, 87, 174,
                         307, 36, 148, 302, 198, 24, 338, 276, 327, 150, 110, 188, 309, 354, 190, 265, 3, 108,
                         218, 164, 145, 285, 99, 60, 286, 103, 119, 29, 75, 212, 290, 301, 151, 17, 147, 94,
                         138, 272, 279, 222, 315, 116, 262, 1, 334, 41, 54, 208, 139, 332, 89, 18, 233, 268,
                         7, 214, 20, 46, 326, 298, 101, 47, 236, 216, 359, 161, 350, 5, 49, 122, 345, 269, 73,
                         76, 221, 280, 322, 149, 318, 135, 234, 82, 120, 335, 98, 274, 182, 129, 106, 248, 64,
                         121, 258, 113, 349, 167, 192, 356, 51, 166, 77, 297, 39, 305, 260, 14, 63, 165, 85, 224,
                         19, 27, 177, 344, 33, 259, 292, 100, 43, 314, 170, 97, 4, 78, 310, 61, 328, 199, 255, 159,
                         185, 261, 229, 11, 295, 353, 186, 325, 79, 142, 223, 211, 152, 266, 48, 347, 21, 169, 65,
                         140, 83, 156, 340, 56, 220, 130, 117, 143, 277, 235, 59, 205, 153, 352, 300, 114, 84, 183,
                         333, 230, 197, 336, 244, 195, 37, 23, 206, 86, 15, 187, 181, 308, 109, 293, 128, 66, 270,
                         209, 158, 32, 25, 227, 191, 35, 40, 13, 175, 146, 299, 207, 217, 281, 30, 357, 184, 133,
                         245, 284, 343, 53, 210, 306, 136, 132, 239, 155, 73, 193, 278, 257, 126, 331, 294, 250,
                         252, 263, 92, 267, 282, 72, 95, 337, 154, 319, 341, 70, 81, 68, 160, 8, 249, 96, 104,
                         137, 256, 93, 178, 296, 225, 237]))

#####		Min Steps Infinite Grid		#####

"""
You are in an infinite 2D grid where you can move in any of the 8 directions :

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points.
Give the minimum number of steps in which you can achieve it. You start from the first point.

Input :

Given two integer arrays A and B, where A[i] is x coordinate and B[i] is y coordinate of ith point respectively.
Output :

Return an Integer, i.e minimum number of steps.
Example :

Input : [(0, 0), (1, 1), (1, 2)]
Output : 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).

This question is intentionally left slightly vague.
Clarify the question by trying out a few cases in the “See Expected Output” section.
"""


class Solution:
    def coverPoints(self, A, B):
        prev_x, prev_y, total = A[0], B[0], 0
        for curr_x, curr_y in zip(A, B):
            dx, dy = abs(curr_x - prev_x), abs(curr_y - prev_y)
            if dx < dy:
                total += dy
            else:
                total += dx
            prev_x, prev_y = curr_x, curr_y
        return total


A = [0, 1, 1]
B = [0, 1, 2]
P = [(0, 0), (1, 1), (1, 2)]
s = Solution()
print(s.coverPoints(A, B))

#####		Simple Queries		#####

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


#####		Max Non Neg Subarray		#####

"""
Max Non Negative SubArray
Asked in:
Google
Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.

The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array.

Find and return the required subarray.

NOTE:

    1. If there is a tie, then compare with segment's length and return segment which has maximum length.
    2. If there is still a tie, then return the segment with minimum starting index.


Input Format:

The first and the only argument of input contains an integer array A, of length N.
Output Format:

Return an array of integers, that is a subarray of A that satisfies the given conditions.
Constraints:

1 <= N <= 1e5
1 <= A[i] <= 1e5
Examples:

Input 1:
    A = [1, 2, 5, -7, 2, 3]

Output 1:
    [1, 2, 5]

Explanation 1:
    The two sub-arrays are [1, 2, 5] [2, 3].
    The answer is [1, 2, 5] as its sum is larger than [2, 3].

Input 2:
    A = [10, -1, 2, 3, -4, 100]

Output 2:
    [100]

Explanation 2:
    The three sub-arrays are [10], [2, 3], [100].
    The answer is [100] as its sum is larger than the other two.
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    # Approach: Maintain 2 dictionaries with values of the start index, end index,
    # sum and length for the current and max
    # Append(-1) to avoid handling end of array separately
    def maxset(self, A):
        # Edge case
        if len(A) == 1:
            return A if A[0] > 0 else []

        A.append(-1)
        # Dict to store various useful intermediary values to reach the solution
        val_now = {
            'inx_low': -1,
            'inx_high': -1,
            'sum': 0,
            'len': 0
        }
        val_max = val_now.copy()

        for idx, val in enumerate(A):
            if val > -1:
                if val_now['inx_low'] == -1:
                    val_now['inx_low'] = idx
                val_now['sum'] += val
                val_now['len'] += 1
            else:
                # Encountered first -ve value
                if val_now['inx_low'] != -1:  # If `val_now` is set
                    val_now['inx_high'] = idx - 1  # Set `ind_high`
                    if val_now['sum'] > val_max['sum'] or \
                            (val_now['sum'] == val_max['sum'] and val_now['len'] > val_max['len']):
                        val_max = val_now.copy()

                    # Reset `val_now`
                    val_now['sum'] = val_now['len'] = 0
                    val_now['inx_low'] = val_now['inx_high'] = -1
                # Consecutive -ve value found
                else:
                    pass  # Do nothing
        return A[val_max['inx_low']: val_max['inx_high'] + 1]

    # Approach: Maintain just indices with values of the start index, end index, sum and length for the current and max
    # Edge cases don't need to be handled separately
    def maxset_billbezos(self, A):
        s, j = 0, 0
        a, b, max_s = 0, -1, 0
        A.append(float('-inf'))
        for i in range(len(A)):
            if A[i] < 0:
                if s > max_s or (s == max_s and i - j > b - a):
                    a, b, max_s = j, i - 1, s
                j, s = i + 1, 0
            else:
                s += A[i]
        return A[a:b + 1]


s = Solution()
print(s.maxset([1, 2, 5, -7, -18, 2, 3, 8]))
print(s.maxset_billbezos([1, 2, 5, -7, -18, 2, 3, -3, 8]))

#####		Rotate Matrix		#####

"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
You need to do this in place.
Note that if you end up using an additional array, you will only receive partial score.
Example:
If the array is
[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:
[
    [3, 1],
    [4, 2]
]
"""


class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        # transpose the matrix
        for i in range(len(A)):
            for j in range(i, len(A)):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        N = len(A)
        print(A)
        # swap columns moving inwards from outwards
        for i in range(N // 2):
            for j in range(N):
                A[j][i], A[j][N - 1 - i] = A[j][N - 1 - i], A[j][i]
        return (A)


A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

s = Solution()
print(s.rotate(A))

#####		Kth Row Pascal Triangle		#####

"""
Given an index k, return the kth row of the Pascal’s triangle.
Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.
Example:
Input : k = 3
Return : [1,3,3,1]
NOTE : k is 0 based. k = 0, corresponds to the row [1].
Note:Could you optimize your algorithm to use only O(k) extra space?
"""


class Solution:

    def getRow(self, A):
        if A == 0:
            return [1]
        x = [1] * (A + 1)
        for i in range(1, A):
            x[i] = x[i - 1] * (A + 1 - i) // i
        return x


s = Solution()
print(s.getRow(5))

#####		First Missing Positive		#####

"""
Given an unsorted integer array, find the first missing positive integer.
Example:
Given [1,2,0] return 3,
[3,4,-1,1] return 2,
[-8, -7, -6] returns 1
Your algorithm should run in O(n) time and use constant space.
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        A = list(filter(lambda x: x > 0, A))
        # print(A)
        A = [len(A) + 2] + A  # Add the next number. This is for proper indexing (zero based).
        # print(A)
        for i, num in enumerate(A):
            num = abs(num)
            if num < len(A):
                A[num] = - abs(A[num])
        # print(A)
        for i in range(1, len(A)):
            if A[i] > 0:
                return i
        return len(A)


s = Solution()
s.firstMissingPositive([3, 5, 2, 1])

#####		Merge Overlapping Intervals		#####

"""
Given a collection of intervals, merge all overlapping intervals.
For example:
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
Make sure the returned intervals are sorted.
"""


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        res = []
        for interval in sorted(intervals, key=lambda x: x.start):
            if res and interval.start <= res[-1].end:
                res[-1].end = max(interval.end, res[-1].end)
            else:
                res.append(interval)
        return res


#####		Max Sum Contigous Array		#####

"""
Find the contiguous subarray within an array, A of length N which has the largest sum.
Input Format:
The first and the only argument contains an integer array, A.
Output Format:
Return an integer representing the maximum possible sum of the contiguous subarray.
Constraints:
1 <= N <= 1e6
-1000 <= A[i] <= 1000
For example:
Input 1:
    A = [1, 2, 3, 4, -10]
Output 1:
    10
Explanation 1:
    The subarray [1, 2, 3, 4] has the maximum possible sum of 10.
Input 2:
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output 2:
    6
Explanation 2:
    The subarray [4,-1,2,1] has the maximum possible sum of 6.
"""

inf = float('inf')


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        if not A:
            return 0
        max_so_far, max_sum = 0, -inf
        for val in A:
            max_so_far += val
            max_sum = max(max_so_far, max_sum)
            # Doing this last, to handle case
            # when all numbers are negative.
            max_so_far = max(max_so_far, 0)
        return max_sum


s = Solution()
print(s.maxSubArray([1, 2, 3, 4, -10]))
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

#####		Nobel Integer		#####

"""
Given an integer array, find if an integer p exists in the array such
that the number of integers greater than p in the array equals to p
If such an integer is found return 1 else return -1.
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        n = len(A)
        for i in range(n - 1):
            # When certain element repeats many times.
            if A[i] == A[i + 1]:
                continue
            if A[i] == n - i - 1:
                return 1
        if A[n - 1] == 0:
            return 1
        return -1


#####		Max Consecutive Gap		#####

"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
Try to solve it in linear time/space.
Example :
Input : [1, 10, 5]
Output : 5
Return 0 if the array contains less than 2 elements.
You may assume that all the elements in the array are non-negative integers and fit in the 32-bit signed integer range.
You may also assume that the difference will not overflow.
"""


# So, we know now that our answer will lie in the range [gap, MAX - MIN].
# Now, if we know the answer is more than gap, what we do is create buckets of size gap for ranges
# [MIN, MIN + gap), [Min + gap, `MIN` + 2* gap) ... and so on
# There will only be (N-1) such buckets. We place the numbers in these buckets based on their value.
# If you pick any 2 numbers from a single bucket, their difference will be less than gap, and
# hence they would never contribute to maxgap ( Remember maxgap >= gap ). We only need to store the largest
# number and the smallest number in each bucket, and we only look at the numbers across bucket.
# Now, we just need to go through the bucket sequentially ( they are already sorted by value ),
# and get the difference of min_value with max_value of previous bucket with at least one value.
# We take maximum of all such values.


class Solution:
    def maximumGap(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) < 2:
            return 0
        min_v, max_v = min(arr), max(arr)
        if max_v - min_v < 2:
            return max_v - min_v
        min_gap = max(1, (max_v - min_v) // (len(arr)))  # The minimum possible gap
        sentinel_min, sentinel_max = 2 ** 32 - 1, -1
        buckets_min = [sentinel_min] * len(arr)
        buckets_max = [sentinel_max] * len(arr)
        for x in arr:
            i = min((x - min_v) // min_gap, len(arr) - 1)
            buckets_min[i] = min(buckets_min[i], x)
            buckets_max[i] = max(buckets_max[i], x)
        max_gap = 0
        prev_max = buckets_max[0]  # First gap is always non-empty
        for i in range(1, len(arr)):
            if buckets_min[i] == sentinel_min:
                continue
            max_gap = max(buckets_min[i] - prev_max, max_gap)
            prev_max = buckets_max[i]
        return max_gap


#####		Maxprod		#####

"""
You are given an array A containing N integers. The special product of each ith integer in this array
is defined as the product of the following:<ul>
LeftSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (i>j). If multiple A[j]’s are
present in multiple positions, the LeftSpecialValue is the maximum value of j.
RightSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (j>i). If multiple A[j]s are
present in multiple positions, the RightSpecialValue is the minimum value of j.
Write a program to find the maximum special product of any integer in the array.
Input: You will receive array of integers as argument to function.
Return: Maximum special product of any integer in the array modulo 1000000007.
Note: If j does not exist, the LeftSpecialValue and RightSpecialValue are considered to be 0.
Constraints 1 <= N <= 10^5 1 <= A[i] <= 10^9
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        n = len(A)
        if n < 3:
            return 0
        rightspval = [0] * n
        leftspval = [0] * n
        stack = []

        stack.append(0)
        for i in range(1, n):
            while stack and A[stack[-1]] < A[i]:
                rightspval[stack.pop()] = i
            stack.append(i)
        stack.clear()

        stack.append(n - 1)
        for i in range(n - 1, -1, -1):
            while stack and A[stack[-1]] < A[i]:
                leftspval[stack.pop()] = i
            stack.append(i)
        del (stack)

        maxi = -1
        for i in range(n):
            maxi = max(maxi, leftspval[i] * rightspval[i])
        return maxi % 1000000007


#####		Result		#####

"""
You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

For example,

A=[1, 3, -1]

f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

So, we return 5.
f(i, j) = |A[i] - A[j]| + |i - j| can be written in 4 ways (Since we are looking at max value,
we don’t even care if the value becomes negative as long as we are also covering the max value in some way).

(A[i] + i) - (A[j] + j)
-(A[i] - i) + (A[j] - j)
(A[i] - i) - (A[j] - j)
(-A[i] - i) + (A[j] + j) = -(A[i] + i) + (A[j] + j)
Note that case 1 and 4 are equivalent and so are case 2 and 3.

We can construct two arrays with values: A[i] + i and A[i] - i.
Then, for above 2 cases, we find the maximum value possible.
For that, we just have to store minimum and maximum values of expressions A[i] + i and A[i] - i for all i.
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        n = len(A)
        max1 = -9999999999999999
        max2 = -9999999999999999
        min1 = 9999999999999999
        min2 = 999999999999999
        result = -999999999999999

        for i in range(n):
            max1 = max(A[i] + i, max1)
            min1 = min(A[i] + i, min1)

            max2 = max(A[i] - i, max2)
            min2 = min(A[i] - i, min2)

        result = max(max1 - min1, result)
        result = max(max2 - min2, result)

        return result


s = Solution()
print(s.maxArr([1, 3, -1]))
"""
You are given a read only array of n integers from 1 to n.
Each integer appears exactly once except A which appears twice and B which is missing.
Return A and B.
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Note that in your output A should precede B.
Example:
Input:[3 1 2 5 3]
Output:[3, 4]
A = 3, B = 4
"""


class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        seen = set()
        len_a = len(A)
        sum_a = (len_a * (len_a + 1)) // 2
        repeated = None

        for i in A:
            if i not in seen:
                seen.add(i)
                sum_a -= i
            else:
                repeated = i
        return repeated, sum_a

    def repeatedNumber2(self, A):
        n = len(A)
        x = sum(range(1, n + 1)) - sum(A)
        y = sum([i ** 2 for i in range(1, n + 1)]) - sum([i ** 2 for i in A])
        b = ((x ** 2) + y) // (2 * x)
        a = (y - (x ** 2)) // (2 * x)
        return a, b


s = Solution()
print(s.repeatedNumber2([3, 1, 2, 5, 3]))
"""
Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.
Example:
Input:
1 2 3
4 5 6
7 8 9
Return the following :
[
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]
Input :
1 2
3 4
Return the following  :
[
  [1],
  [2, 3],
  [4]
]
"""


class Solution:
    # @param a : list of list of integers
    # @return a list of list of integers
    def diagonal(self, a):
        B = [[] for i in range(len(a) * 2)]
        # Done smoothly
        for i in range(len(a)):
            for j in range(len(a)):
                B[i + j].append(a[i][j])
        return B[:-1]


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = Solution()
print(s.diagonal(A))

"""
Given an array of integers, sort the array into a wave like array and return it,
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....
Example
Given [1, 2, 3, 4]
One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]
NOTE : If there are multiple answers possible, return the one that's lexicographically smallest.
So, in example case, you will return [2, 1, 4, 3]
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        # For the answer to be the lexicographically smallest,
        # we want the first element to be the second smallest,
        # the 2nd element to be the smallest, and so on with
        # the rest of the sequence.
        A = sorted(A)
        for i in range(0, len(A) - 1, 2):
            A[i], A[i + 1] = A[i + 1], A[i]
        return A


"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.
Example 1:
Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].
Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].
This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
Make sure the returned intervals are also sorted.
"""


# Given all the intervals, you need to figure out the sequence of intervals which intersect with the given newInterval.
# Note that if max(a,c) > min(b,d), then the intervals do not overlap. Otherwise, they overlap.
# Once we figure out the intervals ( interval[i] to interval[j] ) which overlap with newInterval,
# note that we can replace all the overlapping intervals with one interval which would be
# (min(interval[i].start, newInterval.start), max(interval[j].end, newInterval.end)).

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        start = newInterval.start
        end = newInterval.end
        right = left = 0
        while right < len(intervals):
            if start <= intervals[right].end:
                if end < intervals[right].start:
                    break
                start = min(start, intervals[right].start)
                end = max(end, intervals[right].end)
            else:
                left += 1
            right += 1
        return intervals[:left] + [Interval(start, end)] + intervals[right:]


s = Solution()
print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 9]))
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


"""
You’re given a read only array of n integers.
Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.
If so, return the integer. If not, return -1.
If there are multiple solutions, return any one.
Example :
Input : [1 2 3 1 1]
Output : 1
1 occurs 3 times which is more than 5/3 times.
"""


# It is important to note that if at a given time,
# you have 3 distinct element from the array, if you remove them from the array, your answer does not change.
# Assume that we maintain 2 elements with their counts as we traverse along the array.
# When we encounter a new element, there are 3 cases possible :
# We don’t have 2 elements yet. So add this to the list with count as 1.
# This element is different from the existing 2 elements. As we said before, we have 3 distinct numbers now.
# Removing them does not change the answer. So decrement 1 from count of 2 existing elements.
# If their count falls to 0, obviously its not a part of 2 elements anymore.
# The new element is same as one of the 2 elements. Increment the count of that element.
# Consequently, the answer will be one of the 2 elements left behind.
# If they are not the answer, then there is no element with count > N / 3.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n = len(A)
        l = n / 3

        maj1 = 0
        maj2 = 0
        first = float('inf')
        second = float('inf')

        for i in range(n):
            if first == A[i]:
                maj1 += 1
            elif second == A[i]:
                maj2 += 1
            elif maj1 == 0:
                maj1 += 1
                first = A[i]
            elif maj2 == 0:
                maj2 += 1
                second = A[i]
            else:
                maj1 -= 1
                maj2 -= 1

        maj1 = 0
        maj2 = 0

        for i in range(n):
            if A[i] == first:
                maj1 += 1
            elif A[i] == second:
                maj2 += 1

        if maj1 > l:
            return first
        if maj2 > l:
            return second
        return -1


s = Solution()
print(s.repeatedNumber([1, 2, 3, 1, 1]))
print(s.repeatedNumber([4, 2, 5, 3, 1]))
"""
Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

Example:

If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124.

 NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer.
For example, for this problem, following are some good questions to ask :
Q : Can the input have 0’s before the most significant digit. Or in other words, is 0 1 2 3 a valid input?
A : For the purpose of this question, YES
Q : Can the output have 0’s before the most significant digit? Or in other words, is 0 1 2 4 a valid output?
A : For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        num = int(''.join([str(val) for val in A])) + 1
        return [int(val) for val in str(num)]

    def plusOne_editorial(self, A):
        val = 1;
        for i in range(len(A), 0, -1):
            val = val + A[i - 1]
            borrow = int(val / 10)
            if borrow == 0:
                A[i - 1] = val
                break;
            else:
                A[i - 1] = val % 10
                val = borrow
        A = [borrow] + A  # Not sure what this does!
        while A[0] == 0:
            del A[0]
        return A


s = Solution()
print(s.plusOne([1, 2, 3, 4]))
print(s.plusOne([0, 0, 1, 2, 3, 4]))
"""
Find Duplicate in Array
Asked in:
Amazon
VMWare
Riverbed
Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.

Sample Input:

[3 4 1 4 1]
Sample Output:

1
If there are multiple possible answers ( like in the sample case above ), output any one.

If there is no duplicate, output -1
"""


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        B = list(A)
        B.append(0)
        for val in B:
            if B[abs(val)] < 0:
                return abs(val)
            else:
                B[abs(val)] *= -1
        return -1

    def repeatedNumber_editorial(self, A):
        if len(A) == 0:
            return -1
        p1 = A[-1]
        p2 = A[p1 - 1]
        while p1 != p2:
            p1 = A[p1 - 1]
            p2 = A[A[p2 - 1] - 1]
        p2 = 0
        while p1 != p2:
            p1 = A[p1 - 1]
            p2 = A[p2 - 1]
        return p2


s = Solution()
print(s.repeatedNumber2([247, 240, 303, 9, 304, 105, 44, 204, 291, 26, 242, 2, 358, 264, 176, 289, 196, 329,
                         189, 102, 45, 111, 115, 339, 74, 200, 34, 201, 215, 173, 107, 141, 71, 125, 6, 241,
                         275, 88, 91, 58, 171, 346, 219, 238, 246, 10, 118, 163, 287, 179, 123, 348, 283, 313,
                         226, 324, 203, 323, 28, 251, 69, 311, 330, 316, 320, 312, 50, 157, 342, 12, 253, 180,
                         112, 90, 16, 288, 213, 273, 57, 243, 42, 168, 55, 144, 131, 38, 317, 194, 355, 254, 202,
                         351, 62, 80, 134, 321, 31, 127, 232, 67, 22, 124, 271, 231, 162, 172, 52, 228, 87, 174,
                         307, 36, 148, 302, 198, 24, 338, 276, 327, 150, 110, 188, 309, 354, 190, 265, 3, 108,
                         218, 164, 145, 285, 99, 60, 286, 103, 119, 29, 75, 212, 290, 301, 151, 17, 147, 94,
                         138, 272, 279, 222, 315, 116, 262, 1, 334, 41, 54, 208, 139, 332, 89, 18, 233, 268,
                         7, 214, 20, 46, 326, 298, 101, 47, 236, 216, 359, 161, 350, 5, 49, 122, 345, 269, 73,
                         76, 221, 280, 322, 149, 318, 135, 234, 82, 120, 335, 98, 274, 182, 129, 106, 248, 64,
                         121, 258, 113, 349, 167, 192, 356, 51, 166, 77, 297, 39, 305, 260, 14, 63, 165, 85, 224,
                         19, 27, 177, 344, 33, 259, 292, 100, 43, 314, 170, 97, 4, 78, 310, 61, 328, 199, 255, 159,
                         185, 261, 229, 11, 295, 353, 186, 325, 79, 142, 223, 211, 152, 266, 48, 347, 21, 169, 65,
                         140, 83, 156, 340, 56, 220, 130, 117, 143, 277, 235, 59, 205, 153, 352, 300, 114, 84, 183,
                         333, 230, 197, 336, 244, 195, 37, 23, 206, 86, 15, 187, 181, 308, 109, 293, 128, 66, 270,
                         209, 158, 32, 25, 227, 191, 35, 40, 13, 175, 146, 299, 207, 217, 281, 30, 357, 184, 133,
                         245, 284, 343, 53, 210, 306, 136, 132, 239, 155, 73, 193, 278, 257, 126, 331, 294, 250,
                         252, 263, 92, 267, 282, 72, 95, 337, 154, 319, 341, 70, 81, 68, 160, 8, 249, 96, 104,
                         137, 256, 93, 178, 296, 225, 237]))
"""
You are in an infinite 2D grid where you can move in any of the 8 directions :

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points.
Give the minimum number of steps in which you can achieve it. You start from the first point.

Input :

Given two integer arrays A and B, where A[i] is x coordinate and B[i] is y coordinate of ith point respectively.
Output :

Return an Integer, i.e minimum number of steps.
Example :

Input : [(0, 0), (1, 1), (1, 2)]
Output : 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).

This question is intentionally left slightly vague.
Clarify the question by trying out a few cases in the “See Expected Output” section.
"""


class Solution:
    def coverPoints(self, A, B):
        prev_x, prev_y, total = A[0], B[0], 0
        for curr_x, curr_y in zip(A, B):
            dx, dy = abs(curr_x - prev_x), abs(curr_y - prev_y)
            if dx < dy:
                total += dy
            else:
                total += dx
            prev_x, prev_y = curr_x, curr_y
        return total


A = [0, 1, 1]
B = [0, 1, 2]
P = [(0, 0), (1, 1), (1, 2)]
s = Solution()
print(s.coverPoints(A, B))
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
"""
Max Non Negative SubArray
Asked in:
Google
Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.

The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array.

Find and return the required subarray.

NOTE:

    1. If there is a tie, then compare with segment's length and return segment which has maximum length.
    2. If there is still a tie, then return the segment with minimum starting index.


Input Format:

The first and the only argument of input contains an integer array A, of length N.
Output Format:

Return an array of integers, that is a subarray of A that satisfies the given conditions.
Constraints:

1 <= N <= 1e5
1 <= A[i] <= 1e5
Examples:

Input 1:
    A = [1, 2, 5, -7, 2, 3]

Output 1:
    [1, 2, 5]

Explanation 1:
    The two sub-arrays are [1, 2, 5] [2, 3].
    The answer is [1, 2, 5] as its sum is larger than [2, 3].

Input 2:
    A = [10, -1, 2, 3, -4, 100]

Output 2:
    [100]

Explanation 2:
    The three sub-arrays are [10], [2, 3], [100].
    The answer is [100] as its sum is larger than the other two.
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    # Approach: Maintain 2 dictionaries with values of the start index, end index,
    # sum and length for the current and max
    # Append(-1) to avoid handling end of array separately
    def maxset(self, A):
        # Edge case
        if len(A) == 1:
            return A if A[0] > 0 else []

        A.append(-1)
        # Dict to store various useful intermediary values to reach the solution
        val_now = {
            'inx_low': -1,
            'inx_high': -1,
            'sum': 0,
            'len': 0
        }
        val_max = val_now.copy()

        for idx, val in enumerate(A):
            if val > -1:
                if val_now['inx_low'] == -1:
                    val_now['inx_low'] = idx
                val_now['sum'] += val
                val_now['len'] += 1
            else:
                # Encountered first -ve value
                if val_now['inx_low'] != -1:  # If `val_now` is set
                    val_now['inx_high'] = idx - 1  # Set `ind_high`
                    if val_now['sum'] > val_max['sum'] or \
                            (val_now['sum'] == val_max['sum'] and val_now['len'] > val_max['len']):
                        val_max = val_now.copy()

                    # Reset `val_now`
                    val_now['sum'] = val_now['len'] = 0
                    val_now['inx_low'] = val_now['inx_high'] = -1
                # Consecutive -ve value found
                else:
                    pass  # Do nothing
        return A[val_max['inx_low']: val_max['inx_high'] + 1]

    # Approach: Maintain just indices with values of the start index, end index, sum and length for the current and max
    # Edge cases don't need to be handled separately
    def maxset_billbezos(self, A):
        s, j = 0, 0
        a, b, max_s = 0, -1, 0
        A.append(float('-inf'))
        for i in range(len(A)):
            if A[i] < 0:
                if s > max_s or (s == max_s and i - j > b - a):
                    a, b, max_s = j, i - 1, s
                j, s = i + 1, 0
            else:
                s += A[i]
        return A[a:b + 1]


s = Solution()
print(s.maxset([1, 2, 5, -7, -18, 2, 3, 8]))
print(s.maxset_billbezos([1, 2, 5, -7, -18, 2, 3, -3, 8]))
"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
You need to do this in place.
Note that if you end up using an additional array, you will only receive partial score.
Example:
If the array is
[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:
[
    [3, 1],
    [4, 2]
]
"""


class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        # transpose the matrix
        for i in range(len(A)):
            for j in range(i, len(A)):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        N = len(A)
        print(A)
        # swap columns moving inwards from outwards
        for i in range(N // 2):
            for j in range(N):
                A[j][i], A[j][N - 1 - i] = A[j][N - 1 - i], A[j][i]
        return (A)


A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

s = Solution()
print(s.rotate(A))
"""
Given an index k, return the kth row of the Pascal’s triangle.
Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.
Example:
Input : k = 3
Return : [1,3,3,1]
NOTE : k is 0 based. k = 0, corresponds to the row [1].
Note:Could you optimize your algorithm to use only O(k) extra space?
"""


class Solution:

    def getRow(self, A):
        if A == 0:
            return [1]
        x = [1] * (A + 1)
        for i in range(1, A):
            x[i] = x[i - 1] * (A + 1 - i) // i
        return x


s = Solution()
print(s.getRow(5))
"""
Given an unsorted integer array, find the first missing positive integer.
Example:
Given [1,2,0] return 3,
[3,4,-1,1] return 2,
[-8, -7, -6] returns 1
Your algorithm should run in O(n) time and use constant space.
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        A = list(filter(lambda x: x > 0, A))
        # print(A)
        A = [len(A) + 2] + A  # Add the next number. This is for proper indexing (zero based).
        # print(A)
        for i, num in enumerate(A):
            num = abs(num)
            if num < len(A):
                A[num] = - abs(A[num])
        # print(A)
        for i in range(1, len(A)):
            if A[i] > 0:
                return i
        return len(A)


s = Solution()
s.firstMissingPositive([3, 5, 2, 1])
"""
Given a collection of intervals, merge all overlapping intervals.
For example:
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
Make sure the returned intervals are sorted.
"""


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        res = []
        for interval in sorted(intervals, key=lambda x: x.start):
            if res and interval.start <= res[-1].end:
                res[-1].end = max(interval.end, res[-1].end)
            else:
                res.append(interval)
        return res


"""
Find the contiguous subarray within an array, A of length N which has the largest sum.
Input Format:
The first and the only argument contains an integer array, A.
Output Format:
Return an integer representing the maximum possible sum of the contiguous subarray.
Constraints:
1 <= N <= 1e6
-1000 <= A[i] <= 1000
For example:
Input 1:
    A = [1, 2, 3, 4, -10]
Output 1:
    10
Explanation 1:
    The subarray [1, 2, 3, 4] has the maximum possible sum of 10.
Input 2:
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output 2:
    6
Explanation 2:
    The subarray [4,-1,2,1] has the maximum possible sum of 6.
"""

inf = float('inf')


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        if not A:
            return 0
        max_so_far, max_sum = 0, -inf
        for val in A:
            max_so_far += val
            max_sum = max(max_so_far, max_sum)
            # Doing this last, to handle case
            # when all numbers are negative.
            max_so_far = max(max_so_far, 0)
        return max_sum


s = Solution()
print(s.maxSubArray([1, 2, 3, 4, -10]))
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
"""
Given an integer array, find if an integer p exists in the array such
that the number of integers greater than p in the array equals to p
If such an integer is found return 1 else return -1.
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        n = len(A)
        for i in range(n - 1):
            # When certain element repeats many times.
            if A[i] == A[i + 1]:
                continue
            if A[i] == n - i - 1:
                return 1
        if A[n - 1] == 0:
            return 1
        return -1


"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
Try to solve it in linear time/space.
Example :
Input : [1, 10, 5]
Output : 5
Return 0 if the array contains less than 2 elements.
You may assume that all the elements in the array are non-negative integers and fit in the 32-bit signed integer range.
You may also assume that the difference will not overflow.
"""


# So, we know now that our answer will lie in the range [gap, MAX - MIN].
# Now, if we know the answer is more than gap, what we do is create buckets of size gap for ranges
# [MIN, MIN + gap), [Min + gap, `MIN` + 2* gap) ... and so on
# There will only be (N-1) such buckets. We place the numbers in these buckets based on their value.
# If you pick any 2 numbers from a single bucket, their difference will be less than gap, and
# hence they would never contribute to maxgap ( Remember maxgap >= gap ). We only need to store the largest
# number and the smallest number in each bucket, and we only look at the numbers across bucket.
# Now, we just need to go through the bucket sequentially ( they are already sorted by value ),
# and get the difference of min_value with max_value of previous bucket with at least one value.
# We take maximum of all such values.


class Solution:
    def maximumGap(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) < 2:
            return 0
        min_v, max_v = min(arr), max(arr)
        if max_v - min_v < 2:
            return max_v - min_v
        min_gap = max(1, (max_v - min_v) // (len(arr)))  # The minimum possible gap
        sentinel_min, sentinel_max = 2 ** 32 - 1, -1
        buckets_min = [sentinel_min] * len(arr)
        buckets_max = [sentinel_max] * len(arr)
        for x in arr:
            i = min((x - min_v) // min_gap, len(arr) - 1)
            buckets_min[i] = min(buckets_min[i], x)
            buckets_max[i] = max(buckets_max[i], x)
        max_gap = 0
        prev_max = buckets_max[0]  # First gap is always non-empty
        for i in range(1, len(arr)):
            if buckets_min[i] == sentinel_min:
                continue
            max_gap = max(buckets_min[i] - prev_max, max_gap)
            prev_max = buckets_max[i]
        return max_gap


"""
You are given an array A containing N integers. The special product of each ith integer in this array
is defined as the product of the following:<ul>
LeftSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (i>j). If multiple A[j]’s are
present in multiple positions, the LeftSpecialValue is the maximum value of j.
RightSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (j>i). If multiple A[j]s are
present in multiple positions, the RightSpecialValue is the minimum value of j.
Write a program to find the maximum special product of any integer in the array.
Input: You will receive array of integers as argument to function.
Return: Maximum special product of any integer in the array modulo 1000000007.
Note: If j does not exist, the LeftSpecialValue and RightSpecialValue are considered to be 0.
Constraints 1 <= N <= 10^5 1 <= A[i] <= 10^9
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        n = len(A)
        if n < 3:
            return 0
        rightspval = [0] * n
        leftspval = [0] * n
        stack = []

        stack.append(0)
        for i in range(1, n):
            while stack and A[stack[-1]] < A[i]:
                rightspval[stack.pop()] = i
            stack.append(i)
        stack.clear()

        stack.append(n - 1)
        for i in range(n - 1, -1, -1):
            while stack and A[stack[-1]] < A[i]:
                leftspval[stack.pop()] = i
            stack.append(i)
        del (stack)

        maxi = -1
        for i in range(n):
            maxi = max(maxi, leftspval[i] * rightspval[i])
        return maxi % 1000000007


"""
Given numRows, generate the first numRows of Pascal’s triangle.
Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.
Example:
Given numRows = 5,
Return
[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]
"""


# For Row i, Row[i][0] = Row[i][i] = 1. And Row[i][j] = Row[i-1][j] + Row[i-1][j-1], when j belongs to [1, i)
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        if A <= 0:
            return []
        result = [[1]]
        for r in range(1, A):
            row = [1]
            for i in range(1, r):
                row.append(result[r - 1][i - 1] + result[r - 1][i])
            row.append(1)
            result.append(row)
        return result


s = Solution()
print(s.generate(5))
"""
A hotel manager has to process N advance bookings of rooms for the next season.
His hotel has K rooms. Bookings contain an arrival date and a departure date.
He wants to find out whether there are enough rooms in the hotel to satisfy the demand.
Write a program that solves this problem in time O(N log N) .
Input:
First list for arrival time of booking.
Second list for departure time of booking.
Third is K which denotes count of rooms.
Output:
A boolean which tells whether its possible to make a booking.
Return 0/1 for C programs.
O -> No there are not enough rooms for N booking.
1 -> Yes there are enough rooms for N booking.
Example :
Input :
        Arrivals :   [1 3 5]
        Departures : [2 6 8]
        K : 1
Return : False / 0
At day = 5, there are 2 guests in the hotel. But I have only one room.
"""


class Solution:
    def hotel(self, arrive, depart, K):
        # Elegantly done using arrival as 1 and departure as 0
        events = [(t, 1) for t in arrive] + [(t, 0) for t in depart]
        events = sorted(events)
        guests = 0
        for event in events:
            if event[1] == 1:
                guests += 1
            else:
                guests -= 1
            if guests > K:
                return 0
        return 1


s = Solution()
print(s.hotel([1, 3, 5], [2, 6, 8], 1))
"""
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].
If there is no solution possible, return -1.
Example :
A : [3 5 4 2]
Output : 2
for the pair (3, 4)
"""


# Since the array is sorted, the values will be all the elements to the right of A[i].
# Since we want to maximize index[j] - index[i], and index[i] is fixed,
# we are essentially looking at max index[j] for all j > i.
# The problem concludes to finding the max in all the suffix of the array.
# We can preprocess the index array and let indexMax[i] store the maximum of index[i….len]


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if len(A) == 0:
            return -1
        # arr[i][j] = max distance starting from i and including up to j
        index = list(range(len(A)))
        index.sort(key=lambda x: A[x])  # Indices of elements in the sorted array
        print(index)
        largest_distance = 0
        max_index_from_i = [index[-1]] * len(A)  # Preprocessed array
        i = len(A) - 2
        while i >= 0:
            max_index_from_i[i] = max(max_index_from_i[i + 1], index[i])
            i -= 1
        for i in range(len(A) - 1):
            largest_distance = max(largest_distance, max_index_from_i[i] - index[i])
        if largest_distance <= 0:
            return 0
        else:
            return largest_distance


s = Solution()
print(s.maximumGap([3, 5, 4, 2]))

"""
Largest Number
Asked in: Amazon, Goldman Sachs, Microsoft

Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9, 91], the largest formed number is 919534330.

Note: The result may be very large, so you need to return a string instead of an integer.

NOTE: You only need to implement the given function. Do not read input, instead use the arguments to the function.
Do not print the output, instead return values as specified. Still have a doubt? Checkout Sample Codes for more details.
"""


class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber_old(self, A):
        # Fails in cases like: 298 29
        # Various padding value were used like 0, 9, last digit, last digit - 1 but they all have issues
        sol_array, max_len, solution = [], 0, ''
        # Finding the max length value
        for val in A:
            if len(str(val)) > max_len:
                max_len = len(str(val))
        # Converting each value to length `max_len` and storing the number of digits appended
        # We are repeating a value less than the last digit for padding, for proper comparison reasons
        for val in A:
            num = val
            if len(str(val)) < max_len:
                num = int(str(val) + str(val % 10) * (max_len - len(str(val))))
            sol_array.append((num, max_len - len(str(val))))

        sol_array = sorted(sol_array, key=lambda x: (-x[0], -x[1]))
        # Generating the solution string by removing the appended digits
        for val in sol_array:
            solution += ' ' + str(val[0]) if val[1] == 0 else ' ' + str(val[0])[:-val[1]]
        return solution

    def largestNumber(self, A):
        import functools
        A = map(str, A)
        res = ''.join(sorted(A, key=functools.cmp_to_key(lambda a, b: 1 if a + b >= b + a else -1), reverse=True))
        return int(res) if res else '0'


s = Solution()
print(s.largestNumber([3, 30, 34, 5, 9]))
print(s.largestNumber([0, 0, 0, 0, 0]))
print(s.largestNumber([12, 121]))
print(s.largestNumber([9, 99, 999, 9999, 9998]))
print(s.largestNumber([782, 240, 409, 678, 940, 502, 113, 686, 6, 825, 366, 686, 877, 357,
                       261, 772, 798, 29, 337, 646, 868, 974, 675, 271, 791, 124, 363, 298,
                       470, 991, 709, 533, 872, 780, 735, 19, 930, 895, 799, 395, 905]))

"""
Given an array of real numbers greater than zero in form of strings.
Find if there exists a triplet (a,b,c) such that 1 < a+b+c < 2 .
Return 1 for true or 0 for false.
Example:
Given [0.6, 0.7, 0.8, 1.2, 0.4] ,
You should return 1
as
0.6+0.7+0.4=1.7
1<1.7<2
Hence, the output is 1.
O(n) solution is expected.
Note: You can assume the numbers in strings don’t overflow the primitive data type and
there are no leading zeroes in numbers. Extra memory usage is allowed.
"""


class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        n = len(A)
        a = float(A[0])
        b = float(A[1])
        c = float(A[2])
        for i in range(3, n):
            if 1 < (a + b + c) < 2:
                return 1
            elif (a + b + c) > 2:
                # If overflow, replace the max
                if a > b and a > c:
                    a = float(A[i])
                elif b > a and b > c:
                    b = float(A[i])
                elif c > a and c > b:
                    c = float(A[i])
            else:
                # If underflow, replace the min
                if a < b and a < c:
                    a = float(A[i])
                elif b < a and b < c:
                    b = float(A[i])
                elif c < a and c < b:
                    c = float(A[i])
        return 1 if 1 < (a + b + c) < 2 else 0


s = Solution()
print(s.solve([0.6, 0.7, 0.8, 1.2, 0.4]))
"""
You are given a binary string(i.e. with characters 0 and 1) S consisting of characters S1, S2, …, SN.
In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and
flip the characters SL, SL+1, …, SR. By flipping, we mean change character 0 to 1 and vice-versa.
Your aim is to perform ATMOST one operation such that in final string number of 1s is maximised.
If you don’t want to perform the operation, return an empty array. Else, return an array consisting of two
elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.
Notes:
Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.
For example,
S = 010
Pair of [L, R] | Final string
_______________|_____________
[1 1]          | 110
[1 2]          | 100
[1 3]          | 101
[2 2]          | 000
[2 3]          | 001
We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].
Another example,
If S = 111
No operation can give us more than three 1s in final string. So, we return empty array [].
"""


# Say it has A 0s and B 1s. Eventually, there are B 0s and A 1s.
# So, number of 1s increase by A - B. We want to choose a subarray which maximises this.
# Note, if we change 1s to -1, then sum of values will give us A - B.
# Then, we have to find a subarray with maximum sum, which can be done via Kadane’s Algorithm.

class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        max_diff = 0
        diff = 0
        start = 0
        ans = None

        for i, a in enumerate(A):
            diff += (1 if a is '0' else -1)

            if diff < 0:
                diff = 0
                start = i + 1
                continue

            if diff > max_diff:
                max_diff = diff
                ans = [start, i]

        if ans is None:
            return []
        return list(map(lambda x: x + 1, ans))


s = Solution()
print(s.flip('010'))
"""
Given a matrix, A of size M x N of 0s and 1s. If an element is 0, set its entire row and column to 0.
Note: This will be evaluated on the extra memory used. Try to minimize the space and time complexity.
Input Format:
The first and the only argument of input contains a 2-d integer matrix, A, of size M x N.
Output Format:
Return a 2-d matrix that satisfies the given conditions.
Constraints:
1 <= N, M <= 1000
0 <= A[i][j] <= 1
Examples:
Input 1:
    [   [1, 0, 1],
        [1, 1, 1],
        [1, 1, 1]   ]
Output 1:
    [   [0, 0, 0],
        [1, 0, 1],
        [1, 0, 1]   ]
Input 2:
    [   [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1]   ]
Output 2:
    [   [0, 0, 0],
        [1, 0, 1],
        [0, 0, 0]   ]
"""


# Now, if R = 0, your job is simple. In the end, mark every element in the first row as 0.
# If R = 1, then leave the row as it is

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        col, row = set(), set()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    row.add(i)
                    col.add(j)

        t = [0] * len(A[0])
        for r in row:
            A[r] = t

        for c in col:
            for i in range(len(A)):
                A[i][c] = 0

        return A

    class Solution:
        # @param A : list of list of integers
        # @return the same list modified
        def setZeroes(self, A):
            N = len(A)
            M = len(A[0])
            del_first_row = False
            del_first_col = False

            for i in range(N):
                if A[i][0] == 0:
                    del_first_row = True
                    break
            for i in range(M):
                if A[0][i] == 0:
                    del_first_col = True
                    break

            for i in range(N):
                for j in range(M):
                    if A[i][j] == 0:
                        A[i][0] = 2
                        A[0][j] = 2

            for i in range(1, N):
                for j in range(1, M):
                    if A[i][0] == 2:
                        A[i][j] = 0
                    elif A[0][j] == 2:
                        A[i][j] = 0
            for i in range(N):
                if A[i][0] > 1 or del_first_row:
                    A[i][0] = 0
            for i in range(M):
                if A[0][i] > 1 or del_first_col:
                    A[0][i] = 0

            return A


"""
Next Permutation
Asked in: Microsoft Amazon
Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers for a given array A of size N.

If such arrangement is not possible, it must be rearranged as the lowest possible order i.e., sorted in an ascending order.
Note:
1. The replacement must be in-place, do **not** allocate extra memory.
2. DO NOT USE LIBRARY FUNCTION FOR NEXT PERMUTATION. Use of Library functions will disqualify your submission retroactively and will give you penalty points.
Input Format:

The first and the only argument of input has an array of integers, A.
Output Format:
Return an array of integers, representing the next permutation of the given array.
Constraints:

1 <= N <= 5e5
1 <= A[i] <= 1e9
Examples:

Input 1:
    A = [1, 2, 3]

Output 1:
    [1, 3, 2]

Input 2:
    A = [3, 2, 1]

Output 2:
    [1, 2, 3]

Input 3:
    A = [1, 1, 5]

Output 3:
    [1, 5, 1]

Input 4:
    A = [20, 50, 113]

Output 4:
    [20, 113, 50]
"""


class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        for idx in range(len(A) - 1, -1, -1):
            if idx > 0:
                # Last part should be reverse sorted (in descending order)
                if A[idx] < A[idx - 1]:
                    continue
                # Found the position to generate the next permutation
                else:
                    # Find a number in sorted array which is greater than element at `idx-1`
                    idx_swap = 1
                    while A[len(A) - idx_swap] < A[idx - 1]:
                        idx_swap += 1
                    A[idx - 1], A[len(A) - idx_swap] = A[len(A) - idx_swap], A[idx - 1]
                    A[idx:len(A)] = reversed(A[idx:len(A)])
                    return A
            # All the array is reverse sorted (in descending order)
            else:
                return sorted(A)


s = Solution()
print(s.nextPermutation([1, 2, 3, 6, 5, 4]))
print(s.nextPermutation([1, 2, 3]))
print(s.nextPermutation([3, 2, 1]))
print(s.nextPermutation([444, 994, 508, 72, 125, 299, 181, 238, 354, 223, 691, 249, 838, 890, 758, 675,
                         424, 199, 201, 788, 609, 582, 979, 259, 901, 371, 766, 759, 983, 728, 220, 16,
                         158, 822, 515, 488, 846, 321, 908, 469, 84, 460, 961, 285, 417, 142, 952, 626,
                         916, 247, 116, 975, 202, 734, 128, 312, 499, 274, 213, 208, 472, 265, 315, 335,
                         205, 784, 708, 681, 160, 448, 365, 165, 190, 693, 606, 226, 351, 241, 526, 311,
                         164, 98, 422, 363, 103, 747, 507, 669, 153, 856, 701, 319, 695, 52
                         ]))
"""
You are given an array (zero indexed) of N non-negative integers, A0, A1 ,…, AN-1.
Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order) that sub array,
then the whole array should get sorted.
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


"""
Given a positive integer n and a string s consisting only of letters D or I, you have to find any permutation of
first n positive integer that satisfy the given input string.
D means the next number is smaller, while I means the next number is greater.
Notes:
Length of given string s will always equal to n - 1
Your solution should run in linear time and space.
Example :
Input 1:
n = 3
s = ID
Return: [1, 3, 2]
"""


class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        mn, mx = 1, B
        result = []
        for x in A:
            if x == 'D':
                result.append(mx)
                mx -= 1
            elif x == 'I':
                result.append(mn)
                mn += 1
        result.append(mn)
        return result


s = Solution()
print(s.findPerm('DIDD', 5))
"""
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.
Input Format:
The first and the only argument contains an integer, A.
Output Format:
Return a 2-d matrix of size A x A satisfying the spiral order.
Constraints:
1 <= A <= 1000
Examples:
Input 1:
    A = 3
Output 1:
    [   [ 1, 2, 3 ],
        [ 8, 9, 4 ],
        [ 7, 6, 5 ]   ]
Input 2:
    4
Output 2:
    [   [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]   ]
"""


class Direction(object):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3


class Solution:
    # @param A :
    # @return a list of integers
    def generateMatrix(self, A):
        result = [[0] * A for _ in range(A)]
        t, b, l, r = 0, A - 1, 0, A - 1
        direction = Direction.EAST
        lastN = 1
        while t <= b and l <= r:
            if direction is Direction.EAST:
                # A[t][l:r + 1]
                for col in range(l, r + 1):
                    result[t][col] = lastN
                    lastN += 1
                t += 1
            elif direction is Direction.SOUTH:
                # A[r][t:b + 1]
                for row in range(t, b + 1):
                    result[row][r] = lastN
                    lastN += 1
                r -= 1
            elif direction is Direction.WEST:
                # reversed(A[b][l:r + 1])
                for col in reversed(range(l, r + 1)):
                    result[b][col] = lastN
                    lastN += 1
                b -= 1
            elif direction is Direction.NORTH:
                for row in reversed(range(t, b + 1)):
                    result[row][l] = lastN
                    lastN += 1
                l += 1
            direction = (direction + 1) % 4
        return result


s = Solution()
print(s.generateMatrix(4))

#####		Pascal Triangle		#####

"""
Given numRows, generate the first numRows of Pascal’s triangle.
Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.
Example:
Given numRows = 5,
Return
[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]
"""


# For Row i, Row[i][0] = Row[i][i] = 1. And Row[i][j] = Row[i-1][j] + Row[i-1][j-1], when j belongs to [1, i)
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        if A <= 0:
            return []
        result = [[1]]
        for r in range(1, A):
            row = [1]
            for i in range(1, r):
                row.append(result[r - 1][i - 1] + result[r - 1][i])
            row.append(1)
            result.append(row)
        return result


s = Solution()
print(s.generate(5))

#####		Hotel Bookings Possible		#####

"""
A hotel manager has to process N advance bookings of rooms for the next season.
His hotel has K rooms. Bookings contain an arrival date and a departure date.
He wants to find out whether there are enough rooms in the hotel to satisfy the demand.
Write a program that solves this problem in time O(N log N) .
Input:
First list for arrival time of booking.
Second list for departure time of booking.
Third is K which denotes count of rooms.
Output:
A boolean which tells whether its possible to make a booking.
Return 0/1 for C programs.
O -> No there are not enough rooms for N booking.
1 -> Yes there are enough rooms for N booking.
Example :
Input :
        Arrivals :   [1 3 5]
        Departures : [2 6 8]
        K : 1
Return : False / 0
At day = 5, there are 2 guests in the hotel. But I have only one room.
"""


class Solution:
    def hotel(self, arrive, depart, K):
        # Elegantly done using arrival as 1 and departure as 0
        events = [(t, 1) for t in arrive] + [(t, 0) for t in depart]
        events = sorted(events)
        guests = 0
        for event in events:
            if event[1] == 1:
                guests += 1
            else:
                guests -= 1
            if guests > K:
                return 0
        return 1


s = Solution()
print(s.hotel([1, 3, 5], [2, 6, 8], 1))

#####		Max Distance		#####

"""
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].
If there is no solution possible, return -1.
Example :
A : [3 5 4 2]
Output : 2
for the pair (3, 4)
"""


# Since the array is sorted, the values will be all the elements to the right of A[i].
# Since we want to maximize index[j] - index[i], and index[i] is fixed,
# we are essentially looking at max index[j] for all j > i.
# The problem concludes to finding the max in all the suffix of the array.
# We can preprocess the index array and let indexMax[i] store the maximum of index[i….len]


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if len(A) == 0:
            return -1
        # arr[i][j] = max distance starting from i and including up to j
        index = list(range(len(A)))
        index.sort(key=lambda x: A[x])  # Indices of elements in the sorted array
        print(index)
        largest_distance = 0
        max_index_from_i = [index[-1]] * len(A)  # Preprocessed array
        i = len(A) - 2
        while i >= 0:
            max_index_from_i[i] = max(max_index_from_i[i + 1], index[i])
            i -= 1
        for i in range(len(A) - 1):
            largest_distance = max(largest_distance, max_index_from_i[i] - index[i])
        if largest_distance <= 0:
            return 0
        else:
            return largest_distance


s = Solution()
print(s.maximumGap([3, 5, 4, 2]))

#####		Largest Number		#####

"""
Largest Number
Asked in: Amazon, Goldman Sachs, Microsoft

Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9, 91], the largest formed number is 919534330.

Note: The result may be very large, so you need to return a string instead of an integer.

NOTE: You only need to implement the given function. Do not read input, instead use the arguments to the function.
Do not print the output, instead return values as specified. Still have a doubt? Checkout Sample Codes for more details.
"""


class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber_old(self, A):
        # Fails in cases like: 298 29
        # Various padding value were used like 0, 9, last digit, last digit - 1 but they all have issues
        sol_array, max_len, solution = [], 0, ''
        # Finding the max length value
        for val in A:
            if len(str(val)) > max_len:
                max_len = len(str(val))
        # Converting each value to length `max_len` and storing the number of digits appended
        # We are repeating a value less than the last digit for padding, for proper comparison reasons
        for val in A:
            num = val
            if len(str(val)) < max_len:
                num = int(str(val) + str(val % 10) * (max_len - len(str(val))))
            sol_array.append((num, max_len - len(str(val))))

        sol_array = sorted(sol_array, key=lambda x: (-x[0], -x[1]))
        # Generating the solution string by removing the appended digits
        for val in sol_array:
            solution += ' ' + str(val[0]) if val[1] == 0 else ' ' + str(val[0])[:-val[1]]
        return solution

    def largestNumber(self, A):
        import functools
        A = map(str, A)
        res = ''.join(sorted(A, key=functools.cmp_to_key(lambda a, b: 1 if a + b >= b + a else -1), reverse=True))
        return int(res) if res else '0'


s = Solution()
print(s.largestNumber([3, 30, 34, 5, 9]))
print(s.largestNumber([0, 0, 0, 0, 0]))
print(s.largestNumber([12, 121]))
print(s.largestNumber([9, 99, 999, 9999, 9998]))
print(s.largestNumber([782, 240, 409, 678, 940, 502, 113, 686, 6, 825, 366, 686, 877, 357,
                       261, 772, 798, 29, 337, 646, 868, 974, 675, 271, 791, 124, 363, 298,
                       470, 991, 709, 533, 872, 780, 735, 19, 930, 895, 799, 395, 905]))

#####		Triplets With Sum Between Given Range		#####

"""
Given an array of real numbers greater than zero in form of strings.
Find if there exists a triplet (a,b,c) such that 1 < a+b+c < 2 .
Return 1 for true or 0 for false.
Example:
Given [0.6, 0.7, 0.8, 1.2, 0.4] ,
You should return 1
as
0.6+0.7+0.4=1.7
1<1.7<2
Hence, the output is 1.
O(n) solution is expected.
Note: You can assume the numbers in strings don’t overflow the primitive data type and
there are no leading zeroes in numbers. Extra memory usage is allowed.
"""


class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        n = len(A)
        a = float(A[0])
        b = float(A[1])
        c = float(A[2])
        for i in range(3, n):
            if 1 < (a + b + c) < 2:
                return 1
            elif (a + b + c) > 2:
                # If overflow, replace the max
                if a > b and a > c:
                    a = float(A[i])
                elif b > a and b > c:
                    b = float(A[i])
                elif c > a and c > b:
                    c = float(A[i])
            else:
                # If underflow, replace the min
                if a < b and a < c:
                    a = float(A[i])
                elif b < a and b < c:
                    b = float(A[i])
                elif c < a and c < b:
                    c = float(A[i])
        return 1 if 1 < (a + b + c) < 2 else 0


s = Solution()
print(s.solve([0.6, 0.7, 0.8, 1.2, 0.4]))

#####		Flip		#####

"""
You are given a binary string(i.e. with characters 0 and 1) S consisting of characters S1, S2, …, SN.
In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and
flip the characters SL, SL+1, …, SR. By flipping, we mean change character 0 to 1 and vice-versa.
Your aim is to perform ATMOST one operation such that in final string number of 1s is maximised.
If you don’t want to perform the operation, return an empty array. Else, return an array consisting of two
elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.
Notes:
Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.
For example,
S = 010
Pair of [L, R] | Final string
_______________|_____________
[1 1]          | 110
[1 2]          | 100
[1 3]          | 101
[2 2]          | 000
[2 3]          | 001
We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].
Another example,
If S = 111
No operation can give us more than three 1s in final string. So, we return empty array [].
"""


# Say it has A 0s and B 1s. Eventually, there are B 0s and A 1s.
# So, number of 1s increase by A - B. We want to choose a subarray which maximises this.
# Note, if we change 1s to -1, then sum of values will give us A - B.
# Then, we have to find a subarray with maximum sum, which can be done via Kadane’s Algorithm.

class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        max_diff = 0
        diff = 0
        start = 0
        ans = None

        for i, a in enumerate(A):
            diff += (1 if a is '0' else -1)

            if diff < 0:
                diff = 0
                start = i + 1
                continue

            if diff > max_diff:
                max_diff = diff
                ans = [start, i]

        if ans is None:
            return []
        return list(map(lambda x: x + 1, ans))


s = Solution()
print(s.flip('010'))

#####		Set Matrix Zeros		#####

"""
Given a matrix, A of size M x N of 0s and 1s. If an element is 0, set its entire row and column to 0.
Note: This will be evaluated on the extra memory used. Try to minimize the space and time complexity.
Input Format:
The first and the only argument of input contains a 2-d integer matrix, A, of size M x N.
Output Format:
Return a 2-d matrix that satisfies the given conditions.
Constraints:
1 <= N, M <= 1000
0 <= A[i][j] <= 1
Examples:
Input 1:
    [   [1, 0, 1],
        [1, 1, 1],
        [1, 1, 1]   ]
Output 1:
    [   [0, 0, 0],
        [1, 0, 1],
        [1, 0, 1]   ]
Input 2:
    [   [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1]   ]
Output 2:
    [   [0, 0, 0],
        [1, 0, 1],
        [0, 0, 0]   ]
"""


# Now, if R = 0, your job is simple. In the end, mark every element in the first row as 0.
# If R = 1, then leave the row as it is

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        col, row = set(), set()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    row.add(i)
                    col.add(j)

        t = [0] * len(A[0])
        for r in row:
            A[r] = t

        for c in col:
            for i in range(len(A)):
                A[i][c] = 0

        return A

    class Solution:
        # @param A : list of list of integers
        # @return the same list modified
        def setZeroes(self, A):
            N = len(A)
            M = len(A[0])
            del_first_row = False
            del_first_col = False

            for i in range(N):
                if A[i][0] == 0:
                    del_first_row = True
                    break
            for i in range(M):
                if A[0][i] == 0:
                    del_first_col = True
                    break

            for i in range(N):
                for j in range(M):
                    if A[i][j] == 0:
                        A[i][0] = 2
                        A[0][j] = 2

            for i in range(1, N):
                for j in range(1, M):
                    if A[i][0] == 2:
                        A[i][j] = 0
                    elif A[0][j] == 2:
                        A[i][j] = 0
            for i in range(N):
                if A[i][0] > 1 or del_first_row:
                    A[i][0] = 0
            for i in range(M):
                if A[0][i] > 1 or del_first_col:
                    A[0][i] = 0

            return A


#####		Next Permutation		#####

"""
Next Permutation
Asked in: Microsoft Amazon
Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers for a given array A of size N.

If such arrangement is not possible, it must be rearranged as the lowest possible order i.e., sorted in an ascending order.
Note:
1. The replacement must be in-place, do **not** allocate extra memory.
2. DO NOT USE LIBRARY FUNCTION FOR NEXT PERMUTATION. Use of Library functions will disqualify your submission retroactively and will give you penalty points.
Input Format:

The first and the only argument of input has an array of integers, A.
Output Format:
Return an array of integers, representing the next permutation of the given array.
Constraints:

1 <= N <= 5e5
1 <= A[i] <= 1e9
Examples:

Input 1:
    A = [1, 2, 3]

Output 1:
    [1, 3, 2]

Input 2:
    A = [3, 2, 1]

Output 2:
    [1, 2, 3]

Input 3:
    A = [1, 1, 5]

Output 3:
    [1, 5, 1]

Input 4:
    A = [20, 50, 113]

Output 4:
    [20, 113, 50]
"""


class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        for idx in range(len(A) - 1, -1, -1):
            if idx > 0:
                # Last part should be reverse sorted (in descending order)
                if A[idx] < A[idx - 1]:
                    continue
                # Found the position to generate the next permutation
                else:
                    # Find a number in sorted array which is greater than element at `idx-1`
                    idx_swap = 1
                    while A[len(A) - idx_swap] < A[idx - 1]:
                        idx_swap += 1
                    A[idx - 1], A[len(A) - idx_swap] = A[len(A) - idx_swap], A[idx - 1]
                    A[idx:len(A)] = reversed(A[idx:len(A)])
                    return A
            # All the array is reverse sorted (in descending order)
            else:
                return sorted(A)


s = Solution()
print(s.nextPermutation([1, 2, 3, 6, 5, 4]))
print(s.nextPermutation([1, 2, 3]))
print(s.nextPermutation([3, 2, 1]))
print(s.nextPermutation([444, 994, 508, 72, 125, 299, 181, 238, 354, 223, 691, 249, 838, 890, 758, 675,
                         424, 199, 201, 788, 609, 582, 979, 259, 901, 371, 766, 759, 983, 728, 220, 16,
                         158, 822, 515, 488, 846, 321, 908, 469, 84, 460, 961, 285, 417, 142, 952, 626,
                         916, 247, 116, 975, 202, 734, 128, 312, 499, 274, 213, 208, 472, 265, 315, 335,
                         205, 784, 708, 681, 160, 448, 365, 165, 190, 693, 606, 226, 351, 241, 526, 311,
                         164, 98, 422, 363, 103, 747, 507, 669, 153, 856, 701, 319, 695, 52
                         ]))

#####		Max Unsorted Subarray		#####

"""
You are given an array (zero indexed) of N non-negative integers, A0, A1 ,…, AN-1.
Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order) that sub array,
then the whole array should get sorted.
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


#####		Find Permutation		#####

"""
Given a positive integer n and a string s consisting only of letters D or I, you have to find any permutation of
first n positive integer that satisfy the given input string.
D means the next number is smaller, while I means the next number is greater.
Notes:
Length of given string s will always equal to n - 1
Your solution should run in linear time and space.
Example :
Input 1:
n = 3
s = ID
Return: [1, 3, 2]
"""


class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        mn, mx = 1, B
        result = []
        for x in A:
            if x == 'D':
                result.append(mx)
                mx -= 1
            elif x == 'I':
                result.append(mn)
                mn += 1
        result.append(mn)
        return result


s = Solution()
print(s.findPerm('DIDD', 5))

#####		Sprial Order Matrix 2		#####

"""
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.
Input Format:
The first and the only argument contains an integer, A.
Output Format:
Return a 2-d matrix of size A x A satisfying the spiral order.
Constraints:
1 <= A <= 1000
Examples:
Input 1:
    A = 3
Output 1:
    [   [ 1, 2, 3 ],
        [ 8, 9, 4 ],
        [ 7, 6, 5 ]   ]
Input 2:
    4
Output 2:
    [   [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]   ]
"""


class Direction(object):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3


class Solution:
    # @param A :
    # @return a list of integers
    def generateMatrix(self, A):
        result = [[0] * A for _ in range(A)]
        t, b, l, r = 0, A - 1, 0, A - 1
        direction = Direction.EAST
        lastN = 1
        while t <= b and l <= r:
            if direction is Direction.EAST:
                # A[t][l:r + 1]
                for col in range(l, r + 1):
                    result[t][col] = lastN
                    lastN += 1
                t += 1
            elif direction is Direction.SOUTH:
                # A[r][t:b + 1]
                for row in range(t, b + 1):
                    result[row][r] = lastN
                    lastN += 1
                r -= 1
            elif direction is Direction.WEST:
                # reversed(A[b][l:r + 1])
                for col in reversed(range(l, r + 1)):
                    result[b][col] = lastN
                    lastN += 1
                b -= 1
            elif direction is Direction.NORTH:
                for row in reversed(range(t, b + 1)):
                    result[row][l] = lastN
                    lastN += 1
                l += 1
            direction = (direction + 1) % 4
        return result


s = Solution()
print(s.generateMatrix(4))

#########################	backtracking	#########################


#####		Combinations Sum 2		#####

"""
Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.
Each number in C may only be used once in the combination.
Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
Example :
Given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
"""


# Some elements can be repeated in the input set.
# Make sure you iterate over the number of occurrences of those elements to make sure you are not
# counting the same combinations again.


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A.sort()
        ans = set()

        def combinationSumHelper(arr, sumSoFar, index):
            if sumSoFar == B:
                ans.add(tuple(arr))
            elif sumSoFar > B:
                return
            else:
                for i in range(index, len(A)):
                    combinationSumHelper(arr + [A[i]], sumSoFar + A[i], i + 1)

        combinationSumHelper([], 0, 0)

        return list(ans)


#####		Gray Code		#####

"""
The gray code is a binary numeral system where two successive values differ in only one bit.
Given a non-negative integer n representing the total number of bits in the code,
print the sequence of gray code. A gray code sequence must begin with 0.
For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
00 - 0
01 - 1
11 - 3
10 - 2
There might be multiple gray code sequences possible for a given n.
Return any such sequence.
"""


# The bruteforce method would be to start with 0, change any of the bits, keeping track of the numbers
# already constructed. When you run into a number where there is no way forward possible, you backtrack,
# and try to change some other bit instead. This might however be inefficient.
# You can notice that if a sequence is gray code, then its reverse is also a gray code.
# Where 0G(n) means all elements of G(n) prefixed with 0 bit and 1R(n) means all elements of R(n) prefixed with 1.
# Note that last element of G(n) and first element of R(n) is same.

class Solution:
    # input: length of binary words
    # output: list of integers in gray code
    def grayCode(self, n):
        gray_seq = [0, 1]  # gray code for n=1
        for i in range(1, n):  # recursivley extending for n>1
            # 2 ** i gives us 2, 4, 8 ...
            # Reversing at each iteration
            gray_seq += [s + 2 ** i for s in reversed(gray_seq)]
        return gray_seq


s = Solution()
print(s.grayCode(3))

#####		Subset 2		#####

"""
Given a collection of integers that might contain duplicates, S, return all possible subsets.
Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
The subsets must be sorted lexicographically.
Example :
If S = [1,2,2], the solution is:
[
[],
[1],
[1,2],
[1,2,2],
[2],
[2, 2]
]
"""


# This is very similar to the problem where you need to generate subsets for distinct integer.
# However, in this case, because of repetitions, things are not as simple as choosing or rejecting an element.
# Now for the  elements which are repeated you need to iterate over the count of elements
# you are going to include in your subset.

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        ans = []
        A.sort()

        def solution(A, sub_set, i):
            ans.append(sub_set)
            for j in range(i, len(A)):
                if i != j and A[j - 1] == A[j]:
                    continue
                solution(A, sub_set + [A[j]], j + 1)

        solution(A, [], 0)
        return ans


#####		Permutations		#####

"""
Given a collection of numbers, return all possible permutations.
Example:
[1,2,3] will have the following permutations:
[1,2,3]
[1,3,2]
[2,1,3]
[2,3,1]
[3,1,2]
[3,2,1]
NOTE
No two entries in the permutation sequence should be the same.
For the purpose of this problem, assume that all the numbers in the collection are unique.
"""


# Lets say we are at index start then we can swap element at this index with any index>start and permute the
# elements starting from start+1 using recursion. You can swap back the elements at start and index in order
# to maintain the order for next recursive call.

class Solution:

    def helper(self, res, cur, A):
        if not A:  # A == [] # If we've exhausted the array, we would've got a permutation. Append it to result.
            res.append(cur)
            return
        for i in range(len(A)):
            self.helper(res, cur + [A[i]], A[:i] + A[i + 1:])

    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        res = []
        self.helper(res, [], A)
        return res


s = Solution()
print(s.permute([1, 2, 3]))

#####		Kth Permutation Sequence		#####

"""
The set [1,2,3,…,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3 ) :
1. "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"
Given n and k, return the kth permutation sequence.
For example, given n = 3, k = 4, ans = "231"
Good questions to ask the interviewer :
What if n is greater than 10. How should multiple digit numbers be represented in string?
In this case, just concatenate the number to the answer.
so if n = 11, k = 1, ans = "1234567891011"
Whats the maximum value of n and k?
In this case, k will be a positive integer thats less than INT_MAX.
n is reasonable enough to make sure the answer does not bloat up a lot.
"""

# Generating all permutation wont help here. What you can do is try out elements which can you keep at any position.
# If the permutation resulting from keeping this element does not becomes >= k you keep incrementing the element
# to be put.
# Number of permutation possible using n distinct numbers = n!
# Lets first make k 0 based.
# Let us first look at what our first number should be.
# Number of sequences possible with 1 in first position : (n-1)!
# Number of sequences possible with 2 in first position : (n-1)!
# Number of sequences possible with 3 in first position : (n-1)!
# Hence, the number at our first position should be k / (n-1)! + 1 th integer.
# Can we reduce the k and modify the set we pick our numbers from ( initially 1 2 3 … n )
# to call the function for second position onwards ?


import math


class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def getPermutation(self, n, k):
        numbers = list(range(1, n + 1))
        permutation = ''
        k -= 1  # Making it zero based
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])
        return permutation


s = Solution()
print(s.getPermutation(5, 3))

#####		Palindrome Partioning		#####

"""
Given a string s, partition s such that every string of the partition is a palindrome.
Return all possible palindrome partitioning of s.
For example, given s = "aab",
Return
  [
    ["a","a","b"]
    ["aa","b"],
  ]
 Ordering the results in the answer : Entry i will come before Entry j if :
len(Entryi[0]) < len(Entryj[0]) OR
(len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR
*
*
*
(len(Entryi[0]) == len(Entryj[0]) AND … len(Entryi[k] < len(Entryj[k]))
In the given example,
["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa")
"""


# Since, we are listing out all the partitions ( and not counting them), we need to do brute force here.
# When on index i, you incrementally check all substring starting from i for being palindromic.
# If found, you recursively solve the problem for the remaining string and add it to your solution.
# Start this recursion from starting position of the string.
# PS: You can optimize your solution by not computing the answer for same index multiple times using DP.

class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        def checkpal(S):
            return S == S[::-1]

        def recur(S, res, cur):
            if len(S) == 0:
                res += [cur]
            else:
                for i in range(1, len(S) + 1):
                    if checkpal(S[:i]):
                        recur(S[i:], res, cur + [S[:i]])  # cur + [S[:i]] will append this palen and find a bigger one

        res = []
        recur(A, res, [])
        return res


s = Solution()
print(s.partition('aaabc'))

#####		Combinations Sum		#####

"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where
the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.
Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The combinations themselves must be sorted in ascending order.
CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR … (a1 = b1 AND a2 = b2 AND … ai = bi
AND ai+1 > bi+1)
The solution set must not contain duplicate combinations.
Example,
Given candidate set 2,3,6,7 and target 7,
A solution set is:

[2, 2, 3]
[7]
"""


# In every recursion run, you either include the element in the combination or you don’t.
# To account for multiple occurrences of an element, make sure you call the next function without
# incrementing the current index.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A = sorted(list(set(A)))

        def rec(A, s):
            if len(A) == 0: return []
            if s < 0: return []
            if s == 0: return [[]]
            aux = rec(A[1:], s)
            aux2 = rec(A[0:], s - A[0])
            for i in range(len(aux2)):
                aux2[i] = [A[0]] + aux2[i]
            return aux + aux2

        return sorted(rec(A, B))


#####		Subset		#####

"""
"""


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A.sort(reverse=True)
        res = []
        for i in range(len(A)):
            x = [A[i]]
            # Extends(not appends) by adding new entries
            # Each entry is adding in reverse order so higher order entries are created first
            res.extend([x + y for y in res])
            res.append(x)
        res.append([])
        res.reverse()
        return res


s = Solution()
print(s.subsets([1, 2, 3]))

#####		Generate Perenthesis		#####

"""
Generate all Parentheses II
Asked in:
Facebook
Microsoft
Given n pairs of parentheses, write a function to generate
all combinations of well-formed parentheses of length 2*n.
For example, given n = 3, a solution set is:
"((()))", "(()())", "(())()", "()(())", "()()()"
Make sure the returned list of strings are sorted.
"""


class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, n):
        if n == 0:
            return ['']
        res = []
        for i in range(n):
            suffixs = self.generateParenthesis(i)
            res += [
                '(' + p + ')' + suffix for suffix in suffixs
                for p in self.generateParenthesis(n - i - 1)
            ]
        return sorted(res)


#####		Sudoku		#####

"""
Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.'
You may assume that there will be only one unique solution.
A sudoku puzzle, and its solution numbers marked in red.
Example :
For the above given diagrams, the corresponding input to your program will be
[[53..7....], [6..195...], [.98....6.], [8...6...3], [4..8.3..1], [7...2...6], [.6....28.], [...419..5], [....8..79]]
and we would expect your program to modify the above array of array of characters to
[[534678912], [672195348], [198342567], [859761423], [426853791], [713924856], [961537284], [287419635], [345286179]]
"""


class Solution:
    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, A):
        def findempty(grid, row, col):
            # row=0
            col = 0
            for row in range(row, 9):
                for col in range(9):
                    if grid[row][col] == 0:
                        return row, col, True
            return row, col, False

            # CHECK THE 3*3 SMALL GRID

        def checkSmallBox(grid, row, col, num):
            j = col - (col % 3)
            i = row - (row % 3)
            x = i
            y = j
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    if grid[x][y] == num:
                        return False
            return True

        # CHECK HORIZONTAL AND VERTICAL
        def checkXY(grid, row, col, num):
            # HORIZONTAL
            for x in range(9):
                if grid[row][x] == num:
                    return False
            # VERTICAL
            for x in range(9):
                if grid[x][col] == num:
                    return False
            return True

        def Sudoku(grid, row, col):
            arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            k = 0

            # CHECK WHETHER THERE IS ANY BLANK BOX
            row, col, result = findempty(grid, row, col)
            if result == False:
                return True, grid

            for k in range(1, 10):
                if checkSmallBox(grid, row, col, k):
                    if checkXY(grid, row, col, k):
                        grid[row][col] = k
                        res, gri = Sudoku(grid, row, col)
                        if res:
                            return True, grid
                        grid[row][col] = 0

            return False, grid

        for i in range(9):
            A[i] = [int(A[i][elem].replace(".", "0")) for elem in range(9)]

        bl, A = Sudoku(A, 0, 0)

        for i in range(9):
            A[i] = "".join(list(map(str, A[i])))

        return A


#####		Combinations		#####

"""
Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.
Make sure the combinations are sorted.
To elaborate,
Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
Entries should be sorted within themselves.
Example :
If n = 4 and k = 2, a solution is:
[
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4],
]
Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
Example : itertools.combinations in python.
If you do, we will disqualify your submission retroactively and give you penalty points.
"""


class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, A, B):
        return self.x(1, A, B)

    def x(self, start, end, length):
        if length == 0:
            return [[]]  # only one combination for k=0
        if end - start + 1 < length:
            return []  # no combination possible
        result = []
        for i in range(start, end + 1):  # Pick each element as the start
            for e in self.x(i + 1, end, length - 1):  # This does the core operation
                result.append([i] + e)
        return result


s = Solution()
print(s.combine(5, 3))

#####		N Queens		#####

"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
N Queens: Example 1
Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens’ placement, where 'Q' and '.'
both indicate a queen and an empty space respectively.
For example,
There exist two distinct solutions to the 4-queens puzzle:
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""


# Unfortunately, there is no magic trick to solve this problem. This is more of a bruteforce problem.
# A more intelligent brute force.
# 1) There can exactly be one queen per row. Otherwise the 2 queens in the row would collide.
# If you miss out on a row, there cannot be N queens on the board.
# 2) Every column needs to have exactly one queen.
# 3) The left diagonal cannot have more than one queen ( Unique (row + col) )
# 4) The right diagonal cannot have more than one queen ( Unique (row - col) )


class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        fin = []

        def solve(A, res):
            if len(res) == A:
                fin.append(res)
            for i in range(1, A + 1):
                if not self.attack(res, i):
                    solve(A, res + [i])

        solve(A, [])
        return [["." * (i - 1) + "Q" + "." * (A - i) for i in cols] for cols in fin]

    def attack(self, prev, pos):
        for i in range(len(prev)):
            if prev[i] == pos or abs(len(prev) - i) == abs(prev[i] - pos):
                return True
        return False


s = Solution()
print(s.solveNQueens(4))

#####		Letter Phone		#####

"""
Given a digit string, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.
The digit 0 maps to 0 itself.
The digit 1 maps to 1 itself.
Input: Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Make sure the returned strings are lexicographically sorted.
"""


class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, digits):
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': '0', '1': '1'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])
        prev = self.letterCombinations(digits[:-1])  # Recurse for element except the last one
        additional = mapping[digits[-1]]  # Use the combinations for last element
        return [s + c for s in prev for c in additional]  # Append additional for last to recursion result


s = Solution()
print(s.letterCombinations('132'))

#########################	binary-search	#########################


#####		Rotated Sorted Array Search		#####

"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).
You are given a target value to search. If found in the array, return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Input : [4 5 6 7 0 1 2] and target = 4
Output : 0
NOTE : Think about the case when there are duplicates.
Does your current solution work? How does the time complexity change?*
"""


# Think a modified version of the binary search.
# If the pivot is known, the binary search becomes trivial as the array to the either side of the pivot is sorted.
# Can you somehow search for the pivot in your binary search?
# First, we find the pivot (the index of minimum in the array).
# Once we know the pivot, to search for x,
# we can do a conventional binary search in the left and right part of the pivot in the array.
# Now, let us look at how binary search can be applied in this scenario to find the minimum.
# There are 2 cases:
# 1)
#           mid
#            |
#    6 7 8 9 1 2 3 4 5
# arr[mid] > arr[end]
# The min lies in (mid, end]
# Mid is excluded from the range because arr[mid] > arr[end]
# 2)
#          mid
#           |
#   6 7 8 9 1 2 3 4 5
# arr[mid] < arr[end]
# The min lies in [start, mid]
# 3) Note: If there are duplicates, making either decision might be difficult and hence linear search might be required.
#                mid
#                 |
# 1 1 1 1 2 0 1 1 1 1 1 1 1 1 1 1 1
# arr[mid] = arr[end]
#
# Indecisive. We would need to explore the whole array.

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):

        lft, rgt = 0, len(A) - 1
        while lft <= rgt:
            mid = (lft + rgt) / 2
            l, m, r = A[lft], A[mid], A[rgt]
            if m == B:
                return mid
            elif l <= B < m or (l > m and not (m < B <= r)):
                # We choose left half if either :
                #    * left half is sorted and B in this range
                #    * left half is not sorted,
                #      but B isn't in the sorted right half.
                rgt = mid - 1
            else:
                lft = mid + 1

        return -1


#####		Matrix Search		#####

"""
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Example:
Consider the following matrix:
[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return 1 ( 1 corresponds to true )
Return 0 / 1 ( 0 if the element is not present, 1 if the element is present ) for this problem
"""


# If you write down the numbers of row 1 followed by numbers in row2,
# row3 and so on, do you think the resulting array would be sorted ?
# If yes, how do you search for a number efficiently in a sorted array ?

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        m = len(A)
        n = len(A[0])
        start = 0
        end = m * n - 1

        while start <= end:
            mid = (start + end) // 2
            i = mid // n
            j = mid % n
            if B == A[i][j]:
                return 1
            elif B > A[i][j]:
                start = mid + 1
            else:
                end = mid - 1
        return 0


#####		Matrix Median		#####

"""
Given a N cross M matrix in which each row is sorted, find the overall median of the matrix. Assume N*M is odd.
For example,
Matrix=
[1, 3, 5]
[2, 6, 9]
[3, 6, 9]
A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
Median is 5. So, we return 5.
Note: No extra memory is allowed.
"""


# We cannot use extra memory, so we can’t actually store all elements in an array and sort the array.
# But since, rows are sorted it must be of some use, right?
# Note that in a row you can binary search to find how many elements are smaller than a value X in O(log M).
# This is the base of our solution.
# Say k = N*M/2. We need to find (k + 1)^th smallest element.
# We can use binary search on answer. In O(N log M), we can count how many elements are smaller than X in the matrix.
# So, we use binary search on interval [1, INT_MAX]. So, total complexity is O(30 * N log M).
# Note:
# This problem can be solve by using min-heap, but extra memory is not allowed.

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def binary_search_count(self, array, target):
        """ Returns number of elements <= target in sorted array.
        Time complexity: O(lg(n)). Space complexity: O(1), n is len(array).
        """
        # special case
        if target < array[0]:  # target is less than min element
            return 0

        n = len(array)
        start, end = 0, n - 1
        while start < end:
            mid = (start + end + 1) // 2
            if target < array[mid]:
                end = mid - 1
            else:
                start = mid
        return start + 1

    def count_target(self, matrix, target):
        """ Returns number of elements <= target in matrix.
        Time complexity: O(n * lg(m)). Space complexity: O(1),
        n, m are dimensions of the matrix.
        """
        total = 0
        for arr in matrix:
            total += self.binary_search_count(arr, target)
        return total

    def findMedian(self, matrix):
        """ Returns matrix median.
        Time complexity: O(n * lg(m)). Space complexity: O(1),
        n, m are dimensions of the matrix.
        """
        n, m = len(matrix), len(matrix[0])
        # find min and max element in matrix
        min_num, max_num = float("inf"), float("-inf")
        for row in matrix:
            min_num = min(min_num, row[0])  # compare 1st element of each row
            max_num = max(max_num, row[-1])  # compare last element of each row

        goal = (n * m) // 2 + 1  # min count of <= elements for element to be median
        # find matrix median using binary search between min_num and max_num
        while min_num < max_num:
            mid = (min_num + max_num) // 2
            # mid = min_num + (max_num - min_num) // 2
            curr_count = self.count_target(matrix, mid)
            if curr_count < goal:
                min_num = mid + 1
            else:  # curr_count >= goal
                max_num = mid  # update the upper limit for median number
        return min_num


#####		Square Root Of Integer		#####

"""
Implement int sqrt(int x).
Compute and return the square root of x.
If x is not a perfect square, return floor(sqrt(x))
Example :
Input : 11
Output : 3
"""


# Think in terms of binary search.
# Let us say S is the answer.
# We know that 0 <= S <= x.
# Consider any random number r.
# If r*r <= x, S >= r
# If r*r > x, S < r.
# Maybe try to run a binary search for S

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        left = 0
        right = A
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= A:
                left = mid + 1
            else:
                right = mid - 1
        return right


#####		Implement Power Function		#####

"""
Implement pow(x, n) % d.
In other words, given x, n and d,
find (xn % d)
Note that remainders on division cannot be negative.
In other words, make sure the answer you return is non negative.
Input : x = 2, n = 3, d = 3
Output : 2
2^3 % 3 = 8 % 3 = 2.
"""


# You need to come up with a solution better than O(n).
# Think recursively. You can think of an example like 3^8. How many multiplication do you really need to evaluate 3^8?
# There are two major things to note here:
# 1) Overflow situation: Note that if x is large enough, multiplying x to the answer might overflow in integer.
# 2) Multiplying x one by one to the answer is O(n). We are looking for something better than O(n).
# If n is even, note the following:
# x ^ n = (x * x) ^ n/2
# Can you use the above observation to come up with a solution better than O(n)?

class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if x == 0:
            return 1 % d
        ans = 1
        base = x
        base = base % d

        while n > 0:
            # We need (base ** n) % p.
            # Now there are 2 cases.
            # 1) n is even. Then we can make base = base^2 and n = n / 2.
            # 2) n is odd. So we need base * base^(n-1)
            if n % 2 == 1:
                ans = (ans * base) % d
                n -= 1
            else:
                n = n >> 1
                base = (base * base) % d
        # if ans < 0:
        #     ans = (ans + d) % d
        return ans


#####		Search For A Range		#####

"""
Given a sorted array of integers, find the starting and ending position of a given target value.
Your algorithm’s runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
Example:
Given [5, 7, 7, 8, 8, 10]
and target value 8,
return [3, 4].
"""


# First, let us find the left boundary of the range.
# We initialize the range to [i=0, j=n-1]. In each step, calculate the middle element [mid = (i+j)/2].
# Now according to the relative value of A[mid] to target, there are three possibilities:
# If A[mid] < target, then the range must begin on the right of mid (hence i = mid+1 for the next iteration)
# If A[mid] > target, it means the range must begin on the left of mid (j = mid-1)
# If A[mid] = target, then the range must begins on the left of or at mid (j= mid)
# Since we would move the search range to the same side for case 2) and 3), we might as well merge
# them as one single case so that less code is needed:
# 2*. If A[mid] >= target, j = mid;
# Surprisingly, 1 and 2* are the only logic you need to put in loop while (i < j). When the while loop terminates,
# the value of i/j is where the start of the range is. Why?
# No matter what the sequence originally is, as we narrow down the search range, eventually we will be at a situation
# where there are only two elements in the search range.
# Suppose our target is 5, then we have only 7 possible cases:
# Case 1: [5 7] (A[i] = target < A[j])
# Case 2: [5 3] (A[i] = target > A[j])
# Case 3: [5 5] (A[i] = target = A[j])
# Case 4: [3 5] (A[j] = target > A[i])
# Case 5: [3 7] (A[i] < target < A[j])
# Case 6: [3 4] (A[i] < A[j] < target)
# Case 7: [6 7] (target < A[i] < A[j])
# For case 1, 2 and 3, if we follow the above rule, since mid = i => A[mid] = target
# in these cases, then we would set j = mid.
# Now the loop terminates and i and j both point to the first 5.
# For case 4, since A[mid] < target, then set i = mid+1. The loop terminates and both i and j point to 5.
# For all other cases, by the time the loop terminates, A[i] is not equal to 5. So we can easily know 5 is
# not in the sequence if the comparison fails.
# In conclusion, when the loop terminates, if A[i]==target, then i is the left boundary of the range;
# otherwise, just return -1;
# For the right of the range, we can use a similar idea. Again we can come up with several rules:
# If A[mid] > target, then the range must begin on the left of mid (j = mid-1)
# If A[mid] < target, then the range must begin on the right of mid (hence i = mid+1 for the next iteration)
# If A[mid] = target, then the range must begins on the right of or at mid (i= mid)
# Again, we can merge conditions 2 and 3 into:
# 2*. If A[mid] <= target, then i = mid;
# However, the terminate condition on longer works this time.
# Consider the following case:
# [5 7], target = 5
# Now A[mid] = 5, then according to rule 2), we set i = mid.
# This practically does nothing because i is already equal to mid.
# As a result, the search range is not moved at all!
# The solution is in using a small trick:
# Instead of calculating mid as mid = (i+j)/2, we now do:
# mid = (i+j)/2+1
# Why does this trick work?
# When we use mid = (i+j)/2, the mid is rounded to the lowest integer.
# In other words, mid is always biased towards the left. This means we could have i == mid when j - i == mid,
# but we NEVER have j == mid. So in order to keep the search range moving, we must make sure that the
# new i is set to something different than mid, otherwise we are at the risk that i gets stuck.
# But for the new j, it is okay if we set it to mid, since it was not equal to mid anyway.
# Our two rules in search for the left boundary happen to satisfy these requirements, so it works perfectly in that
# situation. Similarly, when we search for the right boundary,
# we must make sure i does not get stuck when we set the new i to i = mid.
# The easiest way to achieve this is by making mid biased to the right, i.e. mid = (i+j)/2+1.

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        low = self.lowi(A, B)
        high = self.highi(A, B, len(A))
        return [low, high]

    def lowi(self, A, B):
        high = len(A) - 1
        low = 0
        while low <= high:
            mid = (low + high) // 2
            if A[mid] == B and (mid == 0 or (mid > 0 and (A[mid - 1] != B))):
                return mid
            if A[mid] >= B:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def highi(self, A, B, n):
        high = len(A) - 1
        low = 0
        while low <= high:
            mid = (low + high) // 2
            if A[mid] == B and (mid == n - 1 or (mid < n - 1 and (A[mid + 1] != B))):
                return mid
            if A[mid] > B:
                high = mid - 1
            else:
                low = mid + 1
        return -1


#####		Painters Partition Problem		#####

"""
You have to paint N boards of length {A0, A1, A2, A3 … AN-1}. There are K painters available and you are also given how
much time a painter takes to paint 1 unit of board. You have to get this job done as soon as possible under the
constraints that any painter will only paint contiguous sections of board.
2 painters cannot share a board to paint. That is to say, a board
cannot be painted partially by one painter, and partially by another.
A painter will only paint contiguous boards. Which means a
configuration where painter 1 paints board 1 and 3 but not 2 is
invalid.
Return the ans % 10000003
Input :
K : Number of painters
T : Time taken by painter to paint 1 unit of board
L : A List which will represent length of each board
Output:
     return minimum time to paint all boards % 10000003
Example
Input :
  K : 2
  T : 5
  L : [1, 10]
Output : 50
"""


# If you have already solved the problem corresponding to hint1, you are already halfway there.
# You can do a binary search for the answer :
#   start = 0, end = max_time_possible
#   mid = (start + end) / 2
#   if isPossible(mid):
#   	end = mid - 1
#   else
# 	start = mid + 1
# Now, lets look into how isPossible would be implemented.
# Keep assigning boards to painter greedily till the time taken < mid. If you run out of painters, isPossible = false.
# else isPossible = true.

def is_poss(sumi, l, k):
    m = 0
    cur_sum = 0
    for i in range(len(l)):
        if l[i] > sumi:
            return False
        if l[i] + cur_sum <= sumi:
            cur_sum += l[i]
        else:
            m += 1
            cur_sum = l[i]

    if m == 0 or m >= k:
        return False

    return True


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        start = 0
        end = sum(C)

        while start < end:

            mid = (start + end) // 2
            if is_poss(mid, C, A):
                end = mid
            else:
                start = mid + 1

        return (start * B) % 10000003


#####		Allocate Books		#####

"""
N number of books are given.
The ith book has Pi number of pages.
You have to allocate books to M number of students so that maximum number of pages alloted to a student is minimum.
A book will be allocated to exactly one student. Each student has to be allocated at least one book. Allotment should
be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.
NOTE: Return -1 if a valid assignment is not possible
Input:
List of Books
M number of students
Your function should return an integer corresponding to the minimum number.
Example:
P : [12, 34, 67, 90]
M : 2
Output : 113
There are 2 number of students. Books can be distributed in following fashion :
  1) [12] and [34, 67, 90]
      Max number of pages is allocated to student 2 with 34 + 67 + 90 = 191 pages
  2) [12, 34] and [67, 90]
      Max number of pages is allocated to student 2 with 67 + 90 = 157 pages
  3) [12, 34, 67] and [90]
      Max number of pages is allocated to student 1 with 12 + 34 + 67 = 113 pages
Of the 3 cases, Option 3 has the minimum pages = 113.
"""


# Can you find how many number of students we need if we fix that one student can read at most V number of pages ?
# Problem statement : Given fixed number of pages (V),  how many number of students we need?
# Solution :
#    simple simulation approach
#    intially Sum := 0
#    cnt_of_student = 0
#    iterate over all books:
#         If Sum + number_of_pages_in_current_book > V :
#                   increment cnt_of_student
#                   update Sum
#         Else:
#                   update Sum
#    EndLoop;
#     fix range LOW, HIGH
#     Loop until LOW < HIGH:
#             find MID_point
#             Is number of students required to keep max number of pages below MID < M ?
#             IF Yes:
#                 update HIGH
#             Else
#                 update LOW
#     EndLoop;


class Solution:
    def numberOfStudents(self, A, pages):
        count = 0
        students = 1
        for i in range(len(A)):
            count += A[i]
            if count > pages:
                count = A[i]
                students += 1
        return students

    def books(self, A, M):
        if M > len(A):
            return -1
        min_pages = max(A)
        max_pages = sum(A)
        while min_pages < max_pages:
            mid = int((min_pages + max_pages) / 2)
            if self.numberOfStudents(A, mid) > M:
                min_pages = mid + 1
            else:
                max_pages = mid
        return min_pages


#####		Sorted Insert Position		#####

"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""


# You need to return the index of least element >= x.

def bisect_left(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


class Solution:
    def searchInsert(self, arr, target):
        return bisect_left(arr, target)


#####		Median Of Array		#####

"""
There are two sorted arrays A and B of size m and n respectively.
Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).
The overall run time complexity should be O(log (m+n)).
Sample Input
A : [1 4 5]
B : [2 3]
Sample Output
3
 NOTE: IF the number of elements in the merged array is even,
 then the median is the average of n / 2 th and n/2 + 1th element.
For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5
"""


# Given a sorted array A of length m, we can split it into two parts:
# { A[0], A[1], … , A[i - 1] }	{ A[i], A[i + 1], … , A[m - 1] }
# All the elements in right part are greater than the elements in left part.
# The left part has “i” elements, and right part has “m - i” elements.
# There are “m + 1” kinds of splits. (i = 0 ~ m)
# When i = 0, the left part has “0” elements, right part has “m” elements.
# When i = m, the left part has “m” elements, right part has “0” elements.
# For array B, we can split it with the same way:
# { B[0], B[1], … , B[j - 1] }	{ B[j], B[j + 1], … , B[n - 1] }
# The left part has “j” elements, and right part has “n - j” elements.
# Put A’s left part and B’s left part into one set. (Let us name this set “LeftPart”)
# Put A’s right part and B’s right part into one set. (Let us name this set”RightPart”)
#         LeftPart           |            RightPart
# { A[0], A[1], … , A[i - 1] }	{ A[i], A[i + 1], … , A[m - 1] }
# { B[0], B[1], … , B[j - 1] }	{ B[j], B[j + 1], … , B[n - 1] }
# If we can ensure the following:
# 1) LeftPart’s length == RightPart’s length (or RightPart’s length + 1)
# 2) All elements in RightPart is greater than elements in LeftPart,
# then we split all elements in {A, B} into two parts with eqaul length, and one part is
# always greater than the other part.
# Then the median can be easily found.
# The expected time complexity gives away binary search in this case.
# We are going to do binary search for the answer in this case.
# Given a sorted array A of length m, we can split it into two parts:
# { A[0], A[1], … , A[i - 1] }	{ A[i], A[i + 1], … , A[m - 1] }
# All elements in right part are greater than elements in the left part.
# The left part has i elements, and right part has m - i elements.
# There are m + 1 kinds of splits.
# (i = 0 ~ m)
# When i = 0, the left part has “0” elements, the right part has “m” elements.
# When i = m, the left part has “m” elements, right part has “0” elements.
# For the array B, we can split it in the same way:
# { B[0], B[1], … , B[j - 1] }	{ B[j], B[j + 1], … , B[n - 1] }
# The left part has “j” elements, and right part has “n - j” elements.
# Put A’s left part and B’s left part into one set. (Let’s name this set “LeftPart”)
# Put A’s right part and B’s right part into one set. (Let’s name this set”RightPart”)
#         LeftPart           |            RightPart
# { A[0], A[1], … , A[i - 1] }	{ A[i], A[i + 1], … , A[m - 1] }
# { B[0], B[1], … , B[j - 1] }	{ B[j], B[j + 1], … , B[n - 1] }
# If we can ensure the following:
# LeftPart’s length == RightPart’s length (or RightPart’s length + 1)
# All elements in RightPart is greater than elements in LeftPart,
# then we can split all elements in {A, B} into two parts with equal length, and one part is always greater than the other part.
# Then the median can thus be easily found.
# To ensure these two condition, we just need to ensure:
# Condition 1 :
#  i + j == (m - i) + (n - j)
#  OR i + j == (m - i) + (n - j) + 1
# Which means if n >= m,
# i = 0 to m
# j = (m + n + 1) / 2 - i
# Condition 2
#  B[j - 1] <= A[i] and A[i - 1] <= B[j]
# Considering edge values, we need to ensure:
#    (j == 0 or i == m or B[j - 1] <= A[i]) and
#    (i == 0 or j == n or A[i - 1] <= B[j])
# So, all we need to do is:
# Search i from 0 to m, to find an object i to meet condition (1) and (2) above.
# And we can do this search by binary search.
# How?
# If B[j0 - 1] > A[i0], than the object ix can’t be in [0, i0].
# Why?
# Because if
#   ix < i0,
#   => jx = (m + n + 1) / 2 - ix > j0
#   => B[jx - 1] >= B[j0 - 1] > A[i0] >= A[ix].
# This violates the condition (2). So ix can’t be less than i0.
#
# And if A[i0 - 1] > B[j0], than the object ix can’t be in [i0, m].
# So we can do the binary search following the steps described below:
#
# set imin, imax = 0, m, then start searching in [imin, imax]
# Search in [imin, imax]:
#     i = (imin + imax) / 2
#     j = ((m + n + 1) / 2) - i
#     if B[j - 1] > A[i]:
#         search in [i + 1, imax]
#     else if A[i - 1] > B[j]:
#         search in [imin, i - 1]
#     else:
#         if m + n is odd:
#             answer is max(A[i - 1], B[j - 1])
#         else:
#             answer is (max(A[i - 1], B[j - 1]) + min(A[i], B[j])) / 2


class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and B[j - 1] > A[i]:
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                imax = i - 1
            else:
                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0


#########################	bit-manipulation	#########################


#####		Reverse Bits		#####

"""
Reverse bits of an 32 bit unsigned integer
Example 1:
x = 0,
          00000000000000000000000000000000
=>        00000000000000000000000000000000
return 0
Example 2:
x = 3,
          00000000000000000000000000000011
=>        11000000000000000000000000000000
return 3221225472
"""


# How do you swap the ‘i’th bit with the ‘j’th bit?
# Try to figure out if you could use the XOR operation to do it.
# 0 ^ 0 == 0,
# 1 ^ 1 == 0,
# 0 ^ 1 == 1, and
# 1 ^ 0 == 1.
# We only need to perform the swap when the ‘i’th bit and the ‘j’th bit are different.
# To test if two bits are different, we could use the XOR operation. Then, we need to toggle both ‘i’th and ‘j’th bits.
# We could apply the XOR operation again.
# By XOR-ing the ‘i’th and ‘j’th bit with 1, both bits are toggled.

class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        result = 0
        n = 32
        for i in range(n):
            if (A >> i) & 1: result |= 1 << (n - 1 - i)
        return result


#####		Different Bits Sum Pairwise		#####

"""
We define f(X, Y) as number of different corresponding bits in binary representation of X and Y.
For example, f(2, 7) = 2, since binary representation of 2 and 7 are 010 and 111, respectively.
The first and the third bit differ, so f(2, 7) = 2.
You are given an array of N positive integers, A1, A2 ,…, AN. Find sum of f(Ai, Aj) for all pairs (i, j)
such that 1 ≤ i, j ≤ N. Return the answer modulo 109+7.
For example,
A=[1, 3, 5]
We return
f(1, 1) + f(1, 3) + f(1, 5) +
f(3, 1) + f(3, 3) + f(3, 5) +
f(5, 1) + f(5, 3) + f(5, 5) =
0 + 1 + 1 +
1 + 0 + 2 +
1 + 2 + 0 = 8
"""


# Assume that all values in input have only 1 bit i.e. Ai = 0 or 1.
# Lets say A = count of elements which are 0
# and B = count of elements which are 1
# In this case our answer is just 2AB, since each such pair contributes 1 to answer.
# Can you combine this logic if we have multiple bits?
# Note that all bits are independent in counting, since we are counting number of bits which are different in each pair.
# So, we just do the same process for all different bits. Since Ai is an integer, we just have to do this for
# 31 different bits, so our solution is O(31*N).

class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        self.cache = {}
        sum1 = 0
        next_iter = True
        while next_iter:
            cnt = 0
            next_iter = False
            for i in range(len(A)):
                if A[i] & 1 == 0:
                    cnt += 1
                A[i] = A[i] >> 1
                if A[i] != 0:
                    next_iter = True
            sum1 += cnt * (len(A) - cnt)
        return (2 * sum1) % (10 ** 9 + 7)


#####		Divide Integers		#####

"""
Divide two integers without using multiplication, division and mod operator.
Return the floor of the result of the division.
Example:
5 / 2 = 2
Also, consider if there can be overflow cases. For overflow case, return INT_MAX.
"""


# dividend = answer * divisor + c
# You need to find the answer here without using any of the operators mentioned in the question.
# Think about the binary expansion of answer.
# Think in terms of bits.
# How do you do the division with bits?
# How do you determine the most significant bit in the answer?
# Iterate on the bit position ‘i’ from 31 to 1 and find the first bit for which divisor«i is less than dividend.
# How do you use (1) to move forward in similar fashion?

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, dividend, divisor):
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        res = 0
        p = abs(dividend)
        q = abs(divisor)
        if divisor == 0 or (divisor == 1 and dividend >= INT_MAX):
            return INT_MAX
        if dividend <= INT_MIN and divisor == -1:
            return INT_MAX
        if abs(divisor) == 1:
            return dividend * divisor
        while p >= q:
            c = 0
            while p > (q << c):
                c += 1
            res += 1 << (c - 1)
            p -= q << (c - 1)

        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            return res
        else:
            return -res


#####		Number Of 1 Bits		#####

"""
Write a function that takes an unsigned integer and returns the number of 1 bits it has.
Example:
The 32-bit integer 11 has binary representation
00000000000000000000000000001011
so the function should return 3.
"""


# Iterate 32 times, each time determining if the ith bit is a ’1′ or not.
# This is probably the easiest solution, and the interviewer would probably not be too happy about it.
# In addition, this solution is not very efficient too because you need to iterate 32 times no matter what.
# This means that if we do (x & (x - 1)),
# it would just unset the last set bit in x (which is why x&(x-1) is 0 for powers of 2).
# x - 1 would find the first set bit from the end, and then set it to 0, and set all the bits following it.
# Which means if x = 10101001010100 then x - 1 becomes 10101001010(011)

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        count = 0
        while A > 0:
            A &= A - 1  # When we do &, all the bits set after doing A-1 will be cleared
            count += 1
        return count


#####		Single Number		#####

"""
Given an array of integers, every element appears twice except for one. Find that single one.
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Example :
Input : [1 2 2 3 1]
Output : 3
"""

# Every number that occurs twice will either contribute 2 ‘1’s or 2 ‘0’s to the position.
# The number that occurs once-‘X’ will contribute exactly one 0 or 1 to the position
# depending on whether it has 0 or 1 in that position.
# So:
# If X has 1 in that position, we will have odd number of 1s in that position.
# If X has 0 in that position, we will have odd number of 0s in that position.

from functools import reduce


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        return reduce(lambda x, y: x ^ y, A)


#####		Min Xor Value		#####

"""
Given an array of N integers, find the pair of integers in the array which have minimum XOR value.
Report the minimum XOR value.
Examples :
Input
0 2 5 7
Output
2 (0 XOR 2)
Input
0 4 7 9
Output
3 (4 XOR 7)
Constraints:
2 <= N <= 100 000
0 <= A[i] <= 1 000 000 000
"""


# The first step is to sort the array. The answer will be the minimal value of X[i] XOR X[i+1] for every i.
# Proof:
# Let’s suppose that the answer is not X[i] XOR X[i+1], but A XOR B and there exists C in the array such as A <= C <= B.
# Next is the proof that either A XOR C or C XOR B are smaller than A XOR B.
# Let A[i] = 0/1 be the i-th bit in the binary representation of A
# Let B[i] = 0/1 be the i-th bit in the binary representation of B
# Let C[i] = 0/1 be the i-th bit in the binary representation of C
# This is with the assumption that all of A, B and C are padded with 0 on the left until they all have the same length
# Example: A=169, B=187, C=185
# A=101010012
# B=101110112
# C=101110012
# Let i be the leftmost (biggest) index such that A[i] differs from B[i]. There are 2 cases now:
# 1) C[i] = A[i] = 0,
# then (A XOR C)[i] = 0 and (A XOR B)[i] = 1
# This implies (A XOR C) < (A XOR B)
# 2) C[i] = B[i] = 1,
# then (B XOR C)[i] = 0 and (A XOR B)[i] = 1
# This implies (B XOR C) < (A XOR B)
# Time complexity: O(N * l)

class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        s = sorted(A)
        minn = s[0] ^ s[1]
        for i in range(1, len(A)):
            if s[i] ^ s[i - 1] < minn:
                minn = s[i] ^ s[i - 1]
        return minn


#####		Single Number 2		#####

"""
Given an array of integers, every element appears thrice except for one which occurs once.
Find that element which does not appear thrice.
Note: Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
Example :
Input : [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
Output : 4
"""


# Let us look at every bit position.
# Every number that occurs thrice will either contribute 3 ‘1’s or 3 ‘0’s to the position.
# The number that occurs once X will contribute exactly one 0 or 1 to the position
# depending on whether it has 0 or 1 in that position.
# So:
# If X has 1 in that position, we will have (3x+1) number of 1s in that position.
# If X has 0 in that position, we will have (3x+1) number of 0s in that position.
# Having noticed that if X has 1 in that position, we will have 3x+1 number of 1s in that position.
# If X has 0 in that position, we will have 3x+1 number of 0 in that position.
# A straightforward implementation is to use an array of size 32 to keep track of the total count of ith bit.
# We can improve this based on the previous solution using three bitmask variables:
# ones as a bitmask to represent the ith bit had appeared once.
# twos as a bitmask to represent the ith bit had appeared twice.
# threes as a bitmask to represent the ith bit had appeared three times.
# When the ith bit had appeared for the third time, clear the ith bit of both ones and twos to 0.
# The final answer will be the value of ones.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        res = 0
        for j in range(31, -1, -1):
            c = 0
            for i in A:
                if i & (1 << j):
                    c += 1  # Count the number of elements in A that has bit i set
            if c % 3 != 0:
                res |= (1 << j)
        return res


#########################	dp	#########################


#####		Best Time To Buy And Sell Stocks 3		#####

"""
Say you have an array, A, for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit.
You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
Input Format:
The first and the only argument is an array of integer, A.
Output Format:
Return an integer, representing the maximum possible profit.
Constraints:
1 <= len(A) <= 1e5
1 <= A[i] <= 1e7
Example :
Input 1:
    A = [1, 2, 3]
Output 1:
    2
Explanation 1:
    => Buy a stock on day 0.
    => Sell the stock on day 1. (Profit +1)
    => Buy a stock on day 1.
    => Sell the stock on day 2. (Profit +1)
    Overall profit = 2
Input 2:
    A = [5, 2, 10]
Output 2:
    8
Explanation 2:
    => Buy a stock on day 1.
    => Sell the stock on on day 2. (Profit +8)
    Overall profit = 8
"""


# Observation based solution:
# Note 1: I will never buy a stock and sell it in loss.
# Note 2: If A[i] < A[i+1], I will always buy a stock on i and sell it on i+1.
# Think and try to come up with a proof on the validity of the statement.
# DP based solution:
# Let Dp[i] = max profit you can gain in region (i,i+1,….,n).
# Then Dp[i] = max(Dp[i+1],-A[i] + max( A[j]+Dp[j] st j > i ) )
# Can you come up with base cases and direction of computation now?

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        temp = []
        for i in range(len(A) - 1):
            temp.append(A[i + 1] - A[i])
        sumi = 0
        currmax = 0
        for i in range(len(temp)):
            if temp[i] > 0:
                currmax += temp[i]
            else:
                sumi += currmax
                currmax = 0
        sumi += currmax
        return sumi


#####		Unique Bst 2		#####

"""
Given an integer A, how many structurally unique BST’s (binary search trees) exist that can store values 1…A?
Input Format:
The first and the only argument of input contains the integer, A.
Output Format:
Return an integer, representing the answer asked in problem statement.
Constraints:
1 <= A <= 18
Example:
Input 1:
    A = 3
Output 1:
    5
Explanation 1:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


# Lets say you know the answer for values i which ranges from 0 <= i <= n - 1.
# How do you calculate the answer for n.
# Lets consider the number [1, n]
# We have n options of choosing the root.
# If we choose the number j as the root, j - 1 numbers fall in the left subtree, n - j numbers
# fall in the right subtree. We already know how many ways there are to forming j - 1 trees
# using j - 1 numbers and n -j numbers.
# So we add number(j - 1) * number(n - j) to our solution.
# Can you use the above fact to construct a DP relation ?

class Solution:
    # @param A : integer
    # @return an integer
    def numTrees(self, A):
        n = A
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[i - j] * dp[j - 1]
        return dp[n]


#####		Coins In A Line		#####

"""
There are A coins (Assume A is even) in a line.
Two players take turns to take a coin from one of the ends of the line until there are no more coins left.
The player with the larger amount of money wins.
Assume that you go first.
Return the maximum amount of money you can win.
Input Format:
The first and the only argument of input contains an integer array, A.
Output Format:
Return an integer representing the maximum amount of money you can win.
Constraints:
1 <= length(A) <= 500
1 <= A[i] <= 1e5
Examples:
Input 1:
    A = [1, 2, 3, 4]
Output 1:
    6
Explanation 1:
    You      : Pick 4
    Opponent : Pick 3
    You      : Pick 2
    Opponent : Pick 1
    Total money with you : 4 + 2 = 6
Input 2:
    A = [5, 4, 8, 10]
Output 2:
    15
Explanation 2:
    You      : Pick 10
    Opponent : Pick 8
    You      : Pick 5
    Opponent : Pick 4
    Total money with you : 10 + 5 = 15
"""


# So, the question is what’s the recurrence relation for this problem
# Rec(player = you, start, end) =
# 	    |
# 	max | v(end) + Rec(opposite_player, start, end - 1)
# 	    |
# 	    | v(start) + Rec(opposite_player, start + 1, end)
# 	    |
# Rec(player = opposite, start, end) =
# 	    |
# 	min | Rec(you, start, end - 1)
# 	    |
# 	    | Rec(you, start + 1, end)
# 	    |
# now can you define base cases and memorize it ?


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxcoin(self, A):
        '''
        Solution by dynamic programming.
           dp[i][j] = maximum score possible for current player for subgame A[i:j]
        Base cases, only one option:
           dp[i][i+1] = A[i]
        Otherwise, we pick at either end, eventually getting
        all the coins but the ones picked by next player:
           dp[i][j] = sum(A[i:j]) - min(dp[i+1][j], dp[i][j-1])

        Now, we only have to maintain one column (j-1) to obtain new one (j).

        Time: O(n**2)   Space: O(n)
        '''

        n = len(A)
        dp = [None] * n

        for j in range(1, n + 1):
            dp[j - 1] = A[j - 1]  # dp[j-1][j]
            total = A[j - 1]
            # dp[i+1][j] must be already computed, so we iterate backward
            for i in range(j - 2, -1, -1):
                total += A[i]  # sum[i:j]
                dp[i] = total - min(dp[i + 1], dp[i])

        return dp[0]


#####		Rod Cutting		#####

"""
There is a rod of length N lying on x-axis with its left end at x = 0 and right end at x = N. Now, there are M weak
 points on this rod denoted by positive integer values(all less than N) A1, A2, …, AM. You have to cut rod at all
 these weak points. You can perform these cuts in any order. After a cut, rod gets divided into two smaller sub-rods.
 Cost of making a cut is the length of the sub-rod in which you are making a cut.
Your aim is to minimise this cost. Return an array denoting the sequence in which you will make cuts. If two different
sequences of cuts give same cost, return the lexicographically smallest.
Notes:
Sequence a1, a2 ,…, an is lexicographically smaller than b1, b2 ,…, bm, if and only if at the first i where ai and bi
differ, ai < bi, or if no such i found, then n < m.
N can be upto 109.
For example,
N = 6
A = [1, 2, 5]
If we make cuts in order [1, 2, 5], let us see what total cost would be.
For first cut, the length of rod is 6.
For second cut, the length of sub-rod in which we are making cut is 5(since we already have made a cut at 1).
For third cut, the length of sub-rod in which we are making cut is 4(since we already have made a cut at 2).
So, total cost is 6 + 5 + 4.
Cut order          | Sum of cost
(lexicographically | of each cut
 sorted)           |
___________________|_______________
[1, 2, 5]          | 6 + 5 + 4 = 15
[1, 5, 2]          | 6 + 5 + 4 = 15
[2, 1, 5]          | 6 + 2 + 4 = 12
[2, 5, 1]          | 6 + 4 + 2 = 12
[5, 1, 2]          | 6 + 5 + 4 = 15
[5, 2, 1]          | 6 + 5 + 2 = 13
So, we return [2, 1, 5].
"""

# We rewrite our problem as given N cut points(and you cannot make first and last cut), decide order of these cuts
# to minimise the cost. So, we insert 0 and N at beginning and end of vector B. Now, we have solve our new problem
# with respect to this new array(say A).
# We define dp(i, j) as minimum cost for making cuts Ai, Ai+1, …, Aj. Note that you are not making cuts Ai and Aj,
# but they decide the cost for us.
# For solving dp(i, j), we iterate k from i+1 to j-1, assuming that the first cut we make in this interval is Ak.
# The total cost required(if we make first cut at Ak) is Aj - Ai + dp(i, k) + dp(k, j).
# This is our solution. We can implement this DP recursively with memoisation. Total complexity will be O(N3).
# For actually building the solution, after calculating dp(i, j), we can store the index k which gave the minimum
# cost and then we can build the solution backwards.
from functools import wraps


def memo(f):
    cache = {}

    @wraps(f)
    def wrap(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return wrap


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def rodCut(self, n, A):
        A = tuple(A)
        return self.recurse(A, 0, n)[1]

    @memo
    def recurse(self, A, left, right):
        if not len(A):
            return 0, []
        elif len(A) == 1:
            return right - left, [A[0]]
        else:
            mi = 999999999999
            min_sequence = None
            for i, a in enumerate(A):
                l = self.recurse(A[:i], left, a)
                r = self.recurse(A[i + 1:], a, right)
                tot = l[0] + r[0] + (right - left)
                if tot < mi:
                    mi = tot
                    min_sequence = (tot, [a] + l[1] + r[1])
            return min_sequence


#####		Queen Attack		#####

"""
On a N * M chessboard, where rows are numbered from 1 to N and columns from 1 to M, there are queens at some cells.
Return a N * M array A, where A[i][j] is number of queens that can attack cell (i, j). While calculating answer for
cell (i, j), assume there is no queen at that cell.
Notes:
Queen is able to move any number of squares vertically, horizontally or diagonally on a chessboard. A queen cannot
jump over another queen to attack a position.
You are given an array of N strings, each of size M. Each character is either a 1 or 0 denoting if there is a queen at
that position or not, respectively.
Expected time complexity is worst case O(N*M).
For example,
Let chessboard be,
[0 1 0]
[1 0 0]
[0 0 1]
where a 1 denotes a queen at that position.
Cell (1, 1) is attacked by queens at (2, 1), (1,2) and (3,3).
Cell (1, 2) is attacked by queen at (2, 1). Note that while calculating this, we assume that there is no queen at (1, 2).
Cell (1, 3) is attacked by queens at (3, 3) and (1, 2).
and so on...
Finally, we return matrix
[3, 1, 2]
[1, 3, 3]
[2, 3, 0]
"""

# If you actually traverse in all 8 directions for each cell, total complexity in worst case will be O(N*M*(N+M)).
# Can you store some data for cells in such a way that for finding answer to cell (i, j)
# you just have to look at its neighbours only.
# We define f(i, j, k) as a number of queen attacks on the cell (i, j) from direction k.
# Eight directions can be given numbers 0 to 7.
# Now, to see how many attacks are there on a cell (i, j), we go to its neighbour in direction k(say n_i, n_j).
# If the cell (n_i, n_j) has a queen, then there is just 1 attack. Else, number of attacks is f(n_i, n_j, k).
# Can you formulate base cases?
# We just have to take the sum of f(i, j, k) for all k=0 to 7 to find the answer for the position (i, j).
# The total number of states is O(N*M*8) and the transition is O(1), so total complexity is O(N*M).

from collections import defaultdict


class Solution:
    # @param A : list of strings
    # @return a list of list of integers
    def queenAttack(self, A):
        n, m = len(A), len(A[0])
        res = [[0] * m for _ in range(n)]

        hasTop = [0] * m
        hasDiag = defaultdict(int)
        hasRdiag = defaultdict(int)
        for i in range(n):
            hasLeft = 0
            for j in range(m):
                res[i][j] += hasLeft + hasTop[j] + hasDiag[j - i] + hasRdiag[j + i]
                if A[i][j] == '1':
                    hasLeft = 1
                    hasTop[j] = 1
                    hasDiag[j - i] = 1
                    hasRdiag[j + i] = 1

        hasBottom = [0] * m
        hasDiag = defaultdict(int)
        hasRdiag = defaultdict(int)
        for i in range(n - 1, -1, -1):
            hasRight = 0
            for j in range(m - 1, -1, -1):
                res[i][j] += hasRight + hasBottom[j] + hasDiag[j - i] + hasRdiag[j + i]
                if A[i][j] == '1':
                    hasRight = 1
                    hasBottom[j] = 1
                    hasDiag[j - i] = 1
                    hasRdiag[j + i] = 1

        return res


#####		Arrange 2		#####

"""
You are given a sequence of black and white horses, and a set of K stables numbered 1 to K. You have to accommodate
 the horses into the stables in such a way that the following conditions are satisfied:
You fill the horses into the stables preserving the relative order of horses. For instance, you cannot put horse 1
into stable 2 and horse 2 into stable 1. You have to preserve the ordering of the horses.
No stable should be empty and no horse should be left unaccommodated.
Take the product (number of white horses * number of black horses) for each stable and take the sum of all these
products. This value should be the minimum among all possible accommodation arrangements
Example:
Input: {WWWB} , K = 2
Output: 0
Explanation:
We have 3 choices {W, WWB}, {WW, WB}, {WWW, B}
for first choice we will get 1*0 + 2*1 = 2.
for second choice we will get 2*0 + 1*1 = 1.
for third choice we will get 3*0 + 0*1 = 0.
Of the 3 choices, the third choice is the best option.
If a solution is not possible, then return -1
"""


# Recurrence relation
# Rec(Current_Horse, Current_Stable) =  |
#                             |           |
#                             |           |Rec(i + 1, Next_Stable) + (White_Horses * Black Horses in Current_Stable)
#                             |       min |
#                             |           |
#                             |
#                             | i = Current_Horse to Number_of_Horses
#                             |
# Now can you implement it?

def cost(A):
    tw = 0
    tb = 0
    for i in A:
        if i == 'W':
            tw += 1
        else:
            tb += 1
    return tw * tb


class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer

    def arrange(self, A, B):
        d = [[10000000000 for i in range(len(A))] for j in range(B)]
        tb = 0
        tw = 0
        for i in range(1, len(A) + 1):
            if A[-i] == 'W':
                tw += 1
            else:
                tb += 1
            d[0][-i] = tw * tb

        # print(d[0])
        for i in range(1, B):
            for j in range(2, len(A) + 1):
                c = []
                b = A[-j:]
                for k in range(1, len(b)):
                    # print(b[k:])
                    if len(b[k:]) > 0:
                        c += [cost(b[:k]) + d[i - 1][-(j - k)]]
                    else:
                        c += [10000000000]
                        break
                # print(c,i,j)
                d[i][-j] = min(c)
        if d[B - 1][0] == 10000000000:
            return -1
        else:
            return d[B - 1][0]


#####		Longest Artithematic Progression		#####

"""
Find longest Arithmetic Progression in an integer array A of size N, and return its length.
More formally, find longest sequence of indices, 0 < i1 < i2 < … < ik < ArraySize(0-indexed) such that sequence
A[i1], A[i2], …, A[ik] is an Arithmetic Progression.
Arithmetic Progression is a sequence in which all the differences between consecutive pairs are the same,
i.e sequence B[0], B[1], B[2], …, B[m - 1] of length m is an Arithmetic Progression if and only if
B[1] - B[0] == B[2] - B[1] == B[3] - B[2] == … == B[m - 1] - B[m - 2]
Note: The common difference can be positive, negative or 0.
Input Format:
The first and the only argument of input contains an integer array, A.
Output Format:
Return an integer, representing the length of the longest possible arithmetic progression.
Constraints:
1 <= N <= 1000
1 <= A[i] <= 1e9
Examples:
Input 1:
    A = [3, 6, 9, 12]
Output 1:
    4
Explanation 1:
    [3, 6, 9, 12] form an arithmetic progression.
Input 2:
    A = [9, 4, 7, 2, 10]
Output 2:
    3
Explanation 2:
    [4, 7, 10] form an arithmetic progression.
"""


# Bruteforce solution. Let n be the length of input array. Iterate all over pairs 0 <= i < j < n and
# build Arithmetic Progression that has first two elements A[i], A[j].
# for i : [0..n - 1]
# 	for j : [i + 1..n - 1]
# 		cur = 2
# 		lst = A[j]
# 		dif = A[j] - A[i]
# 		for k : [j + 1..n - 1]
# 			if (A[k] == lst + dif)
# 				cur++
# 				lst = A[k]
# 		ans = max(ans, cur)
# It’s O(n ^ 3) solution. Think about Dynamic Programming.
# Let dp[i][j] be the length of Longest Arithmetic progression that ends in positions i and j, i.e.
# last element is A[j] and element before last is A[i]. How can we calculate a value for fixed i and j?
# We know two last elements. So we know which number should be before position i. It’s number X such that
# A[i] - X == A[j] - A[i] -> X == 2 * A[i] - A[j]. I.e we can iterate all over 0 <= k < i and
# if A[k] == X then update dp[i][j] by the value of dp[k][i] + 1(it’s easy to understand
# we only need to find rightmost such position).

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, A):
        dp = {}
        prev = A[0]
        d = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                # In Every iteration, we first check if i th index along with A[j]-A[i]
                # difference has been memoized. If yes, we add jth index along with
                # same difference as key in dp, and value is 1+dp[(i,A[j]-A[i])] and
                # remove the previous memo (to save space). If the original memo wasn't
                # present, we memoize it now.
                if (i, A[j] - A[i]) in dp:
                    dp[(j, A[j] - A[i])] = 1 + dp[(i, A[j] - A[i])]  # From ith element to jth element
                    del dp[(i, A[j] - A[i])]
                else:
                    dp[(j, A[j] - A[i])] = 1
        maxx = 0
        # we now find the maximum count
        for i in dp:
            if dp[i] > maxx: maxx = dp[i]
        return maxx + 1


A = [9, 4, 7, 2, 10]
s = Solution()
print(s.solve(A))

#####		Evaluate Expression To True		#####

"""
Given an expression, A, with operands and operators (OR , AND , XOR), in how many ways can you evaluate the
expression to true, by grouping in different ways?
Operands are only true and false.
Return the number of ways to evaluate the expression modulo 103 + 3.
Input Format:
The first and the only argument of input will contain a string, A.
The string A, may contain these characters:
    '|' will represent or operator
    '&' will represent and operator
    '^' will represent xor operator
    'T' will represent true operand
    'F' will false
Output:
Return an integer, representing the number of ways to evaluate the string.
Constraints:
1 <= length(A) <= 150
Example:
Input 1:
    A = "T|F"
Output 1:
    1
Explanation 1:
    The only way to evaluate the expression is:
        => (T|F) = T
Input 2:
    A = "T^T^F"
Output 2:
    0
Explanation 2:
    There is no way to evaluate A to a true statement.
"""


# T|F
# The operator here is 'or'. So, we need to find the number of ways sub-expression left of `|` operator,
# or the sub-expression to the right of the operator, evaluates to true.
# In other words,
# ways = (ways_T_left * ways_T_right) + (ways_F_left * ways_T_right) + (ways_T_left * ways_F_right)
# because T | T = T
#         T | F = T
#         F | T = T
# Can you extend the same analogy to other operators ?
# Assume Tr(i, j) tell us the number of ways to get True from sub-expresion i to j
# Fa(i, j) tell us the number of ways to get False from subexpresion i to j.
# The recurrence relation will look like the following :
# some rules =>
# or operator:
# T|F = T
# T|T = T
# F|T = T
# F|F = F
# and operator:
# T&F = F
# T&T = T
# F&T = F
# F&F = F
# x-or operator
# T^T = F
# T^F = T
# F^T = T
# F^F = F
# for Tr(i, j) :
#    Loop from i to j - 1 into variable k
#      IF(k == AND) :
# 	Tr(i, j) = Tr(i, j) + (Tr(i, k) * Tr(k + 1, j))
#      IF(k == OR) :
# 	Tr(i, j) = Tr(i, j) + (Tr(i, k) * Tr(k + 1, j)) + (Tr(i, k) * Fa(k + 1, j)) + (Fa(i, k) * Tr(k + 1, j))
#      If(k == XOR) :
# 	Tr(i, j) = Tr(i, j) + (Tr(i, k) * Fa(k + 1, j)) + (Fa(i, k) * Tr(k + 1, j))
# for Fa(i, j) :
#  Loop from i to j - 1 into variable k
#    IF(k == AND) :
#      Fa(i, j) = Fa(i, j) + (Fa(i, k) * Fa(k + 1, j)) + (Fa(i, k) * Tr(k + 1, j)) + (Tr(i, k) * Fa(k + 1, j))
#    IF(k == OR) :
# 	Fa(i, j) = Fa(i, j) + (Fa(i, k) * Fa(k + 1, j))
#    If(k == XOR) :
# 	Fa(i, j) = Fa(i, j) + (Tr(i, k) * Tr(k + 1, j)) + (Fa(i, k) * Fa(k + 1, j))
# then use memoziation for better time complexity

class Solution:
    # @param A : string
    # @return an integer
    def cnttrue(self, A):
        bits_and_ops = []
        MOD = 1003
        map_chars = {
            'T': 1,
            'F': 0,
            '|': '|',
            '&': '&',
            '^': '^',
            '|': lambda x, y: sum(x) * sum(y) - x[0] * y[0],
            '&': lambda x, y: x[1] * y[1],
            '^': lambda x, y: x[0] * y[1] + x[1] * y[0]
        }

        if len(A) <= 1:
            if len(A) == 0 or A[0] == 'F':
                return 0
            else:
                return 1

        for idx, curr_char in enumerate(A):
            if idx % 2 == 0 and curr_char not in ['T', 'F']:
                return 0
            if idx % 2 == 1 and curr_char not in ['|', '&', '^']:
                return 0

            bits_and_ops.append(map_chars[curr_char])

        dp = {}
        for i in range(0, len(bits_and_ops) - 2, 2):
            if bits_and_ops[i] == 0:
                x = [1, 0]
            else:
                x = [0, 1]
            if bits_and_ops[i + 2] == 0:
                y = [1, 0]
            else:
                y = [0, 1]

            dp[i, i] = x
            dp[i + 2, i + 2] = y

            cnt_ones_combs = bits_and_ops[i + 1](x, y)
            total_combs = sum(x) * sum(y)
            dp[i, i + 2] = [total_combs - cnt_ones_combs, cnt_ones_combs]

        for d in range(4, len(bits_and_ops), 2):
            for i in range(0, len(bits_and_ops) - d, 2):
                dp[i, i + d] = [0, 0]
                for j in range(i, i + d, 2):
                    x = dp[i, j]
                    y = dp[j + 2, i + d]
                    cnt_ones_combs = bits_and_ops[j + 1](x, y)
                    total_combs = sum(x) * sum(y)

                    dp[i, i + d] = [dp[i, i + d][0] + total_combs - cnt_ones_combs, dp[i, i + d][1] + cnt_ones_combs]

        return dp[0, len(bits_and_ops) - 1][1] % MOD


#####		Best Time To Buy And Sell Stocks 2		#####

"""
Say you have an array, A, for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.
Return the maximum possible profit.
Input Format:
The first and the only argument is an array of integers, A.
Output Format:
Return an integer, representing the maximum possible profit.
Constraints:
1 <= len(A) <= 7e5
1 <= A[i] <= 1e7
Examples:
Input 1:
    A = [1, 2]
Output 1:
    1
Explanation:
    Buy the stock on day 0, and sell it on day 1.
Input 2:
    A = [1, 4, 5, 2, 4]
Output 2:
    4
Explanation:
    Buy the stock on day 0, and sell it on day 2.
"""


# If you buy your stock on day i, you’d obviously want to sell it on the day its price is maximum after that day.
# So essentially at every index i, you need to find the maximum in the array in the suffix.
# Now this part can be done in 2 ways :
# 1) Have another array which stores that information.
# max[i] = max(max[i+1], A[i])
# 2) Start processing entries from the end maintaining a maximum till now. Constant additional space requirement.


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        prices = A
        buy_price, profit = float('inf'), 0  # set buy_price and profit to the highest and lowest possible options
        for price in prices:
            if price < buy_price: buy_price = price  # in case you find the lowest price, set it as buy_price
            # in case profit is the highest, set it as new profit
            if price - buy_price > profit: profit = price - buy_price
        return profit


#####		Word Break 1		#####

"""
Given a string A and a dictionary of words B, determine if A can be segmented into a
space-separated sequence of one or more dictionary words.
Input Format:
The first argument is a string, A.
The second argument is an array of strings, B.
Output Format:
Return 0 / 1 ( 0 for false, 1 for true ) for this problem.
Constraints:
1 <= len(A) <= 6500
1 <= len(B) <= 10000
1 <= len(B[i]) <= 20
Examples:
Input 1:
    A = "myinterviewtrainer",
    B = ["trainer", "my", "interview"]
Output 1:
    1
Explanation 1:
    Return 1 ( corresponding to true ) because "myinterviewtrainer" can be segmented as "my interview trainer".
Input 2:
    A = "a"
    B = ["aaa"]
Output 2:
    0
Explanation 2:
    Return 0 ( corresponding to false ) because "a" cannot be segmented as "aaa".
"""


# Lets again look at the bruteforce solution.
# You start exploring every substring from the start of the string, and check if its in the dictionary. If it is, then
# you check if it is possible to form rest of the string using the dictionary words. If yes, my answer is true.
# If none of the substrings qualify, then our answer is false.
# So something like this :
#     bool wordBreak(int index, string &s, unordered_set<string> &dict) {
#         // BASE CASES
#
#         bool result = false;
#         // try to construct all substrings.
#         for (int i = index; i < s.length(); i++) {
#             substring = *the substring s[index..i] with i inclusive*
#             if (dict contains substring) {
#                 result |= wordBreak(i + 1, s, dict); // If this is true, we are done.
#             }
#         }
#         return result;
#     }
# This solution itself is exponential. However, do note that we are doing a lot of repetitive work.
# Do note, that index in the wordBreak function call can only take s.length() number of values [0, s.length].
# What if we stored the result of the function somehow and did not process it everytime the function is called ?

class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        group = set()
        for i in B:
            group.add(i)

        store = dict([])
        for i in range(len(A) - 1, -1, -1):
            for j in range(i + 1, len(A) + 1):
                if A[i:j] in group:
                    if j < len(A) and A[j:] in store:
                        store[A[i:]] = 1
                        break
                    elif j == len(A):
                        store[A[i:]] = 1

        if A in store:
            return 1
        else:
            return 0


#####		Intersecting Chords In A Circle		#####

"""
Given a number A, return number of ways you can draw A chords in a circle
with 2 x A points such that no 2 chords intersect.
Two ways are different if there exists a chord which is present in one way and not in other.
Return the answer modulo 109 + 7.
Input Format:
The first and the only argument contains the integer A.
Output Format:
Return an integer answering the query as described in the problem statement.
Constraints:
1 <= A <= 1000
Examples:
Input 1:
    A = 1
Output 1:
    1
Explanation 1:
    If points are numbered 1 to 2 in clockwise direction, then different ways to draw chords are:
    {(1-2)} only.
    So, we return 1.
Input 2:
    A = 2
Output 2:
    2
Explanation 2:
    If points are numbered 1 to 4 in clockwise direction, then different ways to draw chords are:
    {(1-2), (3-4)} and {(1-4), (2-3)}.
    So, we return 2.
"""


# Think in terms of DP.
# Can we relate answer for N with smaller answers.
# If we draw a chord between any two points, can you observe current set of points getting broken into two
# smaller sets S_1 and S_2? Can a chord be drawn between two points where each point belong to different set?
# If we draw a chord from a point in S_1 to a point in S_2, it will surely intersect the chord we’ve just drawn.
# So, we can arrive at a recurrence that Ways(n) = sum[i = 0 to n-1] { Ways(i)*Ways(n-i-1) }.
# Here we iterate over i, assuming that size of one of the sets is i and size of other set automatically
# is (n-i-1) since we’ve already used a pair of points and i pair of points in one set.

class Solution:
    # @param A : integer
    # @return an integer
    def chordCnt(self, A):
        from math import factorial
        ans = factorial(2 * A) // factorial(A + 1)
        ans = ans // factorial(A)
        ans = ans % (10 ** 9 + 7)
        return ans


#####		Edit Distance		#####

"""
Given two strings A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)
You have the following 3 operations permitted on a word:
Insert a character
Delete a character
Replace a character
Input Format:
The first argument of input contains a string, A.
The second argument of input contains a string, B.
Output Format:
Return an integer, representing the minimum number of steps required.
Constraints:
1 <= length(A), length(B) <= 450
Examples:
Input 1:
    A = "abad"
    B = "abac"
Output 1:
    1
Explanation 1:
    Operation 1: Replace d with c.
Input 2:
    A = "Anshuman"
    B = "Antihuman"
Output 2:
    2
Explanation 2:
    => Operation 1: Replace s with t.
    => Operation 2: Insert i.
"""


# int editDistance(string &S1, int index1, string &S2, int index2) {
# // BASE CASES
#
# if (S1[index1] == S2[index2]) {
#      return editDistance(S1, index1 + 1, S2, index2 + 1);
# } else {
#      return min(
#     1 + editDistance(S1, index1 + 1, S2, index2), // Delete S1 char
#             1 + editDistance(S1, index1, S2, index2 + 1), // Insert S2 char
#             1 + editDistance(S1, index1 + 1, S2, index2 + 1) // Replace S1 first char with S2 first char
#      );
# } }
# The above approach is definitely exponential.
# However, lets look at the number of ways in which the function can be called. S1 and S2 remain constant.
# The only thing changing is index1 and index2 which can take len(S1) * len(S2) number of values.
# Can you use it to memoize ?

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        n = len(A) + 1
        m = len(B) + 1
        M = [[0] * m for _ in range(n)]
        for j in range(m):
            M[0][j] = j  # Setting the boundary as number of characters
        for i in range(n):
            M[i][0] = i  # Setting the boundary as number of characters
        print(M)
        for i in range(1, n):
            for j in range(1, m):
                c = 0 if A[i - 1] == B[j - 1] else 1
                M[i][j] = min(M[i][j - 1] + 1, M[i - 1][j] + 1, M[i - 1][j - 1] + c)
        return M[-1][-1]


s = Solution()
print(s.minDistance('abad', 'abac'))

#####		Max Sum Path Binary Tree		#####

"""
Given a binary tree T, find the maximum path sum.
The path may start and end at any node in the tree.
Input Format:
The first and the only argument contains a pointer to the root of T, A.
Output Format:
Return an integer representing the maximum sum path.
Constraints:
1 <= Number of Nodes <= 7e4
-1000 <= Value of Node in T <= 1000
Example :
Input 1:
       1
      / \
     2   3
Output 1:
     6
Explanation 1:
    The path with maximum sum is: 2 -> 1 -> 3
Input 2:
       -10
       /  \
     -20  -30
Output 2:
    -10
Explanation 2
    The path with maximum sum is: -10
"""


# There are several ways of looking at this problem.
# If we knew that root R is going to be a part of the longest path. Then we can look at the longest path to any
# leaf in the left subtree, longest path in the right subtree, and add them up along with root’s value to get the
# answer ( Obviously we only consider a path if its value is not negative ). To calculate the longest path till a leaf
# is O(n) [ Recursive call carrying forward the cumulative sum to a node ].
# Given N possible roots, and then the O(n) leaf path calculation, the bruteforce becomes O(n^2).
# However, note that the calculation of the longest path to the leaf is very redundant. So, to calculate the
# result for root R, can you reuse the results you have for R->left / R->right ?

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxPathSum(self, root):
        if root is None:
            return 0
        res = [-2 ** 31]

        def maxPathSumUtil(root):
            if root is None:
                return 0
            l = maxPathSumUtil(root.left)
            r = maxPathSumUtil(root.right)
            max_single = max(max(l, r) + root.val, root.val)
            max_top = max(max_single, l + r + root.val)
            res[0] = max(res[0], max_top)
            return max_single

        maxPathSumUtil(root)
        return res[0]


#####		Stairs		#####

"""
You are climbing a stair case and it takes A steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Input Format:
The first and the only argument contains an integer A, the number of steps.
Output Format:
Return an integer, representing the number of ways to reach the top.
Constrains:
1 <= A <= 36
Example :
Input 1:
A = 2 Output 1:
2 Explanation 1:
[1, 1], [2] Input 2:
A = 3 Output 2:
3 Explanation 2:
[1 1 1], [1 2], [2 1]
"""


# This is the most basic dynamic programming problem.
# We know that we can take 1 or 2 step at a time. So, to take n steps, we must have arrived at it immediately from
# n - 1 or n-2th step.
# If we knew the number of ways to reach n-1 and n-2th step, our answer would be the summation of their number of ways.
# BONUS: Can you come up with O(logn) solution

class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        if A > 1:
            res = [0 for i in range(A + 1)]
        elif A == 1:
            return 1
        res[0] = 1
        res[1] = 1
        for i in range(2, A + 1):
            res[i] = res[i] + res[i - 1] + res[i - 2]
        return res[A]


s = Solution()
print(s.climbStairs(3))

#####		Repeating Subsequence		#####

"""
Given a string A, find if there is any subsequence that repeats itself.
A subsequence of a string is defined as a sequence of characters generated by deleting
some characters in the string without changing the order of the remaining characters.
NOTE : sub-sequence length should be greater than or equal to 2.
Input Format:
The first and the only argument of input contains a string A.
Output Format:
Return an integer, 0 or 1:
    => 0 : False
    => 1 : True
Constraints:
1 <= length(A) <= 100
Examples:
Input 1:
    A = "abab"
Output 1:
    1
Explanation 1:
    "ab" is repeated.
Input 2:
    A = "abba"
Output 2:
    0
Explanation 2:
    There is no repeating subsequence.
"""


# Now, to find longest repeating subsequence, lets try finding the longest common subsequence
# between the string A and itself ( LCS(A, A) ). The only restriction we want to impose is that you cannot match a
# character with its replica in the other string. In other words, if S1 and S2 are the replicas of the string
# for which we want to find LCS, S1[i] != S2[i] for all index i.
# Rec(i, j) =   |
#               |   Rec(i + 1, j)
#          max  |
#               |   Rec(i, j + 1)
#               |
#               |   Rec(i + 1, j + 1) + 1 IF i != j and A[i] == A[j]


class Solution:
    # @param A : string
    # @return an integer
    def anytwo(self, A):
        # tab represents length of matching substring from index i to j
        tab = [[0 for i in range(len(A) + 1)] for j in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(A) + 1):
                if i != j and A[i - 1] == A[j - 1]:
                    tab[i][j] = 1 + tab[i - 1][j - 1]  # For i and j value increments due to match
                    if tab[i][j] >= 2:
                        return 1
                else:
                    tab[i][j] = max(tab[i - 1][j], tab[i][j - 1])
        return 0


A = 'abcdbcab'
s = Solution()
print(s.anytwo(A))

#####		Max Sum Without Adjacent Elements		#####

"""
Given a 2 x N grid of integer, A, choose numbers such that the sum of the numbers
is maximum and no two chosen numbers are adjacent horizontally, vertically or diagonally, and return it.
Note: You can choose more than 2 numbers.
Input Format:
The first and the only argument of input contains a 2d matrix, A.
Output Format:
Return an integer, representing the maximum possible sum.
Constraints:
1 <= N <= 20000
1 <= A[i] <= 2000
Example:
Input 1:
    A = [   [1]
            [2]    ]
Output 1:
    2
Explanation 1:
    We will choose 2.
Input 2:
    A = [   [1, 2, 3, 4]
            [2, 3, 4, 5]    ]
Output 2:
    We will choose 3 and 5.
"""


# Suppose we have 2 * N list :
# 1 |  2  |  3  | 4
# 2 |  3  |  4  | 5
# Now suppose we choose 2, then we can't choose the element just above it 1,
# the element next it 3, or the element diagonally opposite.
# In other words, if we are on (x, y), then if we choose (x, y), we can't choose
# (x + 1, y), (x, y + 1) and (x + 1, y + 1)

# This means that choosing V[0][i] or V[1][i] has identical bearing on the elements which are ruled out.
# So, instead we replace each column with a single element which is the max of V[0][i], V[1][i]
# Now we have the list as : 2 3 4 5
# Now our recurrence relation will depend only on position i and,
# a "include_current_element" which will denote whether we picked last element or not.


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        if len(A[0]) == 1:
            return max(A[0][-1], A[1][-1])
        n = len(A[0])
        arr = [0 for i in range(n)]
        arr[-1] = max(A[0][-1], A[1][-1])  # Choosing the max of the last elements
        arr[-2] = max(A[0][-2], A[1][-2], arr[-1])  # Either choosing the second last column or last column max
        for i in range(n - 3, -1, -1):
            temp = max(A[0][i], A[1][i])  # Instead of changing/creating array, just store the present value
            arr[i] = max(temp + arr[i + 2], arr[i + 1])
        return arr[0]


#####		Min Sum Path In Triangle		#####

"""
In triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
 Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""


# Brute force : Try traversing each possible path from top to the leaves. Not an acceptable solution in this case.
#
# The triangle has a tree-like structure, which would lead people to think about traversal algorithms such as DFS.
# However, if you look closely, you would notice that the adjacent nodes always share a ‘branch’. In other word,
# there are overlapping subproblems. Also, suppose x and y are ‘children’ of k. Once minimum paths from x and y to
# the bottom are known, the minimum path starting from k can be decided in O(1), that is optimal substructure.
# Therefore, dynamic programming would be the best solution to this problem in terms of time complexity.
# For ‘top-down’ DP, starting from the node on the very top, we recursively find the minimum path sum of each node.
# When a path sum is calculated, we store it in an array (memoization); the next time we need to calculate the path
# sum of the same node, just retrieve it from the array. However, you will need a cache that is at least the same
# size as the input triangle itself to store the pathsum, which takes O(N^2) space. With some clever thinking, it
# might be possible to release some of the memory that will never be used after a particular point, but the order
# of the nodes being processed is not straightforwardly seen in a recursive solution, so deciding which part of the
# cache to discard can be a hard job.
# ‘Bottom-up’ DP, on the other hand, is very straightforward: we start from the nodes on the bottom row; the min
# pathsums for these nodes are the values of the nodes themselves. From there, the min pathsum at the ith node on the
# kth row would be the lesser of the pathsums of its two children plus the value of itself, i.e.:
# minpath[k][i] = min( minpath[k+1][i], minpath[k+1][i+1]) + triangle[k][i];
# Or even better, since the row minpath[k+1] would be useless after minpath[k] is computed, we can simply set minpath
# as a 1D array, and iteratively update itself:
# For the kth level:
# minpath[i] = min( minpath[i], minpath[i+1]) + triangle[k][i];


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        # filling bottom up
        for i in range(len(A) - 2, -1, -1):
            for j in range(len(A[i])):
                A[i][j] += min(A[i + 1][j], A[i + 1][j + 1])
        return A[0][0]


#####		N Digit Numbers With Digit Sum S		#####

"""
Find out the number of N digit numbers, whose digits on being added equals to a given number S.
Note that a valid number starts from digits 1-9 except the number 0 itself. i.e. leading zeroes are not allowed.
Since the answer can be large, output answer modulo 1000000007
**
N = 2, S = 4
Valid numbers are {22, 31, 13, 40}
Hence output 4.
"""


# Part 1
# Lets build a recursive approach to this problem. Let rec_Count(id, sum) be the number of numbers having digit count
# as id and digit sum as sum. To be more clear,
# rec_Count(id, sum) = ∑ rec_Count(id-1,sum-x) where 0 <= x <= 9 && sum-x >= 0.
# Note that the above relation has not handled the leading zeroes case. How can you handle them ?
# Part 2
# We can handle them by calling this rec_Count function for the first digit explicitly. i.e. we can fix the starting
# digits from 1-9 explicitly and then call the recursion function to handle the other digits(i.e. N - 1 digits).
# Finally we can add them together to get the final answer.
# Gotcha : Try to think about the approach when sum is given as 0.
# Now, we have the recursive solution. However, the recursive solution is too
# expensive because of the exponential time complexity.
# A key thing to note here is that there are overlapping subproblems as many things are being calculated repeatedly
# in the recursive solution ? Can you use the concept of Dynamic programming to optimize the time complexity here ?
# Final solution
# My recursive function only depends on id and sum variable. If ID is the max possible id, and SUM is the max possible
# sum, then there are only ID * SUM number of ways in which the function can be called.
# We can use memoization to store those values.


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, N, S):
        arr = [[0 for j in range(S + 1)] for i in range(N + 1)]
        arr[0][0] = 1
        for n in range(N):
            for s in range(S):
                for digit in range(10):
                    if s + digit <= S:
                        arr[n + 1][s + digit] += arr[n][s]
                    else:
                        break
        return arr[N][S] % 1000000007


s = Solution()
print(s.solve(10, 16))

#####		Largest Area Rectangle Permutations		#####

"""
Given a binary grid i.e. a 2D grid only consisting of 0’s and 1’s, find the area of the largest rectangle inside the
grid such that all the cells inside the chosen rectangle should have 1 in them. You are allowed to permutate the
columns matrix i.e. you can arrange each of the column in any order in the final grid.
Please follow the below example for more clarity.
Lets say we are given a binary grid of 3 * 3 size.
1 0 1
0 1 0
1 0 0
At present we can see that max rectangle satisfying the criteria mentioned in the problem is of 1 * 1 = 1 area
i.e either of the 4 cells which contain 1 in it. Now since we are allowed to permutate the columns of the given matrix,
we can take column 1 and column 3 and make them neighbours. One of the possible configuration of the grid can be:
1 1 0
0 0 1
1 0 0
Now In this grid, first column is column 1, second column is column 3 and third column is column 2 from the original
given grid. Now, we can see that if we calculate the max area rectangle, we get max area as 1 * 2 = 2 which is bigger
than the earlier case. Hence 2 will be the answer in this case.
"""


# Let’s try to think polynomial time approach.
# Let’s say for each index i.e. (i, j) pair, we store a value which corresponds to the number of consecutive cells
# having 1 as their value which are directly above that cell starting from the given cell itself. Lets store this
# value in an array called count. Thus count[i][j] will denote the number of
# consecutive 1’s starting from the cell (i, j) and continuing upwards.
# For example, for a given matrix
# 1 0 1
# 1 1 0
# 1 0 1
#  Its count matrix will be -
# 1 0 1
# 2 1 0
# 3 0 1
# Now, once we have got this array, let’s consider a row i. Each element of this row will have some count[i][j]
# value where j is from 1 to m. Now as permutation is allowed, we can select any order for keeping the columns.
# Let’s fix that ordering for time being with lower the value of count[i][j], the earlier it is getting placed.
# So we will have a sorted arrangement of columns according to their count[i][j] values. We can easily see that
# while traversing through the above sorted arrangement, we can calculate the maximum area possible for that particular
# row. On repeating this algorithm for each row of the grid will give us the maximum area rectangle
# possible in the given grid.

class Solution:
    def solve(self, A):
        x = len(A)
        y = len(A[0])
        for j in range(y):
            count = 0
            for i in range(x):  # Going column wise
                if A[i][j] == 1:
                    count = count + 1  # Number of 1s in row
                else:
                    count = 0  # If 0
                A[i][j] = count  # Setting Matrix entry with the count of 1s
        for k in range(x):
            A[k].sort(reverse=True)  # Descending order arrangement of 1s count
        size = 0
        for i in range(x - 1, -1, -1):
            for j in range(y - 1, -1, -1):
                mult1 = A[i][j]
                mult2 = j + 1  # This is non zero so all those to the left can be taken in the rectangle
                size = max(size, mult1 * mult2)  # Maximum Size by finding length*breadth
        return size  # Size denotes the Maximum Size of the rectangle with 1s


A = [
    [1, 0, 1],
    [1, 1, 0],
    [1, 0, 1]
]

s = Solution()
print(s.solve(A))

#####		Jump Game Array		#####

"""
Given an array of non-negative integers, A, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
Input Format:
The first and the only argument of input will be an integer array A.
Output Format:
Return an integer, representing the answer as described in the problem statement.
    => 0 : If you cannot reach the last index.
    => 1 : If you can reach the last index.
Constraints:
1 <= len(A) <= 1e6
0 <= A[i] <= 30
Examples:
Input 1:
    A = [2,3,1,1,4]
Output 1:
    1
Explanation 1:
    Index 0 -> Index 2 -> Index 3 -> Index 4 -> Index 5
Input 2:
    A = [3,2,1,0,4]
Output 2:
    0
Explanation 2:
    There is no possible path to reach the last index.
"""


# Note that from an index i, you can choose to jump to any index in the range [i, i+A[i]].
# Now if there is at least one index in the said range from where it is possible to jump to the end index, we are done.
# So if we start solving from end to start, and for every i, we loop j from i to i + A[i], and check if a
# solution is possible for j, then solution is possible for i.
# This approach is however not linear. Take a moment and try to think if you can reduce this to O(n) approach.
# To move to linear approach, just maintain the minimum index which has solution possible till now.
# If its less than i+A[i]], then solution is possible for i and the minimum index gets updated to i.
class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
        chk = [i for i in A]
        print(chk)
        for i in range(len(A) - 1):
            for j in range(i + 1, min(i + A[i] + 1, len(A))):
                chk[j] += A[i] - (j - i)  # What is this trying to do??
        print(chk)
        for i in range(len(chk)):
            if chk[i] == 0 and i != len(chk) - 1:  # Any unreachable position, except end
                return 0
        return 1


A = [3, 2, 1, 0, 4]
s = Solution()
print(s.canJump(A))

#####		Ways To Decode		#####

"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.
Input Format:
The first and the only argument is a string A.
Output Format:
Return an integer, representing the number of ways to decode the string.
Constraints:
1 <= length(A) <= 1e5
Example :
Input 1:
    A = "8"
Output 1:
    1
Explanation 1:
    Given encoded message "8", it could be decoded as only "H" (8).
    The number of ways decoding "8" is 1.
Input 2:
    A = "12"
Output 2:
    2
Explanation 2:
    Given encoded message "12", it could be decoded as "AB" (1, 2) or "L" (12).
    The number of ways decoding "12" is 2.
"""


# So, when looking at the start of the string, we can either form a one digit code, and then look at the ways of
# forming the rest of the string of length L - 1, or we can form 2 digit code if its valid and add up the ways
# of decoding rest of the string of length L - 2.


class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        if len(A) == 0:
            return 0

        # No decoding starting with 0 will be a valid decoding.
        if int(A[0]) == 0:
            return 0

        n = len(A)

        # Mark everything as zero initially
        result = [0 for _ in range(0, n + 1)]  # Notice how it is initialized to size n+1 not n

        # Now that we know that the string does not begin with zero,
        # the minimum number of decodings for a length 2 string will be 1.
        # So mark both as 1.
        result[0] = result[1] = 1

        for i in range(1, n):

            # At every step, we can either decode 1 or 2 characters. Fish them out.
            v1 = int(A[i:i + 1])
            v2 = int(A[i - 1:i + 1])

            # A number starting with 0, won't be a valid single number decoding.
            # It can only fit with either 10 or 20 (depends on previous number)
            if 0 < v1 <= 9:
                # If we get a valid single number decoding, the number of decodings will
                # same as previous. Because a single valid decoding won't add to your count.
                result[i + 1] = result[i]

            if 10 <= v2 <= 26:
                # Check if a double number decoding is valid.
                # If it is valid, we need to add everything before this two digit number to the current number.
                result[i + 1] = result[i + 1] + result[i - 1]

            # At any state, if we are not able to modify something, it is invalid.
            if result[i + 1] == 0:
                return 0

        answer = result[n]
        return answer


s = Solution()
print(s.numDecodings("121"))

#####		Unique Paths In A Grid		#####

"""
Given a grid of size m * n, lets assume you are starting at (1,1) and your goal is to reach (m,n). At any instance,
if you are on (x,y), you can either go to (x, y + 1) or (x + 1, y).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
Example :
There is one obstacle in the middle of a 3x3 grid as illustrated below.
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
 Note: m and n will be at most 100.
"""


# Dynamic programming FTW.
# If you look at a cell, there are atmost 2 ways to reach it. From the cell left and up.
# If the cell does not have an obstacle, then the number of ways to reach this cell would be the summation of the
# number of ways to reach the immediate neighbors preceding it ( left and up ).

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        if not A: return 0
        if A[-1][-1] == 1 or A[0][0] == 1: return 0

        paths = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
        paths[0][0] = 1

        for x in range(len(A)):
            for y in range(len(A[0])):
                prev_left_val = 0 if x - 1 < 0 else paths[x - 1][y]
                prev_down_val = 0 if y - 1 < 0 else paths[x][y - 1]
                paths[x][y] += (prev_left_val + prev_down_val) if A[x][y] == 0 else 0

        return paths[x][y]


#####		Best Time To Buy And Sell Stocks		#####

"""
Say you have an array, A, for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most 2 transactions.
Return the maximum possible profit.
Note: You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
Input Format:
The first and the only argument is an integer array, A.
Output Format:
Return an integer, representing the maximum possible profit.
Constraints:
1 <= length(A) <= 7e5
1 <= A[i] <= 1e7
Examples:
Input 1:
    A = [1, 2, 1, 2]
Output 1:
    2
Explanation 1:
    Day 0 : Buy
    Day 1 : Sell
    Day 2 : Buy
    Day 3 : Sell
Input 2:
    A = [7, 2, 4, 8, 7]
Output 2:
    6
Explanation 2:
    Day 1 : Buy
    Day 3 : Sell
"""

# What if you construct your DP space as :
# f[k, ii] represents the max profit up until prices[ii] (Note: NOT ending with prices[ii]) using at most k transactions
# How would you fill in values in f[k, ii] and how would the DP relations look like.

INF = float('inf')


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        """
        For one transaction, we can do it linearly:
        price that day - minimum seen so far.
        For two transactions, we evaluates this at day i + best for remaining days.
        """

        # Best solutions based on increasing starting days
        # We are doing it backward
        bystart = []
        high = -INF  # maximum so far
        best = 0
        for x in reversed(A):
            best = max(best, high - x)
            bystart.append(best)
            high = max(high, x)
        low = INF  # minimum so far
        best = 0
        total = 0
        for x, best2 in zip(A, reversed(bystart)):
            best = max(best, x - low)
            total = max(total, best + best2)
            low = min(low, x)
        return total


#####		Regex Match 2		#####

"""
Implement regular expression matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
The function prototype should be:
int isMatch(const char *s, const char *p)
Some examples:
isMatch("aa","a") → 0
isMatch("aa","aa") → 1
isMatch("aaa","aa") → 0
isMatch("aa", "a*") → 1
isMatch("aa", ".*") → 1
isMatch("ab", ".*") → 1
isMatch("aab", "c*a*b") → 1
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""


# This looks just like a straight forward string matching, isn’t it? Couldn’t we just match the pattern and the input
# string character by character? The question is, how to match a '*' ?
# A natural way is to use a greedy approach; that is, we attempt to match the previous character as many as we can.
# Does this work? Let us look at some examples.
# s = “abbbc”
# p = “ab*c”
# Assume we have matched the first ‘a’ on both s and p. When we see "b*" in p, we skip all b’s in s. Since the
# last ‘c’ matches on both side, they both match.
# s = “ac”
# p = “ab*c”
# After the first ‘a’, we see that there is no b’s to skip for “b*”. We match the last ‘c’ on both side and
# conclude that they both match.
# It seems that being greedy is good. But how about this case?
# s = “abbc”
# p = “ab*bbc”
# When we see “b*” in p, we would have skip all b’s in s. They both should match, but we have no more b’s to match.
# Therefore, the greedy approach fails in the above case.
# One might be tempted to think of a quick workaround. How about counting the number of consecutive b’s in s? If it
# is smaller or equal to the number of consecutive b’s after “b*” in p, we conclude they both match and continue from
# there. For the opposite, we conclude there is not a match.
# This seem to solve the above problem, but how about this case:
# s = “abcbcd”
# p = “a.*c.*d”
# Here, “.*” in p means repeat ‘.’ 0 or more times. Since ‘.’ can match any character, it is not clear how many times
# ‘.’ should be repeated. Should the ‘c’ in p matches the first or second ‘c’ in s? Unfortunately, there is no way
# to tell without using some kind of exhaustive search.
# We need some kind of backtracking mechanism such that when a matching fails, we return to the last successful matching
# state and attempt to match more characters in s with ‘*’. This approach leads naturally to recursion.
# The recursion mainly breaks down elegantly to the following two cases:
# If the next character of p is NOT ‘*’, then it must match the current character of s. Continue pattern matching
# with the next character of both s and p.
# If the next character of p is ‘*’, then we do a brute force exhaustive matching of 0, 1, or more repeats of current
# character of p… Until we could not match any more characters.
# You would need to consider the base case carefully too. That would be left as an exercise to the reader. :)

class Solution:
    def isMatch(self, A, B, index_s=0, index_r=0):
        while index_s < len(A) and index_r < len(B):
            if B[index_r] == '.':
                if index_r + 1 < len(B) and B[index_r + 1] == '*':
                    for i in range(index_s, len(A) + 1):
                        if self.isMatch(A, B, i, index_r + 2):
                            return 1
                    return 0
                else:
                    index_s += 1
                    index_r += 1
            else:
                ch = B[index_r]
                if index_r + 1 < len(B) and B[index_r + 1] == '*':
                    for i in range(index_s, len(A) + 1):
                        if i > index_s and A[i - 1] != ch:
                            break
                        if self.isMatch(A, B, i, index_r + 2):
                            return 1
                    return 0
                else:
                    if ch == A[index_s]:
                        index_r += 1
                        index_s += 1
                    else:
                        return 0
        if index_s == len(A) and index_r == len(B):
            return 1
        if index_s == len(A) or index_r == len(B):
            return 0


#####		Palindrome Partitioning 2		#####

"""
Given a string A, partition A such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of A.
Input Format:
The first and the only argument contains the string A.
Output Format:
Return an integer, representing the answer as described in the problem statement.
Constraints:
1 <= length(A) <= 501
Examples:
Input 1:
    A = "aba"
Output 1:
    0
Explanation 1:
    "aba" is already a palindrome, so no cuts are needed.
Input 2:
    A = "aab"
Output 2:
    1
Explanation 2:
    Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""


# Firstly, we should be able to answer if substring [i,i+1,….j]
# is palindrome or not in O(1) with pre-computation of O(n^2).
# Now try to come up with some DP state which can find minimum cut using above data.

class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, A):
        def palin(string):
            if string == string[::-1]:
                return 1
            else:
                return 0

        dp = [0 for i in range(len(A) + 1)]
        dp[-1] = -1
        for i in range(len(A) - 1, -1, -1):
            val = len(A) - 1 - i
            for j in range(i + 1, len(A) + 1):
                if palin(A[i:j]) == 1:
                    val = min(val, 1 + dp[j])
            dp[i] = val
        return dp[0]


#####		Tushars Birthday Party		#####

"""
As it is Tushar’s Birthday on March 1st, he decided to throw a party to all his friends at TGI Fridays in Pune.
Given are the eating capacity of each friend, filling capacity of each dish and cost of each dish.
A friend is satisfied if the sum of the filling capacity of dishes he ate is equal to his capacity. Find the minimum
cost such that all of Tushar’s friends are satisfied (reached their eating capacity).
NOTE:
Each dish is supposed to be eaten by only one person. Sharing is not allowed.
Each friend can take any dish unlimited number of times.
There always exists a dish with filling capacity 1 so that a solution always exists.
Input Format
Friends : List of integers denoting eating capacity of friends separated by space.
Capacity: List of integers denoting filling capacity of each type of dish.
Cost :    List of integers denoting cost of each type of dish.
Constraints:
1 <= Capacity of friend <= 1000
1 <= No. of friends <= 1000
1 <= No. of dishes <= 1000
Example:
Input:
    2 4 6
    2 1 3
    2 5 3
Output:
    14
Explanation:
    First friend will take 1st and 2nd dish, second friend will take 2nd dish twice.  Thus, total cost = (5+3)+(3*2)= 14
"""


# **Observations: **
# As the friends cannot share dishes, we can calculate the cost for each of them independently and add all such costs.
# Now, the problem instance for every friend is reduced to standard KnapSack problem.
# **Dynamic programming recurrence: **
# dp[i][j] –> min. cost to satisfy a person with capacity i using first j dishes.
# dp[i][j] = min( dp[i][j-1] , dp[ i-fillCap[j] ][j] + cost[j] ) // if ( i-fillCap[j] ) >= 0
# dp[i][j] = dp[i][j-1] // otherwise
# As one dish can be taken multiple times, we have used dp[ i-fillCap[j] ][ j ]
# and not dp[ i-fillCap[j] ][ j-1 ]. This is different from standard KnapSack where one element can be used only once.
# Note: Base cases should be handled properly.

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def solve(self, friends, capacity, price):
        goal = max(friends)
        dp = [0] + [float("inf")] * goal

        for cap, pr in zip(capacity, price):
            for i in range(cap, goal + 1):
                cand_price = dp[i - cap] + pr
                if cand_price < dp[i]:
                    dp[i] = cand_price

        return sum(dp[friend] for friend in friends)


#####		Scramble String		#####

"""
Given a string A, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
Below is one possible representation of A = “great”:
    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.
For example, if we choose the node “gr” and swap its two children, it produces a scrambled string “rgeat”.
    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that “rgeat” is a scrambled string of “great”.
Similarly, if we continue to swap the children of nodes “eat” and “at”, it produces a scrambled string “rgtae”.
    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that “rgtae” is a scrambled string of “great”.
Given two strings A and B of the same length, determine if B is a scrambled string of S.
Input Format:
The first argument of input contains a string A.
The second argument of input contains a string B.
Output Format:
Return an integer, 0 or 1:
    => 0 : False
    => 1 : True
Constraints:
1 <= len(A), len(B) <= 50
Examples:
Input 1:
    A = "we"
    B = "we"
Output 1:
    1
Input 2:
    A = "phqtrnilf"
    B = "ilthnqrpf"
Output 2:
    0
"""


# Lets first think of a bruteforce solution.
# Obviously the 2 strings need to have the same number of characters and the same character set,
# otherwise the answer is definitely no.
# In the bruteforce solution, we loop to find out the root of the tree.
# Lets say the root is the ith character of string s1. Then the first part of s1 [0…i) can either match
# ( be a scrambled string of ) to s2[0…i) or s2(i+1 .. L]. Depending on which part s1[0…i) matches to,
# we match the remaining part of s1 to remaining part of s2. Just to clarify when we say s1 matches s2,
# we mean s1 is a scrambled string of s2.
# We can write a very easy recursive function for this.
#     public boolean isScramble(String s1, String s2) {
#         // CHECK BASE CASES HERE
#         if (s1 not anagram of s2) return false;
#         for(int i = 1; i < s1.length(); i++) { // i being the root position
#             if(isScramble(s1.substring(0,i), s2.substring(0,i)) && isScramble(s1.substring(i),
#                      s2.substring(i))) return true;
#             if(isScramble(s1.substring(0,i), s2.substring(s2.length()-i)) && isScramble(s1.substring(i),
#                       s2.substring(0, s2.length()-i))) return true;
#         }
#         return false;
#     }
# Now note that in any call for this function, the strings s1 and s2 would always be substrings of original S1 and S2.
# And we can specify substrings using startIndex, endIndex.
# Which means the recursive function can only be called with (startIndex1, endIndex1, startIndex2, endIndex2)
# possible tuples which can only take LLL*L possibilities roughly.
# Memoization ?
# Additional Hint :
# Function calls are only valid if endIndex1 - startIndex1 = endIndex2 - startIndex2.
# Can you just look at (startIndex1, endIndex1, startIndex2) and infer the endIndex2 based on these values ?
# Or keep passing around (startIndex1, startIndex2, length) ?

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isScramble(self, A, B):
        dpMap = dict()

        def helper(i1, i2, l):
            key = (i1, i2, l)
            if key not in dpMap:
                dpMap[key] = l == 0
                if l == 1:
                    dpMap[key] = A[i1] == B[i2]
                else:
                    for ind in range(1, l):
                        if any([
                            helper(i1, i2, ind) and helper(i1 + ind, i2 + ind, l - ind),
                            helper(i1, i2 + l - ind, ind) and helper(i1 + ind, i2, l - ind)
                        ]):
                            dpMap[key] = True
                            break
            return dpMap[key]

        return int(helper(0, 0, len(A)))


#####		Flip Array		#####

"""
Given an array of positive elements, you have to flip the sign of some of its elements such that the resultant sum of
the elements of array should be minimum non-negative(as close to zero as possible). Return the minimum no. of elements
whose sign needs to be flipped such that the resultant sum is minimum non-negative.
Constraints:
 1 <= n <= 100
Sum of all the elements will not exceed 10,000.
Example:
A = [15, 10, 6]
ans = 1 (Here, we will flip the sign of 15 and the resultant sum will be 1 )
A = [14, 10, 4]
ans = 1 (Here, we will flip the sign of 14 and the resultant sum will be 0)
 Note that flipping the sign of 10 and 4 also gives the resultant sum 0 but flippings there are not minimum
"""


# Let the sum of all the given elements be S.
# This problem can be reduced to a Knapsack problem where we have to fill a Knapsack of capacity (S/2) as fully as
# possible and using the minimum no. of elements. We will fill the Knapsack with the given elements. Sign of all the
# elements which come into the knapsack will be flipped.
# As sum of all the elements in the Knapsack will be as close to S/2 as possible, we are indirectly calculating
# minimum non-negative sum of all the elements after flipping the sign. Give it a thought and code your way out!


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, A):
        n = len(A)

        def helper(i, cur, memo={}):
            """ Sub problem: minimum reachable from cur,
                by picking elements from A[i:]
                Return minimum reached, minimum numbers of flip """
            if i == n or cur == 0:
                return (cur, 0)
            if (i, cur) in memo:
                return memo[(i, cur)]
            res, flip = helper(i + 1, cur)  # Don't flip A[i]
            if 2 * A[i] <= cur:  # Flip A[i] if valid
                res2, flip2 = helper(i + 1, cur - 2 * A[i])
                res, flip = min((res, flip), (res2, flip2 + 1))
            memo[(i, cur)] = (res, flip)
            return res, flip

        return helper(0, sum(A))[1]


#####		Sub Matrices With Sum Zero		#####

"""
Given a 2D matrix, find the number non-empty sub matrices, such that the sum of the elements inside the
sub matrix is equal to 0. (note: elements might be negative).
Example:
Input

-8 5  7
3  7 -8
5 -8  9
Output
2

Explanation
-8 5 7
3 7 -8
5 -8 9

-8 5 7
3 7 -8
5 -8 9
"""


# Iterate over all pairs of rows. When fixing two rows r1 and r2, we can convert this to 1D version of the problem.
# When we have a 1D array ARR we want to find number of subarrays such that the sum of the elements in the
# subarray is equal to 0. To do that lets iterate from left to right, say we are currently at i-th element.
# If we have i-th prefix sum equal to sum(ARR[0..i]), then we want to find number of such j’s
# that sum(ARR[0..i]) = sum(ARR[0..j]). That means that the subarray ARR[j + 1..i] will have zero sum.
# To efficiently count number of such j’s we can use a HashMap (unordered_map in C++).
# In order to convert the problem to 1D, when we have a pair of fixed rows r1 and r2, we will keep a 2D prefix sums,
# let’s call it PRE (let’s also assume that initial matrix is A). PRE[i, j] will be the sum of elements in sub matrix
# whose upper left corner is [0, 0] and lower right corner is [i, j]. In other words it is a sum of all A[p, q] where
# 0 <= p <= i and 0 <= q <= j.
# The calculation of PRE is very easy: PRE[i, j] = A[i, j] + PRE[i - 1, j] + PRE[i, j - 1] - PRE[i - 1, j - 1]
# (if i - 1 or j - 1 are less than 0 then we just omit the terms where they appear). Notice, that we need to
# subtract PRE[i - 1, j - 1] since it is contained in both PRE[i - 1, j] and PRE[i, j - 1] and we want every
# element to appear in PRE[i, j] exactly once. This is called inclusion exclusion principle.
# When we have two fixed rows r1, r2 and have calculated PRE, we can obtain ARR. Note that we don’t really need to
# calculate each element of ARR, since we only need prefix sums of ARR, that is sum(ARR[0..i]) for each i.
# The sum(ARR[0..i]) is equal to PRE[r2][i] - PRE[r1 - 1][i] (if r1 - 1 < 0 then omit second operand).
# Being able to efficiently calculate sum(ARR[0..i]), let’s apply the 1D solution.
# The answer to the problem will be simply the sum of answers for all different pairs of rows.
# Overall time complexity is O(N3).
# Space complexity is O(N2)


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n, m = len(A), len(A[0]) if A else 0
        if not (n and m):
            return 0
        dp_sum, ans = [[0] * (m + 1) for _ in range(n + 1)], 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp_sum[i][j] = dp_sum[i - 1][j] + dp_sum[i][j - 1] - dp_sum[i - 1][j - 1] + A[i - 1][j - 1]

        for i in range(1, n + 1):
            for j in range(i, n + 1):
                counti = {0: 1}
                for k in range(1, m + 1):
                    val = dp_sum[j][k] - dp_sum[i - 1][k]
                    if val in counti:
                        ans = ans + counti[val]
                        counti[val] = counti[val] + 1
                    else:
                        counti[val] = 1
        return ans

    def solve_another(self, A):
        dpMap = dict()

        def presum(i, j):
            key = (i, j)
            if key in dpMap:
                return dpMap[key]
            ans = 0
            if i < 0 or j < 0:
                return 0
            ans = A[i][j] + presum(i - 1, j) + presum(i, j - 1) - presum(i - 1, j - 1)
            dpMap[key] = ans
            return ans

        N, M = len(A), len(A) and len(A[0])
        count = 0

        for i1 in range(N):
            for i2 in range(i1, N):
                countMap = defaultdict(int)
                for j in range(M):
                    s = presum(i2, j) - presum(i1 - 1, j)
                    if s == 0:
                        count += 1
                    count += countMap[s]
                    countMap[s] += 1

        return count


#####		Regex Match 1		#####

"""
Implement wildcard pattern matching with support for ‘?’ and ‘*’ for strings A and B.
’?’ : Matches any single character.
‘*’ : Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
Input Format:
The first argument of input contains a string A.
The second argument of input contains a string B.
Output Format:
Return 0 or 1:
    => 0 : If the patterns do not match.
    => 1 : If the patterns match.
Constraints:
1 <= length(A), length(B) <= 9e4
Examples :
Input 1:
    A = "aa"
    B = "a"
Output 1:
    0
Input 2:
    A = "aa"
    B = "aa"
Output 2:
    1
Input 3:
    A = "aaa"
    B = "aa"
Output 3:
    0
Input 4:
    A = "aa"
    B = "*"
Output 4:
    1
Input 5:
    A = "aa"
    B = "a*"
Output 5:
    1
Input 6:
    A = "ab"
    B = "?*"
Output 6:
    1
Input 7:
    A = "aab"
    B = "c*a*b"
Output 7:
    0
"""


# Think about the bruteforce solution.
# When you encounter ‘’, you would try to call the same isMatch function in the following manner:
# If p[0] == ‘’, then isMatch(s, p) is true if isMatch(s+1, p) is true OR isMatch(s, p+1) is true.
# else if p[0] is not ‘*’ and the characters s[0] and p[0] match ( or p[0] is ‘?’ ),
# then isMatch(s,p) is true only if isMatch(s+1, p+1) is true.
# If the characters don’t match isMatch(s, p) is false.
# This appraoch is exponential. Think why.
# Lets see how we can make this better. Note that isMatch function can only be called with
# suffixes of s and p. As such, there could only be length(s) * length(p) unique calls to isMatch.
# Lets just memoize the result of the calls so we only do processing for unique calls.
# This makes the time and space complexity O(len(s) * len(p)).
# There could be ways of optimizing the approach rejecting certain suffixes without processing them.
# For example, if len(non star characters in p) > len(s), then we can return false without checking anything.

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isMatch(self, s, p):
        if len(p) - p.count('*') > len(s):
            return 0
        DP = [True] + [False] * len(s)
        for c in p:
            if c == '*':
                for n in range(1, len(s) + 1):
                    DP[n] = DP[n - 1] or DP[n]
            else:
                for n in range(len(s) - 1, -1, -1):
                    DP[n + 1] = DP[n] and (c == s[n] or c == '?')
            DP[0] = DP[0] and c == '*'
        return 1 if DP[-1] else 0


#####		Longest Increasing Subsequence		#####

"""
Find the longest increasing subsequence of a given array of integers, A.
In other words, find a subsequence of array in which the subsequence’s elements are
in strictly increasing order, and in which the subsequence is as long as possible.
This subsequence is not necessarily contiguous, or unique.
In this case, we only care about the length of the longest increasing subsequence.
Input Format:
The first and the only argument is an integer array A.
Output Format:
Return an integer representing the length of the longest increasing subsequence.
Constraints:
1 <= length(A) <= 2500
1 <= A[i] <= 2000
Example :
Input 1:
    A = [1, 2, 1, 5]
Output 1:
    3
Explanation 1:
    The sequence : [1, 2, 5]
Input 2:
    A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
Output 2:
    6
Explanation 2:
    The sequence : [0, 2, 6, 9, 13, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15]
"""


class Solution:
    # @param A : tuple of integers
    # @return an integer

    def lis(self, A):
        if len(A) == 0:
            return 0
        arr = [1] * len(A)  # array to store the count of subsequences
        # iterate over the complete array
        for i in range(1, len(A)):
            # check the previous largest subsequence before this element
            # and update the current element value
            for j in range(i - 1, -1, -1):
                if A[i] > A[j]:
                    arr[i] = max(arr[i], arr[j] + 1)
        return max(arr)


arr = [1, 11, 2, 10, 4, 5, 2, 1]
s = Solution()
print("Length of lis is", s.lis(arr))

#####		Dungeon Princess		#####

"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon.
The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the
top-left room and must fight his way through the dungeon to rescue the princess.
The knight has an initial health point represented by a positive integer. If at any point his health point drops to
0 or below, he dies immediately.
Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms;
other rooms are either empty (0’s) or contain magic orbs that increase the knight’s health (positive integers).
In order to reach the princess as quickly as possible knight decides to move only rightward or downward in each step.
Write a function to determine the knight’s minimum initial health so that he is able to rescue the princess.
For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path
RIGHT-> RIGHT -> DOWN -> DOWN.
Dungeon Princess: Example 1
Input arguments to function:
Your function will get an M*N matrix (2-D array) as input which represents the 2D grid as described in the question.
Your function should return an integer corresponding to the knight’s minimum initial health required.
 Note:
The knight’s health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room
where the princess is imprisoned.
"""


# There are only 2 positions you can directly go to from i, j. (i+1, j) and (i, j + 1).
# So if you knew the optimal path requirements for (i + 1, j) and (i, j + 1),
# you could choose the minimum of the two and be done with it.

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def calculateMinimumHP(self, A):
        M, N = len(A), len(A[0])
        INT_MAX = float('inf')
        hp = [[INT_MAX] * (N + 1) for _ in range(M + 1)]

        hp[M][N - 1] = 1
        hp[M - 1][N] = 1

        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                need = min(hp[i + 1][j], hp[i][j + 1]) - A[i][j]
                if need <= 0:
                    hp[i][j] = 1
                else:
                    hp[i][j] = need
        return hp[0][0]


#####		Kingdom War		#####

"""
Two kingdoms are on a war, kingdom X and kingdom Y. As a war specialist of kingdom X, you scouted kingdom Y area.
A kingdom area is defined as a N x M grid with each cell denoting a village.
Each cell has a value which denotes the strength of each corresponding village.
The strength can also be negative, representing those warriors of your kingdom who were held hostages.
There’s also another thing to be noticed.
The strength of any village on row larger than one (2<=r<=N) is stronger or equal
to the strength of village which is exactly above it.
The strength of any village on column larger than one (2<=c<=M) is stronger or equal to the
strength of vilage which is exactly to its left.
(stronger means having higher value as defined above).
So your task is, find the largest sum of strength that you can erase by bombing one sub-matrix in the grid.
Input format:
First line consists of 2 integers N and M denoting the number of rows and columns in the grid respectively.
The next N lines, consists of M integers each denoting the strength of each cell.
1 <= N <= 1500
1 <= M <= 1500
-200 <= Cell Strength <= 200
Output:
The largest sum of strength that you can get by choosing one sub-matrix.
Example:
Input:
3 3
-5 -4 -1
-3 2 4
2 5 8
Output:
19
Explanation:
Bomb the sub-matrix from (2,2) to (3,3): 2 + 4 + 5 + 8 = 19
"""


# Based on the observation in Hint 1, we can assume that the largest sub-array strength may start from any point,
# but will definitely end on bottom-right cell (N,M).
# Therefore, we can use dynamic programming to find the sum of sub-matrix starting
# from the bottom-right cell (N,M) going up and left.
# DP[i][j] = DP[i+1][j] + DP[i][j+1] - DP[i+1][j+1]
# Find the maximum answer from DP[i][j] for each (i,j)

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        m = len(A[0])
        if n < 1 or m < 1:
            return 0
        reversedprefix_arr = []
        for arr in A:
            prefix_arr_cur = [0] * m
            prefix_arr_cur[m - 1] = arr[m - 1]
            for j in range(m - 2, -1, -1):
                prefix_arr_cur[j] = prefix_arr_cur[j + 1] + arr[j]
            reversedprefix_arr.append(prefix_arr_cur)
        arr = [0] * m
        max_sum = A[-1][-1]
        for i in range(n - 1, -1, -1):
            arr = [x + y for x, y in zip(arr, reversedprefix_arr[i])]
            max_sum = max(max_sum, max(arr))
        return max_sum


#####		Interleaving Strings		#####

"""
Given A, B, C, find whether C is formed by the interleaving of A and B.
Input Format:*
The first argument of input contains a string, A.
The second argument of input contains a string, B.
The third argument of input contains a string, C.
Output Format:
Return an integer, 0 or 1:
    => 0 : False
    => 1 : True
Constraints:
1 <= length(A), length(B), length(C) <= 150
Examples:
Input 1:
    A = "aabcc"
    B = "dbbca"
    C = "aadbbcbcac"
Output 1:
    1
Explanation 1:
    "aa" (from A) + "dbbc" (from B) + "bc" (from A) + "a" (from B) + "c" (from A)
Input 2:
    A = "aabcc"
    B = "dbbca"
    C = "aadbbbaccc"
Output 2:
    0
Explanation 2:
    It is not possible to get C by interleaving A and B.
"""


# Given the string S1, S2, S3, the first character of S3 has to match with either the first character of S1 or S2.
# If it matches with first character of S1, we try to see if solution is possible with remaining part of S1,
# all of S2, and remaining part of S3. Then we do the same thing for S2.
# The pseudocode might look something like this :
#     bool isInterleave(int index1, int index2, int index3) {
#                     // HANDLE BASE CASES HERE
#
#         bool answer = false;
#         if (index1 < s1.length() && s1[index1] == s3[index3]) answer |= isInterleave(index1 + 1, index2, index3 + 1);
#         if (index2 < s2.length() && s2[index2] == s3[index3]) answer |= isInterleave(index1, index2 + 1, index3 + 1);
#
#         return answer;
#     }
# Again, index1, index2, and index3 can only take S1.length(), S2.length() and S3.length() possibilities respectively.
# Can you think of a memoization solution using the observation ?
# BONUS: Can you eliminate one of the state i.e. come up with something having only two arguments.

class Solution:
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def isInterleave(self, A, B, C):
        if len(A) + len(B) != len(C):
            return 0
        f = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        f[0][0] = 1
        for i in range(len(A) + 1):
            for j in range(len(B) + 1):
                if i > 0 and A[i - 1] == C[i + j - 1]:
                    f[i][j] = f[i][j] or f[i - 1][j]
                if j > 0 and B[j - 1] == C[i + j - 1]:
                    f[i][j] = f[i][j] or f[i][j - 1]
        return f[-1][-1]


#####		Longest Valid Parenthesis		#####

"""
Given a string A containing just the characters ’(‘ and ’)’.
Find the length of the longest valid (well-formed) parentheses substring.
Input Format:
The only argument given is string A.
Output Format:
Return the length of the longest valid (well-formed) parentheses substring.
Constraints:
1 <= length(A) <= 750000
For Example
Input 1:
    A = "(()"
Output 1:
    2
    Explanation 1:
        The longest valid parentheses substring is "()", which has length = 2.
Input 2:
    A = ")()())"
Output 2:
    4
    Explanation 2:
        The longest valid parentheses substring is "()()", which has length = 4.
"""


# Lets construct longest[i] where longest[i] denotes the longest set of parenthesis ending at index i.
#
# If s[i] is ‘(‘, set longest[i] to 0, because any string end with ‘(‘ cannot be a valid one.
# Else if s[i] is ‘)’
# If s[i-1] is ‘(‘, longest[i] = longest[i-2] + 2
# Else if s[i-1] is ‘)’ and s[i-longest[i-1]-1] == ‘(‘, longest[i] = longest[i-1] + 2 + longest[i-longest[i-1]-2]

class Solution:
    # @param A : string
    # @return an integer
    def longestValidParentheses(self, A):
        dpMap = dict()

        def dp(i):
            if i in dpMap:
                return dpMap[i]
            if i >= len(A) or A[i] == ')':
                return i - 1
            ans = i - 1
            if i + 1 < len(A):
                if A[i + 1] == ')':
                    ans = i + 1 + dp(i + 2) - (i + 2) + 1
                elif dp(i + 1) != i:
                    j = dp(i + 1) + 1
                    if j < len(A) and A[j] == ')':
                        ans = j + dp(j + 1) - (j + 1) + 1
            dpMap[i] = ans
            return ans

        return max(dp(i) - i + 1 for i in reversed(range(len(A))))


#####		Max Rectangle In Binary Matrix		#####

"""
Given a 2D binary matrix filled with 0’s and 1’s, find the largest rectangle containing all ones and return its area.
Bonus if you can solve it in O(n^2) or less.
Example :
A : [  1 1 1
       0 1 1
       1 0 0
    ]
Output : 4
As the max area rectangle is created by the 2x2 rectangle created by (0,1), (0,2), (1,1) and (1,2)
"""


# The bruteforce approach is to look at all pairs of (i,j) to (k,l) and check if its filled with 1s.
# This approach however is O(NNNNN^2) = O(N^6). [ N^4 ways to choose i,j,k,l and then N^2 elements in the square ].
# Can you optimize this approach if you had additional space to store results for your previous calculations ?
# Maybe if you knew the result for (i, j) to (k, l - 1) or (i, j) to (k - 1, l) or both ?
# We can improve from N^6 by storing in dp[i][j][k][l] if (i,j) to (k,l) is all filled with 1.
# dp[i][j[k][l] = 1 iff dp[i][j][k][l-1] = 1 && dp[i][j][k-1][l] = 1 and matrix[k][l] = 1.
# Now we can improve this further.
# What if with every (i,j) we stored the length of 1s in the same row i starting from (i,j).
# Can we move down in the column j from row i and determine the largest rectangle without having to visit all cells ?
# Lets max_x[i][j] denote the length of 1s in the same row i starting from (i,j).
# So our current max with one end of the rectangle at (i,j) would be max_x[i][j].
# As we move to the next row, there are 2 cases :
# 1) max_x[i+1][j] >= max_x[i][j] which means that we can take max_x[i][j] 1s from next column as well and extend
# our current rectangle as it is, with one more extra row.
# 11100000 - 111
# 11111100 - 111
# 2) max_x[i+1][j] < max_x[i][j] which means that if we want to extend our current rectangle to next row, we need
# to reduce the number of columns in it to max_x[i+1][j]
# 11100000 - 11
# 11000000 - 11
# As mentioned above, we keep increasing the columns and adjusting the width of the rectangle.
# O(N^3) time complexity.
# Even though N^3 is acceptable, it might be worth exploring a better solution.
# If you notice, laying out max_x[i][j] helps you make histograms in every row. Then the problem becomes of
# finding the maximum area in histograms ( which we have solved before in Stacks and Queues ) in O(n).
# This would lead to an O(N^2) solution. We strongly suggest you to explore the O(N^2) solution as well.

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, A):
        for r in range(1, len(A)):
            for c in range(len(A[0])):
                if A[r][c] == 1:
                    A[r][c] += A[r - 1][c]
        best_ans = 0
        for hist in A:
            ans = self.solve_hist(hist)
            best_ans = max(ans, best_ans)
        return best_ans

    def solve_hist(self, hist):
        hist.append(0)
        stack = [(-1, -1)]
        best_ans = 0
        for r_op, val in enumerate(hist):
            while stack[-1][0] > val:
                v, i = stack.pop()
                l_op = stack[-1][1]
                l_cl = l_op + 1
                ans = v * (r_op - l_cl)
                best_ans = max(ans, best_ans)
            stack.append((val, r_op))
        return best_ans


#####		Ways To Color 3n Board		#####

"""
Given a 3 x A board, find the number of ways to color it using at most 4 colors such that no
 2 adjacent boxes have same color.
Diagonal neighbors are not treated as adjacent boxes.
Return the ways modulo 109 + 7 as the answer grows quickly.
Input Format:
The first and the only argument contains an integer, A.
Output Format:
Return an integer representing the number of ways to color the board.
Constraints:
1 <= A < 100000
Examples:
Input 1:
    A = 1
Output 1:
    36
Input 2:
    A = 2
Output 2:
    588
"""

# Let us first color a given column with three colors such that no two adjacent boxes have the same color.
# A simple combinatorics reveal that there are 36 ways to do so.
# Let’s say colors are: {0,1,2,3}
# Triplets of color: {0,1,2} , {3,1,2}, {4,1,2}, …..
# Now, suppose that we color the given column with one of these triplets. We acan color the next column
# with the triplets of color that do not contradict our coloring scheme.
# E.g.:
#   0	1
#  	1	3
#  	2	0
# Here, we can color third column using triplets that go well with the triplet {1,3,0}. These are {0,1,2}, {2,1,3}, ……
# This can be coded using a simple dynamic programming approach.
# Recurrence:
# {i,j,k} = triplet of color used to paint nth column in the order given. (1st row: i, 2nd row: j, …. }
# solve(i,j,k,n) = no. of ways to color a 3xn board such that nth column is painted with color triplet {i,j,k}
# solve(i,j,k,n) =$\sum_{triplets(x,y,z)}$ ( solve(x,y,z, n-1) ) such that {i,j,k} and {x,y,z} go well with each other.


from itertools import product


def count(x, y, z):
    ''' number of ways to form 2 and 3-colored column '''
    ''' x, y, z = colors of previous column '''
    num2, num3 = 0, 0
    for a, b, c in product(range(4), repeat=3):
        if a != b and b != c and a != x and b != y and c != z:
            if a == c:
                num2 += 1
            else:
                num3 += 1
    return num2, num3


class Solution:
    def solve_another(self, A):
        # ways to fill first column
        c3 = 24  # when 3 colors (A,B,C,D) used: 4*3*2
        c2 = 12  # when 2 colours (A,B,C) used: 4*3
        # ways to fill 2nd column onwards
        for i in range(2, A + 1):
            temp = c3
            c3 = (11 * c3 + 10 * c2) % 1000000007  # calculated manually
            c2 = (5 * temp + 7 * c2) % 1000000007
        return (c3 + c2) % 1000000007

    # @param A : integer
    # @return an integer
    def solve(self, A):
        MODU = 1000000007
        if A == 0:
            return 1
        # First column
        n2, n3 = count(None, None, None)  # 12, 24
        # When previous column has 2 colors (resp. 3)
        n2_2, n2_3 = count(0, 1, 0)  # 7, 10
        n3_2, n3_3 = count(0, 1, 2)  # 5, 11
        # n2, n3: number of combinations ending with 2 colored column (resp. 3)
        for i in range(1, A):
            n2, n3 = (n2 * n2_2 + n3 * n3_2) % MODU, \
                     (n2 * n2_3 + n3 * n3_3) % MODU
        return (n2 + n3) % MODU


#####		Kth Manhattan Distance Neighbourhood		#####

"""
Given a matrix M of size nxm and an integer K, find the maximum element in the K
manhattan distance neighbourhood for all elements in nxm matrix.
In other words, for every element M[i][j] find the maximum element M[p][q] such that abs(i-p)+abs(j-q) <= K.
Note: Expected time complexity is O(N*N*K)
Constraints:
1 <= n <= 300
1 <= m <= 300
1 <= K <= 300
0 <= M[i][j] <= 1000
Example
Input:
M  = [[1,2,4],[4,5,8]] , K = 2
Output:
ans = [[5,8,8],[8,8,8]]
"""


# This problem can be solved easily using dynamic programming.
# DP recurrence:
# dp[k][i][j] = ans. for kth manhattan distance for element (i,j)
# dp[k+1][i][j] = max(dp[k][i-1][j], dp[k][i+1][j], dp[k][i][j-1], dp[k][i][j+1], dp[k][i][j] )
# Recurrence is easy to get once you draw the figure.

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, B, A):
        r, c = len(A), len(A[0])
        M = [[A[i][j] for j in range(c)] for i in range(r)]
        M_ = [[A[i][j] for j in range(c)] for i in range(r)]
        for k in range(B):
            for i in range(r):
                for j in range(c):
                    M_[i][j] = max(M[i][j], M[i - 1][j] if i > 0 else 0, M[i + 1][j] if i < r - 1 else 0,
                                   M[i][j - 1] if j > 0 else 0, M[i][j + 1] if j < c - 1 else 0)
            M_, M = M, M_
        return M


#####		Min Jumps Array		#####

"""
Given an array of non-negative integers, A, of length N, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Return the minimum number of jumps required to reach the last index.
If it is not possible to reach the last index, return -1.
Input Format:
The first and the only argument contains an integer array, A.
Output Format:
Return an integer, representing the answer as described in the problem statement.
Constraints:
1 <= N <= 1e6
0 <= A[i] <= 50000
Examples:
Input 1:
    A = [2, 1, 1]
Output 1:
    1
Explanation 1:
    The shortest way to reach index 2 is
        Index 0 -> Index 2
    that requires only 1 jump.
Input 2:
    A = [2,3,1,1,4]
Output 2:
    2
Explanation 2:
    The shortest way to reach index 4 is
        Index 0 -> Index 1 -> Index 4
    that requires 2 jumps.
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def jump(self, A):
        last = len(A) - 1
        jumps = 0
        reachable = 0  # reachable with current number of jumps
        next_reachable = 0  # reachable with one additionnal jump
        for i, x in enumerate(A):
            if reachable >= last:
                break
            if reachable < i:
                reachable = next_reachable
                jumps += 1
                if reachable < i:
                    return -1
            next_reachable = max(next_reachable, i + x)
        return jumps


#####		Coin Sum Infinite		#####

"""
You are given a set of coins S. In how many ways can you make sum N assuming you have infinite amount of each coin in the set.
Note : Coins in set S will be unique. Expected space complexity of this problem is O(N).
Example :
Input :
    S = [1, 2, 3]
    N = 4
Return : 4
Explanation : The 4 possible ways are
{1, 1, 1, 1}
{1, 1, 2}
{2, 2}
{1, 3}
Note that the answer can overflow. So, give us the answer % 1000007
"""


# Lets say we can make the sum N - S[i] in X ways. Then if we have a coin of value S[i] we can also make a
# sum of N in X ways. We can memoize the number of ways in which we can make all the sums < N. This can be done by
# keeping a count array for all sums less than N which gives us the expected space complexity of O(N). A sum of 0
# is always possible as we can pick no coins, so the base case will be count[0] = 1
# Remember to avoid counting a way more than once. This can be done by choosing the coins in a particular order.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def coinchange2(self, A, B):
        dp = [0] * (B + 1)
        dp[0] = 1
        for coin in A:
            for i in range(1, B + 1):
                if coin <= i:
                    dp[i] = dp[i] + dp[i - coin]
        return dp[-1] % 1000007


#####		Word Break 2		#####

"""
Given a string A and a dictionary of words B, add spaces in A to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.
Note : Make sure the strings are sorted in your result.
Input Format:
The first argument is a string, A.
The second argument is an array of strings, B.
Output Format:
Return a vector of strings representing the answer as described in the problem statement.
Constraints:
1 <= len(A) <= 50
1 <= len(B) <= 25
1 <= len(B[i]) <= 20
Examples:
Input 1:
    A = "b"
    B = ["aabbb"]
Output 1:
    []
Input 1:
    A = "catsanddog",
    B = ["cat", "cats", "and", "sand", "dog"]
Output 1:
    ["cat sand dog", "cats and dog"]
"""

# Lets again look at the bruteforce solution.
# You start exploring every substring from the start of the string, and check if its in the dictionary.
# If it is, then you check if it is possible to form rest of the string using the dictionary words.
# If yes, you append the current substring to all the substring possible from rest of the string.
# If none of the substrings qualify, then there are no sentences possible from this string. .
# So something like this :
# vector<string> wordBreak(int index, string &s, unordered_set<string> &dict) {
#     // BASE CASES
#
#     vector<string> sentences;
#     // try to construct all substrings.
#     for (int i = index; i < s.length(); i++) {
#         substring = *the substring s[index..i] with i inclusive*
#             if (dict contains substring) {
#                 vector<string> ret = wordBreak(i + 1, s, dict);
#                 foreach (sentence in ret) {
#                     sentences.push_back(substring + " " + sentence);
#                 }
#             }
#     }
#     return sentences;
# }
# This solution itself is exponential. However, do note that we are doing a lot of repetitive work.
# Do note, that index in the wordBreak function call can only take s.length() number of values [0, s.length].
# What if we stored the result of the function somehow and did not process it everytime the function is called ?

from collections import defaultdict


class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of strings
    def wordBreak(self, s, bag_words):
        suffix_words = [[] for i in range(len(s))]
        for i in reversed(range(len(s))):
            for j in range(i + 1, len(s)):
                if s[i:j] in bag_words and suffix_words[j]:
                    suffix_words[i].extend([[s[i:j]] + proper_sentence for proper_sentence in suffix_words[j]])
            if s[i:] in bag_words:
                suffix_words[i].append([s[i:]])

        return [' '.join(t) for t in suffix_words[0]]


#####		Length Of Longest Subsequence		#####

"""
Given an array of integers, A of length N, find length of longest subsequence which is first increasing then decreasing.
Input Format:
The first and the only argument contains an integer array, A.
Output Format:
Return an integer representing the answer as described in the problem statement.
Constraints:
1 <= N <= 3000
1 <= A[i] <= 1e7
Example:
Input 1:
    A = [1, 2, 1]
Output 1:
    3
Explanation 1:
    [1, 2, 1] is the longest subsequence.
Input 2:
    [1, 11, 2, 10, 4, 5, 2, 1]
Output 2:
    6
Explanation 2:
    [1 2 10 4 2 1] is the longest subsequence.
"""


# Construct array inc[i] where inc[i] stores Longest Increasing subsequence ending with A[i]. O(n^2) DP.
# Construct array dec[i] where dec[i] stores Longest Decreasing subsequence ending with A[i]. O(n^2) DP.
# Now we need to find the maximum value of (inc[i] + dec[i] - 1)

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        n = len(A)
        inc = [1] * n
        for i in range(1, n):
            for j in range(0, i):  # Just an inner loop to consider items less than i loop
                if A[i] > A[j] and inc[j] + 1 > inc[i]:
                    inc[i] = inc[j] + 1
        dec = [1] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if A[i] > A[j] and dec[j] + 1 > dec[i]:
                    dec[i] = dec[j] + 1
        maximum = 1
        for x, y in zip(inc, dec):  # Iterating two arrays together
            maximum = max(maximum, x + y)
        return maximum - 1


s = Solution()
print(s.longestSubsequenceLength([1, 11, 2, 10, 4, 5, 2, 1]))

#####		Distinct Subsequences		#####

"""
Given two sequences A, B, count number of unique ways in sequence A,
to form a subsequence that is identical to the sequence B.
Subsequence : A subsequence of a string is a new string which is formed from the original string by deleting
some (can be none) of the characters without disturbing the relative positions of the remaining characters.
(ie, “ACE” is a subsequence of “ABCDE” while “AEC” is not).
Input Format:
The first argument of input contains a string, A.
The second argument of input contains a string, B.
Output Format:
Return an integer representing the answer as described in the problem statement.
Constraints:
1 <= length(A), length(B) <= 700
Example :
Input 1:
    A = "abc"
    B = "abc"
Output 1:
    1
Explanation 1:
    Both the strings are equal.
Input 2:
    A = "rabbbit"
    B = "rabbit"
Output 2:
    3
Explanation 2:
    These are the possible removals of characters:
        => A = "ra_bbit"
        => A = "rab_bit"
        => A = "rabb_it"
    Note: "_" marks the removed character.
"""

# As a typical way to implement a dynamic programming algorithm, we construct a matrix dp,
# where each cell dp[i][j] represents the number of solutions of aligning substring T[0..i] with S[0..j];
# Rule 1). dp[0][j] = 1, since aligning T = “” with any substring of S would have only ONE solution
# which is to delete all characters in S.
# Rule 2). when i > 0, dp[i][j] can be derived by two cases:
# case 1). if T[i] != S[j], then the solution would be to ignore the character S[j] and
# align substring T[0..i] with S[0..(j-1)]. Therefore, dp[i][j] = dp[i][j-1].
# case 2). if T[i] == S[j], then first we could adopt the solution in case 1), but also we
# could match the characters T[i] and S[j] and align the rest of them (i.e. T[0..(i-1)] and S[0..(j-1)].
# As a result, dp[i][j] = dp[i][j-1] + d[i-1][j-1]
# e.g. T = B, S = ABC
# dp[1][2]=1: Align T’=B and S’=AB, only one solution, which is to remove character A in S’.


from functools import lru_cache


class Solution:
    # @param S : string
    # @param T : string
    # @return an integer
    def numDistinct(self, S, T):
        # dpMap = dict()

        @lru_cache(maxsize=None)
        def dp(i, j):
            # key = (i,j)
            # if key in dpMap:
            #     return dpMap[key]
            ans = 0
            if j == len(T) or i == len(S):
                ans = 1 if len(T) == j else 0
            else:
                ans = dp(i + 1, j)
                if S[i] == T[j]:
                    ans += dp(i + 1, j + 1)

            # dpMap[key] = ans
            return ans

        # Avoid recursion limit
        for i in reversed(range(len(S) + 1)):
            for j in reversed(range(min(i + 1, len(T) + 1))):
                dp(i, j)

        return dp(0, 0)

    def numDistinct_rec(self, A, B):
        d = {}

        def rec(p1, p2):
            if p2 > p1:  # What has to be made is greater than from what to make
                return 0
            elif p2 == -1:
                return 1
            if (p1, p2) not in d:
                if A[p1] == B[p2]:  # Try deleting one char from both A and B, deleting just one char from A
                    d[(p1, p2)] = rec(p1 - 1, p2 - 1) + rec(p1 - 1, p2)
                else:
                    d[(p1, p2)] = rec(p1 - 1, p2)  # Delete the last char from A
            return d[(p1, p2)]

        return rec(len(A) - 1, len(B) - 1)


s = Solution()
print(s.numDistinct())
print(s.numDistinct_rec())

#####		Shortest Common Superstring		#####

"""
Given a set of strings, A of length N.
Return the length of smallest string which has all the strings in the set as substring.
Input Format:
The first and the only argument has an array of strings, A.
Output Format:
Return an integer representing the minimum possible length of the resulting string.
Constraints:
1 <= N <= 18
1 <= A[i] <= 100
Example:
Input 1:
    A = ["aaaa", "aa"]
Output 1:
    4
Explanation 1:
    Shortest string: "aaaa"
Input 2:
    A = ["abcd", "cdef", "fgh", "de"]
Output 2:
    8
Explanation 2:
    Shortest string: "abcdefgh"
"""


# Brute force
# Let’s say we have only two strings say s1 and s2, the possible cases are:
#
# They do not overlap [ans = len(s1) + len(s2) ]
# They overlap partially [ans = len(s1)+len(s2)-len(max. overlapping part)]
# They overlap completely [ans = max(len(s1), len(s2)]
# What we can see here is we can easily combine two strings. In the brute force, we could take all the permutations
# of numbers [1 .. N], then combine the strings in that order.
# e.g: strings = [s1, s2, s3], order = [2,3,1]
# Steps are: [s1, s2,s3] –> [s2+s3, s1] –> [s1+s2+s3].
# (Here addition of strings is according to the method described above.
# I would advice you to completely digest that this will give the optimal solution whatever the case may be.
# Considering all the permutations is optimal but time consuming.
#
# Dynamic programming
# We have dynamic programming to our rescue in this case. You can see that there is a optimal substructure and
# overlapping subproblems in the brute force algorithm described above. Well if you can’t already see,
# let me help you out. Example:
# Input = [s1, s2, s3, s4]
# Order 1 = [2,3,1,4] , Steps: [s2+s3, s1, s4] –> [s2+s3+s1, s4] –> [s1+s2+s3+s4]
# Order 2 = [1,3,2,4] , Steps: [s1+s3, s2, s4] –> [s1+s2+s3, s4] –> [s1+s2+s3+s4].
#
# Do you see here that Order1 and Order2 both calculated the optimal solution for set of strings [s1, s2, s3]
# (Intermediate string s1+s2+s3 is the optimal solution for this set)
#
# Hurrah! Time to think Dynamically.
#
# Bitmasking in DP
# Well, this kind of DP formulations require a specific technique called Bitmasking. It is not the conventional type
# and in this case T(N) = CCNN + CN*(2^N) (Still better than O(N!) right).
#
# Formulation:
# dp[i][mask] = Optimal solution for set of strings corresponding to 1’s in the mask where the last added string to
# our solution is i-th string.
# Recurrence:
# dp[i][mask] = min(dp[x][mask ^ (1«i)] where {mask | (1«x) = 1} )
# I recommend you reading about the Bitmask in DP if you still have the doubt.

class Solution:

    def substring(self, a, b):
        if a.find(b) != -1:
            return b
        elif b.find(a) != -1:
            return a
        return None

    def overlap(self, a, b):
        l1 = self.overlap_length(a, b)
        l2 = self.overlap_length(b, a)
        if l1 > l2:
            return l1, a, b
        else:
            return l2, b, a

    def overlap_length(self, a, b):
        length = 0
        for i in range(len(a)):
            x = len(a) - i
            if a[x:] == b[:i]:
                length = i
        return length

    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        a = [i for i in A]

        while len(a) > 1:
            item_to_remove = None
            max_overlap = None
            for i in range(len(a)):
                for j in range(i + 1, len(a)):
                    item_to_remove = self.substring(a[i], a[j])
                    if item_to_remove is not None:
                        break

                    length, first, second = self.overlap(a[i], a[j])
                    if not max_overlap or max_overlap[0] < length:
                        max_overlap = length, first, second

                if item_to_remove is not None:
                    a.remove(item_to_remove)
                    break

            # print max_overlap
            if max_overlap is not None:
                length, first, second = max_overlap
                a.remove(first)
                a.remove(second)
                a.append(first + second[length:])

        return len(a[0])


#####		Tushar Bday Bombs		#####

"""
It’s Tushar’s birthday today and he has N friends.

Friends are numbered [0, 1, 2, …., N-1] and i-th friend have a positive strength B[i].

Today being his birthday, his friends have planned to give him birthday bombs (kicks :P).

Tushar’s friends know Tushar’s pain bearing limit and would hit accordingly.

If Tushar’s resistance is denoted by A (>=0) then find the lexicographically smallest order of friends to kick Tushar
so that the cumulative kick strength (sum of the strengths of friends who kicks) doesn’t exceed his
resistance capacity and total no. of kicks hit are maximum.
Also note that each friend can kick unlimited number of times (If a friend hits x times, his strength will be
counted x times)
Return the lexicographically smallest array of maximum length where the ith index
represents the index of the friend who will hit.
Note:
1. [a1, a2, ...., am] is lexicographically smaller than [b1, b2, .., bm]  if a1 < b1 or (a1 = b1 and a2 < b2) ... .
2. Input cases are such that the length of the answer does not exceed 100000.
Input Format:
The first argument contains an integer, A of length N.
The second argument contains an array of integers, B.
Output Format:
Return an array of integer, as described in the problem statement.
Constraints:
1 <= N <= 100
1 <= A <= 15000000
1 <= B[i] <= 3000
Examples:
Input 1:
    A = 12
    B = [3, 4]
Output 1:
    [0, 0, 0, 0]
Explanation 1:
    [1, 1, 1] is also a possible answer.
Input 2:
    A = 11
    B = [6, 8, 5, 4, 7]
Output 2:
    [0, 2]
Explanation 2:
    [2, 3], [2, 2] and [3, 3] are also possible answers.
"""


# Observations:
# Let the index of friend with minimum strength be F. (Take smallest index in case of a tie)
# It is obvious that –> Maximum no. of kicks = R/(S[F]).
# This is the length of the answer but since we need lexicographically smaller order (according to index),
# friends whose index is less than the F can also hit provided they do not change the length of the answer.
# There is also a crucial observation here, we need not consider the friend which have a friend to their left
# (lesser index) and have lesser than or equal strength than him. (Otherwise we can just take that
# friend with lesser index instead).
# Below is an example to clear the things out:
# R = 11, S = [6, 8, 5, 4, 7]
# In this case:
# Max no. of kicks = 11/4 = 2.
# answer = [3,3] (if we do not consider the lexicographic order)
# But answer may be [0,3] or [0,2] or [2,3] as they also have the same length.
# Here, only required friends to consider are newS = [6,5,4] as we will rather choose friend with strength 6
# than choosing a friend with strength 8, and rather choose any of [6,5,4] than choosing friend with strength 7.
# (Give it a thought, it’s true because our answer should be lexicographically smallest)
# Note that the friend with the minimum strength will be the last element of our newS vector
# (as newS will be in strict decreasing order)
# Algorithm:
# Find the max no. of kicks (length of our answer).
# Make a new S vector which only takes the friends that can be in the answer.
# Iterate through the S vector formed above and see if the friend at
# consideration can be used instead of the friend with minimum strength.
# If he can be successfully used then use him instead of the friend with
# minimum strength to get a lexicographically smaller answer.

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, r, S):
        val, idx = min((val, idx) for (idx, val) in enumerate(S))
        ret = [idx] * (r // val)
        diff = r % val

        i = 0
        for j in range(idx):
            if diff == 0 or i == len(ret):
                break
            elif 0 < S[j] - val <= diff:
                while 0 < S[j] - val <= diff:
                    if i == len(ret):
                        break
                    ret[i] = j
                    i += 1
                    diff -= (S[j] - val)
        return ret


#####		Equal Average Partition		#####

"""
Given an array with non negative numbers, divide the array into two parts such that the average of both the parts is equal.
Return both parts (If exist).
If there is no solution. return an empty list.
Example:
Input:
[1 7 15 29 11 9]
Output:
[9 15] [1 7 11 29]
The average of part is (15+9)/2 = 12,
average of second part elements is (1 + 7 + 11 + 29) / 4 = 12
 NOTE 1: If a solution exists, you should return a list of exactly 2 lists of integers A and B which
 follow the following condition :
numElements in A <= numElements in B
If numElements in A = numElements in B, then A is lexicographically smaller than B
( https://en.wikipedia.org/wiki/Lexicographical_order )
NOTE 2: If multiple solutions exist, return the solution where length(A) is minimum. If there is still a tie,
return the one where A is lexicographically smallest. NOTE 3: Array will contain only non negative numbers.
"""

# Lets try to simplify the problem.
# Lets assume the two sets are set1 and set2.
# Assume sum of set1 = Sum_of_Set1, with size = size_of_set1.
# Assume sum of set2 = Sum_of_Set2, with size = size_of_set2
#  SUM_of_Set1 / size_of_set1 = SUM_of_Set2 / size_of_set2
#  SUM_of_Set1 = SUM_of_Set2 * (size_of_set1 / size_of_set2)
#     total_sum = Sum_of_Set1 + Sum_of_Set2
#     AND size_of_set2 = total_size - size_of_set1
#   Sum_of_Set1 = (total_sum - Sum_of_Set1) * (size_of_set1 / (total_size - size_of_set1))
#   OR on simplifying,
#   total_sum / Sum_of_Set1 - 1 = (total_size - size_of_set1) / size_of_set1
#   total_sum / Sum_of_Set1 = total_size / size_of_set1
#   Sum_of_Set1 / size_of_set1 = total_sum / total_size
# Note that you need the solution with minimum size_of_set1 if multiple solutions exist.
# So, just iterate on size_of_set1.
# Based on size_of_set1, you can determine the value of Sum_of_Set1.
# Now, the problem reduces to
#
# Can I select size_of_set1 values from the array whose sum is Sum_of_Set1 ?
# In previous hint, we explored how we can break down the given problem into a much simpler problem
#
# Can I select current_size values from the array whose sum is current_sum ?
# Lets define our function as
# isPossible(ind, current_sum, current_size) which returns true if it is possible to use elements with index >= ind
# to construct a set of size current_size whose sum is current_sum.
# isPossible(ind, current_sum, current_size :
#                            |
#                            |
#                            |  isPossible(ind + 1, current_sum, current_size)  [ Do not include current element ]
#     Or(|) Logical operator |
#                            |
#                            |
#                            |
#                            |  isPossible(ind + 1, current_sum - value_at(ind), current_size - 1)
#                            |
# Can you memoize values to reduce the time complexity of the above recursive function ?

from functools import wraps
import fractions


def memo(f):
    cache = {}

    @wraps(f)
    def wrap(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return wrap


class Solution:
    # @param A : list of integers
    # @return a list of list of integers

    @memo
    def knapsack(self, i, num, tot):
        # Find num items in A that add up to tot
        if i > len(self.A) - 1 or num <= 0 or tot <= 0:
            return None
        elif num == 1 and self.A[i] == tot:
            return [self.A[i]]
        else:
            include = self.knapsack(i + 1, num - 1, tot - self.A[i])
            exclude = self.knapsack(i + 1, num, tot)

            if include:
                return [self.A[i]] + include
            elif exclude:
                return exclude

    def avgset(self, A):
        tot = sum(A)
        n = len(A)

        gcd = fractions.gcd(tot, n)

        num = n // gcd
        self.A = sorted(A)

        for i in range(num, n // 2 + 1, num):
            k = self.knapsack(0, i, tot * i // n)
            if k is not None:
                temp = k[:]
                return [k, [i for i in self.A if not i in temp or temp.remove(i)]]
        return []


#####		Max Product Subarray		#####

"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.
Return an integer corresponding to the maximum product possible.
Example :
Input : [2, 3, -2, 4]
Return : 6
Possible with [2, 3]
"""


# If there were no zeros or negative numbers, then the answer would definitely be the product of the whole array.
# Now lets assume there were no negative numbers and just positive numbers and 0. In that case we could maintain a
# current maximum product which would be reset to A[i] when 0s were encountered.
# When the negative numbers are introduced, the situation changes ever so slightly. We need to now maintain the
# maximum product in positive and maximum product in negative. On encountering a negative number, the maximum product
# in negative can quickly come into picture.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        assert len(A) > 0
        ans = A[0]
        ma, mi = 1, 1
        for a in A:
            ma, mi = max(a, a * ma, a * mi), min(a, a * ma, a * mi)
            ans = max(ans, ma, mi)
        return ans


#####		Min Sum Path In Matrix		#####

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
 Note: You can only move either down or right at any point in time.
Example :
Input :
    [  1 3 2
       4 3 1
       5 6 1
    ]
Output : 8
     1 -> 3 -> 2 -> 1 -> 1
"""


#  Let DP[i][j] store the minimum sum of numbers along the path from top left to (i,j).
# Basically, DP[i][j] = A[i][j] + min(DP[i-1][j],DP[i][j-1]).
# You only need to figure out the base conditions and boundary conditions now.

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        if (len(A) == 1):
            return sum(A[0])
        m = len(A)
        n = len(A[0])
        mat = [[0 for i in range(n)] for j in range(m)]
        mat[0][0] = A[0][0]
        for i in range(0, m):
            for j in range(0, n):
                if i > 0 and j > 0:
                    mat[i][j] = min(mat[i][j - 1], mat[i - 1][j]) + A[i][j]
                elif j == 0 and i > 0:
                    mat[i][j] = mat[i - 1][j] + A[i][j]
                elif i == 0 and j > 0:
                    mat[i][j] = mat[i][j - 1] + A[i][j]
        return mat[m - 1][n - 1]


#####		Count Permutations Of Bst		#####

"""
You are given two positive integers A and B. For all permutations of [1, 2, …, A], we create a BST.
Count how many of these have height B.
Notes:
Values of a permutation are sequentially inserted into the BST by general rules i.e in increasing order of indices.
Height of BST is maximum number of edges between root and a leaf.
Return answer modulo 109 + 7.
Expected time complexity is worst case O(N4).
1 ≤ N ≤ 50
For example,
A = 3, B = 1
Two permutations [2, 1, 3] and [2, 3, 1] generate a BST of height 1.
In both cases the BST formed is
    2
   / \
  1   3
Another example,
A = 3, B = 2
Return 4.
Next question, can you do the problem in O(N3)?
"""

# BST follows the property that all values in left subtree and less than value at current node and all values
# in right subtree are greater than current node.
# If we fix the root node, the BST formed will be unique.
# Also, the actual values that are being inserted in BST don’t matter. So, we can directly deal with number of values
# being inserted in BST instead of the actual values. This helps in defining states of DP.
# Now, what should be the states of DP? Of course, number of elements is one state. Other can be the height required.
# So, we define DP(N, M) as the number of permutations of N elements which when inserted into BSTs generate
# BSTs of height exactly M. Now, to define a recurrence, we’ll iterate over the root of BST we choose.
# We have N options and based on each option, the size of left and right subtrees are defined.
# If i’th element is choosen as root, the left subtree will now contain (i - 1)
# elements and right subtree will contain (N - i) elements.
# Now, at least one of these subtrees must have a height of (M - 1) because we are right now solving for height M.
# Again, we’ll iterate over the heights of left and right subtrees.
# Now, number of permutations to form left subtree of size x with some height are say, X.
# Also, we call these permutations set A.
# And similarly, number of permutations to form right subtree of size y with some height are say, Y.
# And we call these permutations set B.
# Now, we can choose any permutation from A and any permutation from B, to form a unique tree.
# So, there are total of X*Y permutations. Also, any sequence of size (x+y) can give the same BST if
# the mutual ordering of the permutation from set A and permutation of set B is maintained.
# There are choose(x + y, y) ways to do that. So, total ways are X*Y*choose(x + y, y).
# So, in terms of pseudo code:
# def rec(N, M):
#     if N<=1:
#         if M==0: return 1
#         return 0;
#     ret=0
#     for i=1 to N:
#         x = i-1
#         y = N-i
#         ret1=0
#         //iterate over height of left subtree
#         for j = 0 to M-2:
#             ret1 = ret1 + rec(x, j)*rec(y, M-1)
#         //iterate over height of right subtree
#         for j = 0 to M-2:
#             ret1 = ret1 + rec(y, j)*rec(x, M-1)
#         //add the case when both heights=M-1
#         ret1 = ret1 + rec(x, M-1)*rec(y, M-1)
#         ret = ret + ret1*choose(x+y, y)
#     return ret
# We can precalculate choose table in O(N*N).
# Also, take care of modulo arithmetic.

import math
from functools import wraps


def memo(f):
    cache = {}

    @wraps(f)
    def wrap(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return wrap


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def nCr(self, n, r):
        f = math.factorial
        return f(n) // (f(r) * f(n - r))

    def cntPermBST(self, n, height):
        return self.recurse(n, height)[0] % (10 ** 9 + 7)

    @memo
    def recurse(self, n, height):
        """
            Tuple: (# correct height, # less than correct height)
        """
        if n == 1 and height == 0:
            return [1, 0]
        elif n == 0 and height >= 0:
            return [0, 1]
        elif n == 0 or height == 0:
            return [0, 0]
        else:
            count = [0, 0]
            for i in range(1, n + 1):
                left = self.recurse(i - 1, height - 1)
                right = self.recurse(n - i, height - 1)
                num = left[0] * right[1] + right[0] * left[1] + left[0] * right[0]
                count[0] += self.nCr(n - 1, n - i) * num
                count[1] += self.nCr(n - 1, n - i) * left[1] * right[1]
            return count


#########################	graphs	#########################


#####		Smallest Multiple With Zero And One		#####

"""
You are given an integer N. You have to find smallest multiple of N which consists of digits 0 and 1 only.
Since this multiple could be large, return it in form of a string.

Note:
Returned string should not contain leading zeroes.
For example,
For N = 55, 110 is smallest multiple consisting of digits 0 and 1.
For N = 2, 10 is the answer.
"""


class Solution:
    def multiple(self, A):
        flag = False
        i = 1
        while flag != True:
            result = A * i
            # method returns smallest  multiple which has binary digits
            allowed_chars = set('01')
            validationString = str(result)
            if set(validationString).issubset(allowed_chars):
                flag = True;
                break;
            else:
                i = i + 1
        return validationString


#####		Capture Regions On Board		#####

"""
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Input Format:
First and only argument is a N x M character matrix A
Output Format:
make changes to the the input only as matrix is passed by reference.
Constraints:

    1 <= N,M <= 1000
For Example:

Input 1:
    A = [ [X, X, X, X],
          [X, O, O, X],
          [X, X, O, X],
          [X, O, X, X] ]
Output 1:
    After running your function, the board should be:
    A = [ [X, X, X, X],
          [X, X, X, X],
          [X, X, X, X],
          [X, O, X, X] ]
Explanation:
O in (4,2) is not surrounded by X from below.
"""


class Solution:
    def solve(self, A):

        M = len(A)
        N = len(A[0])

        def inbounds(i, j):
            if i >= 0 and i < M and j >= 0 and j < N:
                return True
            return False

        def mark(i, j):

            todo = [(i, j)]
            while todo:
                i, j = todo.pop()
                if inbounds(i, j) and A[i][j] == 'O' and marked[i][j] == 0:
                    marked[i][j] = 1
                    todo.append((i + 1, j))
                    todo.append((i - 1, j))
                    todo.append((i, j + 1))
                    todo.append((i, j - 1))

        marked = [[0 for _ in range(N)] for _ in range(M)]
        # We already know chunks of O which remain as O are the ones
        # which have at least one O connected to them which is on the boundary.
        # Use BFS starting from ‘O’s on the boundary and mark them as ‘B’ (or 1),
        # then iterate over the whole board and mark ‘O’ as ‘X’ and ‘B’ (or 1) as ‘O’.
        for i in range(M):
            mark(i, 0)
            mark(i, N - 1)
        for j in range(N):
            mark(0, j)
            mark(M - 1, j)

        for i in range(1, M - 1):
            for j in range(1, N - 1):
                if A[i][j] == 'O' and marked[i][j] == 0:
                    A[i][j] = 'X'
        return A


A = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X']
]

A = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'O', 'X', 'X']
]

A = [
    ['X', 'X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X', 'X'],
    ['X', 'X', 'O', 'X', 'X'],
    ['X', 'O', 'X', 'X', 'X'],
    ['X', 'O', 'X', 'X', 'X']
]
s = Solution()
print(s.solve(A))

#####		Valid Path		#####

"""
There is a rectangle with left bottom as  (0, 0) and right up as (x, y).
There are N circles such that their centers are inside the rectangle.
Radius of each circle is R. Now we need to find out if it is possible
that we can move from (0, 0) to (x, y) without touching any circle.

Note : We can move from any cell to any of its 8 adjecent neighbours and we cannot move
outside the boundary of the rectangle at any point of time.

Input Format

1st argument given is an Integer x.
2nd argument given is an Integer y.
3rd argument given is an Integer N, number of circles.
4th argument given is an Integer R, radius of each circle.
5th argument given is an Array A of size N, where A[i] = x cordinate of ith circle
6th argument given is an Array B of size N, where B[i] = y cordinate of ith circle
Output Format

Return YES or NO depending on weather it is possible to reach cell (x,y) or not starting from (0,0).
Constraints

0 <= x, y, R <= 100
1 <= N <= 1000
Center of each circle would lie within the grid
For Example

Input:
    x = 2
    y = 3
    N = 1
    R = 1
    A = [2]
    B = [3]
Output:
    NO
Explanation:
    There is NO valid path in this case
"""


class Solution:

    def notInCircle(self, r, E, F, y, x):
        # E, F will have the x, y coordinates of all the circles
        for z in range(len(E)):
            if ((E[z] - x) ** 2 + (F[z] - y) ** 2) ** 0.5 <= r:
                return False
        return True

    def solve(self, A, B, C, D, E, F):
        stack = []
        graph = [[False] * (A + 1) for _ in range(B + 1)]
        stack.append([0, 0])
        while stack:
            curr = stack.pop()
            if curr[0] + 1 <= B and not graph[curr[0] + 1][curr[1]] \
                    and self.notInCircle(D, E, F, curr[0] + 1, curr[1]):
                stack.append([curr[0] + 1, curr[1]])
                graph[curr[0] + 1][curr[1]] = True
            if curr[0] - 1 >= 0 and not graph[curr[0] - 1][curr[1]] \
                    and self.notInCircle(D, E, F, curr[0] - 1, curr[1]):
                stack.append([curr[0] - 1, curr[1]])
                graph[curr[0] - 1][curr[1]] = True
            if curr[1] + 1 <= A and not graph[curr[0]][curr[1] + 1] \
                    and self.notInCircle(D, E, F, curr[0], curr[1] + 1):
                stack.append([curr[0], curr[1] + 1])
                graph[curr[0]][curr[1] + 1] = True
            if curr[1] - 1 >= 0 and not graph[curr[0]][curr[1] - 1] \
                    and self.notInCircle(D, E, F, curr[0], curr[1] - 1):
                stack.append([curr[0], curr[1] - 1])
                graph[curr[0]][curr[1] - 1] = True
        if graph[B][A]:
            return 'YES'
        else:
            return 'NO'


s = Solution()
print(s.solve(2, 3, 1, 1, [3], [3]))

#####		Knight On Chess Board		#####

"""
Given any source point, (C, D) and destination point, (E, F) on a chess board, we need to find whether Knight
can move to the destination or not. Knight's movements on a chess board
The above figure details the movements for a knight ( 8 possibilities ).
If yes, then what would be the minimum number of steps for the knight to move to the said point.
If knight can not move from the source point to the destination point, then return -1.
Note: A knight cannot go out of the board.
Input Format:

The first argument of input contains an integer A.
The second argument of input contains an integer B.
    => The chessboard is of size A x B.
The third argument of input contains an integer C.
The fourth argument of input contains an integer D.
    => The Knight is initially at position (C, D).
The fifth argument of input contains an integer E.
The sixth argument of input contains an integer F.
    => The Knight wants to reach position (E, F).
Output Format:

If it is possible to reach the destination point, return the minimum number of moves.
Else return -1.
Constraints:

1 <= A, B <= 500
Example

Input 1:
    A = 8
    B = 8
    C = 1
    D = 1
    E = 8
    F = 8

Output 1:
    6

Explanation 1:
    The size of the chessboard is 8x8, the knight is initially at (1, 1) and the knight wants to reach position (8, 8).
    The minimum number of moves required for this is 6.
"""
from collections import deque


class Solution:
    def knight(self, A, B, C, D, E, F):

        i, j = C - 1, D - 1
        queue = deque([((i, j), 0)])

        final = set()
        final.add((i, j))
        while queue:
            pre = queue.pop()
            i, j = pre[0][0], pre[0][1]
            dist = pre[1]
            if (i, j) == (E - 1, F - 1):
                return dist

            xarr = [-1, -2, -2, -1, 1, 2, 2, 1]
            yarr = [-2, -1, 1, 2, 2, 1, -1, -2]

            for k in range(8):
                x, y = i + xarr[k], j + yarr[k]
                if 0 <= x < A and 0 <= y < B:  # Check bounds
                    if (x, y) not in final:
                        final.add((x, y))
                        queue.appendleft(((x, y), dist + 1))
        return -1


s = Solution()
print(s.knight(8, 8, 1, 1, 8, 8))

#####		Word Ladder 1		#####

"""
Given two words A and B, and a dictionary, C, find the length of shortest transformation sequence from A to B, such that:

You must change exactly one character in every transformation.
Each intermediate word must exist in the dictionary.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.


Input Format:

The first argument of input contains a string, A.
The second argument of input contains a string, B.
The third argument of input contains an array of strings, C.
Output Format:

Return an integer representing the minimum number of steps required to change string A to string B.
Constraints:

1 <= length(A), length(B), length(C[i]) <= 25
1 <= length(C) <= 5e3
Example :

Input 1:
    A = "hit"
    B = "cog"
    C = ["hot", "dot", "dog", "lot", "log", "cog"]

Output 1:
    5

Explanation 1:
    "hit" -> "hot" -> "dot" -> "dog" -> "cog"
"""


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not wordList:
            return 0

        n = len(wordList)
        begin_flag = False
        List = set()
        for word in wordList:
            List.add(word)

        if endWord not in List:
            return 0
        if beginWord in List:
            begin_flag = True

        graph = {}

        if not begin_flag:
            graph[beginWord] = []

            for i in range(n):
                if self.dist_one(beginWord, wordList[i]):
                    graph[beginWord].append(wordList[i])
                    graph[wordList[i]] = [beginWord]

        for i in range(n):
            if wordList[i] not in graph:
                graph[wordList[i]] = []
            word = wordList[i]
            for j in range(len(word)):
                for num in range(ord('a'), ord('z') + 1):
                    s = word[:j] + chr(num) + word[j + 1:]
                    if s in List:
                        graph[word].append(s)

        res = self.bfs(graph, beginWord, endWord) + 1

        return res

    def dist_one(self, string1, string2):
        count = 0
        n = len(string1)
        for i in range(n):
            if string1[i] != string2[i]:
                count += 1
            if count > 1:
                return False
        return True

    def bfs(self, graph, beginword, endword):
        visited = set()
        queue = []
        queue.append([beginword, 0])
        visited.add(beginword)

        while queue:
            [string, count] = queue.pop(0)
            if string == endword:
                found = True
                return count
            for item in graph[string]:
                if item not in visited:
                    queue.append([item, count + 1])
                    visited.add(item)
        return -1


A = "hit"
B = "cog"
C = ["hot", "dot", "dog", "lot", "log", "cog"]

s = Solution()
print(s.ladderLength(A, B, C))

#####		Commutable Islands		#####

"""
Commutable Islands
Asked in: Amazon
Problem Setter: amitkgupta94 Problem Tester: archit.rai
There are A islands and there are M bridges connecting them. Each bridge has some cost attached to it.

We need to find bridges with minimal cost such that all islands are connected.

It is guaranteed that input data will contain at least one possible scenario in which all islands are connected with each other.

Input Format:

The first argument contains an integer, A, representing the number of islands.
The second argument contains an 2-d integer matrix, B, of size M x 3:
    => Island B[i][0] and B[i][1] are connected using a bridge of cost B[i][2].
Output Format:

Return an integer representing the minimal cost required.
Constraints:

1 <= A, M <= 6e4
1 <= B[i][0], B[i][1] <= A
1 <= B[i][2] <= 1e3
Examples:

Input 1:
    A = 4
    B = [   [1, 2, 1]
            [2, 3, 4]
            [1, 4, 3]
            [4, 3, 2]
            [1, 3, 10]  ]

Output 1:
    6

Explanation 1:
    We can choose bridges (1, 2, 1), (1, 4, 3) and (4, 3, 2), where the total cost incurred will be (1 + 3 + 2) = 6.

Input 2:
    A = 4
    B = [   [1, 2, 1]
            [2, 3, 2]
            [3, 4, 4]
            [1, 4, 3]   ]

Output 2:
    6

Explanation 2:
    We can choose bridges (1, 2, 1), (2, 3, 2) and (1, 4, 3), where the total cost incurred will be (1 + 2 + 3) = 6.
"""

# class Solution:
#     # @param A : integer
#     # @param B : list of list of integers
#     # @return an integer
#     def solve(self, A, B):
#         from heapq import heappush, heappop
#         heap = []
#         dist = dict()
#         for path in B:
#             dist[(path[0], path[1])] = path[2]
#         mst = set(1)
#         distance = [float("inf")] * A
#         distance[0] = 0
#         while len(mst) < A:
#             max =


from heapq import heappush, heappop


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        adj_list = self.create_adj_list(A, B)
        # print(adj_list)
        start_node = 1  # Start from any node
        return self.total_cost_using_prim(adj_list, start_node)

    def create_adj_list(self, nodes_num, bridges):
        adj_list = [[] for _ in range(nodes_num + 1)]

        for source, dest, cost in bridges:
            adj_list[source] += [(dest, cost)]
            adj_list[dest] += [(source, cost)]

        return adj_list

    def total_cost_using_prim(self, adj_list, start_node):
        visited = set()
        pq = [(0, start_node)]
        total_cost = 0

        while len(pq) > 0:
            cost, cur_node = heappop(pq)

            if cur_node in visited:
                continue

            total_cost += cost

            for neighbor, neighbor_cost in adj_list[cur_node]:
                heappush(pq, (neighbor_cost, neighbor))

            visited.add(cur_node)

        return total_cost


A = 4
B = [[1, 2, 1],
     [2, 3, 4],
     [1, 4, 3],
     [4, 3, 2],
     [1, 3, 10]]
s = Solution()
print(s.solve(A, B))

#####		Stepping Numbers		#####

"""
Given N and M find all stepping numbers in range N to M

The stepping number:
A number is called as a stepping number if the adjacent digits have a difference of 1.
e.g 123 is stepping number, but 358 is not a stepping number

Example:
N = 10, M = 20
all stepping numbers are 10 , 12
Return the numbers in sorted order.
"""

import heapq


class Solution:
    def stepnum(self, A, B):

        ans = []
        # Starts with these numbers and adds one/two numbers for each
        # by either adding one more or reducing once from the end
        final = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        heapq.heapify(final)
        group = set()  # To store which group of number have been processed
        for i in range(11):
            group.add(i)
        while 1:
            val = heapq.heappop(final)
            if val > B:
                break
            if val >= A:
                ans.append(val)

            if str(val)[-1] == '0':
                if val * 10 + 1 not in group:
                    heapq.heappush(final, val * 10 + 1)
                    group.add(val * 10 + 1)
            elif str(val)[-1] == '9':
                if val * 10 - 1 not in group:
                    heapq.heappush(final, val * 10 - 1 + int(str(val)[-1]))
                    group.add(val * 10 - 1)
            else:
                if val * 10 + 1 not in group:
                    heapq.heappush(final, val * 10 + 1 + int(str(val)[-1]))
                    group.add(val * 10 + 1)
                if val * 10 - 1 not in group:
                    heapq.heappush(final, val * 10 - 1 + int(str(val)[-1]))
                    group.add(val * 10 - 1)
        return ans


s = Solution()
# print(s.stepnum(200, 300))
print(s.stepnum(10, 30))

#####		Sum_of_fib_numbers		#####

"""
How many minimum numbers from fibonacci series are required such that sum of numbers should be equal to a given Number N?
Note : repetition of number is allowed.

Example:

N = 4
Fibonacci numbers : 1 1 2 3 5 .... so on
here 2 + 2 = 4
so minimum numbers will be 2
"""


class Solution:
    # @param A : integer
    # @return an integer
    def fibsum(self, A):
        from itertools import combinations
        if A == 0:
            return 0
        fact_list = [1, 1]
        last = fact_list[-1] + fact_list[-2]
        while last <= A:
            fact_list.append(last)
            last = fact_list[-1] + fact_list[-2]
        for i in range(len(fact_list[::-1])):  # Reversing the list to try bigger number first
            if len([comb for comb in combinations(fact_list, i + 1) if sum(comb) == A]) > 0:
                return i + 1

    def fibsum_editorial(self, A):
        # Uses Greedy Approach
        """
        Zeckendorf's theorem states that every positive integer can be represented uniquely as the sum
        of one or more distinct Fibonacci numbers in such a way that the sum does not include any two
        consecutive Fibonacci numbers.
        """
        F = [1, 1]
        while F[-1] < A:
            F.append(F[-1] + F[-2])
        rem = A
        count = 0
        while rem > 0:
            if F[-1] > rem:
                F.pop()
            else:
                rem -= F[-1]
                count += 1
        return count


s = Solution()
print(s.fibsum(7))

#####		__init__		#####


#####		Level Order		#####

"""
Given a binary tree, return the level order traversal of its nodes’ values. (ie, from left to right, level by level).

Example :
Given binary tree

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
Also think about a version of the question where you are asked to do a level order traversal 
of the tree when the depth of the tree is much greater than number of nodes on a level.
"""""


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return "val: {}, left: ({}), right: ({})".format(self.val, self.left, self.right)


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        from collections import deque
        q = deque()
        result = []
        level = []
        if A:
            q.append(A)
            q.append(None)  # Marker signifying end of a level
        else:
            return []
        while len(q) > 0:
            item = q.popleft()
            if item:
                level.append(item.val)  # Creating a list of items in this level
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
            else:
                result.append(level)
                # Add None marker, only when there are items left to process, otherwise it will be infinite loop
                if len(q) > 0:
                    level = []
                    q.append(None)
        return result


root = TreeNode(3)
l = TreeNode(9)
r = TreeNode(20)
rl = TreeNode(15)
rr = TreeNode(7)
r.left = rl
r.right = rr
root.right = r
root.left = l
print(root)
s = Solution()
print(s.levelOrder(root))

#####		Courses Prerequisites		#####

"""
There are a total of A courses you have to take, labeled from 1 to A.
Some courses may have prerequisites, for example to take course 2 you have to first take course 1,
which is expressed as a pair: [1,2].
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
Return 1 if it is possible to finish all the courses, or 0 if it is not possible to finish all the courses.

Input Format:
The first argument of input contains an integer A, representing the number of courses.
The second argument of input contains an integer array, B.
The third argument of input contains an integer array, C.
Output Format:
Return a boolean value:
    1 : If it is possible to complete all the courses.
    0 : If it is not possible to complete all the courses.
Constraints:

1 <= A <= 6e4
1 <= length(B) = length(C) <= 1e5
1 <= B[i], C[i] <= A
Example:

Input 1:
    A = 3
    B = [1, 2]
    C = [2, 3]

Output 1:
    1

Explanation 1:
    It is possible to complete the courses in the following order:
        1 -> 2 -> 3

Input 2:
    A = 2
    B = [1, 2]
    C = [2, 1]

Output 2:
    0

Explanation 2:
    It is not possible to complete all the courses.
"""

# Assume the non-visited node are colored black, the nodes currently present in the recursion stack are colored blue and
# the nodes already visited and out of the recursion stack are colored grey. The edge that connects current
# vertex in DFS to the vertex in the recursion stack(blue coloured node) is back edge.


from collections import defaultdict
from queue import LifoQueue


class Solution:
    def solve(self, A, B, C):
        G = defaultdict(list)
        # Convert to a graph format
        for a, b in zip(B, C):
            G[a].append(b)
        # C = {}  # Checked nodes. Useful for processing disconnected graphs.
        C = set()
        # K = 1
        for i in range(1, A + 1):
            if i not in C:  # If the graph is not connected, we need to make sure all nodes are visited
                visited = defaultdict(bool)
                S = LifoQueue()  # Stack for DFS
                S.put(i)
                visited[i] = True
                while not S.empty():
                    n = S.get()
                    for neighbour in G[n]:  # Visit all neighbours
                        if visited[neighbour]:
                            return 0
                        else:
                            visited[neighbour] = True
                            S.put(neighbour)
                    C.add(n)
                    # C[n] = K  # Checked
                    # K += 1
        return 1


A = 3
B = [1, 2]
C = [2, 3]
s = Solution()
print(s.solve(A, B, C))

#####		Word Search Board		#####

"""
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are
those horizontally or vertically neighboring. The cell itself does not count as an adjacent cell.
The same letter cell may be used more than once.

Example :
Given board =
[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns 1,
word = "SEE", -> returns 1,
word = "ABCB", -> returns 1,
word = "ABFSAB" -> returns 1
word = "ABCD" -> returns 0
Note that 1 corresponds to true, and 0 corresponds to false.
"""


class Solution:
    def exist(self, A, B):
        if not A:
            return 0 if B else 1

        m, n, s = len(A), len(A[0]), len(B)

        def helper(i, j, k=0, memo={}):
            # return whether B[k:] fit from (i, j) starting point
            if k == s:
                return True
            if (i, j, k) in memo:
                return memo[(i, j, k)]

            if 0 <= i < m and 0 <= j < n and B[k] == A[i][j]:
                res = helper(i - 1, j, k + 1) or \
                      helper(i + 1, j, k + 1) or \
                      helper(i, j - 1, k + 1) or \
                      helper(i, j + 1, k + 1)
            else:
                res = False

            memo[(i, j, k)] = res
            return res

        for i in range(m):
            for j in range(n):
                if helper(i, j):
                    return 1

        return 0


A = [
    ["ABCE"],
    ["SFCS"],
    ["ADEE"]
]
s = Solution()
print(s.exist(A, "ABCCED"))
print(s.exist(A, "SEE"))
print(s.exist(A, "ABCB"))
print(s.exist(A, "ABFSAB"))
print(s.exist(A, "ABCD"))

#####		Sorted Ll To Bst		#####

"""
Given a singly linked list where elements
are sorted in ascending order, convert it to a height balanced BST.
A height balanced BST : a height-balanced binary tree is defined as a binary tree in which
the depth of the two subtrees of every node never differ by more than 1.
Example :
Given A : 1 -> 2 -> 3
A height balanced BST  :

      2
    /   \
   1     3

"""
import os

os.path.abspath(__file__ + "/../../")
from DataStructure.treeNode import Node as TreeNode


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the root node in the tree
    def sortedListToBST(self, A):
        if not A:
            return
        if not A.next:
            return TreeNode(A.val)

        slow, fast = A, A.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        tmp = slow.next
        slow.next = None

        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(A)
        root.right = self.sortedListToBST(tmp.next)

        return root


_ = ListNode(7)
__ = ListNode(6)
__.next = _
_ = ListNode(5)
_.next = __
__ = ListNode(4)
__.next = _
_ = ListNode(3)
_.next = __
__ = ListNode(2)
__.next = _
A = ListNode(1)
A.next = __
s = Solution()
s.sortedListToBST(A).display()

#####		Largest Distance Bw Tree Nodes		#####

"""
Find largest distance
Given an arbitrary unweighted rooted tree which consists of N (2 <= N <= 40000) nodes. The goal
of the problem is to find largest distance between two nodes in a tree. Distance between two nodes
is a number of edges on a path between the nodes (there will be a unique path between any pair of
nodes since it is a tree). The nodes will be numbered 0 through N - 1.

The tree is given as an array P, there is an edge between nodes P[i] and i (0 <= i < N).
Exactly one of the i’s will have P[i] equal to -1, it will be root node.

 Example:
If given P is [-1, 0, 0, 0, 3], then node 0 is the root and the whole tree looks like this:
          0
       /  |  \
      1   2   3
               \
                4
 One of the longest path is 1 -> 0 -> 3 -> 4 and its length is 3, thus the answer is 3. Note that there are other
 paths with maximal distance.
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        pass


s = Solution()
s.solve([-1, 0, 0, 0, 3])

#####		Smallest Seq With Primes		#####

"""
Given three prime number(p1, p2, p3) and an integer k. Find the first(smallest) k integers which
have only p1, p2, p3 or a combination of them as their prime factors.

Example:

Input :
Prime numbers : [2,3,5]
k : 5

If primes are given as p1=2, p2=3 and p3=5 and k is given as 5, then the sequence of first 5 integers will be:

Output:
{2,3,4,5,6}

Explanation :
4 = p1 * p1 ( 2 * 2 )
6 = p1 * p2 ( 2 * 3 )

Note: The sequence should be sorted in ascending order
"""


class Solution:
    def solve(self, A, B, C, D):
        """
        Failed to give the right answer. It doesn't know how many combinations to use to get to the answer.
        If there is a very small prime number, it is better to reuse it repeatedly instead of choosing other primes.
        """
        seq = set()
        i = 1
        from itertools import combinations_with_replacement
        from functools import reduce
        import operator
        reduce(operator.mul, (3, 4, 5), 1)
        while i < 9:  # len(seq) < D and
            seq.update([reduce(operator.mul, comb, 1) for comb in combinations_with_replacement([A, B, C], i)])
            i += 1
        return sorted(list(seq))[: D]

    def solve_editorial(self, A, B, C, D):
        prime1 = A
        prime2 = B
        prime3 = C
        count = 0
        ans = []
        i, j, k = 0, 0, 0
        while count != D:
            temp = min(prime1, prime2, prime3)
            ans.append(temp)
            count += 1
            if temp == prime1:
                prime1 = A * ans[i]
                i += 1
            if temp == prime2:
                prime2 = B * ans[j]
                j += 1
            if temp == prime3:
                prime3 = C * ans[k]
                k += 1
        return ans


s = Solution()
# print(s.solve(2, 3, 4, 5))
# print(s.solve(2, 5, 11, 3))
# print(s.solve(3, 11, 7, 50))
print(s.solve_editorial(3, 11, 7, 50))

#####		Black Shapes		#####

"""
Given N x M character matrix A of O's and X's, where O = white, X = black.
Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)
Input Format:
The First and only argument is a N x M character matrix.
Output Format:
Return a single integer denoting number of black shapes.
Constraints:
1 <= N,M <= 1000
A[i][j] = 'X' or 'O'
Example:
Input 1:
    A = [ OOOXOOO
          OOXXOXO
          OXOOOXO  ]
Output 1:
    3
Explanation:
    3 shapes are  :
    (i)    X
         X X
    (ii)
          X
    (iii)
          X
          X
Note: we are looking for connected shapes here.
XXX
XXX
XXX
is just one single connected black shape.
"""


class Solution:
    def black(self, A):
        def dfs(A, i, j, final):
            xarr = [-1, 0, 1, 0]
            yarr = [0, 1, 0, -1]
            for k in range(4):
                x = i + xarr[k]
                y = j + yarr[k]
                if (x, y) not in final:
                    if 0 <= x < len(A) and 0 <= y < len(A[0]) and A[x][y] == 'X':
                        final.add((x, y))
                        dfs(A, x, y, final)

        ans = 0
        final = set()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 'X' and (i, j) not in final:
                    final.add((i, j))
                    dfs(A, i, j, final)
                    ans += 1
        return ans


A = [
    'OOOXOOO',
    'OOXXOXO',
    'OXOOOXO'
]

s = Solution()
print(s.black(A))

#########################	greedy	#########################


#####		Distribute Candy		#####

"""
There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:
1. Each child must have at least one candy.
2. Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
Input Format:
The first and the only argument contains N integers in an array A.
Output Format:
Return an integer, representing the minimum candies to be given.
Example:
Input 1:
    A = [1, 2]
Output 1:
    3
Explanation 1:
    The candidate with 1 rating gets 1 candy and candidate with rating cannot get 1 candy as 1 is its neighbor.
    So rating 2 candidate gets 2 candies. In total, 2 + 1 = 3 candies need to be given out.
Input 2:
    A = [1, 5, 2, 1]
Output 2:
    7\
Explanation 2:
    Candies given = [1, 3, 2, 1]
"""


# Greedy works here ( Think of a supportive proof as as assignment ).
# Start with the guy with the least rating. Obviously he will receive 1 candy.
# If he did recieve more than one candy, we could lower it to 1 as none of the neighbor have higher rating.
# Now lets move to the one which is second least. If the least element is its neighbor, then it receives 2 candies,
# else we can get away with assigning it just one candy.
# We keep repeating the same process to arrive at optimal solution.

class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):

        if not A:
            return 0
        res = len(A) * [1]
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                res[i] = res[i - 1] + 1
        for i in range(len(A) - 1, 0, -1):
            if A[i - 1] > A[i]:
                res[i - 1] = max(res[i - 1], res[i] + 1)
        return sum(res)


#####		Bulbs		#####

"""
N light bulbs are connected by a wire.
Each bulb has a switch associated with it, however due to faulty wiring, a switch also changes the state of all
the bulbs to the right of current bulb.
Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs.
You can press the same switch multiple times.
Note : 0 represents the bulb is off and 1 represents the bulb is on.
Input Format:
The first and the only argument contains an integer array A, of size N.
Output Format:
Return an integer representing the minimum number of switches required.
Constraints:
1 <= N <= 5e5
0 <= A[i] <= 1
Example:
Input 1:
    A = [1]
Output 1:
    0
Explanation 1:
    There is no need to turn any switches as all the bulbs are already on.
Input 2:
    A = [0 1 0 1]
Output 2:
    4
Explanation 2:
    press switch 0 : [1 0 1 0]
    press switch 1 : [1 1 0 1]
    press switch 2 : [1 1 1 0]
    press switch 3 : [1 1 1 1]
"""


# The order in which you press the switch does not affect the final state.
# Example:
# Input : [0 1 0 1]
# Case 1:
# 	Press switch 0 : [1 0 1 0]
# 	Press switch 1 : [1 1 0 1]
# Case 2:
# 	Press switch 1 : [0 0 1 0]
# 	Press switch 0 : [1 1 0 1]
# Therefore we can choose a particular order. To make things easier lets go from left to right.
# At the current position if the bulb is on we move to the right, else we switch it on.
# This works because changing any switch to the right of it will not affect it anymore.

class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        def flip(i):
            return 0 if i else 1

        off = 0
        num = 0
        for i in range(len(A)):
            if A[i] == off:
                num += 1
                off = flip(off)
        return num


#####		Majority Element		#####

"""
Given an array of size n, find the majority element.
 The majority element is the element that appears more than floor(n/2) times.
You may assume that the array is non-empty and the majority element always exist in the array.
Example :
Input : [2, 1, 2]
Return  : 2 which occurs 2 times which is greater than 3/2.
"""


# If we cancel out each occurrence of an element e with all the other elements that are different from e then e will
# exist till end if it is a majority element. Loop through each element and maintains a count of the element that has
# the potential of being the majority element. If next element is same then increments the count, otherwise decrements
# the count. If the count reaches 0 then update the potential index to the current element and reset count to 1.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        curr_majority = A[0]
        cnt = 1
        for x in A[1:]:
            if x != curr_majority:
                cnt -= 1
            else:
                cnt += 1

            if cnt == 0:
                curr_majority = x
                cnt = 1

        return curr_majority


#####		Seats		#####

"""
There is a row of seats. Assume that it contains N seats adjacent to each other. There is a group of people who are
already seated in that row randomly. i.e. some are sitting together & some are scattered.
An occupied seat is marked with a character 'x' and an unoccupied seat is marked with a dot ('.')
Now your target is to make the whole group sit together i.e. next to each other, without having any vacant seat
between them in such a way that the total number of hops or jumps to move them should be minimum.
Return minimum value % MOD where MOD = 10000003
Example
Here is the row having 15 seats represented by the String (0, 1, 2, 3, ......... , 14) -
              . . . . x . . x x . . . x . .
Now to make them sit together one of approaches is -
                  . . . . . . x x x x . . . . .
Following are the steps to achieve this -
1 - Move the person sitting at 4th index to 6th index -
    Number of jumps by him =   (6 - 4) = 2
2 - Bring the person sitting at 12th index to 9th index -
    Number of jumps by him = (12 - 9) = 3
So now the total number of jumps made =
    ( 2 + 3 ) % MOD =
    5 which is the minimum possible jumps to make them seat together.
There are also other ways to make them sit together but the number of jumps will exceed 5 and that will not be minimum.
For example bring them all towards the starting of the row i.e. start placing them from index 0.
In that case the total number of jumps will be
    ( 4 + 6 + 6 + 9 )%MOD
    = 25 which is very costly and not an optimized way to do this movement
"""


# Hint : Is it possible to use the median position somehow ?
# Lets take an exmaple:
# string :  .x..x..x.
# positions where x are present {1, 4, 7}
# Median is 4. So we will move all x near our median. 1st person would need to jump 2 steps and 3rd person would
# also need to jump 2 steps. Total answer = 4.
# Can you prove why this approach works ?


class Solution:
    # @param A : string
    # @return an integer
    def seats(self, A):
        res = 0
        xcount = 0
        space = 0
        n = A.count('x')
        for x in A:
            if x == 'x':
                if space != 0:
                    res += min(n - xcount, xcount) * space;
                    space = 0
                xcount += 1
            else:
                space += 1
        return res % 10000003


#####		Highest Product		#####

"""
Given an array A, of N integers A.
Return the highest product possible by multiplying 3 numbers from the array.
NOTE: Solution will fit in a 32-bit signed integer.
Input Format:
The first and the only argument is an integer array A.
Output Format:
Return the highest possible product.
Constraints:
1 <= N <= 5e5
Example:
Input 1:
A = [1, 2, 3, 4]
Output 1:
24
Explanation 1:
2 * 3 * 4 = 24
Input 2:
A = [0, -1, 3, 100, 70, 50]
Output 2:
350000
Explanation 2:
70 * 50 * 100 = 350000
"""


# Do we need to consider all the elements from the array ?
# Is it enough to consider just the 3 maximum numbers from the array ? Obviously No.
# Product of 2 negative numbers is positive. So, Negative numbers with higher absolute value might also be of interest.
# How about maximum 3 elements, and 2 negative elements with the highest absolute value ?
# Choosing 3 maximum elements in the array and 2 negative elements with the highest absolute value should be enough.
# There are various ways to calculate 3 maximum elements in the array ( and subsequently 2 negative elements with
# highest absolute value ). One such approach is maintaining 3 variables ( m1, m2, m3 where m1 > m2 > m3 ).
# When you encounter new value in the array, if the value is less than m3, then the variables are unaffected.
# Else, depending on where the new value lies, you can update the 3 values.
# Another approach could be maintaining a priority_queue of size 3. You pop out the smallest element if
# the new element if bigger than the smallest element, and then insert the new element into the priority queue.
# Once you have the 5 elements you desire,
# your answer would be one of the following :
# 1) Product of 3 maximum elements
# 2) Product of the 2 negative elements with max absolute value and maximum positive value.


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        A.sort(reverse=True)
        n = len(A) - 1
        if A[n] >= 0:
            p = A[0] * A[1] * A[2]
        elif A[0] > 0:
            p = max(A[0] * A[1] * A[2], A[0] * A[n] * A[n - 1])
        elif A[0] <= 0:
            p = A[0] * A[1] * A[2]
        return p


#####		Assign Mice To Holes		#####

"""
There are N Mice and N holes are placed in a straight line.
Each hole can accomodate only 1 mouse.
A mouse can stay at his position, move one step right from x to x + 1, or move one step left from x to x − 1.
Any of these moves consumes 1 minute.
Assign mice to holes so that the time when the last mouse gets inside a hole is minimized.
Example:
positions of mice are:
4 -4 2
positions of holes are:
4 0 5
Assign mouse at position x=4 to hole at position x=4 : Time taken is 0 minutes
Assign mouse at position x=-4 to hole at position x=0 : Time taken is 4 minutes
Assign mouse at position x=2 to hole at position x=5 : Time taken is 3 minutes
After 4 minutes all of the mice are in the holes.
Since, there is no combination possible where the last mouse's time is less than 4,
answer = 4.
Input:
A :  list of positions of mice
B :  list of positions of holes
Output:
single integer value
 NOTE: The final answer will fit in a 32 bit signed integer.
"""


# Approach:
#
# sort mice positions (in any order)
# sort hole positions
# Loop i = 1 to N:
#     update ans according to the value of |mice(i) - hole(i)|
# Proof of correctness:
# Let i1 < i2 be the positions of two mice and let j1 < j2 be the positions of two holes.
# It suffices to show via case analysis that
# max(|i1 - j1|, |i2 - j2|) <= max(|i1 - j2|, |i2 - j1|) ,
#     where '|a - b|' represent absolute value of (a - b)
# since it follows by induction that every assignment can be transformed by a series of swaps into
# the sorted assignment, where none of these swaps increases the makespan

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, a, b):
        return max(abs(i - j) for i, j in zip(sorted(a), sorted(b)))


#####		Gas Station		#####

"""
Given two integer arrays A and B of size N.
There are N gas stations along a circular route, where the amount of gas at station i is A[i].
You have a car with an unlimited gas tank and it costs B[i] of gas to travel from station i
to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
Return the minimum starting gas station’s index if you can travel around the circuit once, otherwise return -1.
You can only travel in one direction. i to i+1, i+2, … n-1, 0, 1, 2.. Completing the circuit means starting at i and
ending up at i again.
Input Format
The first argument given is the integer array A.
The second argument given is the integer array B.
Output Format
Return the minimum starting gas station's index if you can travel around the circuit once, otherwise return -1.
For Example
Input 1:
    A =  [1, 2]
    B =  [2, 1]
Output 1:
    1
    Explanation 1:
        If you start from index 0, you can fill in A[0] = 1 amount of gas. Now your tank has 1 unit of gas.
        But you need B[0] = 2 gas to travel to station 1.
        If you start from index 1, you can fill in A[1] = 2 amount of gas. Now your tank has 2 units of gas.
        You need B[1] = 1 gas to get to station 0. So, you travel to station 0 and still have 1 unit of gas left over.
        You fill in A[0] = 1 unit of additional gas, making your current gas = 2. It costs you B[0] = 2 to get
        to station 1, which you do and complete the circuit.
"""


# The bruteforce solution should be obvious. Start from every i, and check to see if every point is reachable with the
# gas available. Return the first i for which you can complete the trip without the gas reaching a negative number.
# This approach would however be quadratic.
# Lets look at how we can improve.
# 1) If sum of gas is more than sum of cost, does it imply that there always is a solution ?
# 2) Lets say you start at i, and hit first negative of sum(gas) - sum(cost) at j.
# We know TotalSum(gas) - TotalSum(cost) > 0. What happens if you start at j + 1 instead ?
# Does it cover the validity clause for i to j already ?

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        sumo = 0
        fuel = 0
        start = 0
        for i in range(len(gas)):
            sumo = sumo + (gas[i] - cost[i])
            fuel = fuel + (gas[i] - cost[i])
            if fuel < 0:
                fuel = 0
                start = i + 1
        if sumo >= 0:
            return start % len(gas)
        else:
            return -1


#########################	hashing	#########################


#####		Fraction		#####

"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.
Example :
Given numerator = 1, denominator = 2, return "0.5"
Given numerator = 2, denominator = 1, return "2"
Given numerator = 2, denominator = 3, return "0.(6)"
"""


# Lets simulate the process of converting fraction to decimal. Lets look at the part where we have already
# figured out the integer part which is floor(numerator / denominator).
# Now you are left with ( remainder = numerator%denominator ) / denominator.
# If you remember the process of converting to decimal, at each step you do the following :
# 1) multiply the remainder by 10,
# 2) append remainder / denominator to your decimals
# 3) remainder = remainder % denominator.
# At any moment, if your remainder becomes 0, you are done.
# However, there is a problem with recurring decimals. For example if you look at 1/3, the remainder never becomes 0.
# Notice one more important thing.
# If you start with remainder = R at any point with denominator d, you will always get the same sequence of digits.
# So, if your remainder repeats at any point of time, you know that the digits between the last occurrence
# of R will keep repeating.

class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def fractionToDecimal(self, numerator, denominator):
        result = ""
        if (numerator > 0 > denominator) or (numerator < 0 < denominator):
            result = "-"  # if any of numerator or denominator is negative starting final string with (-) negative sign
        n, d = abs(numerator), abs(denominator)
        result += str(n // d)  # adding Quotient to final string
        remainder = n % d  # remainder
        if remainder > 0:
            result += "."  # if remainder then add decimal point in final string
        hash_map = {}  # creating a hash table for storing the fractional value
        while remainder and remainder not in hash_map:
            hash_map[remainder] = len(result)
            remainder *= 10
            result += str(remainder // d)
            remainder %= d
        if remainder in hash_map:
            result = result[:hash_map[remainder]] + "(" + result[hash_map[remainder]:] + ")"
        return result


#####		Equal		#####

"""
Given an array A of integers, find the index of values that satisfy A + B = C + D,
where A,B,C & D are integers values in the array
Note:
1) Return the indices `A1 B1 C1 D1`, so that
  A[A1] + A[B1] = A[C1] + A[D1]
  A1 < B1, C1 < D1
  A1 < C1, B1 != D1, B1 != C1
2) If there are more than one solutions,
   then return the tuple of values which are lexicographical smallest.
Assume we have two solutions
S1 : A1 B1 C1 D1 ( these are values of indices int the array )
S2 : A2 B2 C2 D2
S1 is lexicographically smaller than S2 iff
  A1 < A2 OR
  A1 = A2 AND B1 < B2 OR
  A1 = A2 AND B1 = B2 AND C1 < C2 OR
  A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2
Example:
Input: [3, 4, 7, 1, 2, 9, 8]
Output: [0, 2, 3, 5] (O index)
If no solution is possible, return an empty list.
"""


# Continuing from the first hint,
# Hashing can provide one more level of optimization.
# Lets look at our bruteforce solution once more :
# Loop I = 1 to N :
#   Loop J = 1 to N :
#     Loop K = 1 to N:
#         Loop L = 1 to N:
#                if condition is true then update ans
#          endLoop;
#      endLoop;
#    endLoop;
# endLoop;
# Do we need a loop for L if we have hashed out the values ?
# We know that A[I] + A[J] = A[K] + A[L].
# If we know, I, J and K, then we can determine what A[L] should be.
# We can lookup the value A[L] = A[I] + A[J] - A[K] in a hashmap.
# The solution then becomes O(N^3) instead of O(N^4).
# Do note that we need to take care of duplicate values here.
# However, this might be a little slow as well. We are looking for something better.
# Can we use more space to optimize the solution ? How about hashing pairwise sums ( A[i] + A[J], A[K] + A[L] ) ?
# Loop i = 1 to N :
#     Loop j = i + 1 to N :
#         calculate sum
#         If in hash table any index already exist for sum then
#             try to find out that it is valid solution or not IF Yes Then update solution
#         update hash table
#     EndLoop;
# EndLoop;

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):

        """ Return matching indices or None """
        n = len(A)
        sums = {}
        res = []
        # Iterate pairs in lexicographical order
        for i in range(n - 1):
            for j in range(i + 1, n):
                s = A[i] + A[j]
                if s in sums:
                    k, l = sums[s]
                    if i != k and i != l and j != l:
                        # Here k < i necessarilly
                        if res:
                            res = min(res, [k, l, i, j])
                        else:
                            res = [k, l, i, j]
                else:
                    sums[s] = (i, j)  # smallest pair for this sum
        return res


#####		Colorful Number		#####

"""
For Given Number N find if its COLORFUL number or not
Return 0/1
COLORFUL number:
A number can be broken into different contiguous sub-subsequence parts.
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
Example:
N = 23
2 3 23
2 -> 2
3 -> 3
23 -> 6
this number is a COLORFUL number since product of every digit of a sub-sequence are different.
Output : 1
"""

# Note that input number can be of length atmax 10.
# So, number of substring can be atmax 45.
# It is one of the easiest problem in this section.
# You just need to simulate what has been stated in the problem.
# Iterate over all substrings of number, and then check if the number
# resulting from the multiplication has been stored by us or not using hashing.
# Example:
# N = 123
# 1 2 3 12 23 123
# 1 -> 1
# 2 -> 2
# 3 -> 3
# 12 -> 2  uh-oh, we have already encountered 2 before. Return 0

from functools import reduce


class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        products = set()
        str_num = str(A)
        for i in range(len(str_num)):
            for j in range(i + 1, len(str_num) + 1):
                product = reduce(lambda x, y: x * y, map(int, list(str_num[i:j])))
                if product in products:
                    return 0
                products.add(product)
        return 1


#####		Anagrams		#####

"""
Given an array of strings, return all groups of strings that are anagrams. Represent a group by a list of integers
representing the index in the original list. Look at the sample case for clarification.
 Anagram : a word, phrase, or name formed by rearranging the letters of another, such as 'spar', formed from 'rasp'
 Note: All inputs will be in lower-case.
Example :
Input : cat dog god tca
Output : [[1, 4], [2, 3]]
cat and tca are anagrams which correspond to index 1 and 4.
dog and god are another set of anagrams which correspond to index 2 and 3.
The indices are 1 based ( the first element has index 1 instead of index 0).
 Ordering of the result : You should not change the relative ordering of the words / phrases within the group. Within a
  group containing A[i] and A[j], A[i] comes before A[j] if i < j.
"""


# Anagrams will map to the same string if the characters in the string are sorted.
# We can maintain a hashmap with the key being the sorted string and the value being the
# list of strings ( which have the sorted characters as key ).

class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        # hashmap with sorted string as key and list of anagrams as values
        hashmap = {}
        for index, word in enumerate(A):
            # sorted() returns a list, hence first convert it to a string
            # so that we can use it as a key in the hashmap
            sorted_word = ''.join(sorted(word))
            if sorted_word not in hashmap:
                # create key if not present and associate
                # the current word with it
                hashmap[sorted_word] = [index + 1]
            else:
                # append the current word to the list associated with the key
                hashmap[sorted_word] += [index + 1]
        # hashmap.values() returns a dict_values object in python 3,
        # hence convert it into a list while returning
        return list(hashmap.values())


#####		Window String		#####

"""
Given a string S and a string T, find the minimum window in S which will
contain all the characters in T in linear time complexity.
Note that when the count of a character C in T is N, then the count of C in minimum window in S should be at least N.
Example :
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC"
 Note:
If there is no such window in S that covers all characters in T, return the empty string ''.
If there are multiple such windows, return the first occurring minimum window ( with minimum start index ).
"""

# Essentially you have a start and end pointer starting from the beginning of the string. You keep moving the end
# pointer and including more characters till you have all the characters of T included. At this point, you start
# moving start pointer and popping out characters till the point that you still have all the characters of T included.
# Update your answer and keep repeating the process.

from collections import deque


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def minWindow(self, A, B):
        if not A or not B:
            return ''
        required_chars = {}
        for b in B:
            if b not in required_chars:
                required_chars[b] = deque()
            required_chars[b].append(-1)
        n_needed = len(B)

        best = None
        cur_min = None
        for idx, a in enumerate(A):
            if a in required_chars:
                old_idx = required_chars[a].popleft()
                required_chars[a].append(idx)
                if n_needed != 0 and old_idx == -1:
                    n_needed -= 1
                if n_needed == 0 and (cur_min is None or old_idx == cur_min):
                    cur_min = min([a[0] for a in required_chars.values()])
                    if best is None or best[1] - best[0] > idx - cur_min:
                        best = [cur_min, idx]
        if best is None:
            return ''
        return A[best[0]:best[1] + 1]


#####		Longest Substring Without Repeat		#####

"""
Given a string,
find the length of the longest substring without repeating characters.
Example:
The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
For "bbbbb" the longest substring is "b", with the length of 1.
"""


# Think in terms of two pointers.
# If you encounter a repeating character, you won’t be able to include the new character till you exclude out the
# previous occurrence of the character. Which means your window needs to shrink till your start character is pointing
# to the position next to previous occurrence of the character.
# All you need to do is use two pointers to keep a window with no repetitions of characters. Keep moving the right
# pointer and if you encounter any repeating character start moving left pointer untill no character is repeated.
# Also, note that the size of character set is small ( 128 at max ), so tracking the count of characters in the
# current set is fairly easy using hashing / array buckets.

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        i = j = result = 0
        sz = len(A)
        storage = set()
        while i < sz and j < sz:
            if A[j] in storage:
                storage.remove(A[i])
                i += 1
            else:
                storage.add(A[j])
                j += 1
                result = max(result, j - i)
        return result


#####		Substring Concatenation		#####

"""
You are given a string, S, and a list of words, L, that are all of the same length.

Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once
and without any intervening characters.
Example :
S: "barfoothefoobarman"
L: ["foo", "bar"]
You should return the indices: [0,9].
(order does not matter).
"""


# You know that every word in L is of same length( say x). Let the number of words in L be n.
# You need to check if every segment of length n*x in our main word consist of some permutation of all
# the words given in the list.
# If you can do that for one segment you can just slide using two pointer and do it for all segments.
# For a single segment you can use hashing. How?
# Think of the bruteforce solution.
# Lets say the size of every word is wsize and number of words is lsize.
# You start at every index i. Look at every lsize number of chunks of size wsize and note down the words.
# Then match the set of words encountered to the set of words expected.
# Now, lets look at ways we can optimize this.
# Right now, to match words, we do it letter by letter. How about hashing the words ?
# With hashing, hash(w1) + hash(w2) = hash(w2) + hash(w1).
# In short, when adding the hashes, the order of words does not matter.
# Can we optimize the matching of all the words encountered using that ?
# an we use sliding pointers to move to index i + wsize from i ?


class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        lits_size = len(B)
        word_size = len(B[0])
        i = 0
        ans = []
        comp = 0
        for word in B:
            comp += hash(word)
        while i + lits_size * word_size <= len(A):
            x = list(A[i:i + lits_size * word_size])
            j = -1
            temp = []
            final = 0
            while x != []:
                k = 0
                tempword = []
                while k < word_size:
                    y = x.pop(0)
                    tempword.append(y)
                    k += 1
                temp.append("".join(tempword))
                final += hash("".join(tempword))
            if comp == final:
                ans.append(i)
            i += 1
        return ans


#####		4 Sum		#####

"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.
 Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
Example :
Given array S = {1 0 -1 0 -2 2}, and target = 0
A solution set is:
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
    (-1,  0, 0, 1)
Also make sure that the solution set is lexicographically sorted.
Solution[i] < Solution[j] iff Solution[i][0] < Solution[j][0] OR (Solution[i][0] == Solution[j][0]
AND ... Solution[i][k] < Solution[j][k])
"""


# The naive approach obviously is exploring all combinations of 4 integers using 4 loops.#
# Now, to look into improving, does it help if we sort the array ?
# Also, think of how your approach would change if you did not have to list all of the unique tuples but
# just tell whether at least one such tuple existed ( YES / NO ).
# When the array is sorted, try to fix the least and second least integer by looping over it.
# Lets say the least integer in the solution is arr[i] and second least is arr[j].
# Now we need to find a pair of integers k and l such that arr[k] + arr[l] is target-arr[i]-arr[j].
# To do that, lets try the 2 pointer approach. If we fix the two pointers at the end ( that is, j+1 and end of array ),
# we look at the sum.
# If the sum is smaller than the sum we want, we increase the first pointer to increase the sum.
# If the sum is bigger than the sum we want, we decrease the end pointer to reduce the sum.
# Note that there is one more solution possible if the question only asked to answer YES / NO to suggest whether
# there existed at least one tuple with the target sum. Then we could have gone with an approach using more memory
# with hashing.
# Getting a Time Limit exceeded or Output Limit exceeded ?
# Make sure you handle case of empty input []. In C++/C, Usually if you run a loop till array.size() - 2, it can
# lead to the program running indefinitely as array.size() is unsigned int, and the subtraction just makes it
# wrap over to a big integer.
# Make sure you are not processing the same triplets again. Skip over the duplicates in the array.
# Try a input like :
# -1 -1 -1 -1 0 0 0 0 1 1 1 1
# Ideally, you should get only 3 pairs : {[-1 -1 1 1], [-1 0 0 1], [0 0 0 0]}

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        seen = dict()
        A.sort()
        result = set()
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                curr_sum = A[i] + A[j]
                diff = B - curr_sum
                if diff in seen:
                    for prev_sum in seen[diff]:
                        if A[prev_sum[1]] <= A[i] and i > prev_sum[1]:
                            result.add((A[prev_sum[0]], A[prev_sum[1]], A[i], A[j]))
                if curr_sum in seen:
                    seen[curr_sum].append((i, j))
                else:
                    seen[curr_sum] = [(i, j)]
        return sorted([list(item) for item in result])


#####		Diff 2		#####

"""
Given an array A of integers and another non negative integer k,
find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
Example :
Input :
A : [1 5 3]
k : 2
Output :
1
as 3 - 1 = 2
Return 0 / 1 for this problem.
"""


# The naive approach obviously is exloring all combinations of 2 integers using 2 loops and then check their difference.
# However, lets look at it like this.
# We are looking to find pair of integers where A[i] - A[j] = k, k being known entity
# Lets say we fix A[i] ( i.e. we know A[i]), do we know what A[j] should be ?
# Once we know what A[j] we want, does it reduce to a search / lookup problem ?
# We can store all the numbers in a hashmap / hashset and then lookup A[j] in it to find out if A[j] exists.
# Corner case : How do you handle case when k = 0 cleanly ?

class Solution:
    def diffPossible(self, A, B):
        dic = set()
        for i in range(len(A)):
            if A[i] - B in dic or A[i] + B in dic:
                return 1
            dic.add(A[i])
        return 0


#####		Largest Continuous Sequence Zero Sum		#####

"""
Find the largest continuous sequence in a array which sums to zero.
Example:
Input:  {1 ,2 ,-2 ,4 ,-4}
Output: {2 ,-2 ,4 ,-4}
 NOTE : If there are multiple correct answers, return the sequence which occurs first in the array.
"""


# Lets try to reduce the problem to a much simpler problem.
# Lets say we have another array sum where
#   sum[i] = Sum of all elements from A[0] to A[i]
# Note that in this array, sum of elements from A[i] to A[j] = Sum[j] - Sum[i-1]
# We need to find j and i such that sum of elements from A[i] to A[j] = 0
#  Or Sum[j] - Sum[i-1] = 0
#  Or Sum[j] = Sum[i-1]
# Now, the problem reduces to finding 2 indices i and j such that sum[i] = sum[j]
# How can you solve the above problem ?
# There are two steps:
# 1. Create cumulative sum array where ith index in this array represents total sum from 1 to ith index element.
# 2. Iterate all elements of cumulative sum array and use hashing to find two elements
# where value at ith index == value at jth index but i != j.
# 3. IF element is not present in hash in fill hash table with current element.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        sumDict = {0: -1}
        total = 0
        maxLCS, maxi, maxj = 0, -1, -1

        for i, val in enumerate(A):
            total += val
            if total in sumDict:
                if maxLCS < i - sumDict[total]:
                    maxLCS = i - sumDict[total]
                    maxi = sumDict[total] + 1
                    maxj = i
            else:
                sumDict[total] = i
        return A[maxi: maxj + 1] if maxLCS else []


#####		Valid Sudoku		#####

"""
Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx
The Sudoku board could be partially filled, where empty cells are filled with the character ‘.’.
The input corresponding to the above configuration :
["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
A partially filled sudoku which is valid.
 Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""


# Very simple simulation problem. Just need to keep track of the digits seen in every row,
# every column and every block as defined in the rules.
# Whenever you encounter a digit already seen, you know the sudoku is not valid.
# Note that this problem will get very complicated if you were to determine if the sudoku was solvable.

class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        for i in range(9):
            if not self.isValidArray(list(A[i])) \
                    or not self.isValidArray([A[j][i] for j in range(9)]) \
                    or not self.isValidArray([A[3 * (i // 3) + j // 3][3 * (i % 3) + j % 3] for j in range(9)]):
                return 0
        return 1

    def isValidArray(self, arr):
        s = set()
        for x in arr:
            if x in s:
                return False
            if x != '.':
                s.add(x)
        return True


#####		Copy List		#####

"""
A linked list is given such that each node contains an additional random pointer which could point to any node in
the list or NULL.
Return a deep copy of the list.
Example
Given list
   1 -> 2 -> 3
with random pointers going from
  1 -> 3
  2 -> 1
  3 -> 1
You should return a deep copy of the list. The returned answer should not contain the same node as the original list,
but a copy of them. The pointers in the returned list should not link to any node in the original input list.
"""


# There are 2 approaches to solving this problem.
# Approach 1 : Using hashmap.
# Use a hashmap to store the mapping from oldListNode to the newListNode.
# Whenever you encounter a new node in the oldListNode (either via random pointer or through the next pointer ),
# create the newListNode, store the mapping. and update the next and random pointers of the newListNode
# using the mapping from the hashmap.
# Approach 2 : Using 2 traversals of the list.
# Step 1: create a new node for each existing node and join them together eg: A->B->C will be A->A’->B->B’->C->C’
# Step2: copy the random links: for each new node n’, n’.random = n.random.next
# Step3: detach the list: basically n.next = n.next.next; n’.next = n’.next.next

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head == None:
            return None

        done = {}
        cur = head

        while cur is not None:
            done[cur] = RandomListNode(cur.label)
            cur = cur.next

        for (k, v) in done.iteritems():
            new_node = v
            new_node.next = done[k.next] if k.next in done else None
            new_node.random = done[k.random] if k.random in done else None

        return done[head]


#####		2 Sum		#####

"""
Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 < index2. Please note that your returned answers (both index1 and index2 ) are not zero-based.
Put both these numbers in order in an array and return the array from your function ( Looking at the function
signature will make things clearer ). Note that, if no pair exists, return empty list.
If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the minimum
index2, choose the one with minimum index1 out of them.
Input: [2, 7, 11, 15], target=9
Output: index1 = 1, index2 = 2
"""


# O(n^2) runtime, O(1) space – Brute force:
# The brute force approach is simple. Loop through each element x and find if there is another value that equals to
# target – x. As finding another value requires looping through the rest of array, its runtime complexity is O(n^2).
# To improve on it, notice that when we fix one of the integers ‘curValue’, we know the value of the other integer we
# need to find ( target - curValue ).
# Then it becomes a simple search problem. You can store all the integers of the array in a hashmap and do a lookup
# to check if the elements exists in the map.
# Have you checked cases where the element you are looking up in the map is same as the curValue.
# For example, consider the following cases :
# A:[4 4] target : 8
# and A :[3 4] target : 8
# The answer in first case should be [1 2] and in second case, it should be empty.

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, k):
        diffs = {}
        for i, v in enumerate(A):
            if k - v in diffs:
                return diffs[k - v] + 1, i + 1
            elif v not in diffs:
                diffs[v] = i
        return []


#####		Points On A Straight Line		#####

"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
Sample Input :
(1, 1)
(2, 2)
Sample Output :
2
You will be given 2 arrays X and Y. Each point is represented by (X[i], Y[i])
"""


# A line is made by a pair of points.
# If a,b and c lie on the same line, then line connecting a and b,
# and line connecting a and c will have the same slope ( (y2 - y1) / (x2 - x1)).
# Make sure you handle all the corner cases.
# Corner cases :
# 1) Have you handled overlapping points ?
# 2) Have you handled negative points for the same slope ? Like (0,0), (1,1) and (-1, -1)
# 3) Did you make sure that there are no divisions by 0 ? Like (1, 0), (1,4), (1, -1)
# 4) How do you handle when one of the differences in x and y is 0, and the other difference
# is negative / positive ? Like (4, -4), (8, -4), (-4, -4)


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, A, B):
        n = len(A)
        if (n <= 2):
            return n
        m = 0  # result value
        for i in range(n):
            l = {}  # every time reset the dict
            dup = 1  # count the duplicates
            for j in range(n):
                if (A[i] == A[j] and B[i] == B[j] and i != j):
                    dup += 1  # count duplicates
                elif i != j:
                    if (A[i] == A[j]):  # vertical line
                        l['v'] = l.get('v', 0) + 1
                    elif (B[i] == B[j]):  # horizontal line
                        l['h'] = l.get('h', 0) + 1
                    else:  # regular slope
                        slope = 1.0 * (B[i] - B[j]) / (A[i] - A[j])
                        l[slope] = l.get(slope, 0) + 1
            if (len(l) > 0):
                m = max(m, max(l.values()) + dup)
            else:  # if all points are duplicates, l is empty.
                m = max(m, dup)
        return m


#########################	heaps-and-maps	#########################


#####		Magician And Chocolates		#####

"""
Given N bags, each bag contains Ai chocolates. There is a kid and a magician. In one unit of time, kid chooses a
random bag i, eats Ai chocolates, then the magician fills the ith bag with floor(Ai/2) chocolates.
Given Ai for 1 <= i <= N, find the maximum number of chocolates kid can eat in K units of time.
For example,
K = 3
N = 2
A = 6 5
Return: 14
At t = 1 kid eats 6 chocolates from bag 0, and the bag gets filled by 3 chocolates
At t = 2 kid eats 5 chocolates from bag 1, and the bag gets filled by 2 chocolates
At t = 3 kid eats 3 chocolates from bag 0, and the bag gets filled by 1 chocolate
so, total number of chocolates eaten: 6 + 5 + 3 = 14
Note: Return your answer modulo 10^9+7
"""

# The solution to this problem can be found greedily. At any time t, the kid will always choose the bag with the
# maximum number of chocolates and consume all it’s chocolates.
# So we need to maintain the current maximum size among all bags for every time t = 1, … , K and
# also updating the sizes of the bags.
# This can be done using a max heap : https://en.wikipedia.org/wiki/Min-max_heap

import heapq


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        choc = 0
        B = [-i for i in B]
        heapq.heapify(B)
        for i in range(A):
            top = heapq.heappop(B)
            pot = -(top)
            pot = pot // 2
            heapq.heappush(B, -pot)
            choc = choc - top
        return choc % (10 ** 9 + 7)


#####		N Max Pair Combinations		#####

"""
N max pair combinations
Asked in:
Liv.ai
Problem Setter: dhruvi Problem Tester: ganeshk2
Given two arrays A & B of size N each.
Find the maximum N elements from the sum combinations (Ai + Bj) formed from elements in array A and B.

For example if A = [1,2], B = [3,4], then possible pair sums can be 1+3 = 4 , 1+4=5 , 2+3=5 , 2+4=6
and maximum 2 elements are 6, 5

Example:

N = 4
a[]={1,4,2,3}
b[]={2,5,1,6}

Maximum 4 elements of combinations sum are
10   (4+6),
9    (3+6),
9    (4+5),
8    (2+6)
"""

# Sort both the arrays in ascending order.
# Let us take priority queue (heap).
# First max element is going to be the sum of the last two elements of array A and B i.e. (A[n-1] + B[n-1]).
# Insert that in heap with indices of both array i.e (n-1, n-1).
# Start popping from heap (n-iterations).
# And insert the sum (A[L-1]+A[R]) and (A[L]+B[R-1]).
# Take care that repeating indices should not be there in the heap (use map for that).

import heapq


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        N = len(A)
        visited = set()
        A = sorted(A, reverse=True)
        B = sorted(B, reverse=True)
        result = []
        heap = []
        visited.add((0, 0))
        heapq.heappush(heap, (-(A[0] + B[0]), (0, 0)))
        for _ in range(N):
            sum, (iA, iB) = heapq.heappop(heap)
            result.append(-sum)
            tuple1 = (iA + 1, iB)
            if iA < N - 1 and tuple1 not in visited:
                heapq.heappush(heap, (-(A[iA + 1] + B[iB]), tuple1))
                visited.add(tuple1)
            tuple2 = (iA, iB + 1)
            if iB < N - 1 and tuple2 not in visited:
                heapq.heappush(heap, (-(A[iA] + B[iB + 1]), tuple2))
                visited.add(tuple2)
        return result


s = Solution()
print(s.solve([1, 2], [3, 4]))

#####		Ways To Form Maxheap		#####

"""
Max Heap is a special kind of complete binary tree in which for every node the value present in that node is greater
 than the value present in it’s children nodes. If you want to know more about Heaps, please visit this link
So now the problem statement for this question is:
How many distinct Max Heap can be made from n distinct integers
In short, you have to ensure the following properties for the max heap :
Heap has to be a complete binary tree ( A complete binary tree is a binary tree in which every level, except
possibly the last, is completely filled, and all nodes are as far left as possible. )
Every node is greater than all its children
Let us take an example of 4 distinct integers. Without loss of generality let us take 1 2 3 4 as our 4 distinct integers
Following are the possible max heaps from these 4 numbers :
         4
       /  \
      3   2
     /
    1
         4
       /  \
      2   3
     /
    1
        4
       /  \
      3   1
     /
    2
These are the only possible 3 distinct max heaps possible for 4 distinct elements.
Implement the below function to return the number of distinct Max Heaps that is possible from n distinct elements.
As the final answer can be very large output your answer modulo 1000000007
Input Constraints : n <= 100
 NOTE: Note that even though constraints are mentioned for this problem, for most problems on InterviewBit,
 constraints are intentionally left out. In real interviews, the interviewer might not disclose constraints
  and ask you to do the best you can do.
"""

# Suppose there are n distinct elements to be used in Max heap. Now it is for sure that the maximum element
# among this n distinct element will surely be placed on the root of the heap.
# Now there will be remaining (n-1) elements to be arranged.
# Now point to be remembered here is that the structure of the heap will remain the same. That is only the values
# within the node will change however the overall structure remaining the same.
# As structure of the heap remains the same, the number of elements that are present in the left sub-tree of the root
# (L) will be fixed. And similarly the number of the elements on the right sub-tree (R) of the root.
# And also following equality holds .
#  L + R = (n-1)
# Now as all the remaining (n-1) elements are less than the element present at the root(The Max Element), whichever L
# elements among ‘n-1` elements we put in the left sub-tree, it doesn’t matter because it will satisfy
# the Max Heap property
# So now there are (n-1)CL ways to pickup L elements from (n-1) elements. And then recurse the solution.
# So final equation will be as follows :
#  (n-1)CL * getNumberOfMaxHeaps(L) * getNumberOfMaxHeaps(R)
# So now the question remains only of finding L for given n. It can be found as follows:
# Find the height of the heap h = log2(n)
# Find the max number of elements that can be present in the hth level of any heap . Lets call it m. m = 2h
# Find the number of elements that are actually present in last level(hth level) in heap of size n.
# Lets call it p. p = n - (2h - 1)
# Now if the last level of the heap is more than or equal to exactly half filled, then L would be 2h - 1
# However if it is half filled then it will reduced by the number of elements in last level
# left to fill exactly half of the last level.
# So final equation for L will be as follows :
#  L = 2h - 1 if p >= m/2
#                     = 2h - 1 - (m/2 - p) if p<(m/2)


MOD = 10 ** 9 + 7


class Solution:
    def comb(self, r, n):
        if 2 * r > n:
            return self.comb(n - r, n)
        c = 1
        for i in range(r):
            c = c * (n - i) // (i + 1)
        return c

    def solve(self, A):
        ans, h = [1, 1], 0
        for n in range(2, A + 1):
            if 2 << h <= n:
                h += 1
            m = n - (1 << h) + 1
            l = (1 << (h - 1)) - 1 + min(m, 1 << (h - 1))
            r = (1 << (h - 1)) - 1 + max(0, m - (1 << (h - 1)))
            ans.append((self.comb(l, n - 1) * ans[l] * ans[r]) % MOD)
        return ans[A]


#####		Lru Cache		#####

"""
Design and implement a data structure for LRU (Least Recently Used) cache. It should support the following operations:
 get and set.
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity,
 it should invalidate the least recently used item before inserting the new item.
The LRU Cache will be initialized with an integer corresponding to its capacity. Capacity indicates the maximum number
of unique keys it can hold at a time.
Definition of “least recently used” : An access to an item is defined as a get or a set operation of the item.
“Least recently used” item is the one with the oldest access time.
 NOTE: If you are using any global variables, make sure to clear them in the constructor.
Example :
Input :
         capacity = 2
         set(1, 10)
         set(5, 12)
         get(5)        returns 12
         get(1)        returns 10
         get(10)       returns -1
         set(6, 14)    this pushes out key = 5 as LRU is full.
         get(5)        returns -1
"""

# Lets approach this question bit by bit.
# If lets say you never had to remove entries from the LRU cache because we had enough space
# , what would you use to support and get and set ?
# A simple map / hashmap would suffice.
# Alright, lets now look at the second part which is where the eviction comes in.
# We need a data structure which at any given instance can give me the least recently used objects in order.
# Lets see if we can maintain a linked list to do it. We try to keep the list ordered by the order in which
# they are used. So whenever, a get operation happens, we would need to move that object from a certain position
# in the list to the front of the list. Which means a delete followed by insert at the beginning.
# Insert at the beginning of the list is trivial. How do we achieve erase of the object
# from a random position in least time possible ?
# How about we maintain another map which stores the pointer to the corresponding linked list node.
# Ok, now when we know the node, we would need to know its previous and next node in the list to enable the deletion
# of the node from the list. We can get the next in the list from next pointer ? What about the previous node ?
# To encounter that, we make the list doubly linked list.
# Now, can you think of an approach using doubly linked list and the map(s) ?
# As discussed in the previous hint, we solve this problem using :
# originalMap : A hashmap which stores the originial key to value mapping
# accessList : A doubly linked list which has keys ordered by their access time ( Most recently
# used key in front of the list to least recently used key at the end of the list ).
# addressMap : A hashmap which saves the mapping of key to address of the key in accessList.
# Lets see now how the get and set operation would work :
# get(key) :
# Look for the value corresponding to key in originalMap.
# If key is not found, we don’t need to change accessList. So, return -1.
# If key is found, then we need to move the node corresponding to the key to front of the list in accessList.
# To do that, we find the address of the node for key from addressMap. We make the node->prev->next = node->next;,
# node->next->prev = node->prev;, node->prev = NULL; node->next = head; head->prev = node;
# We update the head of the accessList to be node now.
# set(key, value)
# If the key is a new entry (it does not exist in the originalMap) AND the cache is full(size = capacity),
# then we would need to remove the least recently used key lkey.
# We know that this key is the key corresponding to the last node in accessList which is accessible in O(1).
# To evict, we delete the last node from accessList, and the entry corresponding to lkey(from last node)
# in addressMap and originalMap.
# Post this, there are 2 cases.
# key is a new entry and is not present in originalMap. In this case, a new node is created for key and
# inserted at the head of accessList. A new (key,value) entry is created into originalMap and addressMap accordingly.
# key is present in the map, in which case the value needs to be updated. We update the value in the originalMap
# and then we update the accessList for key exactly the way we did in the case of get operation.
# A couple of insights for clean code :
# Note that the update of accessList for key when key is present is a common operation in get and a subcase of set
# function. We should create a function for it and call that function in both cases to reduce redundancy.
# Also, note that originalMap and addressMap are always of the same size with the same keys ( One with value and
# the other with address in linkedlist ). If you want to manage less maps, you can just have a masterMap which maps
# key to a pair of (value, address_in_list)


from collections import deque


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {}
        self.q = deque()

    # @return an integer
    def get(self, key):
        if key in self.dic:
            self.q.remove(key)
            self.q.appendleft(key)
            return self.dic[key]
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.dic:
            self.q.remove(key)
        elif self.capacity == len(self.dic):
            keyToRemove = self.q.pop()
            del self.dic[keyToRemove]
        self.q.appendleft(key)
        self.dic[key] = value


#####		Merge K Sorted Linked Lists		#####

"""
Merge k sorted linked lists and return it as one sorted list.
Example :
1 -> 10 -> 20
4 -> 11 -> 13
3 -> 8 -> 9
will result in
1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20
"""


# Lets keep a pointer for every linked list. At any instant you will need to know the minimum of elements at all
# pointer. Following it you will need to advance that pointer. Can you do this in complexity better than O(K).
# Preferably O(logK). But how?
# There are 2 approaches to solving the problem.
# Approach 1 : Using heap.
# At every instant, you need the minimum of the head of all the k linked list. Once you know the minimum,
# you can push the node to your answer list, and move over to the next node in that linked list.
# Approach 2 : Divide and conquer.
# Solve the problem for first k/2 and last k/2 list. Then you have 2 sorted lists. Then simiply merge the lists.
# Analyze the time complexity.
# T(N) = 2 T(N/2) + N
# T(N) = O (N log N)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        ans = []
        for i in A:
            current = i
            while (current != None):
                ans.append((current.val, current))
                current = current.next
        ans = sorted(ans)
        # ans1 = []
        for i in range(len(ans) - 1):
            ans[i][1].next = ans[i + 1][1]
        return ans[0][1]


#####		Distinct Numbers In Window		#####

"""
You are given an array of N integers, A1, A2 ,…, AN and an integer K.
Return the of count of distinct numbers in all windows of size K.
Formally, return an array of size N-K+1 where i’th element in this array contains
number of distinct elements in sequence Ai, Ai+1 ,…, Ai+k-1.
Note:
 If K > N, return empty array.
 A[i] is a signed integer
For example,
A=[1, 2, 1, 3, 4, 3] and K = 3
All windows of size K are
[1, 2, 1]
[2, 1, 3]
[1, 3, 4]
[3, 4, 3]
So, we return an array [2, 3, 3, 2].
"""


# If you have solution for window [i, i+k-1], can you quickly build solution for window [i+1, i+k]?
# If we have a data structure where we can maintain count of all keys and number of distinct keys,
# then we just have to reduce count of key A[i] and increasing count of A[i+k].
# If count of some key has been reduced to zero, we need to remove that key.
# This structure is a hashmap. All operations that we have said a constant time in it.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        app = {}
        ans = []
        for x in range(B):
            if A[x] not in app:
                app[A[x]] = 1
            else:
                app[A[x]] += 1
        ans.append(len((app)))
        for x in range(B, len(A)):
            if A[x] in app:
                app[A[x]] += 1
            else:
                app[A[x]] = 1
            if app[A[x - B]] == 1:
                del app[A[x - B]]
            else:
                app[A[x - B]] -= 1
            ans.append(len(app))
        return ans


#########################	linked-lists	#########################


#####		Palindrome List		#####

"""
Given a singly linked list, determine if its a palindrome.
Return 1 or 0 denoting if its a palindrome or not, respectively.
Notes:
Expected solution is linear in time and constant in space.
For example,
List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.
"""


# To check palindrome, we just have to reverse latter half of linked list and then we can in (n/2)
# steps total can compare if all elements are same or not.
# For finding mid point, first we can in O(N) traverse whole list and calculate total number of elements.
# Reversing is again O(N).

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        slow = A
        fast = A
        prev_of_slow = None
        while fast and fast.next:
            prev_of_slow = slow
            slow = slow.next
            fast = fast.next.next

        if fast is None:
            prev_of_slow.next = None
        else:
            if prev_of_slow is not None:
                prev_of_slow.next = None
            mid = slow
            slow = slow.next

        # reverse the second half
        cur = slow
        prev = None
        while cur:
            fut = cur.next
            cur.next = prev
            prev = cur
            cur = fut

        first = A
        second = prev

        while first and second:
            if first.val != second.val:
                return 0
            first = first.next
            second = second.next

        return 1


#####		Partition List		#####

"""
Given a linked list and a value x, partition it such that all nodes less than x come before
 nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""


# Maintain 2 pointers - one which maintains all nodes less than x and another which
# maintains nodes greater than or equal to x.
# Keep going along our list. When we are at node that is greater than or equal to x,
# we remove this node from our list and move it to list of nodes greater than x.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        head1 = ListNode(0)  # handle for nodes < B
        head2 = ListNode(0)  # handle for nodes >= B
        node1, node2 = head1, head2
        while A:
            if A.val < B:
                node1.next, node1, A = A, A, A.next
            else:
                node2.next, node2, A = A, A, A.next
        # Link the two lists
        node1.next = head2.next
        # Clear last pointer
        node2.next = None
        return head1.next


#####		Add Two Numbers As Lists		#####

"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and
each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
    342 + 465 = 807
Make sure there are no trailing zeros in the output list
So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.
"""


# Very much the simulation of the mathematical process of summing up the numbers.
# You sum the digits and maintain a carry.
# Gotchas :
# 1) What if one list if shorter than the other ? 1->2 + 2->3->4->5
# 2) What if the answer has more digits ? 1 + 9

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        ptr1 = A
        ptr2 = B
        carry = 0
        while ptr1 and ptr2:
            sumi = carry + ptr1.val + ptr2.val
            ptr2.val = sumi % 10
            carry = sumi // 10
            prev = ptr2
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        if ptr1:
            prev.next = ptr1
            while ptr1:
                sumi = carry + ptr1.val
                ptr1.val = sumi % 10
                carry = sumi // 10
                prev = ptr1
                ptr1 = ptr1.next
        while ptr2:
            sumi = carry + ptr2.val
            ptr2.val = sumi % 10
            carry = sumi // 10
            prev = ptr2
            ptr2 = ptr2.next
        if carry != 0:
            prev.next = ListNode(carry)
        return B


#####		K Reverse Linked List		#####

"""
Given a singly linked list and an integer K, reverses the nodes of the
list K at a time and returns modified linked list.
 NOTE : The length of the list is divisible by K
Example :
Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,
You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5
Try to solve the problem using constant extra space.
"""


# Split the list into buckets of length K and then reverse each of them. After this you have to concatenate the buckets
# and return the list. To split the list into buckets of length K, use 2 pointers that are K elements afar.
# To reverse a linked list check this.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        cur = start = A  # cur tracks the current node, start marks the beg. of bucket
        n = 1  # counter to track current bucket size
        while cur:
            if n < B:
                n += 1
                next = cur.next
                if next:
                    cur.next = next.next
                    if start == A:
                        next.next = start
                        A = next
                        start = A
                    else:
                        next.next = start.next
                        start.next = next
            else:  # bucket full, reset the variables
                start = cur
                cur = cur.next
                n = 1
        return A


#####		List Cycle		#####

"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
Try solving it using constant additional space.
Example :
Input :
                  ______
                 |     |
                 \/    |
        1 -> 2 -> 3 -> 4
Return the node corresponding to node 3.
"""


# Lets now look at the starting point.
# If we were using hashing, the first repetition we get is the starting point. Simple!
# What happens with the 2 pointer approach ?
# Method 1 :
# If you detect a cycle, the meeting point is definitely a point within the cycle.
# Can you determine the size of the cycle ? ( Easy ) Let the size be k.
# Fix one pointer on the head, and another pointer to kth node from head.
# Now move them simulataneously one step at a time. They will meet at the starting point of the cycle.
# Method 2 :
# This might be slightly more complicated. It involves a bit of maths and is not as intuitive as method 1.
# Suppose the first meet at step k,the distance between the start node of list and the start node of cycle is s,
# and the distance between the start node of cycle and the first meeting node is m.
# Then
# 2k = (s + m + n1r)
# 2(s + m + n2r) = (s + m + n1r)
# s + m = nr where n is an integer.
# s = nr - m
# s = (r - m) + (n-1)r
# So, if we have one pointer on the head and another pointer at the meeting point. Note that since the distance
# between start node of cycle and the first meeting node is m, therefore if the pointer moves (r - m) steps,
# it will reach the start of the cycle. When the pointer at the head moves s steps, the second pointer moves
# (r-m) + (n-1)r steps which both points to the start of the cycle. In other words, both pointers meet
# first at the start of the cycle.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        if not A: return None
        slow = fast = A
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break

        if slow != fast: return None
        slow = A
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


#####		Remove Duplicates From Sorted List 2		#####

"""
Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.
For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""


# Skip the node where head->next != NULL && head->val == head->next->val. Maintain a “pre”
# ode which is the node just previous to the block of head you are checking.
# Make sure you take care of corner cases :
# 1) Do you handle repetitions at the end ? ex : 1 -> 1
# 2) Do you handle cases where there is just one element ? ex : 1
# 3) Do you handle cases where there is just one element repeated numerous times ? 1->1->1->1->1->1

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        curr = A
        head = prev = ListNode(None)
        head.next = curr
        while curr and curr.next:
            if curr.val == curr.next.val:
                while curr and curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # still one one of duplicate values left so advance
                curr = curr.next
                prev.next = curr
            else:
                prev = prev.next
                curr = curr.next
        return head.next


#####		Insertion Sort List		#####

"""
Sort a linked list using insertion sort.
We have explained Insertion Sort at Slide 7 of Arrays
Insertion Sort Wiki has some details on Insertion Sort as well.
Example :
Input : 1 -> 3 -> 2
Return 1 -> 2 -> 3
"""


# This is very much a simulation problem.
# The only trick is how do you move a node from ith position to jth position.
# How do you move the pointers to do so ? Would having a temporary node help ?

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def revert(node):
    """ Revert list in-place """
    prev = None
    while node:
        prev, node.next, node = node, prev, node.next
    return prev


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        """ This solution:
              * doesn't swap the values themselves
                  -> in Python it doesn't matter much,
                     but in general doing so would kind of defeat
                     one advantage of having a linked list
              * doesn't create new node
              * builds the output list in decreasing order
                  -> if input list is already sorted,
                     the complexity would be O(n)
        """
        source = A
        dest = None
        while source:
            prev = None
            node = dest
            # Find insertion point (between prev and node)
            while node and node.val > source.val:
                prev, node = node, node.next
            if prev is None:
                dest = source
            else:
                prev.next = source
            source.next, source = node, source.next
        return revert(dest)


#####		Rotate List		#####

"""
Given a list, rotate the list to the right by k places, where k is non-negative.
For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""


# Since n may be a large number compared to the length of list. So we need to know the length of linked list.
# After that, move the list after the (l-n % l )th node to the front to finish the rotation.
# Ex: {1,2,3} k = 2 Move the list after the 1st node to the front
# Ex: {1,2,3} k = 5, In this case Move the list after (3-5 % 3=1)st node to the front.
# So the code has three parts.
# 1) Get the length
# 2) Move to the (l-n%l)th node
# 3) Do the rotation

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        temp = A
        lent = 0
        while temp.next is not None:
            lent += 1
            temp = temp.next
        lent += 1
        final = temp
        temp.next = A
        temp1 = A
        B = B % lent
        for i in range(B):
            temp1 = temp1.next
        temp2 = A
        while temp1 != final:
            temp1 = temp1.next
            temp2 = temp2.next
        ans = temp2.next
        temp2.next = None
        return ans


#####		Reverse Link List 2		#####

"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.
For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,
return 1->4->3->2->5->NULL.
 Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list. Note 2:
Usually the version often seen in the interviews is reversing the whole linked list which is
obviously an easier version of this question.
"""


# If you are still stuck at reversing the full linked list problem,
# then would maintaining curNode, nextNode and a tmpNode help ?
# Maybe at every step, you do something like this :
#     tmp = nextNode->next;
#             nextNode->next = cur;
#             cur = nextNode;
#             nextNode = tmp;
# Now, lets say you did solve the problem of reversing the linked list and are stuck at applying it to current problem.
# What if your function reverses the linked list and returns the endNode of the list.
# You can simply do
# prevNodeOfFirstNode->next = everseLinkedList(curNode, n - m + 1);

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        cur_idx = 1
        cur_node = A
        pre_seg = seg_start = seg_end = None
        while cur_idx <= C:
            if cur_idx == B - 1:
                pre_seg = cur_node
            if cur_idx == B:
                seg_start = cur_node
            if cur_idx == C:
                seg_end = cur_node
            cur_idx += 1
            cur_node = cur_node.next

        cur_node = seg_start.next
        seg_start.next = seg_end.next
        if B != 1:
            pre_seg.next = seg_end
        else:
            A = seg_end

        pre_node = seg_start
        while pre_node != seg_end:
            pre_node, cur_node.next, cur_node = cur_node, pre_node, cur_node.next

        return A


#####		Sort List		#####

"""
Sort a linked list in O(n log n) time using constant space complexity.
Example :
Input : 1 -> 5 -> 4 -> 3
Returned list : 1 -> 3 -> 4 -> 5
"""


# Can implement either merge sort or qsort.
# Lets look at merge sort. Traverse the linked list to find the mid point of the list. Now sort the first half and
# second half separatly by calling the function on them. Then merge the 2 lists ( Note that we already
# have solved a problem to merge 2 lists ).

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(A, B):
    i = A;
    j = B
    # i is the pointer to the current node in A
    # j is the pointer to the current node in B
    first = None;
    last = None
    # first is the first node in the sorted list
    # last is the last node in the sorted list
    while i and j:
        # choose node with the minimum value, and update the current one
        if i.val < j.val:
            min_n = i;
            i = i.next
        else:
            min_n = j;
            j = j.next
        # update last and first
        if last is None:
            first = last = min_n
        else:
            last.next = min_n;
            last = min_n
    # extend the rest to the list
    while i:
        last.next = i;
        last = i;
        i = i.next
    while j:
        last.next = j;
        last = j;
        j = j.next
    last.next = None
    return first


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        if A is None or A.next is None:
            return A
        i = A;
        n = 0
        while i is not None:
            i = i.next;
            n += 1
        # now n = len(A)
        mid = A
        for t in range(n // 2 - 1):
            mid = mid.next
        B = mid.next
        mid.next = None
        return mergeTwoLists(self.sortList(A), self.sortList(B))


#####		Merging Two Sorted Lists		#####

"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.
For example, given following linked lists :
  5 -> 8 -> 20
  4 -> 11 -> 15
The merged list should be :
4 -> 5 -> 8 -> 11 -> 15 -> 20
"""


# First thing to note is that all you would want to do is modify the next pointers. You don’t need to create new nodes.
# At every step, you choose the minumum of the current head X on the 2 lists, and modify your answer’s next
# pointer to X. You move the current pointer on the said list and the current answer.
# Corner case,
# Make sure that at the end of the loop, when one of the list goes empty,
# you do include remaining elemnts from the second list into your answer.
# Test case : 1->2->3 4->5->6

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, head1, head2):
        """ Merges two sorted linked lists.
        Time complexity: O(max(n, m)). Space complexity: O(1),
        n, m are lengths of the linked lists.
        """
        dummy = ListNode(None)
        curr = dummy
        while head1 and head2:  # choose node with min value from two lists
            if head1.val <= head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
        if head1:  # list1 is longer, add whatever is left from it
            curr.next = head1
        elif head2:
            curr.next = head2
        return dummy.next


#####		Removing Duplicates From Sorted List		#####

"""
Given a sorted linked list, delete all duplicates such that each element appear only once.
For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""


# Skip the node where head->next != NULL && head->val == head->next->val.
# Make sure you take care of corner cases :
# 1) Do you handle repetitions at the end ? ex : 1 -> 1
# 2) Do you handle cases where there is just one element ? ex : 1
# 3) Do you handle cases where there is just one element repeated numerous times ? 1->1->1->1->1->1

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        head = A
        current = A
        next = current.next
        while current:
            while next and next.val == current.val:
                next = next.next
            current.next = next
            current = current.next
        return head


#####		Swap List Nodes In Pairs		#####

"""
Given a linked list, swap every two adjacent nodes and return its head.
For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.
Your algorithm should use only constant space. You may not modify the values in the list,
 only nodes itself can be changed.
"""


# Lets first look at the problem of swapping 2 nodes.
# Method 1: Just swap the values in the 2 nodes. In most cases, this won’t be a permissible solution.
# Method 2: Move around the pointers.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        head = A.next if A and A.next else A
        while A and A.next:
            C = A.next.next  # 3rd Node
            D = C.next if C and C.next else C  # 4th Node if existing
            A.next.next, A.next, A = A, D, C
        return head


#####		Remove Nth Node From List End		#####

"""
Given a linked list, remove the nth node from the end of list and return its head.
For example,
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
 Note:
If n is greater than the size of the list, remove the first node of the list.
Try doing it using constant additional space.
"""


# Obviously, since we do not have back pointers, reaching the end node and then making our way back is not an option.
# There are 2 approaches :
# 1) Find out the length of the list in one go. Then you know the number of node to be removed.
# Traverse to the node and remove it.
# 2) Make the first pointer go n nodes. Then move the second and first pointer simultaneously.
# This way, the first pointer is always ahead of the second pointer by n nodes. So when first pointer
# reaches the end, you are on the node to be removed.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, head, n):
        slow = fast = head
        count = 0
        while fast and count < n:
            fast = fast.next
            count = count + 1

        if fast is None:
            temp = head
            if head is not None:
                head = head.next
            temp = None
            return head
        prev_of_slow = None
        while slow and fast:
            prev_of_slow = slow
            slow = slow.next
            fast = fast.next

        prev_of_slow.next = slow.next
        slow = None
        return head


#####		Reverse Linked List 2		#####

"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.
For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,
return 1->4->3->2->5->NULL.
 Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list. Note 2:
Usually the version often seen in the interviews is reversing the whole linked list which is obviously an
easier version of this question
"""


# If you are still stuck at reversing the full linked list problem,
# then would maintaining curNode, nextNode and a tmpNode help ?
#
# Maybe at every step, you do something like this :
#
#     tmp = nextNode->next;
#             nextNode->next = cur;
#             cur = nextNode;
#             nextNode = tmp;
# Now, lets say you did solve the problem of reversing the linked list and are stuck at applying it to current problem.
# What if your function reverses the linked list and returns the endNode of the list.
# You can simply do
# prevNodeOfFirstNode->next = everseLinkedList(curNode, n - m + 1);

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        before = ListNode(None)
        before.next = A
        temp = A
        for _ in range(B - 1):
            before = before.next
            temp = temp.next
        firstToReverse = temp
        n = temp.next
        for _ in range(C - B):
            nn = n.next
            n.next = temp
            temp = n
            n = nn
        firstToReverse.next = n
        before.next = temp
        return A if B > 1 else before.next


#####		Reorder List		#####

"""
Given a singly linked list
    L: L0 → L1 → … → Ln-1 → Ln,
reorder it to:
    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
You must do this in-place without altering the nodes’ values.
For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""


# 1) Break the list from middle into 2 lists.
# 2) Reverse the latter half of the list.
# 3) Now merge the lists so that the nodes alternate.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, head):
        """ Modifies input linked list in-place. Returns head of a new list.
        Time complexity: O(n). Space complexity: O(1), n is len(linked list).
        """
        # modifiy the list only if it has more than one node
        if not head or not head.next:
            return head

        # find the middle of the list using slow and fast pointers algorithm
        prev = None  # last node of the left half of the list
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None  # detach left half of the list from the right half
        # reverse right half of the list
        prev = None
        curr = slow  # slow is the start of the right half
        while curr:
            link = curr.next
            curr.next = prev
            prev = curr
            curr = link
        # prev now points to the head of reversed right half
        # combine left and right half, attach it to dummy node
        dummy = ListNode(None)
        tail = dummy  # current tail of a new list
        while head:  # left list is always gonna be shorter
            link = head.next  # save link to the next node in the left list
            head.next = prev
            tail.next = head  # attach connected 2 nodes to the tail
            tail = prev  # update tail
            head = link  # move to the next node in left list
            prev = prev.next
        # if the length of the original list was odd, right half is gonna have
        # 1 node more than the left half
        if prev:
            tail.next = prev
        return dummy.next  # return new head


#########################	math	#########################


#####		Sum Of Pairwise Hamming Distance		#####

"""
Hamming distance between two non-negative integers is defined as the number of positions at
which the corresponding bits are different.
For example,
HammingDistance(2, 7) = 2, as only the first and the third bit
differs in the binary representation of 2 (010) and 7 (111).
Given an array of N non-negative integers, find the sum of hamming distances of all pairs of integers in the array.
Return the answer modulo 1000000007.
Example
Let f(x, y) be the hamming distance defined above.
A=[2, 4, 6]
We return,
f(2, 2) + f(2, 4) + f(2, 6) +
f(4, 2) + f(4, 4) + f(4, 6) +
f(6, 2) + f(6, 4) + f(6, 6) =
0 + 2 + 1
2 + 0 + 1
1 + 1 + 0 = 8
"""


# Suppose the given array contains only binary numbers, i.e A[i] belongs to [0, 1].
# Let X be the number of elements equal to 0, and Y be the number of elements equals to 1.
# Then, sum of hamming distance of all pair of elements equals 2XY, as every pair containing one
# element from X and one element from Y contribute 1 to the sum. (also order matters)
# As A[i] belongs to [0, 231 - 1] and we are counting number of different bits in each pair,
# we can consider all the 31 bit positions independent.
# For example:
# A = [2, 4, 6] = [0102, 1002, 1102]</p>
# At bit position 0 (LSB): x = 3, y = 0
# At bit position 1: x = 1, y = 2
# At bit position 2(MSB): x = 1, y = 2
# Total sum = number of pairs having different bit at each bit-position = (2 * 3 * 0) + (2 * 1 * 2) + (2 * 1 * 2) = 8
# Time complexity: O(N)
# Space complexity: O(1)

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
        n = len(A)
        c = 0
        m = max(A)
        for i in range(32):
            M = 1 << i  # Shifting bit for comparision
            d = 0
            for a in A:
                if M & a:  # Finding if ith bit is set or not
                    d += 1  # Counting such numbers
            c += (d * (n - d))  # (n-d) represents numbers whose ith bit is not set
            if m <= M:  # Ignoring if the 1 << i goes out of numbers range
                break
        return (2 * c) % 1000000007


#####		Sorted Permutation Rank With Repeats		#####

"""
Given a string, find the rank of the string amongst its permutations sorted lexicographically.
Note that the characters might be repeated. If the characters are repeated,
we need to look at the rank in unique permutations.
Look at the example for more details.
Example :
Input : 'aba'
Output : 2
The order permutations with letters 'a', 'a', and 'b' :
aab
aba
baa
The answer might not fit in an integer, so return your answer % 1000003
NOTE: 1000003 is a prime number
NOTE: Assume the number of characters in string < 1000003
"""


# Number of permutation with a character C as the first character = number of permutation possible with remaining
# N-1 character = (N-1)! / (p1! * p2! * p3! ... ) where p1, p2, p3 are the number of occurrences of repeated characters.
# For example, number of permutations possible with 3 ‘a’ and 3 ‘b’ is 6! / 3! 3! = 20
# Now, there is a slight problem.
# (N-1)! / (p1! * p2! * p3! ... ) does not necessarily fit in an integer. It is easy to calculate (N-1)! % MOD.
# However, how do we handle divisions ? Modular_multiplicative_inverse is what you are looking for.
# In short, (1/A) % MOD = A ^ (MOD - 2) % MOD

class Solution:
    # @param A : string
    # @return an integer
    def fact(self, n):
        if n <= 1:
            return 1
        else:
            return n * self.fact(n - 1)

    def findRank(self, A):
        res = 1
        char_occur = {}
        for char in A:
            char_occur[char] = char_occur.get(char, 0) + 1
        for i in range(0, len(A) - 1):
            rank = 0
            for j in range(i + 1, len(A)):
                if A[i] > A[j]:
                    rank += 1
            temp = self.fact(len(A) - i - 1) % 1000003
            temp1 = 1
            for key in char_occur.keys():
                temp1 *= self.fact(char_occur[key])
            temp1 = pow(temp1, 1000001, 1000003)
            res = (res + rank * temp1 * temp) % 1000003
            char_occur[A[i]] -= 1
        return res


#####		Excel Column Number		#####

"""
Given a column title as appears in an Excel sheet, return its corresponding column number.
Example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
"""


# Simple math.
# This is just like base 26 number conversion.
# number = 26^0 * (S[n - 1] - ‘A’ + 1) + 26^1 * (S[n - 2] - ‘A’ + 1) + ….

class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        T = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1, 27)))  # Elegantly done
        return sum(T[ch] * 26 ** i for i, ch in enumerate(A[::-1]))


#####		Convert Base		#####

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


print(numberToBase(10, 2))

#####		Palindrome Integer		#####

"""
Determine whether an integer is a palindrome. Do this without extra space.
A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
Negative numbers are not palindromic.
Example :
Input : 12121
Output : True
Input : 123
Output : False
"""

# Figure out how to extract digit at ith place using some mathematics without using extra space.
# Corner cases to consider:
# 1) Negative numbers
# 2) If you are thinking of converting the integer to string, note the restriction of using extra space.
# 3) Try reversing the integer.

import math


class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        rev = 0
        num = A
        while num > 0:
            temp = num % 10
            rev = rev * 10 + temp
            num = math.floor(num / 10)
        if A == rev:
            return 1
        else:
            return 0


#####		Grid Unique Paths		#####

"""
A robot is located at the top-left corner of an A x B grid (marked ‘Start’ in the diagram below).
Path Sum: Example 1
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).
How many possible unique paths are there?
Note: A and B will be such that the resulting answer fits in a 32 bit signed integer.
Example :
Input : A = 2, B = 2
Output : 2
2 possible routes : (0, 0) -> (0, 1) -> (1, 1)
              OR  : (0, 0) -> (1, 0) -> (1, 1)
"""

# Note that you have to take m + n - 2 steps in total. You have to take (m - 1)
# steps going down and (n-1) steps going right. Can you relate this to combinatorics?
# Let 0 denote a down step and 1 denote a right step.
# So we need to find out the number of strings of length m + n - 2 which have exactly m - 1 zeroes and n - 1 ones.
# Essentially we need to choose the positions of ‘1s’, and then ‘0s’ fall into the remaining positions.
# So, the answer becomes Choose(m+n-2, n - 1).

from math import factorial


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        return int(factorial(A + B - 2) / (factorial(A - 1) * factorial(B - 1)))

    def uniquePath_dp(self, A, B):
        numPaths = [[1 for j in range(B)] for i in range(A)]
        for i in range(1, A):
            for j in range(1, B):
                numPaths[i][j] = numPaths[i - 1][j] + numPaths[i][j - 1]
        return numPaths[-1][-1]


#####		Sorted Permutation Rank		#####

"""
Given a string, find the rank of the string amongst its permutations sorted lexicographically.
Assume that no characters are repeated.
Example :
Input : 'acb'
Output : 2
The order permutations with letters 'a', 'c', and 'b' :
abc
acb
bac
bca
cab
cba
The answer might not fit in an integer, so return your answer % 1000003
"""


# If the first character is X, all permutations which had the first character less than X would
# come before this permutation when sorted lexicographically.
# Number of permutation with a character C as the first character =
# number of permutation possible with remaining N-1 character = (N-1)!
# rank = number of characters less than first character * (N-1)! + rank of permutation
# of string with the first character removed
# Example
# Lets say out string is “VIEW”.
# Character 1 : 'V'
# All permutations which start with 'I', 'E' would come before 'VIEW'.
# Number of such permutations = 3! * 2 = 12
# Lets now remove ‘V’ and look at the rank of the permutation ‘IEW’.
# Character 2 : ‘I’
# All permutations which start with ‘E’ will come before ‘IEW’
# Number of such permutation = 2! = 2.
# Now, we will limit our self to the rank of ‘EW’.
# Character 3:
# ‘EW’ is the first permutation when the 2 permutations are arranged.
# So, we see that there are 12 + 2 = 14 permutations that would come before "VIEW".
# Hence, rank of permutation = 15.

class Solution:
    # @param A : string
    # @return an integer
    def fact(self, n):
        if n <= 1:
            return 1
        else:
            return n * self.fact(n - 1)

    def findRank(self, A):
        res = 1
        for i in range(0, len(A) - 1):
            rank = 0
            for j in range(i + 1, len(A)):
                if A[i] > A[j]:
                    rank += 1
            res = (res + rank * self.fact(len(A) - i - 1)) % 1000003
        return res


#####		Fizzbuzz		#####

"""
Given a positive integer A, return an array of strings with all the integers from 1 to N.
But for multiples of 3 the array should have “Fizz” instead of the number.
For the multiples of 5, the array should have “Buzz” instead of the number.
For numbers which are multiple of 3 and 5 both, the array should have “FizzBuzz” instead of the number.
Look at the example for more details.
Example
A = 5
Return: [1 2 Fizz 4 Buzz]
"""


# While Iterating from 1 to N, you need to check the following conditions in sequence:
#
# Check whether the number is divisible by 3 and 5, if that is the case, print FizzBuzz.
# Check whether the number is divisible by 3, in that case, print Fizz.
# Next, check whether the number is divisible by 5, in that case print Buzz.
# Otherwise, print the number.
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        ans = [i for i in range(1, A + 1)]
        for i in range(2, A, 3):
            ans[i] = "Fizz"
        for i in range(4, A, 5):
            ans[i] = "Buzz"
        for i in range(14, A, 15):
            ans[i] = "FizzBuzz"
        return ans

    def fizzBuzz_iterative(self, A):
        sol = []
        for i in range(1, A + 1):
            if i % 3 == 0 and i % 5 == 0:
                sol.append("FizzBuzz")
            elif i % 3 == 0:
                sol.append("Fizz")
            elif i % 5 == 0:
                sol.append("Buzz")
            else:
                sol.append(i)
        return sol


#####		Reverse Integer		#####

"""
Reverse digits of an integer.
Example1:
x = 123,
return 321
Example2:
x = -123,
return -321
Return 0 if the result overflows and does not fit in a 32 bit signed integer
"""


# Here are some good questions to ask before coding.
# If the integer’s last digit is 0, what should the output be? ie, cases such as 10, 100.
# Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse
# of 1000000003 overflows. How should you handle such cases?
# Tips:
# 1) num % 10 gives you the last digit of a number.
# 2) num / 10 gives you the number after removing the last digit.
# 3) num * 10 + digit appends the digit at the end of the number.

class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        if int(A) > 0:
            k = int(str(A)[::-1])
            return k * (k < 2 ** 31)
        else:
            k = -1 * int(str(A)[1:][::-1])
            return k * (k > -2 ** 31)

    def reverse_another(self, A):
        sgn = -1 if A < 0 else 1
        A = abs(A)
        string = str(A)
        reverse = string[::-1]
        result = int(reverse)
        if result > 2 ** 31 - 1:
            return 0
        return sgn * result


s = Solution()
print(s.reverse("1000000003"))

#####		Rearrange Array		#####

"""
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.
Example:
Input : [1, 0]
Return : [0, 1]
 Lets say N = size of the array. Then, following holds true :
All elements in the array are in the range [0, N-1]
N * N does not overflow for a signed integer
"""


# If you had extra space to do it, the problem will be very easy.
# Store a copy of Arr in B.
# And then for every element, do Arr[i] = B[B[i]]
# Lets restate what we just said for extra space :
# If we could somehow store 2 numbers in every index ( that is, Arr[i] can contain the old value and the new value
# somehow ), then the problem becomes very easy.
# NewValue of Arr[i] = OldValue of Arr[OldValue of Arr[i]]
# Now, we will do a slight trick to encode 2 numbers in one index.
# This trick assumes that N * N does not overflow.
# 1) Increase every Array element Arr[i] by (Arr[Arr[i]] % n)*n.
# 2) Divide every element by N.
# Given a number as
#    A = B + C * N   if ( B, C < N )
#    A % N = B
#    A / N = C
# We use this fact to encode 2 numbers into each element of Arr.

class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):
        n = len(A)
        for i in range(n):
            A[i] += (A[A[i]] % n) * n
        for i in range(n):
            A[i] = A[i] // n


#####		Largest Coprime Divisor		#####

"""
You are given two positive numbers A and B. You need to find the maximum valued integer X such that:
X divides A i.e. A % X = 0
X and B are co-prime i.e. gcd(X, B) = 1
For example,
A = 30
B = 12
We return
X = 5
"""


# We know A is the greatest number dividing A. So if A and B are coprime, we can return the value of X to be A.
# Else, we can try to remove the common factors of A and B from A.
# We can try to remove the common factors of A and B from A by finding the greatest common divisor
# (gcd) of A and B and dividing A with that gcd.
# Mathematically, A = A / gcd(A, B) —— STEP1
# Now, we repeat STEP1 till we get gcd(A, B) = 1.
# Atlast, we return X = A

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, A, B):
        while True:
            A1 = A
            B1 = B
            # Find gcd
            while B1 > 0:
                A1, B1 = B1, A1 % B1
            if A1 == 1:
                return A
            A = A // A1
        return A


#####		Excel Column Title		#####

"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""


# Think of it like this.
# How would you convert a number to binary ?
# Can you apply the same principle here now that the base is different ?

class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        result = []
        while A > 0:
            bit_val = A % 26  # Reduce max possible from A
            if bit_val == 0:
                bit_val = 26
            A = (A - bit_val) // 26  # Each time it is getting 26, 26**2, 26**3 ...
            result.append(chr(bit_val + 64))
        return ''.join(reversed(result))


#####		Number Of Length N And Value Less Than K		#####

"""
Given a set of digits (A) in sorted order, find how many numbers of
length B are possible whose value is less than number C.
 NOTE: All numbers can only have digits from the given set.
Examples:
    Input:
    0 1 5
    1
    2
    Output:
    2 (0 and 1 are possible)
    Input:
    0 1 2 5
    2
    21
    Output:
    5 (10, 11, 12, 15, 20 are possible)
Constraints:
    1 <= B <= 9, 0 <= C <= 1e9 & 0 <= A[i] <= 9
"""


# Find solution of each cases separately.
# Case 1 : When B is greater than length of C
# Case 2: When B is smaller than length of C
# Case 3: When B is equal to length of C.
# For case 3:
# Let First(i) denote number formed by taking first i digits of C
# Then try to find a relation between solution of (A, i, first(i)) and (A, i - 1, first(i - 1)) for i = 1 to i <= B
# Let us try to solve for all the possible cases.
# Let d be size of A, B is the length, C is the max number
# Case 1: If B is greater than length of C or d is 0 then no such number is possible.
# Case 2: If B is smaller than length of C then ALL the possible combination of digits of length B are valid.
# Generate all such B digit numbers.
# For the first position we can’t have 0 and for the rest of (B - 1) position we can have all d possible digits.
# Hence, Answer = d*B if A contains 0 else (d-1) * ( d )(B-1)
# Case 3: If B is equal to length of C
# Construct digit array of C ( call it as digit[]).
# Let First(i) be a number formed by taking first i digits of it.
# Let lower[i] denote number of elements in A which are smaller than i.
# It can be easily computed by idea similar to prefix sum.
# For example:
# First(2) of 423 is 42.
# If  A =  [ 0, 2] then lower[0] = 0, lower[1]  = 1,  lower[2] = 1, lower[3] = 2
# Generate B digit numbers by dynamic programming. Let say dp[i] denotes the total numbers of length
# i which are less than first i digits of C.


class Solution:
    def count(self, A, B, b, i):
        if i >= len(b) or B == 0:
            return 1
        c_max = int(b[i])
        rt = 0
        for x in A:
            if i == 0 and x == 0 and B != 1:
                continue
            if x > c_max:
                continue
            if x == c_max:
                if i >= len(b) - 1:
                    continue
                rt = rt + self.count(A, B - 1, b, i + 1)
            else:
                rt = rt + len(A) ** (B - 1)
        return rt

    def solve(self, A, B, C):
        c = str(C)
        if len(c) < B:
            return 0

        ind = 0
        if len(c) == B:
            return self.count(A, B, c, 0)
        rt = 0
        for x in A:
            if x == 0 and B != 1:
                continue
            if x == 0 and x < C:
                rt += 1
            else:
                rt = rt + len(A) ** (B - 1)
        return rt


#####		Power Of Two Integers		#####

"""
Given a positive integer which fits in a 32 bit signed integer,
find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.
Example
Input : 4
Output : True
as 2^2 = 4.
"""


# Lets look at the number of valid possibilities for A^B.
# For B = 2, number of possibilities = sqrt(INT_MAX) = sqrt(2^31 - 1) < 2^16.
# For B = 3, number of possibilities = INT_MAX**1/3 < 2^11
# For B = 4, number of possibilities = INT_MAX**1/4 < 2^8
# .
# .
# For B = 32, number of possibilities = 0
# ( Not considering 1 as its considered in the first case, and 2^32 exceeds INT_MAX ).
# So, the total number of possibilities are less than 10^5.
# Now, we just need to iterate on these possibilities and see if we find X = A^B.
# Take extra care to make sure there are no overflows.

class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        from math import log, sqrt
        if A == 1:
            return 1
        for i in range(2, int(sqrt(A)) + 1):
            # For each i it will check if A can be represented as a power of 2, 3, 4, 5 ...
            x = round(log(A, i), 5)  # Returns rounded to 5 decimals places
            if x % 1 == 0:  # If not modulo, it is a power
                return 1
        return 0


s = Solution()
print(s.isPower(27))

#####		Prime Sum		#####

"""
Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.
NOTE A solution will always exist. read Goldbach’s conjecture
Example:
Input : 4
Output: 2 + 2 = 4
If there are more than one solutions possible, return the lexicographically smaller solution.
If [a, b] is one solution with a <= b,
and [c,d] is another solution with c <= d, then
[a, b] < [c, d]
If a < c OR a==c AND b < d.
"""

# This problem’s solution is straight forward.
# Generate prime numbers less than N, and hash them in a list.
# Then iterate on the whole list, and for every prime P, check if N-P is also prime.
# If you find such a pair, you are done :)
# Coming to the problem of generating prime numbers quickly, we already have a problem SIEVE where we did it.
# However, re-iterating, there are multiple ways of doing it. Probably the easiest way is Sieve of Erastothenes.

import math


class Solution:
    def primesum(self, n: int) -> 'List[int]':
        is_prime = [True] * (n + 1)
        is_prime[0], is_prime[1] = False, False

        # Sieve of Erastothenes for constructing map of primes
        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime[i]:
                for j in range(i * 2, n + 1, i):
                    is_prime[j] = False

        for i in range(2, n):
            if is_prime[i] and is_prime[n - i]:  # Found a prime pair
                return [i, n - i]
        return []


s = Solution()
print(s.primesum(5))

#####		Trailing Zeroes In Factorial		#####

"""
Given an integer n, return the number of trailing zeroes in n!.
Note: Your solution should be in logarithmic time complexity.
Example :
n = 5
n! = 120
Number of trailing zeros = 1
So, return 1
"""


# For given number 4617.
# 5^1 : 4617 ÷ 5 = 923.4, so we get 923 factors of 5
# 5^2 : 4617 ÷ 25 = 184.68, so we get 184 additional factors of 5
# 5^3 : 4617 ÷ 125 = 36.936, so we get 36 additional factors of 5
# 5^4 : 4617 ÷ 625 = 7.3872, so we get 7 additional factors of 5
# 5^5 : 4617 ÷ 3125 = 1.47744, so we get 1 more factor of 5
# 5^6 : 4617 ÷ 15625 = 0.295488, which is less than 1, so stop here.
# Therefore, 4617! has 923 + 184 + 36 + 7 + 1 = 1151 trailing zeroes.

class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        # Zero is formed by 2*5.
        # No. of 2's always > No. of 5's in factorial of a number.
        # Therefore, counting the No. of 5's gives the number of trailing zeros
        # If A < 5 then its factorial doesn't have any trailing zeros
        if A < 5:
            return 0
        count = 0
        i = 5
        while (A // i > 0):
            count += A // i
            i *= 5
        return count


#####		City Tour		#####

"""
There are A cities numbered from 1 to A. You have already visited M cities,
the indices of which are given in an array B of M integers.
If a city with index i is visited, you can visit either the city with index i-1 (i >= 2) or the city with
index i+1 (i < A) if they are not already visited.
Eg: if N = 5 and array M consists of [3, 4], then in the first level of moves, you can either visit 2 or 5.
You keep visiting cities in this fashion until all the cities are not visited.
Find the number of ways in which you can visit all the cities modulo 10^9+7.
Input Format
The 1st argument given is an integer A, i.e total number of cities.
The 2nd argument given is an integer array B, where B[i] denotes ith city you already visited.
Output Format
Return an Integer X % (1e9 + 7), number of ways in which you can visit all the cities.
Constraints
1 <= A <= 1000
1 <= M <= A
1 <= B[i] <= A
For Example
Input:
    A = 5
    B = [2, 5]
Output:
    6
Explanation:
    All possible ways to visit remaining cities are :
    1. 1 -> 3 -> 4
    2. 1 -> 4 -> 3
    3. 3 -> 1 -> 4
    4. 3 -> 4 -> 1
    5. 4 -> 1 -> 3
    6. 4 -> 3 -> 1
"""

# Brute force solution for this would create a graph and do BFS for all possible
# combinations to visit all cities. But this will result in a timeout.
# This question is simple if you understand how we are dividing the cities.
# Let’s say we start with (a_1, a_2, a_3,…, a_k) as visited cities. Let all cities be (1,2,…,n).
# Also, let’s denote cities between a_i and a_i+1 as X_i. Here, X_0 denotes cities before the first visited city.
# X_k denotes unvisited cities after a_k.
# Now there are total n-k unvisited cities. We can visit them in (n-k)! ways.
# We can not visit cities between a_i and a_i+1 in all possible ways for all i’s. We have counted all
# permutations in (n-k)!. So, we need to divide it with X_i for all i’s.
# This will lead to the expression (n-k)!/(X_0! * X_1! * … *X_k!).
# There are more than one way of visiting cities between the two visited cities. Precisely, there are 2^(X_i-1) ways
# to visit for all i. Thus we need to multiply with X_i’s.
# Here we need to remember that there is only one way to visit X_0 and X_k.
# The final formula becomes ((n-k)!/(X_0!X_2!…X_(k-1)!) )(2^(X_1 -1 + X_2 - 1 + X_3 - 1 + … + X_(k-1)-1))
# The same solution is present as the editorial for this question. You have to remember that
# ((X_0 + X_1)C(X_1))((X_0+X_1+X_3)C(X_3))….((n-k)C(X_k)) is same as ((n-k)!/(X_0!X_2!…*X_(k-1)!) ).

import sys

sys.setrecursionlimit(5000)


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def calc_combs(self, L1, C1, L2, C2, memo):
        return C1 * C2 * self.fact(L1 + L2, memo) // (self.fact(L1, memo) * self.fact(L2, memo))

    def fact(self, n, memo):
        if n in memo: return memo[n]
        if n <= 1: return 1
        v = self.fact(n - 1, memo) * n
        memo[n] = v
        return v

    def solve(self, A, B):
        if not B: return 0
        mod = 1000000007
        memo = {}
        B = sorted(B)

        # 1...B[0] has 1 possible placements of length B[0] - 1
        length, combinations = B[0] - 1, 1

        for i in range(1, len(B)):
            if B[i - 1] == B[i]: continue
            if B[i - 1] + 1 == B[i]: continue
            l = (B[i] - B[i - 1] - 1) % mod
            c = (1 << (l - 1)) % mod
            combinations = self.calc_combs(length, combinations, l, c, memo) % mod
            length += l

        # B[-1]...A has 1 possible placements of length A - B[-1]
        return self.calc_combs(length, combinations, A - B[-1], 1, memo) % mod


#####		Greatest Common Divisor		#####

"""
Given 2 non negative integers m and n, find gcd(m, n)
GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
Both m and n fit in a 32 bit signed integer.
Example
m : 6
n : 9
GCD(m, n) : 3
"""


# Lets say g is gcd(m, n) and m > n.
# m = g * m1
# n = g * m2
# m - n = g * (m1 - m2)
# gcd (m, n) = gcd(m-n, n)
# gcd (m, n) = gcd(m-n, n)
#            = gcd(m - 2n, n) if m >= 2n
#            = gcd(m - 3n, n) if m >= 3n
#              .
#              .
#              .
#            = gcd(m - k*n, n) if m >= k*n
# In other words, we keep subtracting n till the result is greater than 0. Ultimately we will end up with m % n.
# So gcd(m, n)  = gcd(m % n, n)


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if B > A:
            A, B = B, A
        while B != 0:
            temp = B
            B = A % B
            A = temp
        return A


#########################	stacks-and-queues	#########################


#####		Simplify Directory Path		#####

"""
Given a string A representing an absolute path for a file (Unix-style).
Return the string A after simplifying the absolute path.
Note:
Absolute path always begin with ’/’ ( root directory ).
Path will not have whitespace characters.
Input Format
The only argument given is string A.
Output Format
Return a string denoting the simplified absolue path for a file (Unix-style).
For Example
Input 1:
    A = "/home/"
Output 1:
    "/home"
Input 2:
    A = "/a/./b/../../c/"
Output 2:
    "/c"
"""


# More of a simulation problem.
# Break the string along ‘/’ and process the substrings in order one by one. ‘..’
# indicates popping an entry unless there is nothing to pop.

class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        dirs = A.split('/')
        result = []
        for c in dirs:
            if c == '' or c == '.':
                continue
            elif c == '..':
                if len(result) > 0: result.pop()
            else:
                result.append(c)
        return '/' + '/'.join(result)


#####		Sliding Window Maximum		#####

"""
Given an array of integers A. There is a sliding window of size B which
is moving from the very left of the array to the very right.
You can only see the w numbers in the window. Each time the sliding window moves
rightwards by one position. You have to find the maximum for each window.
The following example will give you more clarity.
The array A is [1 3 -1 -3 5 3 6 7], and B is 3.
Window position	        Max
———————————-	        ————————-
[1 3 -1] -3 5 3 6 7	    3
1 [3 -1 -3] 5 3 6 7	    3
1 3 [-1 -3 5] 3 6 7	    5
1 3 -1 [-3 5 3] 6 7	    5
1 3 -1 -3 [5 3 6] 7	    6
1 3 -1 -3 5 [3 6 7]	    7
Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1].
Note: If B > length of the array, return 1 element with the max of the array.
Input Format
The first argument given is the integer array A.
The second argument given is the integer B.
Output Format
Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1]
For Example
Input 1:
    A = [1, 3, -1, -3, 5, 3, 6, 7]
    B = 3
Output 1:
    C = [3, 3, 5, 5, 6, 7]
"""


# Approach 1 :
# The obvious brute force solution with run time complexity of O(nw) is definitely not efficient enough.
# Every time the window is moved, you have to search for a total of w elements in the window.
# Approach 2:
# A heap data structure quickly comes to mind. We could boost the run time to approximately O(n lg w)
# (Note that I said approximately because the size of the heap changes constantly and averages about w).
# Insert operation takes O(lg w) time, where w is the size of the heap. However, getting the maximum value is cheap,
# it merely takes constant time as the maximum value is always kept in the root (head) of the heap.
# As the window slides to the right, some elements in the heap might not be valid anymore (range is outside of
# the current window). How should you remove them? You would need to be somewhat careful here. Since you only
# remove elements that are out of the window’s range, you would need to keep track of the elements’ indices too.
# TIme complexity : O ( n log n ). Not good enough.
# Approach 3 :
# A double-ended queue should do the trick here.
# The double-ended queue is the perfect data structure for this problem. It supports insertion/deletion from the front
# and back. The trick is to find a way such that the largest element in the window would always appear in the front of
# the queue. How would you maintain this requirement as you push and pop elements in and out of the queue?
# You might notice that there are some redundant elements in the queue that we shouldn’t even consider about.
# For example, if the current queue has the elements: [10 5 3], and a new element in the window has the element 11.
# Now, we could have emptied the queue without considering elements 10, 5, and 3, and insert only element 11
# into the queue. A natural way most people would think is to try to maintain the queue size the same as the window’s
# size. Try to break away from this thought and try to think outside of the box. Removing redundant elements and
# storing only elements that need to be considered in the queue is the key to achieve the efficient O(n) solution.

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        if B >= len(A):
            return [max(A)]

        result = [0] * (len(A) - B + 1)
        deque = []

        for i in range(len(A)):
            if deque and deque[0] == i - B:
                del deque[0]
            while deque and A[deque[-1]] < A[i]:
                del deque[-1]
            deque.append(i)
            if i + 1 >= B:
                result[i - B + 1] = A[deque[0]]

        return result


#####		Evaluate Expression		#####

"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.
Input Format
The only argument given is character array A.
Output Format
Return the value of arithmetic expression formed using reverse Polish Notation.
For Example
Input 1:
    A =   ["2", "1", "+", "3", "*"]
Output 1:
    9
Explaination 1:
    starting from backside:
    *: ( )*( )
    3: ()*(3)
    +: ( () + () )*(3)
    1: ( () + (1) )*(3)
    2: ( (2) + (1) )*(3)
    ((2)+(1))*(3) = 9

Input 2:
    A = ["4", "13", "5", "/", "+"]
Output 2:
    6
Explaination 2:
    +: ()+()
    /: ()+(() / ())
    5: ()+(() / (5))
    1: ()+((13) / (5))
    4: (4)+((13) / (5))
    (4)+((13) / (5)) = 6
"""


# This is pretty much a simulation problem.
# Think stack.
# When you encounter an operator is when you need the top 2 numbers on the stack,
# perform the operation on them and put them on the stack.

class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = []
        group = {'+': 1, '-': 2, '*': 3, '/': 4}

        def sumi(a, b):
            return a + b

        def sub(a, b):
            return b - a

        def mul(a, b):
            return int(a * b)

        def div(a, b):
            return int(b / a)

        for i in range(len(A)):
            if A[i] not in group:
                stack.append(A[i])
            else:
                val = group[A[i]]
                a = int(stack.pop())
                b = int(stack.pop())
                if val == 1:
                    stack.append(sumi(a, b))
                elif val == 2:
                    stack.append(sub(a, b))
                elif val == 3:
                    stack.append(mul(a, b))
                elif val == 4:
                    stack.append(div(a, b))
        return stack[0]


#####		Min Stack		#####

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) – Push element x onto stack.
pop() – Removes the element on top of the stack.
top() – Get the top element.
getMin() – Retrieve the minimum element in the stack.
Note that all the operations have to be constant time operations.
Questions to ask the interviewer :
Q: What should getMin() do on empty stack?
A: In this case, return -1.
Q: What should pop do on empty stack?
A: In this case, nothing.
Q: What should top() do on empty stack?
A: In this case, return -1
 NOTE : If you are using your own declared global variables, make sure to clear them out in the constructor.
"""


# Lets look at solution number 1.
#
# What if you maintained 2 queues. One which stored the actual stack of element,
# and the other which stored the minimum of elements.
# So when pushing new element,
# min = min(top of minimum stack, current value) which is pushed to minimum stack.
# However, this uses 2N memory.
# Can you think of slight optimizations to this ?
# What if you maintained the current minimum in a variable and only stored the places
# where the minimum changes or the element is same as the minimum.
# pop() becomes a little trickier in such a case.
# You only pop() from the min stack if the top() of min stack is same as the current minimum.
# Space complexity : O(N + X) where X = number of places where minimum changes or the element is same as the minimum

class MinStack:
    stack = []
    minimums = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        if len(self.stack) == 0:
            self.stack.append(x)
            self.minimums.append(x)
        else:
            self.stack.append(x)
            if x < self.minimums[-1]:
                self.minimums.append(x)
            else:
                self.minimums.append(self.minimums[-1])

    # @return nothing
    def pop(self):
        if len(self.stack) != 0:
            self.stack.pop()
            self.minimums.pop()

    # @return an integer
    def top(self):
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack[-1]

    # @return an integer
    def getMin(self):
        if len(self.stack) == 0:
            return -1
        else:
            return self.minimums[-1]

    def __init__(self):
        self.stack = []
        self.minimums = []


#####		Nearest Smallest Element		#####

"""
Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.
More formally,
    G[i] for an element A[i] = an element A[j] such that
    j is maximum possible AND
    j < i AND
    A[j] < A[i]
Elements for which no smaller element exist, consider next smaller element as -1.
Input Format
The only argument given is integer array A.
Output Format
Return the integar array G such that G[i] contains nearest smaller number than A[i].If no such element occurs G[i] should be -1.
For Example
Input 1:
    A = [4, 5, 2, 10, 8]
Output 1:
    G = [-1, 4, -1, 2, 2]
Explaination 1:
    index 1: No element less than 4 in left of 4, G[1] = -1
    index 2: A[1] is only element less than A[2], G[2] = A[1]
    index 3: No element less than 2 in left of 2, G[3] = -1
    index 4: A[3] is nearest element which is less than A[4], G[4] = A[3]
    index 4: A[3] is nearest element which is less than A[5], G[5] = A[3]
Input 2:
    A = [3, 2, 1]
Output 2:
    [-1, -1, -1]
Explaination 2:
    index 1: No element less than 3 in left of 3, G[1] = -1
    index 2: No element less than 2 in left of 2, G[2] = -1
    index 3: No element less than 1 in left of 1, G[3] = -1
"""


# Naive Solution O(N^2)
#
# A naive solution would be to take a nested loop, and for every element keep
# iterating back till we find a smaller element.
# This can be O(N^2) in worst case.
# Better solution hint
# The naive solution would look something like :
#   for i = 0 to size(A):
#     G[i] = -1
#     for j = i - 1 to 0:
#         if A[j] < A[i]:
#             G[i] = A[j]
#             break
# Now look at A[i-1]. All elements with index smaller than i - 1 and greater than A[i-1]
# are useless to us because they would never qualify for G[i], G[i+1], ...
# Can you use the above fact to come up with a solution ?
# Hint : Stack
# Using the above fact, we know that we only need previous numbers in descending order.
# The pseudocode would look something like :
# 1) Create a new empty stack st
# 2) Iterate over array `A`,
#    where `i` goes from `0` to `size(A) - 1`.
#     a) We are looking for value just smaller than `A[i]`. So keep popping from
#     `st` till elements in `st.top() >= A[i]` or st becomes empty.
#     b) If `st` is non empty, then the top element is our previous element. Else the previous element does not exist.
#     c) push `A[i]` onto st

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, array):
        """ Time complexity: O(n). Space complexity: O(n), n is len(array).
        """
        stack = []
        result = []
        for num in array:
            # see of there's integer smaller than num in the stack
            while stack and stack[-1] >= num:
                stack.pop()
            if stack:  # found the smaller integer
                result.append(stack[-1])
            else:  # stack is empty, smaller integer wasn't found
                result.append(-1)
            stack.append(num)  # push current num to the stack
        return result


#####		Largest Rectangle In Histogram		#####

"""
Given an array of integers A of size N. A represents a histogram i.e A[i] denotes height of
the ith histogram’s bar. Width of each bar is 1.
Largest Rectangle in Histogram: Example 1
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
Largest Rectangle in Histogram: Example 2
The largest rectangle is shown in the shaded area, which has area = 10 unit.
Find the area of largest rectangle in the histogram.
Input Format
The only argument given is the integer array A.
Output Format
Return the area of largest rectangle in the histogram.
For Example
Input 1:
    A = [2, 1, 5, 6, 2, 3]
Output 1:
    10
    Explanation 1:
        The largest rectangle is shown in the shaded area, which has area = 10 unit.
"""


# Whats the brute force approach here?
#
# We know that the height of the largest rectange will be one of the heights of the histogram (Think about why?)
# If that is the case, we can iterate on all the histograms, and for each histogram H, we try to create the maximum
# rectange with H as the height.
# To do that, we keep going left L and right R till we encounter a histogram with height less than H.
# Now, (R - L - 1) * H is one of the possibilities for the largest rectangle.
# Doing this for all the histograms will give us the right solution.
# Following is a rough pseudocode for the approach mentioned above :
# max_rectangle = 0
# for index = 0 to all_histograms.length
#   H = all_histograms[index]
#   L = index, R = index
#   while L >= 0 AND all_histograms[L] >= H
#     L = L - 1
#   while R < all_histograms.length AND all_histograms[R] >= H
#     R = R + 1
#   max_rectangle = MAX(max_rectangle, (R - L - 1) * H)
# return max_rectangle
# This approach is however O(N^2) time complexity in the worst case. How can we do better than this approach?
# Hint : Think in terms of using a stack ?
# As discussed in the previous hint, height of the maximum rectangle will be height of one of the histograms.
# For each histogram H, we need to know index of the first smaller (smaller than H) bar on left of H (lets call it L)
# and index of first smaller bar on right of H.
# We already tried the brute force approach. How can we do better?
# Important observation:
# Lets consider 2 consecutive histograms H[i] and H[i+1]. Lets assume H[i+1] < H[i]
# In such a case, for all histograms X with index > i + 1 when traversing left for L, there is no point looking
# at H[i] after looking at H[i+1]. If H[i+1] > X, obviously H[i] > X as we already know H[i] > H[i+1]
# Then, whats the next entry we would want to look at? We would want to look at the first histogram
# left of H[i+1] with height less than H[i+1].
# Can you think of a stack based approach based on the above observation?

class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        stack = []
        result = 0

        i = 0
        while i < len(A):
            if not stack or A[stack[-1]] <= A[i]:
                stack.append(i)
                i += 1
            else:
                tp = stack.pop()
                tmp = A[tp] * (i - stack[-1] - 1 if stack else i)
                if result < tmp:
                    result = tmp

        while stack:
            tp = stack.pop()
            tmp = A[tp] * (i - stack[-1] - 1 if stack else i)
            if result < tmp:
                result = tmp

        return result


#####		Redundant Braces		#####

"""
Given a string A denoting an expression. It contains the following operators ’+’, ‘-‘, ‘*’, ‘/’.
Chech whether A has redundant braces or not.
Return 1 if A has redundant braces, else return 0.
Note: A will be always a valid expression.
Input Format
The only argument given is string A.
Output Format
Return 1 if string has redundant braces, else return 0.
For Example
Input 1:
    A = "((a + b))"
Output 1:
    1
    Explanation 1:
        ((a + b)) has redundant braces so answer will be 1.
Input 2:
    A = "(a + (a + b))"
Output 2:
    0
    Explanation 2:
        (a + (a + b)) doesn't have have any redundant braces so answer will be 0.
"""


# If we somehow pick out sub-expressions surrounded by ( and ),
# then if we are left with () as a part of the string, we know we have redundant braces.
# Lets take an example:
# (a+(a+b))
# We keep pushing elements onto the stack till we encounter ')'.
# When we do encounter ')', we start popping elements till we find a matching '('.
# If the number of elements popped do not correspond to '()', we are fine and we can move forward.
# Otherwise, voila! Matching braces have been found.
# Some Extra Hints:
# Try to run your code on test cases like (a*(a))  and (a) ??

class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = []
        for i in range(len(A)):
            if A[i] in '(+-/*':
                stack.append(A[i])
            elif A[i] == ')':
                if stack.pop() == '(':
                    return 1
                stack.pop()
        return 0


#####		Rain Water Trapped		#####

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
Input Format
The only argument given is integer array A.
Output Format
Return the total water it is able to trap after raining..
For Example
Input 1:
    A = [0,1,0,2,1,0,1,3,2,1,2,1]
Output 1:
    6
Explaination 1: <img src="http://i.imgur.com/0qkUFco.png">
    In this case, 6 units of rain water (blue section) are being trapped.
"""


# instead of calculating area by height*width, we can think it in a cumulative way. In other words,
# sum water amount of each bin(width=1). Search from left to right and maintain a max height of left
# and right separately, which is like a one-side wall of partial container. Fix the higher one and flow water
# from the lower part. For example, if current height of left is lower, we fill water in the left bin.
# Until left meets right, we filled the whole container.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        # Visits each element of the array A twice
        # (stacking and popping).
        # If the stack is implemented in a more basic
        # form and stack[0] is not a fast operation,
        # we could store the current maximal element
        # separately.
        stack = []
        water = 0
        for a in A:
            if stack and stack[0] <= a:
                h = stack[0]
                while stack:
                    water += h - stack.pop()
            stack.append(a)
        h = stack.pop()
        while stack:
            n = stack.pop()
            if n > h:
                h = n
                continue
            water += h - n
        return water


A = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

s = Solution()
print(s.trap(A))

#########################	strings	#########################


#####		Compare Version Numbers		#####

"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1,
If version1 < version2 return -1,
otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the
second first-level revision.
Here is an example of version numbers ordering:
0.1 < 1.1 < 1.2 < 1.13 < 1.13.4
"""


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        a = list(map(int, A.split('.')))
        x = len(a)
        b = list(map(int, B.split('.')))
        y = len(b)
        # Make length of both the version equal
        while x > y:
            b.append(0)
            y += 1
        while y > x:
            a.append(0)
            x += 1
        # Now it is just a simple comparison
        if a > b:
            return 1
        if a < b:
            return -1
        return 0


#####		Add Binary Strings		#####

"""
Given two binary strings, return their sum (also a binary string).
Example:
a = "100"
b = "11"
Return a + b = “111”
"""


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, x, y):

        max_len = max(len(x), len(y))
        x = x.zfill(max_len)  # zfill is useful here
        y = y.zfill(max_len)

        result = ''
        carry = 0

        for i in range(max_len - 1, -1, -1):
            r = carry
            r += 1 if x[i] == '1' else 0
            r += 1 if y[i] == '1' else 0
            result = ('1' if r % 2 == 1 else '0') + result
            carry = 0 if r < 2 else 1

        if carry != 0: result = '1' + result
        return result.zfill(max_len)


#####		Valid Ip Address		#####

"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255.
The numbers cannot be 0 prefixed unless they are 0.
Example:
Given “25525511135”,
return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)
"""


# Essentially you have to place 3 dots in the given string.
# Try out all the possible combinations for the 3 dots.
# Corner case:
# 25011255255
# 25.011.255.255 is not valid as 011 is not valid.
# 25.11.255.255 is not valid either as you are not allowed to change the string.
# 250.11.255.255 is valid.

def solve(i, s, count, stack, ans):
    if i == len(s):
        return False

    if count == 3:
        if 0 <= int(s[i:]) <= 255:
            if len(s[i:]) > 1 and s[i:][0] == '0':
                return False
            bo = []
            for j in stack:
                bo.append(j)

            bo.append(s[i:])
            ans.append('.'.join(bo))

        return False

    st = ''
    for i in range(i, len(s)):
        st += s[i]
        if 0 <= int(st) <= 255:
            if len(st) > 1 and st[0] == '0':
                return False
            stack.append(st)
            z = solve(i + 1, s, count + 1, stack, ans)
            if z == False:
                stack.pop(-1)

    return False


class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        i = 0
        s = A
        count = 0
        stack = []
        ans = []
        solve(i, s, count, stack, ans)
        ans.sort()
        return ans


IP = "25525511135"
s = Solution()
print(s.restoreIpAddresses(IP))

#####		Amazing Subarrays		#####

"""
You are given a string S, and you have to find all the amazing substrings of S.
Amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).
Input
Only argument given is string S.
Output
Return a single integer X mod 10003, here X is number of Amazing Substrings in given string.
Constraints
1 <= length(S) <= 1e6
S can have special characters
Example
Input
    ABEC
Output
    6
Explanation
    Amazing substrings of given string are :
    1. A
    2. AB
    3. ABE
    4. ABEC
    5. E
    6. EC
    here number of substrings are 6 and 6 % 10003 = 6.
"""


# The main idea to solve this problem is to traverse the string and when you encounter a vowel,
# add ( length(string) - position_of_curr_char ) to the answer.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        ans = 0
        for i in range(len(A)):
            if A[i] in vowels:
                ans = ans + (len(A) - i) % 10003
        return ans % 10003


#####		Length Of Last Word		#####

"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.
Example:
Given s = "Hello World",
return 5 as length("World") = 5.
Please make sure you try to solve this problem without using library functions.
Make sure you only traverse the string once.
"""


# How can you detect the end of the string?
# How can you detect where the word begins?
# What if you maintained the length of the current word?
# You reset the length of the word when the next word begins (When does a new word begin?)
# Return the last length you have.

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        counter = 0
        if A == "":
            return 0
        else:
            for c in A[::-1]:
                if c == " ":
                    if counter != 0:
                        return counter
                else:
                    counter += 1
            return counter


#####		Valid Number		#####

"""
Note: It is intended for some problems to be ambiguous. You should gather all requirements up front before implementing one.
Please think of all the corner cases and clarifications yourself.
Validate if a given string is numeric.
Examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
Clarify the question using “See Expected Output”
Is 1u ( which may be a representation for unsigned integers valid?
For this problem, no.
Is 0.1e10 valid?
Yes
-01.1e-10?
Yes
Hexadecimal numbers like 0xFF?
Not for the purpose of this problem
3. (. not followed by a digit)?
No
Can exponent have decimal numbers? 3e0.1?
Not for this problem.
Is 1f ( floating point number with f as prefix ) valid?
Not for this problem.
How about 1000LL or 1000L ( C++ representation for long and long long numbers )?
Not for this problem.
How about integers preceded by 00 or 0? like 008?
Yes for this problem
"""


# This is a brute force problem with lot of corner cases. You need to properly figure them out before coding.
# Some of them includes dealing with numbers having different signs.
# To start with, make sure you skip the whitespaces.
# Then ignore the ‘+’ or ‘-‘ sign.
# Scan the following string till you find numbers and ‘.’ and confirm at least one digit, less than one ‘.’
# and the string not ending with ‘.’.
# Now the remaining string could have ‘e’ followed by a number.
# Confirm if the next character is ‘e’, then again repeat the process of skipping the sign and looking for digits.

class Solution:
    # @param A : string
    # @return an integer
    def isNumber(self, A):
        while len(A) > 0 and A[0] == ' ':
            A = A[1:]
        A = A[::-1]
        while len(A) > 0 and A[0] == ' ':
            A = A[1:]
        A = A[::-1]
        if len(A) == 0:
            return 0
        for c in A:
            if c not in [str(i) for i in range(10)] + ['.', 'e', '-', '+']:
                return 0
        if 'e' in A:
            A = A.split('e')
            if len(A) != 2:
                return 0
            return int(self.isnum(A[0], 0) and self.isnum(A[1], 1))
        return int(self.isnum(A, 0))

    def isnum(self, A, i):
        # print(A,i)
        if A == '':
            return False
        if i == 1 or (i == 0 and '.' not in A):
            if A[0] in ['+', '-']:
                A = A[1:]
            if A == '':
                return False
            for c in A:
                if c not in [str(i) for i in range(10)]:
                    return False
            return True
        A = A.split('.')
        return (self.isnum(A[0], 1) or A[0] == '') and self.isnum(A[1], 1)

    def isNumber_re(self, A):
        import re
        p = re.compile(r"^\s*[+-]?\d+(\.\d+)?(e[-+]?\d+)?\s*$")
        if (p.match(A)):
            return 1
        p = re.compile(r"^\s*[+-]?\.\d+(e[-+]?\d+)?\s*$")
        if (p.match(A)):
            return 1
        return 0


s = Solution()
print(s.isNumber_re("2e10"))

#####		Min Char Required To Make String Palen		#####

"""
Given an string A. The only operation allowed is to insert characters in the beginning of the string.
Find how many minimum characters are needed to be inserted to make the string a palindrome string.
Input Format
The only argument given is string A.
Output Format
Return the minimum characters that are needed to be inserted to make the string a palindrome string.
For Example
Input 1:
    A = "ABC"
Output 1:
    2
    Explanation 1:
        Insert 'B' at beginning, string becomes: "BABC".
        Insert 'C' at beginning, string becomes: "CBABC".
Input 2:
    A = "AACECAAAA"
Output 2:
    2
    Explanation 2:
        Insert 'A' at beginning, string becomes: "AAACECAAAA".
        Insert 'A' at beginning, string becomes: "AAAACECAAAA".
"""


# Each index of LPS array contains the longest prefix which is also a suffix. Now take the string and reverse of a
# string and combine them with a sentinal character in between them and compute the LPS array of this combined string.
# Now take the last value of the LPS array and subtract it with the length of the original string, This will give us
# the minimum number of insertions required in the begining of the string .

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        count = 0
        while A != A[::-1]:
            A = A[:-1]  # Remove the last char
            count += 1
        return count


s = Solution()
print(s.solve("AAABCA"))

#####		Longest Palindromic Substring		#####

"""
Given a string S, find the longest palindromic substring in S.
Substring of string S:
S[i...j] where 0 <= i <= j < len(S)
Palindrome string:
A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.
Incase of conflict, return the substring which occurs first ( with the least starting index ).
Example :
Input : "aaaabaaa"
Output : "aaabaaa"
"""


# A common mistake:
#
# Some people will be tempted to come up with a quick solution,
# which is unfortunately flawed (however can be corrected easily):
#  Reverse S and become S’. Find the longest common substring between S and S’,
#  which must also be the longest palindromic substring.
# This seemed to work, let’s see some examples below.
# For example,
# S = “caba”
# S’ = “abac”
# The longest common substring between S and S’ is “aba”, which is the answer.
# Let’s try another example:
# S = “abacdfgdcaba”
# S’ = “abacdgfdcaba”
# The longest common substring between S and S’ is “abacd”. Clearly, this is not a valid palindrome.
# We could see that the longest common substring method fails when there exists a reversed copy of a
# non-palindromic substring in some other part of S. To rectify this, each time we find a longest common
# substring candidate, we check if the substring’s indices are the same as the reversed substring’s original
# indices. If it is, then we attempt to update the longest palindrome found so far; if not,
# we skip this and find the next candidate.
# This gives us a O(N2) DP solution which uses O(N2) space (could be improved to use O(N) space).
# Please read more about Longest Common Substring here.
# Brute force solution, O(N3):
# The obvious brute force solution is to pick all possible starting and ending positions for a substring,
# and verify if it is a palindrome. There are a total of C(N, 2) such substrings (excluding the
# trivial solution where a character itself is a palindrome).
# Since verifying each substring takes O(N) time, the run time complexity is O(N3).
# Dynamic programming solution, O(N2) time and O(N2) space:
# To improve over the brute force solution from a DP approach, first think how we can avoid unnecessary
# re-computation in validating palindromes. Consider the case “ababa”. If we already knew that “bab” is a
# palindrome, it is obvious that “ababa” must be a palindrome since the two left and right end letters are the same.
# Stated more formally below:
# Define P[ i, j ] ← true iff the substring Si … Sj is a palindrome, otherwise false.
# Therefore,
# P[ i, j ] ← ( P[ i+1, j-1 ] and Si = Sj )
# The base cases are:
# P[ i, i ] ← true
# P[ i, i+1 ] ← ( Si = Si+1 )
# This yields a straight forward DP solution, which we first initialize the one and two letters palindromes,
# and work our way up finding all three letters palindromes, and so on…
# Can you come up with a O(N^2) time complexity and O(1) space solution ?
# A simpler approach, O(N2) time and O(1) space:
# In fact, we could solve it in O(N2) time without any extra space.
# We observe that a palindrome mirrors around its center.
# Therefore, a palindrome can be expanded from its center, and there are only 2N-1 such centers.
# You might be asking why there are 2N-1 but not N centers?
# The reason is that the center of a palindrome can be in between two letters.
# Such palindromes have even number of letters (such as “abba”) and their center are between the two ‘b’s.
# Since expanding a palindrome around its center could take O(N) time, the overall complexity is O(N2).

class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        n = len(A)
        if n <= 1:
            return A
        cs = 2 * n - 1
        ans = ''
        for c in range(cs):
            i = int(c / 2)  # Elegantly done
            j = i
            if c % 2 != 0:  # Using different i and j for palindrome center with 2 characters
                i = i + 1
            while i < n and j >= 0 and A[i] == A[j]:
                if len(ans) < i - j + 1:
                    ans = A[j:i + 1]
                i += 1
                j -= 1

        return ans


s = Solution()
print(s.longestPalindrome("aaaabaaa"))

#####		Stringholics		#####

"""
You are given an array A consisting of strings made up of the letters ‘a’ and ‘b’ only.
Each string goes through a number of operations, where:
1.	At time 1, you circularly rotate each string by 1 letter.
2.	At time 2, you circularly rotate the new rotated strings by 2 letters.
3.	At time 3, you circularly rotate the new rotated strings by 3 letters.
4.	At time i, you circularly rotate the new rotated strings by i % length(string) letters.
Eg: String is "abaa"
1.	At time 1, string is "baaa", as 1 letter is circularly rotated to the back
2.	At time 2, string is "aaba", as 2 letters of the string "baaa" is circularly rotated to the back
3.	At time 3, string is "aaab", as 3 letters of the string "aaba" is circularly rotated to the back
4.	At time 4, string is again "aaab", as 4 letters of the string "aaab" is circularly rotated to the back
5.	At time 5, string is "aaba", as 1 letters of the string "aaab" is circularly rotated to the back
After some units of time, a string becomes equal to it’s original self.
Once a string becomes equal to itself, it’s letters start to rotate from the first letter again (process resets). So,
if a string takes t time to get back to the original, at time t+1 one letter will be rotated and the string will be
it’s original self at 2t time.
You have to find the minimum time, where maximum number of strings are equal to their original self.
As this time can be very large, give the answer modulo 109+7.
Note: Your solution will run on multiple test cases so do clear global variables after using them.
Input:
A: Array of strings.
Output:
Minimum time, where maximum number of strings are equal to their original self.
Constraints:
1 <= size(A) <= 10^5
1 <= size of each string in A <= 10^5
Each string consists of only characters 'a' and 'b'
Summation of length of all strings <= 10^7
Example:
Input
A: [a, ababa, aba]
Output
4
String 'a' is it's original self at time 1, 2, 3 and 4.
String 'ababa' is it's original self only at time 4. (ababa => babaa => baaba => babaa => ababa)
String 'aba' is it's original self at time 2 and 4. (aba => baa => aba)
Hence, 3 strings are their original self at time 4.
"""


# The number of bits being rotated for each string goes in the series 1,1+2,1+2+3,1+2+3+4 etc.
# So for the ith operation, (i*(i+1))/2 bits are rotated.
# Find the smallest i for which you get the same string.
# Strings with same lengths may have different answers depending on the string.
# String 1010 takes 3 operations, while string 1001 takes 7 operations.
# But there is a catch, this wont always give you the minimum number of operations.
# Its possible that during rotation, you can get the original string before the number of bits
# rotated is a multiple of LEN.
# Example: S=> 100100
# Here, in 2 operations, we get the original string back.
# This takes place because the string is made up of recurring substrings.
# Assume string A to be 100
# S => AA
# Hence, over here our length S of string is the length of recurring substring A,
# so N*(N+1)/2 should be a multiple of length of A.
# Length of recurring substring can easily be found out using KMP algorithm in O(N) time complexity for each string.
# Find the minimum number of operations for each string, and take the LCM of all these values to get the answer.
# Handling of overflow for LCM should be handled by breaking the number down into factors, and then
# taking LCM (Not needed for languages that don’t have integer limit).
# Hence total time complexity is O(N).

class Solution:
    def gcd(self, A, B):
        if B > A:
            A, B = B, A
        if B == 0:
            return A
        return self.gcd(B, A % B)

    def solve(self, A):
        ans = 1
        for k in A:
            for i in range(1, 1000000000):
                if ((i * (i + 1)) // 2) % len(k) == 0:
                    ans = ((ans * i) // self.gcd(ans, i))
                    break
        return ans % 1000000007


#####		Implement Strstr		#####

"""
Please Note:
Another question which belongs to the category of questions which are intentionally stated vaguely.
Expectation is that you will ask for correct clarification or you will state your assumptions before you start coding.
Implement strStr().
 strstr - locate a substring ( needle ) in a string ( haystack ).
Try not to use standard library string functions for this question.
Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
 NOTE: Good clarification questions:
What should be the return value if the needle is empty?
What if both haystack and needle are empty?
For the purpose of this problem, assume that the return value should be -1 in both cases
"""


# Let us first think about a simpler problem. How do you find out if 2 strings are equal?
# Implementing strstr is just plain simple simulation.
# Consider every index i for the answer. Find if the following 2 strings are equal:
# 1) Needle string and,
# 2) String haystack from index i with length the same as needle’s length
# Note that the complexity of this solution is O(M*N) where M is length of haystack and N is length of needle.
# If you are feeling more adventurous, try solving it in O(M).
# *Hint: KMP Algorithm**

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        if len(A) == 0 or len(B) == 0:
            return -1
        if len(A) == len(B) and B == A:
            return 0
        for i in range(len(A) - len(B)):
            # print(A[i:len(B)+i],B)
            if A[i:i + len(B)] == B:
                return i
        return -1


#####		Palindrome String		#####

"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Example:
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""


# This is a fairly simple question.
# You need to maintain 2 pointers, one from the beginning and one from the end.
# At every iteration, after skipping the non alphanumeric characters, both the characters should match.


class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        end = len(A) - 1
        start = 0
        if not A:
            return 1
        while start < end:
            if A[start].isalnum() and A[end].isalnum():
                ast = A[start].lower()
                aen = A[end].lower()
                if ast != aen:
                    return 0
                else:  # One more matching pair processed
                    start += 1
                    end -= 1
            elif not A[start].isalnum():
                start += 1
            elif not A[end].isalnum():
                end -= 1
        return 1


#####		Roman To Integer		#####

"""
Given a string A representing a roman numeral.
Convert A into integer.
A is guaranteed to be within the range from 1 to 3999.
Input Format
The only argument given is string A.
Output Format
Return an integer which is the integer verison of roman numeral string.
For Example
Input 1:
    A = "XIV"
Output 1:
    14
Input 2:
    A = "XX"
Output 2:
    20
"""


# Note how the number XVI(10+5+1) and XIV(10-1+5) differs.
# In one case we are adding the numeric value of a letter and in other case we are subtracting it.
# How can you simulate this?
# The key is to notice that in a valid Roman numeral representation the letter
# with the most value always occurs at the start of the string.
# Whenever a letter with lesser value precedes a letter of higher value,
# it means its value has to be added as negative of that letter’s value. In all other cases, the values get added.

class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        # I V X  L  C   D   M
        # 1 5 10 50 100 500 1000
        d = {}
        d['I'] = 1
        d['V'] = 5
        d['X'] = 10
        d['L'] = 50
        d['C'] = 100
        d['D'] = 500
        d['M'] = 1000
        n = len(A)
        r = 0
        if n == 0:
            return 0
        if n == 1:
            return d[A[0]]
        for i in range(1, n):
            a = d[A[i - 1]]
            b = d[A[i]]
            if a >= b:  # If the last digit was bigger
                r += a
            else:
                r -= a
        r += d[A[n - 1]]  # Adding the final digit
        return r


#####		Justify Text		#####

"""
Given an array of words and a length L, format the text such that each line has
exactly L characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
Pad extra spaces ‘ ‘ when necessary so that each line has exactly L characters.
Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words, the empty slots
on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.
Your program should return a list of strings, where each string represents a single line.
Example:
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.
Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.
"""


# This problem is more of simulation. Take care of some of corner cases like space distribution in different lines.
# Corner Cases:
# 1) A line other than the last line might contain only one word. What should you do in this case?
# In this case, that line should be left-justified.
# 2) Have you noticed that the last line is an exception in terms of spaces?
# This is more of a simulation problem. The more elegant your code, the less chances of it being bug prone,
# and more marks in the interview.
# Give a lot of thought to the structure of the code before you start coding.

class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def splitWords(self, words, curr, L):
        if len(words) == 1:
            return words[0] + " " * (L - curr)
        to_all = (L - curr) // (len(words) - 1)
        additional = (L - curr) % (len(words) - 1)
        res = words.pop(0)

        for word in words:
            res += " " * (to_all + 1)
            if additional > 0:
                res += " "
                additional -= 1
            res += word
        return res

    def fullJustify(self, A, B):
        result = []
        curr = 0
        tmp = []
        for word in A:
            if not word:
                continue
            if curr + len(word) <= B:
                curr += len(word) + 1
                tmp.append(word)
            else:
                result.append(self.splitWords(tmp, curr - 1, B))
                tmp = [word]
                curr = len(word) + 1
        if curr:
            result.append(' '.join(tmp) + ' ' * (B - curr + 1))
        return result


s = Solution()
print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))

#####		Pretty Json		#####

"""
Given a string A representing json object. Return an array of string denoting json object with proper indentation.
Rules for proper indentation:
Every inner brace should increase one indentation to the following lines.
Every close brace should decrease one indentation to the same line and the following lines.
The indents can be increased with an additional ‘\t’
Note:
[] and {} are only acceptable braces in this case.
Assume for this problem that space characters can be done away with.
Input Format
The only argument given is the integer array A.
Output Format
Return a list of strings, where each entry corresponds to a single line. The strings should not have "\n" character.
For Example
Input 1:
    A = "{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}"
Output 1:
    {
        A:"B",
        C:
        {
            D:"E",
            F:
            {
                G:"H",
                I:"J"
            }
        }
    }
Input 2:
    A = ["foo", {"bar":["baz",null,1.0,2]}]
Output 2:
   [
        "foo",
        {
            "bar":
            [
                "baz",
                null,
                1.0,
                2
            ]
        }
    ]
"""


# This is more of a parsing problem.
# Make sure you take a lot of time thinking about the corner cases and structure of the code before you start coding.
# Fixing corner cases on the fly can make your code really ugly.
# Note the following:
# 1) ‘{‘, ‘[’ have the same effect on the printing
# 2) ‘}’, ‘]’ have the same effect as well
# 3) ‘:’ and ‘,’ are the only other 2 characters that matter.
# Think about the behavior when you encounter the following characters.
# Also think about the behavior based on the following character.

class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        indent = 0
        res = []
        line = ''
        for x in A:
            if x in '{[':
                if line:
                    res.append(line)
                res.append('\t' * indent + x)
                line = ''
                indent += 1
            elif x in ']}':
                if line:
                    res.append(line)
                indent -= 1
                line = '\t' * indent + x  # Might be followed by ','
            else:
                if not line:
                    line = '\t' * indent
                line += x
                if x == ",":
                    res.append(line)
                    line = ''
        if line:
            res.append(line)
        return res


s = Solution()
print(s.prettyJSON('{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}'))

#####		Count And Say		#####

"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11.
11 is read off as two 1s or 21.
21 is read off as one 2, then one 1 or 1211.
Given an integer n, generate the nth sequence.
Note: The sequence of integers will be represented as a string.
Example:
if n = 2,
the sequence is 11
"""


# You need to figure out how the new sequence is constructed from old sequence by counting contiguous same numbers.

class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        if A <= 0:
            return ''
        seq = '1'
        for n in range(1, A):
            prev = seq
            seq = ''  # As new seq would be created
            count = 1
            for i in range(1, len(prev)):  # Length of prev sequence
                if prev[i] == prev[i - 1]:
                    count += 1
                else:
                    seq += str(count) + prev[i - 1]
                    count = 1
            seq += str(count) + prev[-1]
        return seq


#####		Multiply Strings		#####

"""
Given two numbers represented as strings, return multiplication of the numbers as a string.
 Note: The numbers can be arbitrarily large and are non-negative.
Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer.
For example,
given strings "12", "10", your answer should be “120”.
NOTE : DO NOT USE BIG INTEGER LIBRARIES ( WHICH ARE AVAILABLE IN JAVA / PYTHON ).
We will retroactively disqualify such submissions and the submissions will incur penalties.
"""


class Solution:
    # @param A : string
    # @param B : string
    # @return a string = A*B
    def multiply(self, A, B):
        # School multiplication implemented
        # max no. of digits result can have
        ans = ['0'] * (len(A) + len(B) + 1)
        pos = 0  # rightmost in ans at curr level
        for i in range(len(B)):
            k = int(B[-(i + 1)])
            carr = 0  # carry
            pos -= 1  # putting a cross on right
            for j in range(len(A)):
                temp = k * int(A[-(j + 1)]) + int(ans[pos - j]) + carr
                ans[pos - j] = str(temp % 10)
                carr = temp / 10
            ans[pos - len(A)] = str(carr)
        ret = ''.join(ans).lstrip('0')
        if ret == '':
            ret = '0'
        return ret


#####		Integer To Roman		#####

"""
Please Note:
Another question which belongs to the category of questions which are intentionally stated vaguely.
Expectation is that you will ask for correct clarification or you will state your assumptions before you start coding.
Given an integer A, convert it to a roman numeral, and return a string corresponding to its roman numeral version
 Note : This question has a lot of scope of clarification from the interviewer. Please take a moment to think of all
 the needed clarifications and see the expected response using “See Expected Output” For the purpose of this question,
 https://projecteuler.net/about=roman_numerals has very detailed explanations.
Input Format
The only argument given is integer A.
Output Format
Return a string denoting roman numeral version of A.
Constraints
1 <= A <= 3999
For Example
Input 1:
    A = 5
Output 1:
    "V"
Input 2:
    A = 14
Output 2:
    "XIV"
"""


# It is very much like learning our own number system.
# All you need to know is how to write 0-9, 10, 20, 30, 40, .. 90, 100, 200, 300,… 900, 1000, 2000, 3000.
# You can derive rest of the numbers using the above.

class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        s = ""
        num = A
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        i = 0
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        while num > 0:
            for x in range(num // val[i]):
                s = s + syb[i]  # Add roman
                num = num - val[i]  # Reduce integer
            i = i + 1  # Controls the steps
        return s


#####		Power Of Two		#####

"""
Find if Given number is power of 2 or not.
More specifically, find if given number can be expressed as 2^k where k >= 1.
Input:
number length can be more than 64, which mean number can be greater than 2 ^ 64 (out of long long range)
Output:
return 1 if the number is a power of 2 else return 0
Example:
Input : 128
Output : 1
"""


# There is no shortcut to this problem.
# We need to divide the number by 2 till it is greater than 1.
# At any point, if the last digit is odd, then the number is not a power of 2.
# Lets see how we would implement division by 2.
# The division process is just the simulation of human division process.
# Start from the first digit. If the current digit is less than 2,
# then we append the next digit to current digit, and append 0 to our answer.

class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        n = int(A)
        if n == 1:
            return 0
        if n & (n - 1) == 0:  # That's cool
            return 1
        else:
            return 0

    def power_bin(self, A):
        m = bin(int(A))  # convert A to binary
        if m.count('1') == 1 and m[len(m) - 1] != '1':  # check if occurence is 1 and also last digit not equal to 1
            return 1
        else:
            return 0


#####		Zigzag String		#####

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P.......A........H.......N
..A..P....L....S....I...I....G
....Y.........I........R
And then read line by line: PAHNAPLSIIGYIR
Write the code that will take a string and make this conversion given a number of rows:
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
**Example 2 : **
ABCD, 2 can be written as
A....C
...B....D
and hence the answer would be ACBD.
"""


# Just look at simply simulating what is being told in the problem.
# Follow the simple steps:
# You need to maintain numRows number of strings S[numRows].
# And then populating string S in each row in zigzag fashion.
# Finally concatenate S[0] .. S[numRows-1] to get the answer.

class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, n):
        if len(A) == 1:
            return A
        ans = {}
        j = 0
        down = True
        for i in range(0, len(A)):
            ans[j] = ans.get(j, []) + [A[i]]  # Gets [] if key doesn't exist
            if down:
                j += 1
            else:
                j -= 1
            if j == n - 1:  # Time to change direction
                down = False
            if j == 0:  # Time to change direction
                down = True
        temp = []
        for i in ans:
            for j in ans[i]:
                temp.append(j)
        x = "".join(temp)
        return x


#####		Reverse The String		#####

"""
Given a string A.
Return the string A after reversing the string word by word.
NOTE:
A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.
Input Format
The only argument given is string A.
Output Format
Return the string A after reversing the string word by word.
For Example
Input 1:
    A = "the sky is blue"
Output 1:
    "blue is sky the"
Input 2:
    A = "this is ib"
Output 2:
    "ib is this"
"""


# One simple approach is a two-pass solution:
# First pass to split the string by spaces into an array of words
# Then second pass to extract the words in reversed order
# We can do better in one-pass. While iterating the string in reverse order,
# we keep track of a word’s beginning and end position.
# When we are at the beginning of a word, we append it.

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        flag = 0
        for i in range(len(A)):
            if A[i] == " ":
                flag = 1
                break
        if flag == 0:
            return A
        start = 0
        last = 0
        s = ""
        while last < len(A):
            if A[last] == " ":  # Found a word between start and last
                start += 1
                last += 1
                if last == len(A) - 1 and A[last] != " ":
                    s = A[start:last + 1] + " " + s
            if A[last] != " ":
                last += 1
                if last < len(A):
                    if A[last] == " ":
                        s = A[start:last] + " " + s
                        start = last  # For the next word
                        continue
                    if last == len(A) - 1:
                        s = A[start:last + 1] + " " + s
        return s[:len(s) - 1]

    def solve_easy(self, a):
        l = a.split()
        l.reverse()
        return ' '.join(l)


s = Solution()
print(s.solve("the sky is blue"))

#####		Atoi		#####

"""
Implement atoi to convert a string to an integer.
Example :
Input : "9 2704"
Output : 9
Note: There might be multiple corner cases here. Clarify all your doubts using “See Expected Output”.
Questions: Q1. Does string contain whitespace characters before the number?
A. Yes Q2. Can the string have garbage characters after the number?
A. Yes. Ignore it. Q3. If no numeric character is found before encountering garbage characters, what should I do?
A. Return 0. Q4. What if the integer overflows?
A. Return INT_MAX if the number is positive, INT_MIN otherwise.
"""


# We only need to handle four cases:
# Discards all leading whitespaces
# Sign of the number
# Overflow
# Invalid input
# Detecting overflow gets tricky. You need to detect overflow before the number is about to overflow. So:
# If the number is positive and the current number is greater than MAX_INT/10,
# and you are about to append a digit, then certainly your number will overflow.
# If the current number = MAX_INT / 10, then based on the last digit, we can detect if the number will overflow.

class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        sign = 1
        j = 0

        # Process potential spaces
        # Note: using the string "strip" method makes a copy
        # which we prefer to avoid to save memory
        while j < len(A) and A[j] == " ":
            j += 1

        # If there are only spaces, return 0
        if j == len(A):
            return 0

        # Process potential +/- sign
        if A[j] == "+":
            j += 1
        elif A[j] == '-':
            j += 1
            sign = -1

        # Process digits
        start = j
        while j < len(A) and A[j] in map(str, range(10)):  # or use .isnumeric()
            j += 1

        # If there are no digits, return 0
        if start == j:
            return 0

        r = sign * int(A[start:j])
        return max(-2147483648, min(r, 2147483647))


s = Solution()
print(s.atoi("9 2704"))
print(s.atoi(" 000191 3483AUBER1"))

#####		Longest Common Prefix		#####

"""
Given the array of strings A,
you need to find the longest string S which is the prefix of ALL the strings in the array.
Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.
For Example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".
Input Format
The only argument given is an array of strings A.
Output Format
Return longest common prefix of all strings in A.
For Example
Input 1:
    A = ["abcdefgh", "aefghijk", "abcefgh"]
Output 1:
    "a"
    Explanation 1:
        Longest common prefix of all the strings is "a".
Input 2:
    A = ["abab", "ab", "abcd"];
Output 2:
    "ab"
    Explanation 2:
        Longest common prefix of all the strings is "ab".
"""


# You can pick any random string from the array and start checking its characters from the beginning in order to see
# if they can be a part of the common substring.

class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, words):
        min_word = min(words, key=lambda word: len(word))
        n = len(min_word)  # Smallest word
        m = len(words)  # Total words

        for i in range(n):
            for j in range(m):
                if words[j][i] != min_word[i]:
                    return min_word[:i]  # Return whatever is matched
        return min_word  # Return the full word


#########################	tree	#########################


#####		Two Sum Binary Tree		#####

"""
Given a binary search tree T, where each node contains a positive integer, and an integer K, you have to find whether
or not there exist two different nodes A and B such that A.value + B.value = K.
Return 1 to denote that two such nodes exist. Return 0, otherwise.
Notes
Your solution should run in linear time and not take memory more than O(height of T).
Assume all values in BST are distinct.
Example :
Input 1:
T :       10
         / \
        9   20
K = 19
Return: 1
Input 2:
T:        10
         / \
        9   20
K = 40
Return: 0
"""


# How would you solve with O(N) memory? Let’s say you are given a sorted array and you need to find two indices i < j,
# such that A[i] = A[j]. Can you relate between a sorted array and a BST? Can you avoid O(N) memory
# and do with O(height) memory?
# If you do inorder traversal of BST you visit elements in increasing order. So, we use a two pointer approach,
# where we keep two pointers pt1 and pt2. Initially pt1 is at smallest value and pt2 at largest value.
# Then we compare sum = pt1.value + pt2.value. If sum < target, we increase pt2,
# else we decrease pt2 until we reach target.
# Using the same concept used in
# https://www.interviewbit.com/courses/programming/topics/trees/problems/treeiterator/ we can do this.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, root, k):
        if self.helper(root, k, {}) is True:
            return 1
        else:
            return 0

    def helper(self, root, k, store):

        if root is None:
            return False
        subtractedValue = k - root.val
        if subtractedValue not in store:
            store[root.val] = subtractedValue
        else:
            return True
        return self.helper(root.left, k, store) or self.helper(root.right, k, store)


#####		Populate Next Right Pointers Tree		#####

"""
Given a binary tree
    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
 Note:
You may only use constant extra space.
Example :
Given the following binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
 Note 1: that using recursion has memory overhead and does not qualify for constant space.
Note 2: The tree need not be a perfect binary tree.
"""


# Lets say you have already created next pointers till level L. To create next
# pointer for level L+1, start with the first node on level L.
#         1   ->  2   ->  3  -> 4
#        /         \           / \
#       /           \         /    \
#      5            6        7      8
#
#
#         1   ->  2   ->  3  -> 4
#        /         \           / \
#       /           \         /   \
#      4     ->      7   ->  8 ->  9
# Keep track of the previous node you encountered on the next level. For the current node, explore the left and
# right child if they are not null in that order. If the prev is not set, that means we are looking at the leftmost
# node on the next level ( Lets store it because we will begin the next iteration from this node ). Else you can
# assign prev->next as the current node in next level you are exploring and update the prev node.

class Solution:

    def populate_next_r_02(self, root):
        if root is None:
            return
        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                head = root
                while head.next:
                    if head.next.left:
                        root.left.next = head.next.left
                        break
                    elif head.next.right:
                        root.left.next = head.next.right
                        break
                    head = head.next
        if root.right:
            head = root

            while head.next:
                if head.next.left:
                    root.right.next = head.next.left
                    break
                elif head.next.right:
                    root.right.next = head.next.right

                head = head.next
        self.populate_next_r_02(root.right)
        self.populate_next_r_02(root.left)


#####		Invert The Binary Tree		#####

"""
Given a binary tree, invert the binary tree and return it.
Look at the example for more details.
Example :
Given binary tree
     1
   /   \
  2     3
 / \   / \
4   5 6   7
invert and return
     1
   /   \
  3     2
 / \   / \
7   6 5   4
"""


# Think recursively.
# On every node, you need to invert the left and right subtree and then swap them.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, A):
        if not A:
            return None
        ileft = self.invertTree(A.left)
        iright = self.invertTree(A.right)
        A.left, A.right = iright, ileft
        return A


#####		Inorder Traversal Cartesian Tree		#####

"""
Given an inorder traversal of a cartesian tree, construct the tree.
 Cartesian tree : is a heap ordered binary tree, where the root is greater than all the elements in the subtree.
 Note: You may assume that duplicates do not exist in the tree.
Example :
Input : [1 2 3]
Return :
          3
         /
        2
       /
      1
"""


# Note that the root is the max element in the whole array. Based on the info, can you figure out the position of the
# root in inorder traversal ? If so, can you separate out the elements which go in the left subtree and right subtree ?
# Once you have the inorder traversal for left subtree, you can recursively solve for left and right subtree.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):

        root = TreeNode(A[0])
        i = 1
        while i < len(A):
            node = TreeNode(A[i])
            if A[i] > root.val:
                node.left = root
                root = node
            else:
                temp = root
                while (temp.right is not None) and temp.right.val > A[i]:
                    temp = temp.right
                if temp.right is None:
                    temp.right = node
                else:
                    x = temp.right
                    temp.right = node
                    node.left = x
            i += 1
        return root


#####		2 Sum Binary Tree		#####

"""
Given a binary search tree T, where each node contains a positive integer,
and an integer K, you have to find whether or not there exist two different
nodes A and B such that A.value + B.value = K.

Return 1 to denote that two such nodes exist. Return 0, otherwise.

Notes
Your solution should run in linear time and not take memory more than O(height of T).
Assume all values in BST are distinct.
Example :

Input 1:

T :       10
         / \
        9   20

K = 19

Return: 1

Input 2:

T:        10
         / \
        9   20

K = 40

Return: 0
"""


# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:

    def t2Sum(self, A, B):
        pass


#####		Recovery Bst		#####

"""
Two elements of a binary search tree (BST) are swapped by mistake.
Tell us the 2 values swapping which the tree will be restored.
 Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
Example :
Input :
         1
        / \
       2   3
Output :
       [1, 2]
Explanation : Swapping 1 and 2 will change the BST to be
         2
        / \
       1   3
which is a valid BST
"""


# Lets look at the inorder traversal of the tree.
# In the ideal case, the inorder traversal should be sorted. But in this case,
# because of the swapping 2 cases might arise :
# 1) A sequence like {1, 4, 3, 7, 9}, where the swapped pair are adjacent to each other. Only one inversion
# ( Inversion here means pair of integer A[i], A[i+1] where A[i] > A[i+1] ).
# 2) A sequence like {1, 9, 4, 5, 3, 10} where the swapped pair are not adjacent. 2 inversions. We take the
# min and max of the inversion numbers and we know the number we need to swap to get the right answer.
# Now to figure this out, we need to do an inorder traversal. However, the traditional recursive inorder
# traversal has memory overhead of the depth of the tree.
# Using a stack has the same memory overhead.
# So, we need something which does not use recursion or stack and can still do the inorder traversal. This
# part is a bit tricky. Not all interviewers expect you to know this.
# Morris traversal helps us achieve what we are after. It works on the fact that we can modify the tree when
# traversing and then resetting the tree to its original state once we are done.
# The idea of Morris traversal is based on Threaded Binary tree ( http://en.wikipedia.org/wiki/Threaded_binary_tree ).
# In this traversal, we first create links to Inorder successor and print the data using these links, and
# finally revert the changes to restore original tree.
# Initialize current as root
# While current is not NULL
# If current does not have left child
# a) Print current’s data
# b) Go to the right, i.e., current = current->right
# Else
# a) Make current as right child of the rightmost node in current’s left subtree
# b) Go to this left child, i.e., current = current->left
# Although the tree is modified through the traversal, it is reverted back to its original shape after the completion.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def recoverTree(self, A):
        self.first = None
        self.prev = None
        self.last = None
        self.traverse(A)
        return [self.last, self.first]

    def traverse(self, A):
        if A.left is not None:
            self.traverse(A.left)
        if self.prev is not None and self.prev > A.val:
            if self.first is None:
                self.first = self.prev
                self.last = A.val
            else:
                self.last = A.val
        self.prev = A.val
        if A.right is not None:
            self.traverse(A.right)


#####		Shortest Unique Prefix		#####

"""
Find shortest unique prefix to represent each word in the list.
Example:
Input: [zebra, dog, duck, dove]
Output: {z, dog, du, dov}
where we can see that
zebra = z
dog = dog
duck = du
dove = dov
 NOTE : Assume that no word is prefix of another. In other words, the representation is always possible.
"""


# input: ["zebra", "dog", "duck", "dot"]
# Now we will build prefix tree and we will also store count of characters
#                 root
#                 /|
#          (d, 3)/ |(z, 1)
#               /  |
#           Node1  Node2
#            /|        \
#      (o,2)/ |(u,1)    \(e,1)
#          /  |          \
#    Node1.1  Node1.2     Node2.1
#       | \         \            \
# (g,1) |  \ (t,1)   \(c,1)       \(b,1)
#       |   \         \            \
#     Leaf Leaf       Node1.2.1     Node2.1.1
#     (dog)  (dot)        \                  \
#                          \(k, 1)            \(r, 1)
#                           \                  \
#                           Leaf               Node2.1.1.1
#                           (duck)                       \
#                                                         \(a,1)
#                                                          \
#                                                          Leaf
#                                                          (zebra)
# Now, for every leaf / word , we find the character nearest to the root with frequency as 1.
# The prefix that the path from root to this character corresponds to, is the representation of the word.

class TreeNode(object):
    def __init__(self):
        self._children = {}  # prefix to child

    def add(self, prefix):
        if prefix not in self._children:
            self._children[prefix] = TreeNode()
        return self._children[prefix]

    def num(self):
        return len(self._children)

    def get(self, prefix):
        # Assumes exists
        return self._children[prefix]


class PrefixTree(object):
    def __init__(self, words):
        self._root = TreeNode()  # empty prefix for root
        for word in words:
            self.add(word)

    def add(self, word):
        node = self._root
        for c in word:
            node = node.add(c)

    def get(self, word):
        node = self._root
        counts = []
        for c in word:
            counts.insert(0, node.num())
            node = node.get(c)
        # chop of uniques from the end
        num_remove = 0
        for count in counts:
            if count != 1:
                break
            num_remove += 1
        return word[:-num_remove] if num_remove > 0 else word


class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        # build prefix tree
        tree = PrefixTree(A)
        # apply prefix tree
        return [tree.get(a) for a in A]


#####		Order Of People Heights		#####

"""
You are given the following :
A positive number N
Heights : A list of heights of N persons standing in a queue
Infronts : A list of numbers corresponding to each person (P) that gives the number of persons who are
 taller than P and standing in front of P
You need to return list of actual order of persons’s height
Consider that heights will be unique
Example
Input :
Heights: 5 3 2 6 1 4
InFronts: 0 1 2 0 3 2
Output :
actual order is: 5 3 2 1 6 4
So, you can see that for the person with height 5, there is no one taller than him who is in front of him,
and hence Infronts has 0 for him.
For person with height 3, there is 1 person ( Height : 5 ) in front of him who is taller than him.
You can do similar inference for other people in the list.
"""


# This problem is slightly tricky.
# Really inefficient but correct approach :
# Try out all possible permutation of the give numbers, and verify if the infronts numbers match for the given sequence.
# This is obviously too inefficient. O(N!).
# Lets see if we can do something better.
# Hint towards something better
# What can you say about the position of the shortest person ? If the position of the shortest person is i, how many
# people would be in front of the shortest person ?
# Once you fix the position of the shortest person, what can you say about the position of the second shortest person ?
# If we take that approach, do we need to sort the heights first ?
# O(N^2) approach
# Sort people by heights. Then iterate from shortest to tallest. In each step you need an efficient way to put the
# next person to the correct position. Notice that people we’ve already placed are not taller that the current person.
# And the people we place after are taller than the current. So we have to find a place such that the number of empty
# positions in the front is equal to the inFronts value of this person.
# Lets take an example :
# For example after sorting,
# Height - 1, 2, 3, 4, 5, 6
# Infront - 3, 2, 1, 2, 0, 0.
# 1st element should go in position 3. Hence final array becomes:
# ---1--
# 2nd element shall go in position 2. Hence final array becomes:
# --21--
# 3rd element should go in position 1. Hence final array becomes:
# -321--
# 4th element shall go in position 2. This is the position among the empty ones. Hence final array becomes:
# -321-4
# 5th element shall go in position 0. Hence final array becomes:
# 5321-4
# 6th element should go in position 0. Hence final array becomes:
# 532164
# Hint towards an even better solution
# Can we make the process of finding the ith empty position even more efficient ? Think binary tree / segment tree ?
# Oh, by the way, this would be a nice time to read up on Segment Trees which are incredibly useful
# ( http://codeforces.com/blog/entry/3327 )
# What if you knew how many elements are there in first half of the array, and the second half of the array ?
# Please read the previous hint if you haven’t done so already.
# Here, we will explore how to efficiently answer the query of finding the ith empty space.
# The query can be solved using segment / interval tree.
# The root contains the number of elements in [0, N].
# Left node contains the number of elements in [0, N/2]
# Right node contains the number of elements in [N/2 + 1, N]
# Lets say we need to find the ith empty position.
# We look at the number of elements X in [0, N/2].
# If
#     N / 2 - X >= i, the position lies in the left part of array and we move down to the left node.
#     N / 2 - X < i, we now look for i - (N / 2 - X) th position in the right part of the array and
#     move to the right node in the tree.
# This is a fairly standard use of the segment tree.


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def order(self, A, B):
        N = len(A)
        data = {A[i]: B[i] for i in range(N)}

        positions = list(range(N))

        res = [None] * N

        for k in sorted(data.keys()):
            res[positions[data[k]]] = k
            del positions[data[k]]

        return res


#####		Symmetric Binary Tree		#####

"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
Example :
    1
   / \
  2   2
 / \ / \
3  4 4  3
The above binary tree is symmetric.
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""


# 2 trees T1 and T2 are symmetric if
# 1) value of T1’s root is same as T2’s root
# 2) T1’s left and T2’s right are symmetric.
# 3) T2’s left and T1’s right are symmetric.
# Can you use the above fact to model an easy recursion based solution ?


class Solution:

    def _isSymmetric(self, a, b):
        if a is None:
            return b is None
        if b is None:
            return a is None
        return a.val == b.val and \
               self._isSymmetric(a.right, b.left) and \
               self._isSymmetric(a.left, b.right)

    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        return 1 if self._isSymmetric(A.left, A.right) else 0


#####		Binary Tree From Inorder And Postorder		#####

"""
Given inorder and postorder traversal of a tree, construct the binary tree.
 Note: You may assume that duplicates do not exist in the tree.
Example :
Input :
        Inorder : [2, 1, 3]
        Postorder : [2, 3, 1]
Return :
            1
           / \
          2   3
"""


# Focus on the postorder traversal to begin with.
# The last element in the traversal will definitely be the root.
# Based on this information, can you identify the elements in the left subtree and right subtree ?
# ( Hint : Focus on inorder traversal and root information )
# Once you do that, your problem has now been reduced to a smaller set. Now you have the inorder and
# postorder traversal for the left and right subtree and you need to figure them out.
# Divide and conquer.
# Bonus points if you can do it without recursion.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        if not B:
            return None
        root_pos = A.index(B[-1])
        new_node = TreeNode(B[-1])
        new_node.left = self.buildTree(A[:root_pos], B[:root_pos])
        new_node.right = self.buildTree(A[root_pos + 1:], B[root_pos:-1])
        return new_node


#####		Max Depth Of Binary Tree		#####

"""
Given a binary tree, find its maximum depth.
The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.
 NOTE : The path has to end on a leaf node.
Example :

         1
        /
       2
max depth = 2.
"""


class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxDepth(self, A):
        if A == None:
            return 0
        else:
            return 1 + max(self.maxDepth(A.left),
                           self.maxDepth(A.right))


#####		Least Common Ancestor		#####

"""
Find the lowest common ancestor in an unordered binary tree given two values in the tree.
 Lowest common ancestor : the lowest common ancestor (LCA) of two nodes v and w in a tree or directed acyclic graph
 (DAG) is the lowest (i.e. deepest) node that has both v and w as descendants.
Example :
        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2_     0        8
         /   \
         7    4
For the above tree, the LCA of nodes 5 and 1 is 3.

 LCA = Lowest common ancestor
Please note that LCA for nodes 5 and 4 is 5.

You are given 2 values. Find the lowest common ancestor of the two nodes represented by val1 and val2
No guarantee that val1 and val2 exist in the tree. If one value doesn’t exist in the tree then return -1.
There are no duplicate values.
You can use extra memory, helper functions, and can modify the node struct but, you can’t add a parent pointer.
"""


# Linear solution using path calculation :
#
# 1) Find path from root to n1 and store it in a vector or array.
# 2) Find path from root to n2 and store it in another vector or array.
# 3) Traverse both paths till the values in arrays are same. Return the common element just before the mismatch
# Linear solution using recursion :
# We traverse from the bottom, and once we reach a node which matches one of the two nodes, we pass it up to its parent.
# The parent would then test its left and right subtree if each contain one of the two nodes. If yes, then the parent
# must be the LCA and we pass its parent up to the root. If not, we pass the lower node which contains either one of
# the two nodes (if the left or right subtree contains either p or q), or NULL (if both the left and right subtree
# does not contain either p or q) up.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer

    def findPath(self, root, path, k):
        if root is None:
            return False

        path.append(root.val)
        if root.val == k:
            return True
        if root.left is not None and self.findPath(root.left, path, k) or root.right is not None and self.findPath(
                root.right, path, k):
            return True
        path.pop()
        return False

    def lca(self, A, B, C):
        path1 = []
        path2 = []
        if not self.findPath(A, path1, B) or not self.findPath(A, path2, C):
            return -1
        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                break;
            i = i + 1
        return path1[i - 1]


#####		Min Depth In Binary Tree		#####

"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
 NOTE : The path has to end on a leaf node.
Example :

         1
        /
       2
min depth = 2.
"""


class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, root):
        if root is None:
            return 0
        # Base Case : Leaf node.This acoounts for height = 1
        if root.left is None and root.right is None:
            return 1
        # If left subtree is Null, recur for right subtree
        if root.left is None:
            return self.minDepth(root.right) + 1
        # If right subtree is Null , recur for left subtree
        if root.right is None:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


#####		Hotel Reviews		#####

"""
Given a set of reviews provided by the customers for different hotels and a string containing “Good Words”,
you need to sort the reviews in descending order according to their “Goodness Value” (Higher goodness value first).
We define the “Goodness Value” of a string as the number of “Good Words” in that string.
Note: Sorting should be stable. If review i and review j have the same “Goodness Value” then their original order would be preserved.
 You are expected to use Trie in an Interview for such problems
Constraints:
1.   1 <= No.of reviews <= 200
2.   1 <= No. of words in a review <= 1000
3.   1 <= Length of an individual review <= 10,000
4.   1 <= Number of Good Words <= 10,000
5.   1 <= Length of an individual Good Word <= 4
6.   All the alphabets are lower case (a - z)
Input:
S : A string S containing "Good Words" separated by  "_" character. (See example below)
R : A vector of strings containing Hotel Reviews. Review strings are also separated by "_" character.
Output:
A vector V of integer which contain the original indexes of the reviews in the sorted order of reviews.
V[i] = k  means the review R[k] comes at i-th position in the sorted order. (See example below)
In simple words, V[i]=Original index of the review which comes at i-th position in the sorted order. (Indexing is 0 based)
Example:
Input:
S = "cool_ice_wifi"
R = ["water_is_cool", "cold_ice_drink", "cool_wifi_speed"]
Output:
ans = [2, 0, 1]
Here, sorted reviews are ["cool_wifi_speed", "water_is_cool", "cold_ice_drink"]
"""


# To calculate the “Goodness Value’’ of a review you need to check whether a word in the review is good or not.
# How can you reduce the time complexity of this checking? Brute force is O(N) per word.
# Through a little try, we would know that “Trie” is the best solution. You just need to make a trie of all
# the good words and check the goodness of each word in a review using the trie.
# ** Algorithm: **
# Insert all the good words in a trie.
# For each review, calculate the number of good words in it by checking whether a given word exist in trie or not.
# Output as needed by the solution.
# Come on, code it!

class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        goodWords = set(A.split("_"))
        # Making it into a set is important, as searching through a set is faster
        V = []
        for index in range(len(B)):
            countGoodWords = 0
            for word in B[index].split("_"):
                if word in goodWords:
                    countGoodWords += 1
            V.append([index, countGoodWords])  # store the index and the count
        V.sort(key=lambda a: a[1], reverse=True)  # use the count to sort (descending order)
        return [x[0] for x in V]  # return the sorted list of indexes


#####		Identical Binary Trees		#####

"""
Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
Example :
Input :
   1       1
  / \     / \
 2   3   2   3
Output :
  1 or True
"""


# When are the 2 trees the same ?
# When the root values are the same, and left subtree of both trees are same,
# and right subtree of both trees are the same.
# Can you think of very easy recursive solution based on the above fact ?


class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        if A is None and B is None:
            return 1
        # will only come here if only one of them is None
        # would have returned from above condition otherwise
        elif A is None or B is None:
            return 0
        elif (A.val == B.val
              and self.isSameTree(A.left, B.left)
              and self.isSameTree(A.right, B.right)):
            return 1
        else:
            return 0


#####		Sorted Array To Balanced Bst		#####

"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
 Balanced tree : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees
 of every node never differ by more than 1.
Example :
Given A : [1, 2, 3]
A height balanced BST  :

      2
    /   \
   1     3
"""


# For a BST, all values lower than the root go in the left part of root, and all values higher go in the
# right part of the root. For the tree to be balanced, we will need to make sure we distribute the elements almost
# equally in left and right part. So we choose the mid part of the array as root and divide the elements around it .
# Things to take care of :
# 1) Are you passing a copy of the array around or are you only passing around a reference ?
# 2) Are you dividing the array before passing onto the next function call or are you just specifying
# the start and end index ?

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        if len(A) == 0:
            return None
        mid = len(A) / 2
        root = TreeNode(A[mid])
        root.left = self.sortedArrayToBST(A[:mid])
        root.right = self.sortedArrayToBST(A[mid + 1:])
        return root


#####		Binary Tree From Inorder And Preorder		#####

"""
Given preorder and inorder traversal of a tree, construct the binary tree.
 Note: You may assume that duplicates do not exist in the tree.
Example :
Input :
        Preorder : [1, 2, 3]
        Inorder  : [2, 1, 3]
Return :
            1
           / \
          2   3
"""


# Focus on the preorder traversal to begin with.
# The first element in the traversal will definitely be the root.
# Based on this information, can you identify the elements in the left subtree and right subtree ?
# ( Hint : Focus on inorder traversal and root information )
# Once you do that, your problem has now been reduced to a smaller set. Now you have the inorder and preorder
# traversal for the left and right subtree and you need to figure them out.
# Divide and conquer.
# Bonus points if you can do it without recursion.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        if not B:
            return None
        root_pos = B.index(A[0])
        new_node = TreeNode(A[0])
        new_node.left = self.buildTree(A[1:root_pos + 1], B[:root_pos])
        new_node.right = self.buildTree(A[root_pos + 1:], B[root_pos + 1:])
        return new_node


#####		Postorder Traversal		#####

"""
Given a binary tree, return the postorder traversal of its nodes’ values.
Example :
Given binary tree
   1
    \
     2
    /
   3
return [3,2,1].
Using recursion is not allowed.
"""


# Instead of calling the functions, can you put the nodes on a stack and process them ?
# Would the solution be easier if you were to print the reverse of the asked ?

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        result = [];
        d = [A]
        while d:
            node = d.pop()
            if node:
                result.append(node.val)
                d.append(node.left)
                d.append(node.right)
        return result[::-1]


#####		Preorder Traversal		#####

"""
Given a binary tree, return the preorder traversal of its nodes’ values.
Example :
Given binary tree
   1
    \
     2
    /
   3
return [1,2,3].
Using recursion is not allowed.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, node):
        stack = []
        stack.append(node)
        ans = []
        while len(stack) > 0:
            temp = stack.pop()
            ans.append(temp.val)
            if temp.right is not None:
                stack.append(temp.right)
            if temp.left is not None:
                stack.append(temp.left)
        return ans


#####		Flatten Binary Tree To Linked List		#####

"""
Given a binary tree, flatten it to a linked list in-place.
Example :
Given
         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
Note that the left child of all nodes should be NULL.
"""


# If you notice carefully in the flattened tree, each node’s right child points to the next node of a
# pre-order traversal.
# Now, if a node does not have left node, then our problem reduces to solving it for the node->right.
# If it does, then the next element in the preorder traversal is the immediate left child. But if we make the
# immediate left child as the right child of the node, then the right subtree will be lost. So we figure out where
# the right subtree should go. In the preorder traversal, the right subtree comes right after the rightmost element
# in the left subtree.
# So we figure out the rightmost element in the left subtree, and attach the right subtree as its right child.
# We make the left child as the right child now and move on to the next node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, n):
        # stack for pre-order traversal
        s = [n]
        head = TreeNode(0)  # dummy
        res = head
        while len(s):
            # get last
            n = s.pop()
            if n:
                # add right
                s.append(n.right)
                # add left
                s.append(n.left)
                # add right node
                res.right = TreeNode(n.val)
                # update res
                res = res.right
        # remove dummy
        return head.right


#####		Kth Smallest Element In The Tree		#####

"""
Given a binary search tree, write a function to find the kth smallest element in the tree.
Example :
Input :
  2
 / \
1   3
and k = 2
Return : 2
As 2 is the second smallest element in the tree.
 NOTE : You may assume 1 <= k <= Total number of nodes in BST
"""


# Note the property of the binary search tree.
# All elements smaller than root will be in the left subtree, and all elements greater than root will be in the
# right subtree.
# This means we need not even explore the right subtree till we have explored everything in the left subtree.
# Or in other words, we go to the right subtree only when the size of left subtree + 1 ( root ) < k.
# With that in mind, we can come up with an easy recursive solution which is similar to inorder traversal :
# Step 1: Find the kth smallest element in left subtree decrementing k for every node visited.
# If answer is found, return answer.
# Step 2: Decrement k by 1. If k == 0 ( this node is the kth node visited ), return node’s value
# Step 3: Find the kth smallest element in right subtree.

def dfs(t):
    return [] if t is None else dfs(t.left) + [t.val] + dfs(t.right)


class Solution:
    def kthsmallest(self, t, k):
        return dfs(t)[k - 1]

    def kthsmallest_another(self, A, k):
        s = [A]
        counter = 0
        while s and k:
            top = s[len(s) - 1]
            if top.left:
                s.append(top.left)
                top.left = None
                continue
            latest = s.pop()
            counter += 1
            if counter == k:
                return latest.val
            if latest.right:
                s.append(latest.right)


#####		Balanced Binary Tree		#####

"""
Given a binary tree, determine if it is height-balanced.
 Height-balanced binary tree : is defined as a binary tree in which the depth of the two subtrees of every node never
  differ by more than 1.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
Example :
Input :
          1
         / \
        2   3
Return : True or 1
Input 2 :
         3
        /
       2
      /
     1
Return : False or 0
         Because for the root node, left subtree has depth 2 and right subtree has depth 0.
         Difference = 2 > 1.
"""


# A tree is balanced if :
# 1) Left subtree is balanced
# 2) Right subtree is balanced
# 3) And the difference is height of left and right subtree is atmost 1.
# Can you think of a way to simulate that with recursion ?
# Note that depth of a tree can also be calculated recursively as max(depth(rightSubtree), depth(leftSubtree)) + 1.

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        if A is None or A.left is None and A.right is None:
            return 1
        queue = [A]
        while len(queue) > 0:
            T = queue.pop()
            if T.left:
                queue.append(T.left)
                if not T.right and (T.left.left or T.left.right):
                    return 0
            if T.right:
                queue.append(T.right)
                if not T.left and (T.right.left or T.right.right):
                    return 0
        return 1


#####		Root To Leaf Path With Sum		#####

"""
Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals the given sum.
For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
"""


# Recursion might make this problem much easier to solve.
# You just need to keep a track of :
# 1) the sum from the root to the current node.
# 2) The elements encountered from the root to this node.


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def pathSum(self, A, B):
        self.paths = []

        def path_sum_rec(root, sum_, curr_path):
            if root.left is None and root.right is None:
                if sum_ - root.val == 0:
                    self.paths.append(curr_path + [root.val])
                return
            if root.left is not None:
                path_sum_rec(root.left, sum_ - root.val, curr_path + [root.val])
            if root.right is not None:
                path_sum_rec(root.right, sum_ - root.val, curr_path + [root.val])

        if A is not None:
            path_sum_rec(A, B, [])

        return self.paths


#####		Bst Iterator		#####

"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
The first call to next() will return the smallest number in BST. Calling next() again will return the next smallest
number in the BST, and so on.
 Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
Try to optimize the additional space complexity apart from the amortized time complexity.
"""


# Approach 1 : Do an inorder traversal of the tree and store the entries in an array with the current pointer set
# to the start of the array. hasNext checks if the pointer is less than the size of the array. next() would return
# the element at the current position incrementing the position by 1.
# However, this has an additional space complexity of O(N) where N = number of nodes in the tree.
# This might be an acceptable answer. Most interviewers would look for you to do better.
# Approach 2 : Lets look at the version of this problem when the trees have a back pointer. Can you solve the problem
# without using additional space ? When you are on node N and are asked for next element, you obviously won’t go to
# the left subtree as all the elements there are smaller than N. We would go to the smallest number in the right
# subtree if the right subtree is not null. If the right subtree is null, that means that we need to move up, and
# keep moving up till we are coming from the right subtree.
# Now we don’t have the back pointer in this case. So, we need something to keep track of the path from root to the
# current node, so we can move to the parent when needed. Do note that storing the path from root to the current node
# only requires memory equivalent to the length of the path which is the depth of the tree.
# Also, we can track the path using stack.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        # path_to_min contains the path from the root to the current minimum element
        # maintaining this list enables finding the next minimum in constant time
        # storage is in O(h)
        self.path_to_min = []
        self.populate_min(root, self.path_to_min)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.path_to_min != []

    # @return an integer, the next smallest number
    def next(self):
        if self.hasNext():
            n = self.path_to_min[-1].val
            self.find_next_min(self.path_to_min)
            return n

    def populate_min(self, A, path):
        if A is None:
            pass
        else:
            path.append(A)
            self.populate_min(A.left, path)

    # Finds the next minimum. There are 2 cases:
    # - the current minimum has a right subtree. The next minimum is the leftmost
    #   element of that subtree
    # - the current minimum does not have a right subtree. The next minimum is in the path
    #   from the root to the current min, unless the current min is the maximum of the tree
    def find_next_min(self, path_to_min):
        root = path_to_min[-1]
        # first case, there is a right subtree
        if root.right:
            self.populate_min(root.right, path_to_min)
        # second case, will empty the path completely when called on the maximum
        else:
            while path_to_min != [] and path_to_min[-1].val <= root.val:
                path_to_min.pop()

            # Your BSTIterator will be called like this:


# i = BSTIterator(root)
# while i.hasNext(): print i.next(),


#####		Path Sum		#####

"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding
up all the values along the path equals the given sum.
Example :
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""


# Recursion might make this problem much easier to solve.
# You just need to keep a track of the sum from the root to the current node.
# Then it becomes a question of just checking if the current node is a leaf node, and if so, do the sum match.

# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        if not A:
            return 0
        else:
            if A.val == B and not A.left and not A.right:
                return 1
            else:
                if self.hasPathSum(A.left, B - A.val):
                    return 1
                if self.hasPathSum(A.right, B - A.val):
                    return 1
        return 0


#####		Inorder Traversal		#####

"""
Given a binary tree, return the inorder traversal of its nodes’ values.
Example :
Given binary tree
   1
    \
     2
    /
   3
return [1,3,2].
Using recursion is not allowed
"""


# Instead of calling the functions, can you put the nodes on a stack and process them ?
# How would your solution work if you were allowed to change the original tree ?
# How would it work if you were not allowed to change the tree but use additional memory
# ( track the number of times a node has appeared in the tree ) ?
# How would it work if you were not even allowed the extra memory ?

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        curnode = A
        values = []
        stack = []
        while True:
            if curnode is not None:
                stack.append(curnode)
                curnode = curnode.left
            else:
                if len(stack) > 0:
                    curnode = stack.pop()
                    values.append(curnode.val)
                    curnode = curnode.right
                else:
                    return values


#####		Sum Root To Leaf Number		#####

"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers % 1003.
Example :
    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.
"""


# Think recursion.
# Carrying along the number formed from root to the node when calling the function for node, will make stuff easier for
# you. When you encounter a new digit, you can append it to existing one as newNum = oldNum * 10 + newDigit.

class Solution:
    # @param A : root node of tree
    # @return an integer
    def __init__(self):
        self.sum1 = 0;

    def helper(self, A, sum1, string=""):
        if A is None:
            return

        if A.left is None and A.right is None:
            string += str(A.val)
            self.sum1 = (self.sum1 % 1003 + int(string) % 1003) % 1003
            return

        string += str(A.val)
        self.helper(A.left, sum1, string)
        self.helper(A.right, sum1, string)

    def sumNumbers(self, A):
        if A is None:
            return 0;

        sum1 = 0
        self.helper(A, sum1)
        return self.sum1


#####		Zigzag Order Traversal		#####

"""
Given a binary tree, return the zigzag level order traversal of its nodes’ values. (ie, from left to right,
then right to left for the next level and alternate between).
Example :
Given binary tree
    3
   / \
  9  20
    /  \
   15   7
return
[
         [3],
         [20, 9],
         [15, 7]
]
"""


# We will be using 2 stacks to solve this problem. One for the current layer and other one for the next layer.
# Also keep a flag which indicates the direction of traversal on any level.
# You need to pop out the elements from current layer stack and depending upon the value of flag push the
# childs of current element in next layer stack. You should maintain the output sequence in the process as well.
# Remember to swap the stacks before next iteration. When should you terminate this algorithm?

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        if A is None:
            return []
        lr, rl = [], [A]
        st = rl
        lr_status = True
        result = []
        while st:
            level = []
            for _ in range(len(st)):
                x = st.pop()
                level.append(x.val)
                if lr_status:
                    if x.left:
                        lr.append(x.left)
                    if x.right:
                        lr.append(x.right)
                else:
                    if x.right:
                        rl.append(x.right)
                    if x.left:
                        rl.append(x.left)
            if lr_status:
                st = lr
            else:
                st = rl
            lr_status = not lr_status
            result.append(level)
        return result


#########################	two-pointers	#########################


#####		Contianer With Most Water		#####

"""
Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
'n' vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Your program should return an integer which corresponds to the maximum area of water that can be contained
( Yes, we know maximum area instead of maximum volume sounds weird. But this is 2D plane
we are working with for simplicity ).
 Note: You may not slant the container.
Example :
Input : [1, 5, 4, 3]
Output : 6
Explanation : 5 and 3 are distance 2 apart. So size of the base = 2. Height of container = min(5, 3) = 3.
So total area = 3 * 2 = 6
"""


# Area will be basically min(ai,aj)*(j-i) where j>i.
# Approach 1 (in direction of O(n)) :
# Will the area be maximum if you take j-i to be maximum. If not, then can you reduce the problem to simpler set?
# Approach 2 (in direction of O(nlogn)) :
# Sort the elements with their indexes in descending order. Start iterating from first position of sorted array
# while maintaing the maximum of answer. How?
# Description of approach 1:
# Note 1: When you consider a1 and aN, then the area is (N-1) * min(a1, aN).
# Note 2: The base (N-1) is the maximum possible.
# This implies that if there was a better solution possible, it will definitely have height greater than min(a1, aN).
# B * H > (N-1) * min(a1, aN)
# We know that, B < (N-1)
# So, H > min(a1, aN)
# This means that we can discard min(a1, aN) from our set and look to solve this problem again from the start.
# If a1 < aN, then the problem reduces to solving the same thing for a2, aN.
# Else, it reduces to solving the same thing for a1, aN-1


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        ans = 0
        n = len(A)
        i, j = 0, n - 1
        while i < j:
            ans = max(ans, min(A[i], A[j]) * (j - i))
            if A[i] < A[j]:
                i += 1
            else:
                j -= 1
        return ans


#####		Array 3 Pointers		#####

"""
You are given 3 arrays A, B and C. All 3 of the arrays are sorted.
Find i, j, k such that :
max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))
**abs(x) is absolute value of x and is implemented in the following manner : **
      if (x < 0) return -x;
      else return x;
Example :
Input :
        A : [1, 4, 10]
        B : [2, 15, 20]
        C : [10, 12]
Output : 5
         With 10 from A, 15 from B and 10 from C.
"""


# Windowing strategy works here.
# Lets say the arrays are A,B and C.
#
# Take 3 pointers X, Y and Z
# Initialize them to point to the start of arrays A, B and C
# Find min of X, Y and Z.
# Compute max(X, Y, Z) - min(X, Y, Z).
# If new result is less than current result, change it to the new result.
# Increment the pointer of the array which contains the minimum.
# Note that we increment the pointer of the array which has the minimum, because our goal is to decrease
# the difference. Increasing the maximum pointer is definitely going to increase the difference.
# Increase the second maximum pointer can potentially increase the difference ( however,
# it certainly will not decrease the difference ).

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        pA = 0
        pB = 0
        pC = 0
        minmax = float("inf")
        while pA < len(A) and pB < len(B) and pC < len(C):
            minmax = min(minmax, max(abs(A[pA] - B[pB]), abs(B[pB] - C[pC]), abs(C[pC] - A[pA])))
            if A[pA] == min(A[pA], B[pB], C[pC]):
                pA += 1
            elif B[pB] == min(A[pA], B[pB], C[pC]):
                pB += 1
            else:
                pC += 1

        return minmax


#####		3 Sum Zero		#####

"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Note:
 Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets. For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:
(-1, 0, 1)
(-1, -1, 2)
"""


# When the array is sorted, try to fix the least integer by looping over it.
# Let us say the least integer in the solution is arr[i].
# Now we need to find a pair of integers j and k such that :
#  arr[j] + arr[k] is -arr[i].
# To do that, let us try the 2 pointer approach.
# If we fix the two pointers at the end ( that is, i+1 and end of array ),
# we look at the sum.
# If the sum is smaller than 0, we increase the first pointer to increase the sum.
# If the sum is bigger than 0, we decrease the end pointer to reduce the sum.
# Getting a Time Limit exceeded or Output Limit exceeded?
# Make sure you handle case of empty input [].
# In C++/C, usually if you run a loop till array.size() - 2,
# it can lead to the program running indefinitely as array.size() is unsigned int,
# and the subtraction just makes it wrap over to a big integer.
# Make sure you are not processing the same triplets again.
# Skip over the duplicates in the array.
#  Try a input like :
# -1 -1 -1 -1 0 0 0 0 1 1 1 1
# Ideally, you should get only 2 pairs : {[-1 0 1], [0 0 0]}

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        if A.__len__() < 3:
            return []
        A.sort()
        ret = set()
        for index, ele_a in enumerate(A[:-2]):
            b = index + 1
            c = A.__len__() - 1
            while b < c:
                temp_sum = ele_a + A[b] + A[c]
                if temp_sum == 0:
                    ret.add((ele_a, A[b], A[c]))
                    b += 1
                    c -= 1
                elif temp_sum < 0:
                    b += 1
                else:
                    c -= 1
        return list(ret)


#####		Remove Duplicates From Sorted Array		#####

"""
Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.
Note that even though we want you to return the new length, make sure to change the original array as well in place
Do not allocate extra space for another array, you must do this in place with constant memory.
 Example:
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].
"""


# Notice that the array is sorted.
# This implies that all repetitions for an element are clustered together in the array.
# **Try maintaining 2 pointers in the array: **
# One pointer iterates over the array and
# Other pointer only moves per occurrence of a value in the array.
# Now you need to make sure we choose only one occurrence per
# cluster of repetition in the array, we could probably just check if A[i] != A[i+1].
# So, the second pointer only moves when A[i] != A[i+1]

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i, j = 1, 0
        while i < len(A):
            if A[i] != A[j]:
                A[j + 1] = A[i]
                j += 1

            i += 1
        del A[j + 1:]
        return len(A)


#####		3 Sum		#####

"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers.
Assume that there will only be one solution
Example:
given array S = {-1 2 1 -4},
and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
"""


# As stated in the earlier hint, the naive approach is to have 3 loops of i,j,k over the array.
# We then just track S[i]+S[j]+S[k] for the case when (S[i]+S[j]+S[k]-target) is minimum.
# The code for the same looks something like the following :
#   IF number of elements in S < 3
#     THEN return -1; // Invalid case
#   minDifference = abs(S[0] + S[1] + S[2] - target);
#   bestTillNow = S[0] + S[1] + S[2];
#   FOR i = 0 to size of S
#     FOR j = i + 1 to size of S
#       FOR k = j + 1 to size of S
#         newDiff = abs(S[i] + S[j] + S[k] - target)
#         IF newDiff < minDifference
#           minDifference = newDiff
#           bestTillNow = S[i] + S[j] + S[k]
#         END IF
#       END FOR
#     END FOR
#   END FOR
#   bestTillNow is my answer.
# However, as stated earlier this approach is O(N^3). Lets see if we can do better.
# Lets sort the array.
# When the array is sorted, try to fix the least integer by looping over it.
# Lets say the least integer in the solution is arr[i].
# Now we need to find a pair of integers j and k, such that arr[j] + arr[k] is closest to (target - arr[i]).
# To do that, let us try the 2 pointer approach.
# If we fix the two pointers at the end ( that is, i+1 and end of array ), we look at the sum.
# If the sum is smaller than the sum we need to get to, we increase the first pointer.
# If the sum is bigger, we decrease the end pointer to reduce the sum.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        closest = None
        for i in range(len(A) - 2):
            j, k = i + 1, len(A) - 1
            while k > j:
                threeSum = A[i] + A[j] + A[k]
                if threeSum == B:
                    return threeSum
                if closest is None or abs(B - threeSum) < abs(B - closest):
                    closest = threeSum
                if threeSum < B:
                    j += 1
                else:
                    k -= 1
        return closest


#####		Remove Element From Array		#####

"""
Remove Element
Given an array and a value, remove all the instances of that value in the array.
Also return the number of elements left in the array after the operation.
It does not matter what is left beyond the expected length.
 Example:
If array A is [4, 1, 1, 2, 1, 3]
and value elem is 1,
then new length is 3, and A is now [4, 2, 3]
Try to do it in less than linear additional space complexity.
"""


# Maybe you should try maintaining 2 pointers in the array:
# One pointer iterates over the array
# Other pointer only moves when it finds an element different from ‘elem’.
# In other words, the second pointer only moves when the first pointer is on an element
# worth keeping in the final array.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        """ Maintain position of free slot.
            We shift any valid element in this slot.
        """
        slot = 0
        for x in A:
            if x != B:
                # May replace an element by itself, nevermind.
                A[slot] = x
                slot += 1
        return slot


#####		Merge Two Sorted Lists 2		#####

"""
Given two sorted integer arrays A and B, merge B into A as one sorted array.
 Note: You have to modify the array A to contain the merge of A and B. Do not output anything in your code.
TIP: C users, please malloc the result into a new array and return the result.
If the number of elements initialized in A and B are m and n respectively, the resulting size of array A after
your code is executed should be m + n
Example :
Input :
         A : [1 5 8]
         B : [6 9]
Modified A : [1 5 6 8 9]
"""


# Corner cases :
# What if pointer 1 reaches the end of array first?
# What if pointer 2 reaches the end of array first?

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return A modified after the merge
    def merge(self, A, B):
        i = 0
        j = 0
        n = len(A)
        m = len(B)
        ret = []
        while i < n and j < m:
            if A[i] < B[j]:
                ret.append(A[i])
                i += 1
            else:
                ret.append(B[j])
                j += 1
        while i < n:
            ret.append(A[i])
            i += 1
        while j < m:
            ret.append(B[j])
            j += 1
        return ret


#####		Intersection Of Sorted Arrays		#####

"""
Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.
Example :
Input :
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]
Output : [3 3 5]
Input :
    A : [1 2 3 3 4 5 6]
    B : [3 5]
Output : [3 5]
"""


# Let us name array1 as A and array2 as B, each with size ‘m’ and ‘n’.
#
# The obvious brute-force solution is to scan through each element in A, and
# for each element in A, scan if that element exist in B.
# The running time complexity is O(m*n).
# This is not good!
# Can we do better? Absolutely!
# First of all, we know that both arrays are sorted.
# Can we somehow use this information to our advantage?
# We can apply binary search to find out if an element of A exist in B.
# So, the only modification from the brute-force approach is modifying linear search to binary search.
# This seems like a good improvement, we manage to reduce the complexity to O(m*lg(n)).
# Of course, you know you can trade space for running time by using a hash table. Is it really useful?
# We can definitely hash each element in B to an array index (takes O(n) time).
# Therefore, to find if an element of A exists in B, it would require just O(1) time. The complexity improves to O(m+n).
# But there is a problem.
# What if n is very big? (ie, n is one billion!).
# The hash table will either require a large amount of memory space, or there will be lots of collisions in the table,
# which makes access time no longer than O(1) time.
# Therefore, using a hash table is not a good general solution to this problem. Besides, using hash table DOES NOT
# require for the array to be sorted in the first place.
# Here is the most important observation in order to solve this
# We can have two indices, which both starts at zero.
# Compare the two first elements of A and B.
# If A[0] is greater than B[0], we increase index of B by one.
# If B[0] is greater than A[0], we increase index of A by one.
# If they are equal, we know an intersection has occurred, so add it to the list and increment index of A and B by one.
# Once either of the indices reaches the end of A or B, we have found all the intersections of A and B.
# The complexity of this approach is still O(m+n), but it does not requires any extra space that a hash table requires.
# The complexity is O(m+n) because in the worst case, there would be no intersection between the two arrays, and
# we need to increment the first index a total of m times and increment the second index a total of n times,
# which is a total of m+n times.

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        i = 0
        j = 0
        result = []
        while i < len(A) and j < len(B):
            if A[i] == B[j]:
                result.append(A[i])
                i += 1
                j += 1
            elif A[i] < B[j]:
                i += 1
            else:
                j += 1
        return result


#####		Diffk		#####

"""
Given an array ‘A’ of sorted integers and another non negative integer k,
find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
 Example: Input :
    A : [1 3 5]
    k : 4
 Output : YES as 5 - 1 = 4
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
Try doing this in less than linear space complexity.
"""


# Let us first look at why 2 pointer approach works here.
# A naive 2 loop approach would be:
# for (int i = 0; i < len; i++) {
#   for (int j = i + 1; j < len; j++) {
#     if (A[j] - A[i] > diff) break; // No need going forward as the difference is going to increase even further.
#     if (A[j] - A[i] == diff) return true;
#   }
# }
# Now, let us say that for i = I, we we exploring j.
# At j = J - 1, our difference D1 was less than diff
# At j = J, our difference D2 exceeded diff.
# When i = I + 1, our A[i] increases ( as the array is sorted ).
# So, for j = J - 1, the differece will be smaller than D1
# (which is even more smaller to diff.)
# Which means we do not need to explore j <= J - 1
# and we can begin exploring directly from j = J.
# So, j only keeps moving in forward direction and never needs to come back as i increases.
# Let us use that in a solution now:
# int j = 0;
# for (int i = 0; i < len; i++) {
#   j = max(j, i+1);
#   while (j < len && (arr[j] - arr[i] < diff)) j += 1;
#   if (arr[j] - arr[i] == diff) return true;
# }

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        if len(A) < 2:
            return 0
        i = 0
        j = 1
        while j < len(A) and i < len(A):
            if A[j] - A[i] - B == 0 and i != j:
                return 1
            elif A[j] - A[i] - B > 0:
                i += 1
            elif A[j] - A[i] - B < 0:
                j += 1
            else:
                j += 1
        return 0


#####		Minimize The Absolute Difference		#####

"""
Given three sorted arrays A, B and Cof not necessarily same sizes.
Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively.
i.e. minimize | max(a,b,c) - min(a,b,c) |.
Example :
Input:
A : [ 1, 4, 5, 8, 10 ]
B : [ 6, 9, 15 ]
C : [ 2, 3, 6, 6 ]
Output:
1
Explanation: We get the minimum difference for a=5, b=6, c=6 as | max(a,b,c) - min(a,b,c) | = |6-5| = 1.
"""


# Start with the largest elements in each of the arrays A,B & C. Maintain a variable to update the
# answer during each of the steps to be followed.
# In every step, the only possible way to decrease the difference is to decrease the maximum element out
# of the three elements.
# So traverse to the next largest element in the array containing the maximum element
# for this step and update the answer variable.
# Repeat this step until the array containing the maximum element ends.
# For the given sample example,
# initially, the triplets are { 10, 15, 6} and difference is (15 - 6) = 9 and answer is 9
# in the next step, { 10, 9, 6 }, diff is (10 - 6) = 4 and answer is updated to 4
# next step, { 8, 9, 6 } and diff is 3
# next step, { 8, 6, 6 } and diff is 2
# next step, {5, 6, 6 } and diff is 1
# finally after next two steps we reach { 5, 6, 3 } and cannot continue since array B has ended. Thus the answer is 1.
# Note: you can also start with min element triplet and increment the smallest element at every step.

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        i = 0
        j = 0
        k = 0
        n1 = len(A)
        n2 = len(B)
        n3 = len(C)
        mini = float('inf')
        while i < n1 and j < n2 and k < n3:
            if abs(min(A[i], B[j], C[k]) - max(A[i], B[j], C[k])) < mini:
                mini = abs(min(A[i], B[j], C[k]) - max(A[i], B[j], C[k]))
            if A[i] <= B[j] and A[i] <= C[k]:
                i += 1
            elif B[j] <= A[i] and B[j] <= C[k]:
                j += 1
            else:
                k += 1
        return mini


#####		Counting Triangles		#####

"""
You are given an array of N non-negative integers, A0, A1 ,…, AN-1.
Considering each array element Ai as the edge length of some line segment, count the number of
triangles which you can form using these array values.
Notes:
You can use any value only once while forming each triangle. Order of choosing the edge lengths doesn’t matter.
Any triangle formed should have a positive area.
Return answer modulo 109 + 7.
For example,
A = [1, 1, 1, 2, 2]
Return: 4
"""


# First we sort the array of side lengths. So since Ai < Aj < Ak where i < j < k,
# therefore it is sufficient to check Ai + Aj > Ak to prove they form a triangle.
# Thus for every i and j, we can find the maximum value of k such that the triangle inequality holds.
# Also we can also prove that for every such index i, we only have to increase the value of the
# k (satisfying the above condition) for every iteration of j from i+1 to n. Therefore, we get a O(n2)
# solution (Proof of this is left to the reader).

class Solution:
    # @param A : list of integers
    # @return an integer

    def nTriang(self, A):
        n = len(A)
        A.sort()
        count = 0
        for i in range(0, n - 2):
            k = i + 2
            for j in range(i + 1, n):
                while k < n and A[i] + A[j] > A[k]:
                    k += 1
                count += k - j - 1

        return count % 1000000007

    def nTriang_another(self, A):
        A.sort(reverse=True)
        t = 0
        for i in range(0, len(A) - 2):
            third_side = A[i]
            j = i + 1
            k = len(A) - 1
            while j < k:
                if A[j] + A[k] > third_side:
                    t += (k - j)
                    j += 1
                else:
                    k -= 1
        return t % (10 ** 9 + 7)


#####		Max Contigous Series Of 1s		#####

"""
You are given with an array of 1s and 0s. And you are given with an integer M, which signifies number of flips allowed.
Find the position of zeros which when flipped will produce maximum continuous series of 1s.
For this problem, return the indices of maximum continuous series of 1s in order.
Example:
Input :
Array = {1 1 0 1 1 0 0 1 1 1 }
M = 1
Output :
[0, 1, 2, 3, 4]
If there are multiple possible solutions, return the sequence which has the minimum start index.
"""


# Lets take an example:
# N : 4
# lis : 1 0 1 0
# M : 2
# pointer i and j
# i = j = 0
# iterate till i < N:
#         if(Number_of_Zeros_in_Current_range > M) :
#                 increment j and reduce range till Number_of_Zeros_in_current_range < M
#         else :
#                 add element in range and update all variables


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, array, m):
        """ Returns indices of longest sequence of consecutive 1s that can be
        achieved by flipping m 0s.
        Time complexity: O(n). Space complexity: O(1), n is len(array).
        """
        n = len(array)
        i, j = 0, 0  # start, end of current consecutive 1s sequence
        x, y = 0, 0  # start, end of longest consecutive 1s sequence
        while j < n:
            if array[j]:  # current element is 1
                if j - i > y - x:  # update start, end of longest 1s sequence
                    x, y = i, j
                j += 1  # move the right pointer
            elif not array[j] and m > 0:  # current element is 0, we can flip it
                if j - i > y - x:  # update start, end of longest 1s sequence
                    x, y = i, j
                m -= 1  # deacrese number of allowed flips
                j += 1  # move the right pointer
            else:  # current element is zero and we are out of flips
                if not array[i]:  # start of current 1s sequence is 0
                    m += 1  # increase available flips
                i += 1  # move the left pointer
        return list(range(x, y + 1))


#####		Remove Duplicates From Sorted Array 2		#####

"""
Remove Duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element can appear atmost twice and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
Note that even though we want you to return the new length, make sure to change the original array as well in place
For example,
Given input array A = [1,1,1,2],
Your function should return length = 3, and A is now [1,1,2].
"""


# Notice that the array is sorted. This implies that all repetitions for an element are clustered together in the array.
# Try maintaining 2 pointers in the array:
# One pointer iterates over the array
# Other pointer only moves per occurrence of a value in the array.
# Now you need to make sure we choose atmost 2 occurrences per cluster of repetition in the array,
# We could probably just check **if A[i] != A[i+1] || A[i] != A[i+2] **
# So, the second pointer only moves when A[i] != A[i+1] || A[i] != A[i+2]

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i = 2
        fp = 2
        while i < len(A):
            if A[fp - 1] != A[i] or A[fp - 2] != A[i]:
                A[fp] = A[i]
                fp += 1
            i += 1
        return fp


#####		Sort By Color		#####

"""
Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: Using library sort function is not allowed.
Example :
Input : [0 1 2 0 1 2]
Modify array so that it becomes : [0 0 1 1 2 2]
"""


# There are multiple approaches possible here. We need to make sure we do not allocate extra memory.
# Approach 1:
#  Count the number of red, white and blue balls.
# Then in another pass, set initial redCount number of cells as 0, next whiteCount
# cell as 1 and next bluecount cells as 2.
# *Requires 2 pass of the array. *
# **Approach 2: **
#  Swap the 0s to the start of the array maintaining a pointer, and 2s to the end of the array.
# 1s will automatically be in their right position.

class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        B = [0, 0, 0]
        for i in A:
            B[i] += 1
        return [0] * B[0] + [1] * B[1] + [2] * B[2]
