# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return None
            leftSide = dfs(root.left)
            rightSide = dfs(root.right)
            root.left = rightSide
            root.right = leftSide
            return root
        return dfs(root)