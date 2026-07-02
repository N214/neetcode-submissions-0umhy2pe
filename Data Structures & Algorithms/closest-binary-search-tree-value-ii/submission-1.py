"""
Time complexity, O(nlogn) due to the sorting algo, dfs is O(n)
Space complexity O(n) + n, recursive call stack
"""
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        def dfs(node, arr):
            if not node:
                return
            arr.append(node.val)
            dfs(node.left, arr)
            dfs(node.right, arr)

        arr = []
        dfs(root, arr)
        arr.sort(key= lambda x: abs(x-target))
        return arr[:k]