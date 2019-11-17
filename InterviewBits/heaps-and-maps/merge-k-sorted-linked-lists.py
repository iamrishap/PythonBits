"""
Merge k sorted linked lists and return it as one sorted list.
Example :
1 -> 10 -> 20
4 -> 11 -> 13
3 -> 8 -> 9
will result in
1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20
"""


# Lets keep a pointer for every linked list. At any instant you will need to know the minimum of elements at all
# pointer. Following it you will need to advance that pointer. Can you do this in complexity better than O(K).
# Preferably O(logK). But how?
# There are 2 approaches to solving the problem.
# Approach 1 : Using heap.
# At every instant, you need the minimum of the head of all the k linked list. Once you know the minimum,
# you can push the node to your answer list, and move over to the next node in that linked list.
# Approach 2 : Divide and conquer.
# Solve the problem for first k/2 and last k/2 list. Then you have 2 sorted lists. Then simiply merge the lists.
# Analyze the time complexity.
# T(N) = 2 T(N/2) + N
# T(N) = O (N log N)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        ans = []
        for i in A:
            current = i
            while (current != None):
                ans.append((current.val, current))
                current = current.next
        ans = sorted(ans)
        # ans1 = []
        for i in range(len(ans) - 1):
            ans[i][1].next = ans[i + 1][1]
        return ans[0][1]
