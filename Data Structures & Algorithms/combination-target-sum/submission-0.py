class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # This will store all valid combinations we find
        res = []

        # dfs(i, curr, total)
        # i = current index in nums we are considering
        # curr = current combination being built
        # total = sum of numbers in curr
        def dfs(i, curr, total):
            # Base case: if we've reached the target, we found a valid combination
            if total == target:
                res.append(curr.copy())  # copy because curr will change later during backtracking
                return

            # Base case: stop if we've gone past the end of nums
            # or if the current sum is already too large
            if i >= len(nums) or total > target:
                return

            # Choice 1: include nums[i]
            # We stay at the same index because we can reuse the same number unlimited times
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])

            # Backtrack: remove the last chosen number before trying the next option
            curr.pop()

            # Choice 2: skip nums[i] and move to the next number
            dfs(i + 1, curr, total)

        # Start DFS from index 0, with an empty combination and sum 0
        dfs(0, [], 0)

        return res