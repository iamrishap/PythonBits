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
