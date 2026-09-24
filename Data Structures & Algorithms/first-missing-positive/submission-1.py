class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
         # use the input array nums as storage
         # the negative sign is gonna be the signal that the number exist in the array
         # do a first iteration, clean up the array, replace all preexisting val to 0, to mark a existing 0 as negative val use -len(nums)+1 as replacement
         # do a second iteration, check i and replace the value at i-1 (eg. 3-1=2) to a neg val if it's inbound
         # do a third pass on the len(nums)
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        # if we modify the array we have to iterate on the range
        for i in range(len(nums)):
            idx = abs(nums[i])
            if 1 <= idx <= len(nums):
                if nums[idx-1] > 0:
                    nums[idx-1] *= -1
                elif nums[idx-1] == 0:
                    nums[idx-1] = -1 * (len(nums)+1)
        
        for i in range(1, len(nums) +1):
            if nums[i - 1] >= 0:
                return i
        return len(nums) + 1 
