class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            level = len(q)
            current_level = []
            for _ in range(level):
                node = q.popleft()
                current_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(current_level)
        return res