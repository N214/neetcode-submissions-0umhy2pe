class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = set()
        def dfs():
            if len(path) == len(nums):
                res.append(path[:])
                return

            for num in nums:
                # if already used, skip
                if num in used:
                    continue
                path.append(num)
                used.add(num)

                # explore
                dfs()

                # backtrack
                path.pop()
                used.remove(num)
        dfs()
        return res 
