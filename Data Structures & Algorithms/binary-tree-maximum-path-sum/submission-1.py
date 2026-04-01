# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.total_max = float('-inf')
        def dfs(root):
            """
            intput is the root of the tree
            return the sum of the root node by adding leftval and rightval
            """
            if not root:
                return 0
            # subtitute the val to 0 if negative
            leftSide = max(0,dfs(root.left))
            rightSide = max(0,dfs(root.right))                
            localMax = root.val + leftSide + rightSide
            self.total_max =  max(self.total_max, localMax)
            return root.val + max(leftSide, rightSide)
        dfs(root)
        return self.total_max