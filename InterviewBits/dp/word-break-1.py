"""
Given a string A and a dictionary of words B, determine if A can be segmented into a
space-separated sequence of one or more dictionary words.
Input Format:
The first argument is a string, A.
The second argument is an array of strings, B.
Output Format:
Return 0 / 1 ( 0 for false, 1 for true ) for this problem.
Constraints:
1 <= len(A) <= 6500
1 <= len(B) <= 10000
1 <= len(B[i]) <= 20
Examples:
Input 1:
    A = "myinterviewtrainer",
    B = ["trainer", "my", "interview"]
Output 1:
    1
Explanation 1:
    Return 1 ( corresponding to true ) because "myinterviewtrainer" can be segmented as "my interview trainer".
Input 2:
    A = "a"
    B = ["aaa"]
Output 2:
    0
Explanation 2:
    Return 0 ( corresponding to false ) because "a" cannot be segmented as "aaa".
"""


# Lets again look at the bruteforce solution.
# You start exploring every substring from the start of the string, and check if its in the dictionary. If it is, then
# you check if it is possible to form rest of the string using the dictionary words. If yes, my answer is true.
# If none of the substrings qualify, then our answer is false.
# So something like this :
#     bool wordBreak(int index, string &s, unordered_set<string> &dict) {
#         // BASE CASES
#
#         bool result = false;
#         // try to construct all substrings.
#         for (int i = index; i < s.length(); i++) {
#             substring = *the substring s[index..i] with i inclusive*
#             if (dict contains substring) {
#                 result |= wordBreak(i + 1, s, dict); // If this is true, we are done.
#             }
#         }
#         return result;
#     }
# This solution itself is exponential. However, do note that we are doing a lot of repetitive work.
# Do note, that index in the wordBreak function call can only take s.length() number of values [0, s.length].
# What if we stored the result of the function somehow and did not process it everytime the function is called ?

class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        group = set()
        for i in B:
            group.add(i)

        store = dict([])
        for i in range(len(A) - 1, -1, -1):
            for j in range(i + 1, len(A) + 1):
                if A[i:j] in group:
                    if j < len(A) and A[j:] in store:
                        store[A[i:]] = 1
                        break
                    elif j == len(A):
                        store[A[i:]] = 1

        if A in store:
            return 1
        else:
            return 0
