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
