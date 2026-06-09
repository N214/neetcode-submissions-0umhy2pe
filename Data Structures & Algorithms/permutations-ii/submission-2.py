class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        count = Counter(nums)

        def dfs():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            for x in count:
                if count[x] > 0:
                    count[x] -= 1
                    sol.append(x)
                    dfs()
                    count[x] += 1
                    sol.pop()
        dfs()
        return res