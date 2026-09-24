class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for n in range(1,(2^31)-1):
            if n not in nums:
                return n