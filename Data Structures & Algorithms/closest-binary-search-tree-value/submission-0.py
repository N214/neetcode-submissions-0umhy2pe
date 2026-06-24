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
            #res = min(root.val, res, key=lambda x: (abs(target-x), x))
            curr_diff = abs(target - root.val)
            best_diff = abs(target - res)
            # if current node is smaller than the best diff, update res
            if curr_diff < best_diff:
                res = root.val
            # if current node is equal to best diff, and the current node is smaller, update the res
            elif curr_diff == best_diff and root.val < res:
                res = root.val
            
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return res