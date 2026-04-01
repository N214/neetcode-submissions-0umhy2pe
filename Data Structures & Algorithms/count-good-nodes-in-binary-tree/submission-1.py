# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        better to use BFS and doing that level by level
        """
        if not root:
            return 0
        q = deque([(root, root.val)])
        res = 0
        while q:
            node, max_val = q.popleft()
            if node.val >= max_val:
                res += 1
                max_val = node.val
            if node.left:
                q.append((node.left, max_val))
            if node.right:
                q.append((node.right, max_val))
        return res
