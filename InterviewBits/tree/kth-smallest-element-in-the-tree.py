"""
Given a binary search tree, write a function to find the kth smallest element in the tree.
Example :
Input :
  2
 / \
1   3
and k = 2
Return : 2
As 2 is the second smallest element in the tree.
 NOTE : You may assume 1 <= k <= Total number of nodes in BST
"""


# Note the property of the binary search tree.
# All elements smaller than root will be in the left subtree, and all elements greater than root will be in the
# right subtree.
# This means we need not even explore the right subtree till we have explored everything in the left subtree.
# Or in other words, we go to the right subtree only when the size of left subtree + 1 ( root ) < k.
# With that in mind, we can come up with an easy recursive solution which is similar to inorder traversal :
# Step 1: Find the kth smallest element in left subtree decrementing k for every node visited.
# If answer is found, return answer.
# Step 2: Decrement k by 1. If k == 0 ( this node is the kth node visited ), return node’s value
# Step 3: Find the kth smallest element in right subtree.

def dfs(t):
    return [] if t is None else dfs(t.left) + [t.val] + dfs(t.right)


class Solution:
    def kthsmallest(self, t, k):
        return dfs(t)[k - 1]

    def kthsmallest_another(self, A, k):
        s = [A]
        counter = 0
        while s and k:
            top = s[len(s) - 1]
            if top.left:
                s.append(top.left)
                top.left = None
                continue
            latest = s.pop()
            counter += 1
            if counter == k:
                return latest.val
            if latest.right:
                s.append(latest.right)
