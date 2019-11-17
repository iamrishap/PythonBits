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
