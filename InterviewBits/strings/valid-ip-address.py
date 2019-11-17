"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255.
The numbers cannot be 0 prefixed unless they are 0.
Example:
Given “25525511135”,
return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)
"""


# Essentially you have to place 3 dots in the given string.
# Try out all the possible combinations for the 3 dots.
# Corner case:
# 25011255255
# 25.011.255.255 is not valid as 011 is not valid.
# 25.11.255.255 is not valid either as you are not allowed to change the string.
# 250.11.255.255 is valid.

def solve(i, s, count, stack, ans):
    if i == len(s):
        return False

    if count == 3:
        if 0 <= int(s[i:]) <= 255:
            if len(s[i:]) > 1 and s[i:][0] == '0':
                return False
            bo = []
            for j in stack:
                bo.append(j)

            bo.append(s[i:])
            ans.append('.'.join(bo))

        return False

    st = ''
    for i in range(i, len(s)):
        st += s[i]
        if 0 <= int(st) <= 255:
            if len(st) > 1 and st[0] == '0':
                return False
            stack.append(st)
            z = solve(i + 1, s, count + 1, stack, ans)
            if z == False:
                stack.pop(-1)

    return False


class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        i = 0
        s = A
        count = 0
        stack = []
        ans = []
        solve(i, s, count, stack, ans)
        ans.sort()
        return ans


IP = "25525511135"
s = Solution()
print(s.restoreIpAddresses(IP))

# TODO: Didn't quite catch the logic of the program. Revisit.
