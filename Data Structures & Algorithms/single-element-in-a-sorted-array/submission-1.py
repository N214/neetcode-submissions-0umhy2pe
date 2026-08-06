"""
    before the single element: pairs start at even indices
    after the single element: pairs start at odd indices
"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1
        while l < r:
            m = (l + r)//2
            if (m % 2 == 0 and nums[m] == nums[m+1]) or (m % 2 == 1 and nums[m-1] == nums[m]):
                # only pair values on the left, move to the right
                l = m + 1
            else:
                r = m
        return nums[l]