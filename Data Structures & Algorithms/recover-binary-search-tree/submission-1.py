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
        arr = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            arr.append(root)
            dfs(root.right)
            return
        dfs(root)
        print(f"{arr=}")
        node1, node2 = None, None

        for i in range(len(arr) -1):
            if arr[i].val > arr[i+1].val:
                # update this node as long as the above condition is still True
                node2 = arr[i+1]
                if node1 is None:
                    node1 = arr[i]
                else:
                    break
        node1.val, node2.val = node2.val, node1.val