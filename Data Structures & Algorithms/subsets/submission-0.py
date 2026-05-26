class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision to add to the subset
            subset.append(nums[i])
            dfs(i+1)

            # decision to not add to the subset
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res