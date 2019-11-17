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
