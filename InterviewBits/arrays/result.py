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
        B = [[] for i in range(len(a)*2)]
        # Done smoothly
        for i in range(len(a)):
            for j in range(len(a)):
                B[i+j].append(a[i][j])
        return B[:-1]


A = [[1,2,3],[4,5,6],[7,8,9]]
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
print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,9]))
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
                if val_now['inx_low'] != -1:   # If `val_now` is set
                    val_now['inx_high'] = idx - 1 # Set `ind_high`
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
        for i in range(n-1):
            # When certain element repeats many times.
            if A[i] == A[i+1]:
                continue
            if A[i] == n-i-1:
                return 1
        if A[n-1] == 0:
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


# TODO: Can spend more time understanding the implementation using max_index_from_i
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


# TODO: Spend more time understanding the code. min1, max1
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
