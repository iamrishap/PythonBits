"""
You are given a sequence of black and white horses, and a set of K stables numbered 1 to K. You have to accommodate
 the horses into the stables in such a way that the following conditions are satisfied:
You fill the horses into the stables preserving the relative order of horses. For instance, you cannot put horse 1
into stable 2 and horse 2 into stable 1. You have to preserve the ordering of the horses.
No stable should be empty and no horse should be left unaccommodated.
Take the product (number of white horses * number of black horses) for each stable and take the sum of all these
products. This value should be the minimum among all possible accommodation arrangements
Example:
Input: {WWWB} , K = 2
Output: 0
Explanation:
We have 3 choices {W, WWB}, {WW, WB}, {WWW, B}
for first choice we will get 1*0 + 2*1 = 2.
for second choice we will get 2*0 + 1*1 = 1.
for third choice we will get 3*0 + 0*1 = 0.
Of the 3 choices, the third choice is the best option.
If a solution is not possible, then return -1
"""


# Recurrence relation
# Rec(Current_Horse, Current_Stable) =  |
#                             |           |
#                             |           |Rec(i + 1, Next_Stable) + (White_Horses * Black Horses in Current_Stable)
#                             |       min |
#                             |           |
#                             |
#                             | i = Current_Horse to Number_of_Horses
#                             |
# Now can you implement it?

def cost(A):
    tw = 0
    tb = 0
    for i in A:
        if i == 'W':
            tw += 1
        else:
            tb += 1
    return tw * tb


class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer

    def arrange(self, A, B):
        d = [[10000000000 for i in range(len(A))] for j in range(B)]
        tb = 0
        tw = 0
        for i in range(1, len(A) + 1):
            if A[-i] == 'W':
                tw += 1
            else:
                tb += 1
            d[0][-i] = tw * tb

        # print(d[0])
        for i in range(1, B):
            for j in range(2, len(A) + 1):
                c = []
                b = A[-j:]
                for k in range(1, len(b)):
                    # print(b[k:])
                    if len(b[k:]) > 0:
                        c += [cost(b[:k]) + d[i - 1][-(j - k)]]
                    else:
                        c += [10000000000]
                        break
                # print(c,i,j)
                d[i][-j] = min(c)
        if d[B - 1][0] == 10000000000:
            return -1
        else:
            return d[B - 1][0]
