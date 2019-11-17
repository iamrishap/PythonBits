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
