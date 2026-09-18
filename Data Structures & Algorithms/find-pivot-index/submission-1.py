class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftPrefix = 0
        for i in range(len(nums)):
            rightPrefix = total - leftPrefix - nums[i]
            if leftPrefix == rightPrefix:
                return i
            leftPrefix += nums[i]
        return -1