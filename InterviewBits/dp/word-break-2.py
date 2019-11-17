"""
Given a string A and a dictionary of words B, add spaces in A to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.
Note : Make sure the strings are sorted in your result.
Input Format:
The first argument is a string, A.
The second argument is an array of strings, B.
Output Format:
Return a vector of strings representing the answer as described in the problem statement.
Constraints:
1 <= len(A) <= 50
1 <= len(B) <= 25
1 <= len(B[i]) <= 20
Examples:
Input 1:
    A = "b"
    B = ["aabbb"]
Output 1:
    []
Input 1:
    A = "catsanddog",
    B = ["cat", "cats", "and", "sand", "dog"]
Output 1:
    ["cat sand dog", "cats and dog"]
"""

# Lets again look at the bruteforce solution.
# You start exploring every substring from the start of the string, and check if its in the dictionary.
# If it is, then you check if it is possible to form rest of the string using the dictionary words.
# If yes, you append the current substring to all the substring possible from rest of the string.
# If none of the substrings qualify, then there are no sentences possible from this string. .
# So something like this :
# vector<string> wordBreak(int index, string &s, unordered_set<string> &dict) {
#     // BASE CASES
#
#     vector<string> sentences;
#     // try to construct all substrings.
#     for (int i = index; i < s.length(); i++) {
#         substring = *the substring s[index..i] with i inclusive*
#             if (dict contains substring) {
#                 vector<string> ret = wordBreak(i + 1, s, dict);
#                 foreach (sentence in ret) {
#                     sentences.push_back(substring + " " + sentence);
#                 }
#             }
#     }
#     return sentences;
# }
# This solution itself is exponential. However, do note that we are doing a lot of repetitive work.
# Do note, that index in the wordBreak function call can only take s.length() number of values [0, s.length].
# What if we stored the result of the function somehow and did not process it everytime the function is called ?

from collections import defaultdict


class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of strings
    def wordBreak(self, s, bag_words):
        suffix_words = [[] for i in range(len(s))]
        for i in reversed(range(len(s))):
            for j in range(i + 1, len(s)):
                if s[i:j] in bag_words and suffix_words[j]:
                    suffix_words[i].extend([[s[i:j]] + proper_sentence for proper_sentence in suffix_words[j]])
            if s[i:] in bag_words:
                suffix_words[i].append([s[i:]])

        return [' '.join(t) for t in suffix_words[0]]
