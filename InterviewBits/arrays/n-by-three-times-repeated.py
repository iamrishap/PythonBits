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
