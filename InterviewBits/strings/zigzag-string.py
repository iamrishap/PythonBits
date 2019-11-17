"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P.......A........H.......N
..A..P....L....S....I...I....G
....Y.........I........R
And then read line by line: PAHNAPLSIIGYIR
Write the code that will take a string and make this conversion given a number of rows:
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
**Example 2 : **
ABCD, 2 can be written as
A....C
...B....D
and hence the answer would be ACBD.
"""


# Just look at simply simulating what is being told in the problem.
# Follow the simple steps:
# You need to maintain numRows number of strings S[numRows].
# And then populating string S in each row in zigzag fashion.
# Finally concatenate S[0] .. S[numRows-1] to get the answer.

class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, n):
        if len(A) == 1:
            return A
        ans = {}
        j = 0
        down = True
        for i in range(0, len(A)):
            ans[j] = ans.get(j, []) + [A[i]]  # Gets [] if key doesn't exist
            if down:
                j += 1
            else:
                j -= 1
            if j == n - 1:  # Time to change direction
                down = False
            if j == 0:  # Time to change direction
                down = True
        temp = []
        for i in ans:
            for j in ans[i]:
                temp.append(j)
        x = "".join(temp)
        return x
