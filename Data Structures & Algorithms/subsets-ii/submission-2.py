class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        nums.sort()

        def dfs(i):
            if i == len(nums):
                res.append(sol[:])
                return
            
            sol.append(nums[i])
            dfs(i+1)
            sol.pop()

            next_index = i+1
            while next_index < len(nums) and nums[next_index] == nums[next_index-1] :
                next_index=next_index+1
            dfs(next_index)
        dfs(0)
        return res 