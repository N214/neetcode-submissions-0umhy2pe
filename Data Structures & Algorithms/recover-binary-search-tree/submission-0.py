# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # A key property of BSTs is that an inorder traversal produces 
        # values in sorted order.
        arr = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            arr.append(root)
            dfs(root.right)
        dfs(root)
        node1, node2 = None, None
        print(f"{arr=}")
        for i in range(len(arr) - 1):
            if arr[i].val > arr[i + 1].val:
                node2 = arr[i + 1]
                if node1 is None:
                    node1 = arr[i]
                else:
                    break
        node1.val, node2.val = node2.val, node1.val