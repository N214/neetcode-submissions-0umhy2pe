# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        res = self.stack.pop()
        # this is a inorder traversal, so we go to the most left element so if it's not in the stack, they probably dont exist.
        # so we check if we have a left child, if yes, we add it to the stack
        curr = res.right
        # then from the curr node, which is on the right side, we still have to check the left side of that node.
        while curr:
            self.stack.append(curr)
            curr = curr.left 

        return res.val

    def hasNext(self) -> bool:
        return self.stack != []


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()