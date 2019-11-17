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
