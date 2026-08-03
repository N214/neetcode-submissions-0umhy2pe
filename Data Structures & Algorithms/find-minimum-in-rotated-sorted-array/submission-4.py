class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1
        ans = float("inf")
        while l <= r:
            m = (l + r) //2
            ans = min(ans, nums[m])
            # [3,4,5,6,1,2]
            #  l   m      r
            if nums[m] > nums[r]:
                # the minimum must be in the right half
                l = m + 1
            else:
                r = m - 1
        return ans