class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        reference = set(nums)
        longest = 0
        for num in nums:
            #check if it's the start of a sequence
            if (num-1) not in reference:
                length = 0
                while (num+length) in reference:
                    length += 1
                longest = max(length, longest)
        return longest