class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.largest_val = 0

        self.dfs(root)
        return self.largest_val

    def dfs(self, root):
        if not root:
            return (True, 0, float('inf'), float('-inf'))
            # return float('inf'), float('-inf') because of the condition l_max < root.val < r_min
            
        l_is_bst, l_size, l_min, l_max = self.dfs(root.left)
        r_is_bst, r_size, r_min, r_max = self.dfs(root.right)

        # custom BST logic
        # this is a BST only if 
        ## left and right side are both bst and l_max < root.val < r_min
        if l_is_bst and r_is_bst and l_max < root.val < r_min:
            curr_size = 1 + l_size + r_size
            self.largest_val = max(self.largest_val, curr_size)
            return (True, curr_size, min(root.val, l_min), max(root.val, r_max))
        else:
            return (False, 0, float('-inf'), float('inf'))