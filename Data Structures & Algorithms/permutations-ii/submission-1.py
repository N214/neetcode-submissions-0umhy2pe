class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        nums.sort()
        used = [False] * len(nums)

        def dfs():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                sol.append(nums[i])
                dfs()
                sol.pop()
                used[i] = False

        dfs()
        return res