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
