# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys

sys.setrecursionlimit(1000000000)

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curSum = 0
        def dfs(root):
            nonlocal curSum
            if not root:
                return
            dfs(root.right)
            root.val += curSum
            curSum = root.val
            dfs(root.left)
            return root
        
        return dfs(root)            