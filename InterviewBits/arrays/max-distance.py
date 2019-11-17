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
