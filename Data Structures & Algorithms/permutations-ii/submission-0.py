class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        path = []
        visited = set()  # stores indices

        def dfs():
            if len(path) == n:
                res.append(path[:])
                return

            for i in range(n):
                # already used this position
                if i in visited:
                    continue
                # We are skipping the second one when the first one has not been used yet.
                if (
                    i > 0
                    and nums[i] == nums[i - 1] # current num is the same as prev num
                    and (i - 1) not in visited # previous index not in visited
                ):
                    continue

                visited.add(i)
                path.append(nums[i])

                dfs()

                path.pop()
                visited.remove(i)

        dfs()
        return res