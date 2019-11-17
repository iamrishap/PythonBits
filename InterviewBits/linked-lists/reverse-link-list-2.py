"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.
For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,
return 1->4->3->2->5->NULL.
 Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list. Note 2:
Usually the version often seen in the interviews is reversing the whole linked list which is
obviously an easier version of this question.
"""


# If you are still stuck at reversing the full linked list problem,
# then would maintaining curNode, nextNode and a tmpNode help ?
# Maybe at every step, you do something like this :
#     tmp = nextNode->next;
#             nextNode->next = cur;
#             cur = nextNode;
#             nextNode = tmp;
# Now, lets say you did solve the problem of reversing the linked list and are stuck at applying it to current problem.
# What if your function reverses the linked list and returns the endNode of the list.
# You can simply do
# prevNodeOfFirstNode->next = everseLinkedList(curNode, n - m + 1);

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        cur_idx = 1
        cur_node = A
        pre_seg = seg_start = seg_end = None
        while cur_idx <= C:
            if cur_idx == B - 1:
                pre_seg = cur_node
            if cur_idx == B:
                seg_start = cur_node
            if cur_idx == C:
                seg_end = cur_node
            cur_idx += 1
            cur_node = cur_node.next

        cur_node = seg_start.next
        seg_start.next = seg_end.next
        if B != 1:
            pre_seg.next = seg_end
        else:
            A = seg_end

        pre_node = seg_start
        while pre_node != seg_end:
            pre_node, cur_node.next, cur_node = cur_node, pre_node, cur_node.next

        return A
