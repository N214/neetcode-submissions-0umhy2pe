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
            if not root:
                return
            nonlocal curSum
            dfs(root.right)
            tmp = root.val
            root.val += curSum
            curSum += tmp
            dfs(root.left)
            
        dfs(root)
        return root