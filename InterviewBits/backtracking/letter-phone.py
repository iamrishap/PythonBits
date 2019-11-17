"""
Given a digit string, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.
The digit 0 maps to 0 itself.
The digit 1 maps to 1 itself.
Input: Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Make sure the returned strings are lexicographically sorted.
"""

class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, digits):
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': '0', '1': '1'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])
        prev = self.letterCombinations(digits[:-1])  # Recurse for element except the last one
        additional = mapping[digits[-1]]  # Use the combinations for last element
        return [s + c for s in prev for c in additional]  # Append additional for last to recursion result


s = Solution()
print(s.letterCombinations('132'))


# TODO: Good and short implementation. Revisit to revise.
