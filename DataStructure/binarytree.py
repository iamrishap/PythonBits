from collections import deque
import doctest
q = deque()
'''
                  2
                /    \
               3      7
             /  \     /
           15    1   5
                    / \ 
                   9  45
                        \
                         3
'''


class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return self.data

bt = BinaryTree
root = bt(2, bt(3, bt(15), bt(1)), bt(7, bt(5, bt(9), bt(45, None, bt(3)))))


def level_traversal(root):
    leveltrav = ''
    q.append(root)
    while q:
        current = q.popleft()
        leveltrav += ' ' + str(current.data)
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)
    print(leveltrav)


def preorder(root):
    preord = ''
    stack = []
    stack.append(root)
    while stack:
        current = stack.pop()
        preord += ' ' + str(current.data)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    print(preord)


def inorder(root):
    inord = ''
    stack = []
    current = root
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            inord += ' ' + str(current.data)
            current = current.right
    print(inord)


def postorder(root):
    postord = ''
    visited = set()
    stack = []
    current = root
    while current or stack:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            if current.right and current.right not in visited:
                stack.append(current)
                current = current.right
            else:
                visited.add(current)
                postord += ' ' + str(current.data)
                current = None
    print(postord)


def getheight(root):
    leveltrav = ''
    q.append([root, 1])
    while q:
        current, level = q.popleft()
        leveltrav += ' ' + str(current.data)
        if current.left:
            q.append([current.left, level+1])
        if current.right:
            q.append([current.right, level+1])
    print(level)


def binaryTreePaths(root):
    if root is None:
        return []
    if root.left == None and root.right == None:
        return [str(root.data)]
    return [str(root.data) + ' -> ' + l for l in
             binaryTreePaths(root.right) + binaryTreePaths(root.left)]


def diameter_height(node):
    if node is None:
        return 0, 0
    ld, lh = diameter_height(node.left)
    rd, rh = diameter_height(node.right)
    return max(lh + rh + 1, ld, rd), 1 + max(lh, rh)


def find_tree_diameter(node):
    d, _ = diameter_height(node)
    return d


def calsum(root):
    '''
    >>> sum(map(int,calsum(root)))
    280758
    '''
    if not root:
        return []
    if not root.left and not root.right:
        return [root.data]
    return [str(root.data) + str(l) for l in calsum(root.left) + calsum(root.right)]


def findMaxUtil(root):
    '''
    >>> findMaxUtil.res = 0
    >>> _ = findMaxUtil(root)
    >>> findMaxUtil.res
    80
    '''
    if root is None:
        return 0
    # l and r store maximum path sum going through left
    # and right child of root respetively
    l = findMaxUtil(root.left)
    r = findMaxUtil(root.right)
    # Max path for parent call of root. This path
    # must include at most one child of root
    max_single = max(max(l, r) + root.data, root.data)
    # Max top represents the sum when the node under
    # consideration is the root of the maxSum path and
    # no ancestor of root are there in max sum path
    max_top = max(max_single, l + r + root.data)
    # Static variable to store the changes
    # Store the maximum result
    findMaxUtil.res = max(findMaxUtil.res, max_top)
    return max_single


def findSumPossible(root, path, leftSum):
    '''
    >>> findSumPossible.possible = False
    >>> findSumPossible(root, '', 23)
    >>> findSumPossible.possible
    True
    >>> findSumPossible.possiblePath
    '->2->7->5->9'
    '''
    if not root:
        return
    if not root.left and not root.right:
        if leftSum == root.data:
            findSumPossible.possible = True
            findSumPossible.possiblePath = path + '->' + str(root.data)
        return
    if root.left:
        findSumPossible(root.left, path + '->' + str(root.data), leftSum-root.data)
    if root.right:
        findSumPossible(root.right, path + '->' + str(root.data), leftSum-root.data)


def findlca(root):
    '''
    >>> findlca.node1 = 1
    >>> findlca.node2 = 15
    >>> findlca(root)
    3
    >>> findlca.node2 = 95
    >>> findlca(root)
    True
    '''
    if not root:
        return False
    if root.data == findlca.node1 or root.data == findlca.node2:
        return True
    left = findlca(root.left) if root.left else 0
    right = findlca(root.right) if root.right else 0
    if left and right:
        return root.data
    return left if left else right


def printAncestorWrapper(root, val):
    '''   
    >>> v = printAncestorWrapper(root, 3)
    ['2', '7', '5', '45']
    ['2']
    '''
    ans_list = printAncestors(root, val)
    for item in ans_list:
        print(item.split()[:-1])


def printAncestors(root, value):
    if not root:
        return []
    if root.data == value:
        return [str(root.data)]
    return [str(root.data) + ' ' + l for l in printAncestors(root.right, value) + printAncestors(root.left, value)]


def printAncestors2(root, value):
    '''
    >>> printAncestors2(root, 45)
    5 7 2 True
    '''
    if not root:
        return False
    if (root.left and root.left.data == value) or (root.right and root.right.data == value) or printAncestors2(root.left, value)or printAncestors2(root.right, value):
        print(root.data, end=' ')
        return True
    return False


def isMirror(root1, root2):
    # If both trees are empty, then they are mirror images
    if root1 is None and root2 is None:
        return True
    if root1 is not None and root2 is not None:
        if root1.key == root2.key:
            return isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)
    return False


def isSymmetric(root):
    # Check if tree is mirror of itself
    return isMirror(root, root)


def zigzag(root):
    '''
    >>> zigzag(root)
    [2, 3, 7, 5, 1, 15, 9, 45, 3]
    '''
    ltor = False
    currentLevel = []
    order = []
    if root:
        currentLevel.append(root)
    else:
        return False
    while currentLevel:
        nextLevel = []
        while currentLevel:
            current = currentLevel.pop()
            order.append(current.data)
            if ltor:
                if current.left:
                    nextLevel.append(current.left)
                if current.right:
                    nextLevel.append(current.right)
            else:
                if current.right:
                    nextLevel.append(current.right)
                if current.left:
                    nextLevel.append(current.left)
        ltor = not ltor
        currentLevel = nextLevel
    print(order)


def verticalsum(root, distance):
    '''
    >>> verticalsum.d = {}
    >>> verticalsum(root, 0)
    >>> verticalsum.d
    {0: 8, -1: 12, -2: 15, 1: 52, 2: 3}
    '''
    if not root:
        return -1
    verticalsum.d[distance] = root.data if distance not in verticalsum.d else verticalsum.d[distance] + root.data
    if root.left:
        verticalsum(root.left, distance-1)
    if root.right:
        verticalsum(root.right, distance+1)

doctest.testmod()
# findlca(root)
