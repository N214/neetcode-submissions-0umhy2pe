"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        # by using the properties of inorder traversal of a BST
        # check if the node has a right branch, if it does, then the inorder successor is below
        # if not it's above
        if node.right:
            # the successor is somewhere lower in the right subtree
            node = node.right
            while node.left:
                # inorder we always take the left one if it exist
                node = node.left
            return node

        # the successor is somewhere upper in the tree
        while node.parent:
            # check the parent, the next inorder node is the one with bigger val than the current one.
            if node.parent.val > node.val:
                return node.parent
            # otherwise move up
            node = node.parent