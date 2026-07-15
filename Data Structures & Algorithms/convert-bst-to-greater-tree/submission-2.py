import sys

sys.setrecursionlimit(1000000000)
class Solution:
	def convertBST(self, root: TreeNode) -> TreeNode:
		sum = 0
		
		def dfs(root: TreeNode) -> TreeNode:
			nonlocal sum
			if root:
				dfs(root.right)
				root.val += sum
				sum = root.val
				dfs(root.left)
			return root
		
		return dfs(root)