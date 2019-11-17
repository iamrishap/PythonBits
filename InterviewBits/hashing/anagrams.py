"""
Given an array of strings, return all groups of strings that are anagrams. Represent a group by a list of integers
representing the index in the original list. Look at the sample case for clarification.
 Anagram : a word, phrase, or name formed by rearranging the letters of another, such as 'spar', formed from 'rasp'
 Note: All inputs will be in lower-case.
Example :
Input : cat dog god tca
Output : [[1, 4], [2, 3]]
cat and tca are anagrams which correspond to index 1 and 4.
dog and god are another set of anagrams which correspond to index 2 and 3.
The indices are 1 based ( the first element has index 1 instead of index 0).
 Ordering of the result : You should not change the relative ordering of the words / phrases within the group. Within a
  group containing A[i] and A[j], A[i] comes before A[j] if i < j.
"""


# Anagrams will map to the same string if the characters in the string are sorted.
# We can maintain a hashmap with the key being the sorted string and the value being the
# list of strings ( which have the sorted characters as key ).

class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        # hashmap with sorted string as key and list of anagrams as values
        hashmap = {}
        for index, word in enumerate(A):
            # sorted() returns a list, hence first convert it to a string
            # so that we can use it as a key in the hashmap
            sorted_word = ''.join(sorted(word))
            if sorted_word not in hashmap:
                # create key if not present and associate
                # the current word with it
                hashmap[sorted_word] = [index + 1]
            else:
                # append the current word to the list associated with the key
                hashmap[sorted_word] += [index + 1]
        # hashmap.values() returns a dict_values object in python 3,
        # hence convert it into a list while returning
        return list(hashmap.values())
