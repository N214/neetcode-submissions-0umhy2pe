class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        def dfs(i):
            if i == len(nums):
                res.append(sol[:])
                return
            # decision to not add to the subset
            dfs(i+1)

            # decision to add to the subset
            sol.append(nums[i])
            dfs(i+1)
            sol.pop()
        dfs(0)
        return res