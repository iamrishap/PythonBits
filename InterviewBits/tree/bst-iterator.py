"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
The first call to next() will return the smallest number in BST. Calling next() again will return the next smallest
number in the BST, and so on.
 Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
Try to optimize the additional space complexity apart from the amortized time complexity.
"""


# Approach 1 : Do an inorder traversal of the tree and store the entries in an array with the current pointer set
# to the start of the array. hasNext checks if the pointer is less than the size of the array. next() would return
# the element at the current position incrementing the position by 1.
# However, this has an additional space complexity of O(N) where N = number of nodes in the tree.
# This might be an acceptable answer. Most interviewers would look for you to do better.
# Approach 2 : Lets look at the version of this problem when the trees have a back pointer. Can you solve the problem
# without using additional space ? When you are on node N and are asked for next element, you obviously won’t go to
# the left subtree as all the elements there are smaller than N. We would go to the smallest number in the right
# subtree if the right subtree is not null. If the right subtree is null, that means that we need to move up, and
# keep moving up till we are coming from the right subtree.
# Now we don’t have the back pointer in this case. So, we need something to keep track of the path from root to the
# current node, so we can move to the parent when needed. Do note that storing the path from root to the current node
# only requires memory equivalent to the length of the path which is the depth of the tree.
# Also, we can track the path using stack.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        # path_to_min contains the path from the root to the current minimum element
        # maintaining this list enables finding the next minimum in constant time
        # storage is in O(h)
        self.path_to_min = []
        self.populate_min(root, self.path_to_min)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.path_to_min != []

    # @return an integer, the next smallest number
    def next(self):
        if self.hasNext():
            n = self.path_to_min[-1].val
            self.find_next_min(self.path_to_min)
            return n

    def populate_min(self, A, path):
        if A is None:
            pass
        else:
            path.append(A)
            self.populate_min(A.left, path)

    # Finds the next minimum. There are 2 cases:
    # - the current minimum has a right subtree. The next minimum is the leftmost
    #   element of that subtree
    # - the current minimum does not have a right subtree. The next minimum is in the path
    #   from the root to the current min, unless the current min is the maximum of the tree
    def find_next_min(self, path_to_min):
        root = path_to_min[-1]
        # first case, there is a right subtree
        if root.right:
            self.populate_min(root.right, path_to_min)
        # second case, will empty the path completely when called on the maximum
        else:
            while path_to_min != [] and path_to_min[-1].val <= root.val:
                path_to_min.pop()

            # Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),
