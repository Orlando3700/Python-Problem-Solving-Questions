# Write a Python program to check if a binary
# tree is balanced

# This defines a class called Node, which
# represents a single node in a binary tree.
class Node:
    # __init__ is the constructor that gets
    # called when a new Node is created.
    def __init__(self, value):
        # self.value stores the value of the node.
        self.value = value
        # self.left and self.right initialize
        # the left and right child pointers to
        # None (i.e., no children yet).
        self.left = None
        self.right = None

# This function checks if a binary tree is
# balanced.
# A binary tree is considered balanced if,
# for every node, the difference in height
# between the left and right subtrees is at most 1.
def is_balanced(root):
    # if not root: checks if the tree is empty
    # (i.e., root is None). An empty tree is
    # considered balanced, so it returns True.
    if not root:
        return True

    # This nested helper function computes the
    # height of a subtree rooted at node.
    def height(node):
        # If node is None, it returns 0 (base case).
        if not node:
            return 0
        # Otherwise, it recursively computes the height of
        # the left and right subtrees and returns the larger
        # of the two, plus 1 (for the current node).
        # height(node) helps measure how tall a subtree is.
        return 1 + max(height(node.left), height(node.right))

    # This line checks the difference in height between the
    # left and right subtrees of the root.
    # abs(...) ensures the result is non-negative.
    # If the difference is <= 1, the function returns True,
    # meaning the root is balanced.
    # This code only checks the root node, not the whole tree.
    # So it works only at the root level, not recursively for
    # all nodes.
    return abs(height(root.left) - height(root.right)) <= 1

# Creates a small binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
print(is_balanced(root))  # True

