"""
A linked list is given such that each node contains an additional random pointer which could point to any node in
the list or NULL.
Return a deep copy of the list.
Example
Given list
   1 -> 2 -> 3
with random pointers going from
  1 -> 3
  2 -> 1
  3 -> 1
You should return a deep copy of the list. The returned answer should not contain the same node as the original list,
but a copy of them. The pointers in the returned list should not link to any node in the original input list.
"""


# There are 2 approaches to solving this problem.
# Approach 1 : Using hashmap.
# Use a hashmap to store the mapping from oldListNode to the newListNode.
# Whenever you encounter a new node in the oldListNode (either via random pointer or through the next pointer ),
# create the newListNode, store the mapping. and update the next and random pointers of the newListNode
# using the mapping from the hashmap.
# Approach 2 : Using 2 traversals of the list.
# Step 1: create a new node for each existing node and join them together eg: A->B->C will be A->A’->B->B’->C->C’
# Step2: copy the random links: for each new node n’, n’.random = n.random.next
# Step3: detach the list: basically n.next = n.next.next; n’.next = n’.next.next

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head == None:
            return None

        done = {}
        cur = head

        while cur is not None:
            done[cur] = RandomListNode(cur.label)
            cur = cur.next

        for (k, v) in done.iteritems():
            new_node = v
            new_node.next = done[k.next] if k.next in done else None
            new_node.random = done[k.random] if k.random in done else None

        return done[head]
