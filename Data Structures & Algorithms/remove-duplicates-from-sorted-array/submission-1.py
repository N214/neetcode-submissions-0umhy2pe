class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # initialize both l and r at the second val because the first val will not change for sure. 
        l = 1
        for r in range(1, len(nums)):
            # if current val at r is the not same as the previous one, we increment l and r will shift with the for loop
            if nums[r] != nums[r-1]:
                # put the first seen right val to the left position
                nums[l] = nums[r]
                l += 1
        return l