# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = root.val
        while root:
            curr_diff = abs(target-root.val)
            best_diff = abs(target-res)
            if curr_diff < best_diff:
                res = root.val
            if curr_diff == best_diff and root.val < res:
                res = root.val
            
            if target > root.val:
                root = root.right
            else:
                root = root.left
        return res
        