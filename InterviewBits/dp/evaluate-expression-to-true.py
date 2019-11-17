"""
Given an expression, A, with operands and operators (OR , AND , XOR), in how many ways can you evaluate the
expression to true, by grouping in different ways?
Operands are only true and false.
Return the number of ways to evaluate the expression modulo 103 + 3.
Input Format:
The first and the only argument of input will contain a string, A.
The string A, may contain these characters:
    '|' will represent or operator
    '&' will represent and operator
    '^' will represent xor operator
    'T' will represent true operand
    'F' will false
Output:
Return an integer, representing the number of ways to evaluate the string.
Constraints:
1 <= length(A) <= 150
Example:
Input 1:
    A = "T|F"
Output 1:
    1
Explanation 1:
    The only way to evaluate the expression is:
        => (T|F) = T
Input 2:
    A = "T^T^F"
Output 2:
    0
Explanation 2:
    There is no way to evaluate A to a true statement.
"""


# T|F
# The operator here is 'or'. So, we need to find the number of ways sub-expression left of `|` operator,
# or the sub-expression to the right of the operator, evaluates to true.
# In other words,
# ways = (ways_T_left * ways_T_right) + (ways_F_left * ways_T_right) + (ways_T_left * ways_F_right)
# because T | T = T
#         T | F = T
#         F | T = T
# Can you extend the same analogy to other operators ?
# Assume Tr(i, j) tell us the number of ways to get True from sub-expresion i to j
# Fa(i, j) tell us the number of ways to get False from subexpresion i to j.
# The recurrence relation will look like the following :
# some rules =>
# or operator:
# T|F = T
# T|T = T
# F|T = T
# F|F = F
# and operator:
# T&F = F
# T&T = T
# F&T = F
# F&F = F
# x-or operator
# T^T = F
# T^F = T
# F^T = T
# F^F = F
# for Tr(i, j) :
#    Loop from i to j - 1 into variable k
#      IF(k == AND) :
# 	Tr(i, j) = Tr(i, j) + (Tr(i, k) * Tr(k + 1, j))
#      IF(k == OR) :
# 	Tr(i, j) = Tr(i, j) + (Tr(i, k) * Tr(k + 1, j)) + (Tr(i, k) * Fa(k + 1, j)) + (Fa(i, k) * Tr(k + 1, j))
#      If(k == XOR) :
# 	Tr(i, j) = Tr(i, j) + (Tr(i, k) * Fa(k + 1, j)) + (Fa(i, k) * Tr(k + 1, j))
# for Fa(i, j) :
#  Loop from i to j - 1 into variable k
#    IF(k == AND) :
#      Fa(i, j) = Fa(i, j) + (Fa(i, k) * Fa(k + 1, j)) + (Fa(i, k) * Tr(k + 1, j)) + (Tr(i, k) * Fa(k + 1, j))
#    IF(k == OR) :
# 	Fa(i, j) = Fa(i, j) + (Fa(i, k) * Fa(k + 1, j))
#    If(k == XOR) :
# 	Fa(i, j) = Fa(i, j) + (Tr(i, k) * Tr(k + 1, j)) + (Fa(i, k) * Fa(k + 1, j))
# then use memoziation for better time complexity

class Solution:
    # @param A : string
    # @return an integer
    def cnttrue(self, A):
        bits_and_ops = []
        MOD = 1003
        map_chars = {
            'T': 1,
            'F': 0,
            '|': '|',
            '&': '&',
            '^': '^',
            '|': lambda x, y: sum(x) * sum(y) - x[0] * y[0],
            '&': lambda x, y: x[1] * y[1],
            '^': lambda x, y: x[0] * y[1] + x[1] * y[0]
        }

        if len(A) <= 1:
            if len(A) == 0 or A[0] == 'F':
                return 0
            else:
                return 1

        for idx, curr_char in enumerate(A):
            if idx % 2 == 0 and curr_char not in ['T', 'F']:
                return 0
            if idx % 2 == 1 and curr_char not in ['|', '&', '^']:
                return 0

            bits_and_ops.append(map_chars[curr_char])

        dp = {}
        for i in range(0, len(bits_and_ops) - 2, 2):
            if bits_and_ops[i] == 0:
                x = [1, 0]
            else:
                x = [0, 1]
            if bits_and_ops[i + 2] == 0:
                y = [1, 0]
            else:
                y = [0, 1]

            dp[i, i] = x
            dp[i + 2, i + 2] = y

            cnt_ones_combs = bits_and_ops[i + 1](x, y)
            total_combs = sum(x) * sum(y)
            dp[i, i + 2] = [total_combs - cnt_ones_combs, cnt_ones_combs]

        for d in range(4, len(bits_and_ops), 2):
            for i in range(0, len(bits_and_ops) - d, 2):
                dp[i, i + d] = [0, 0]
                for j in range(i, i + d, 2):
                    x = dp[i, j]
                    y = dp[j + 2, i + d]
                    cnt_ones_combs = bits_and_ops[j + 1](x, y)
                    total_combs = sum(x) * sum(y)

                    dp[i, i + d] = [dp[i, i + d][0] + total_combs - cnt_ones_combs, dp[i, i + d][1] + cnt_ones_combs]

        return dp[0, len(bits_and_ops) - 1][1] % MOD
