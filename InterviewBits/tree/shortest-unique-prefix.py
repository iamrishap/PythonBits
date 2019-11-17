"""
Find shortest unique prefix to represent each word in the list.
Example:
Input: [zebra, dog, duck, dove]
Output: {z, dog, du, dov}
where we can see that
zebra = z
dog = dog
duck = du
dove = dov
 NOTE : Assume that no word is prefix of another. In other words, the representation is always possible.
"""


# input: ["zebra", "dog", "duck", "dot"]
# Now we will build prefix tree and we will also store count of characters
#                 root
#                 /|
#          (d, 3)/ |(z, 1)
#               /  |
#           Node1  Node2
#            /|        \
#      (o,2)/ |(u,1)    \(e,1)
#          /  |          \
#    Node1.1  Node1.2     Node2.1
#       | \         \            \
# (g,1) |  \ (t,1)   \(c,1)       \(b,1)
#       |   \         \            \
#     Leaf Leaf       Node1.2.1     Node2.1.1
#     (dog)  (dot)        \                  \
#                          \(k, 1)            \(r, 1)
#                           \                  \
#                           Leaf               Node2.1.1.1
#                           (duck)                       \
#                                                         \(a,1)
#                                                          \
#                                                          Leaf
#                                                          (zebra)
# Now, for every leaf / word , we find the character nearest to the root with frequency as 1.
# The prefix that the path from root to this character corresponds to, is the representation of the word.

class TreeNode(object):
    def __init__(self):
        self._children = {}  # prefix to child

    def add(self, prefix):
        if prefix not in self._children:
            self._children[prefix] = TreeNode()
        return self._children[prefix]

    def num(self):
        return len(self._children)

    def get(self, prefix):
        # Assumes exists
        return self._children[prefix]


class PrefixTree(object):
    def __init__(self, words):
        self._root = TreeNode()  # empty prefix for root
        for word in words:
            self.add(word)

    def add(self, word):
        node = self._root
        for c in word:
            node = node.add(c)

    def get(self, word):
        node = self._root
        counts = []
        for c in word:
            counts.insert(0, node.num())
            node = node.get(c)
        # chop of uniques from the end
        num_remove = 0
        for count in counts:
            if count != 1:
                break
            num_remove += 1
        return word[:-num_remove] if num_remove > 0 else word


class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        # build prefix tree
        tree = PrefixTree(A)
        # apply prefix tree
        return [tree.get(a) for a in A]
